from django.shortcuts import render,redirect
from movieapp.forms import *
from movieapp.models import *
from django.contrib import messages
from django.views.generic import DetailView,UpdateView,DeleteView,CreateView

# Create your views here.
def home(request):
    return render(request,'movieapp/home.html')

from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="movieapp/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="movieapp/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")

# class movielist(ListView):
# 	model=movie

# class moviedetail(DetailView):
# 	model=movie

class movieAdd(CreateView):
    model=movie
    # fields=('title','auth_name','nopages','price')
    fields='__all__'

from django.views import View

# ...

# class MyProfile(LoginRequiredMixin, View):
#     def get(self, request):
#         user_form = UserUpdateForm(instance=request.user)
#         profile_form = ProfileUpdateForm(instance=request.user.profile)
        
#         context = {
#             'user_form': user_form,
#             'profile_form': profile_form
#         }
        
#         return render(request, 'movieapp/profile.html', context)
    
    # def post(self,request):
    #     user_form = UserUpdateForm(
    #         request.POST, 
    #         instance=request.user
    #     )
    #     profile_form = ProfileUpdateForm(
    #         request.POST,
    #         request.FILES,
    #         instance=request.user.profile
    #     )

    #     if user_form.is_valid() and profile_form.is_valid():
    #         user_form.save()
    #         profile_form.save()
            
    #         messages.success(request,'Your profile has been updated successfully')
            
    #         return redirect('profile')
    #     else:
    #         context = {
    #             'user_form': user_form,
    #             'profile_form': profile_form
    #         }
    #         messages.error(request,'Error updating you profile')
            
    #         return render(request, 'movieapp/profile.html', context)
	

def profile(request):
	return render(request,"movieapp/profile.html")


def updateprofile(request):
    form=CustomUserChangeForm()
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after successful update
    else:
        form = UserChangeForm(instance=request.user)
        return render(request, 'movieapp/updateprofile.html', {'form': form})
    
def movielist(request):
    movielist=movies.objects.all()
    return render(request,'movieapp/movie_list.html',{"movielist":movielist})

from django.shortcuts import render, get_object_or_404
  # Import your Movie model

def movie_detail(request, movies_id):
    movie = get_object_or_404(movies, id=movies_id)
    context = {'movie': movie}
    return render(request, 'details.html', context)


def movie_search(request):
    if request.method == 'POST':
        form = MovieSearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            movie = movies.objects.filter(name__icontains=search_query)
    else:
        form = MovieSearchForm()
        movie = movies.objects.all()

    context = {'form': form, 'movies': movie}
    return render(request, 'movieapp/movie_search.html', context)
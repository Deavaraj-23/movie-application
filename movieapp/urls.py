from django.urls import path
from movieapp import views

urlpatterns=[
    path('',views.home,name="home"),
    # path('movielist/', views.movielist.as_view(),name='list'),
    
    path('movielist/',views.movielist,name='movielist'),
    # path('<int:pk>/', views.moviedetail.as_view(),name='details'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('create/', views.movieAdd.as_view()),
    path('profile/',views.profile,name='profile'),
    path('updateprofile', views.updateprofile, name='updateprofile'),
    path('search/', views.movie_search, name='movie_search'),
]
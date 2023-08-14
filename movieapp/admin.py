from django.contrib import admin
from movieapp.models import *

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=['user','image','movie_name','director','description','release_date']

    
admin.site.register(movie,MovieAdmin)







    
admin.site.register(movies)
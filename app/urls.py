from django.urls import  path
from .views import home, us, ourservices, blog, meditation, reading, journaling, socialmedia

urlpatterns = [
    path('', home, name="home"),
    path('us/', us, name="us"),
    path('ourservices/', ourservices, name="ourservices"),
    path('blog/', blog, name="blog"),
    path('meditation/', meditation, name="meditation"),
    path('reading/', reading, name="reading"),
    path('journaling/', journaling, name="journaling"),
    path('socialmedia/', socialmedia, name="socialmedia")
   
]

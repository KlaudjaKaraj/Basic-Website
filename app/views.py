from django.shortcuts import render

# Create your views here.
def home (request):
    return render (request, 'home.html')

def us (request):
    return render (request, 'us.html')

def ourservices (request):
    return render (request, 'ourservices.html')

def blog (request):
    return render (request, 'blog.html')

def meditation (request):
    return render (request, 'meditation.html')

def reading (request):
    return render (request, 'reading.html')

def journaling (request):
    return render (request, 'journaling.html')

def socialmedia (request):
    return render (request, 'socialmedia.html')

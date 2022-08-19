from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def gallery_single(request):
    return render(request, 'gallery-single.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def sample_inner_page(request):
    return render(request, 'sample-inner-page.html')

def ero(request):
    return render(request, 'gallery/sub/ero.html')

# gallery

def nature(request):
    return render(request, 'gallery/nature.html')
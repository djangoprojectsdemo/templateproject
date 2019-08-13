from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')

def educ_view(request):
    return render(request,'testapp/edu.html')

def poli_view(request):
    return render(request,'testapp/polit.html')

def sprt_view(request):
    return render(request,'testapp/sport.html')

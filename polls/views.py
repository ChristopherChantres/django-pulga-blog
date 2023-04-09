from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home.html')


def create(request):
  return render(request, 'create.html')


def edit(request):
  return render(request, 'edit.html')
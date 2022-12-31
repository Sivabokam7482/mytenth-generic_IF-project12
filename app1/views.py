from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':40}
    return render(request,'if statement.html',d)
    
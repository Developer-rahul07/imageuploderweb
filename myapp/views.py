from django.shortcuts import render,HttpResponse,redirect
from .models import ImageUploder
from .forms import ImageForm

# Create your views here.
def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = ImageUploder.objects.all()
    return render(request , 'home.html',{'form':form , 'img':img})

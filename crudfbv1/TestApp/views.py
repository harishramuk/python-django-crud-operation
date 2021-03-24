from django.shortcuts import render,redirect
from TestApp.models import Parcel
from TestApp.forms import Parcelform

# Create your views here.
def retrieve_views(request):
    parcel = Parcel.objects.all()
    return render(request,'testapp/index.html',{'send':parcel})
def creat_view(request):
    form = Parcelform()
    if request.method =='POST':
        form = Parcelform(request.POST)
        if form.is_valid():
            form.save()
        return redirect ('/')
    return render(request,'testapp/create.html',{'send':form})
def delet_view(request,id):
    parcel = Parcel.objects.get(billno=id)
    parcel.delete()
    return redirect('/')

def update_view(request,id):
    parcel = Parcel.objects.get(billno = id)
    if request.method=='POST':
        form =Parcelform(request.POST,instance =parcel )
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'testapp/update.html',{'send':parcel})

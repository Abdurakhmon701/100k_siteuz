from django.shortcuts import render
from .models import * 
# Create your views here.


def profil_settings(request,user_id):
  user = UserModel.objects.all().filter(id=user_id).values()
  if request.method=='POST':
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    viloyat = request.POST['viloyat']
    shahar = request.POST['shahar']
    manzil = request.POST['manzil']
    image = request.FILES['image']
    print(f"\n{username}\n{firstname}\n{lastname}\n{viloyat}\n{shahar}\n{manzil}")
    form = UserModel.objects.get(id=user_id)
    form.firstname=firstname
    form.lastname=lastname
    form.viloyat=viloyat
    form.shahar=shahar
    form.manzil=manzil
    form.image = image
    form.save()
  ctx = {"users":user}
  return render(request,'sozlamalar.html',ctx)
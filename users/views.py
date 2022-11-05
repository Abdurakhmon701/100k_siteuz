from django.shortcuts import render,redirect
from .models import * 

from django.contrib.auth import authenticate,login,logout
from random import randint 
import requests

def telegram_bot_sendtext(bot_message):
    bot_token = '5736620222:AAETP_ZM6JxGY-bgQk08vi5_AbEHyAy2cRs'
    bot_chatID = '615003781'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)   
    return response.json()


def profil_settings(request,user_id):
  user = UserModel.objects.all().filter(id=user_id).values()
  if request.method=='POST':
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    viloyat = request.POST['viloyat']
    shahar = request.POST['shahar']
    manzil = request.POST['manzil']
    if request.FILES:
      image = request.FILES['image']
      form = UserModel.objects.get(id=user_id)
      form.firstname=firstname
      form.lastname=lastname
      form.viloyat=viloyat
      form.shahar=shahar
      form.manzil=manzil
      form.image = image
      form.save()
    else:
      form = UserModel.objects.get(id=user_id)
      form.firstname=firstname
      form.lastname=lastname
      form.viloyat=viloyat
      form.shahar=shahar
      form.manzil=manzil
      form.save()
  ctx = {"users":user}
  return render(request,'sozlamalar.html',ctx)



  # userni ro'yxatdan o'tkazish

def signUpView(request):
  global x
  x = 0
  if request.method == 'POST':

    if request.POST['phone_number'][5:7].isdigit() and request.POST['phone_number'][13:15].isdigit()  and request.POST['phone_number'][16:19].isdigit() :
      zet = request.POST['phone_number'].replace('-','').replace('(','').replace(')','').replace(' ','')
      global tel 
      tel = zet
      doimiy = UserModel.objects.filter(username = tel)
      if doimiy:
        x = randint(00000,99999)
        telegram_bot_sendtext(f"Telefon raqami:{tel}\nMaxfiy kirish kodi:{x}")
        return redirect('login')
      else:
        x = randint(00000,99999)
        telegram_bot_sendtext(f"Telefon raqami:{tel}\nMaxfiy kirish kodi:{x}")
        return redirect('login')
    else:
      pass
  else:
    pass

  ctx = {}
  return render(request,'signup.html',ctx)



def loginPage(request):
  if request.method == 'POST':
    if int(request.POST['password'])==x:
      login_ = UserModel.objects.filter(username=tel)
      if login_:
        user = UserModel.objects.get(username=tel)
        user.password = str(x)
        user.save()
        login(request,user)
        return redirect('main')
        print("User yangilandi")
      else:
        user = UserModel.objects.create_user(username=tel,password=str(x)) 
        user.save()
        login(request,user)
        return redirect('main')
        print("User yaratildi")
    else:
      pass
  else:
    pass
  ctx = {}
  return render(request,'login.html',ctx)    



def logout_user(request):
  logout(request)
  return redirect('main')

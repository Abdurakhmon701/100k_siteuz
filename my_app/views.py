from django.shortcuts import render
from django.views.generic import ListView,TemplateView,DetailView
from .models import HomePageModel,Category

# class HomePageView(ListView):
# 	model = HomePageModel
# 	template_name = 'main.html'



class AloqaPageView(TemplateView):
	template_name = 'aloqa.html'

class LoginPageView(TemplateView):
	template_name = 'login.html'

class SozlamalarPageView(TemplateView):
	template_name = 'sozlamalar.html'

class ProfilPageView(TemplateView):
	template_name = 'profil.html'

class OffertaPageView(TemplateView):
	template_name = 'oferta.html'

class SevimliPageView(ListView):
	model = HomePageModel
	template_name = 'sevimli.html'

class BarchasiPageView(ListView):
	model = HomePageModel
	template_name = 'barchasi.html'


class DetailPageView(DetailView):
	model = HomePageModel
	template_name = 'detail.html'




def homePageView(requests):
	category = Category.objects.all()
	model = HomePageModel.objects.all()
	model_teskari = HomePageModel.objects.all().order_by()[::-1]
	ctx = {
	"apps": model,
	"apps_teskari": model_teskari,
	"kategoriyalar": category,
	}
	return render(requests,'main.html',ctx)


def categoryPageView(requests,category_id):
	cat = Category.objects.get(pk=category_id)
	print("Category",cat)
	mah = HomePageModel.objects.filter(category=cat)
	print("Mahsulotlar_cate",mah)
	context = {
	"cateMahsulotlar":mah
	}
	return render(requests,'category.html',context)
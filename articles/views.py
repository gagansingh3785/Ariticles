from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import models
from django import template


@login_required(login_url="login")
def home(request):
	articles = models.articles.objects.all()
	count = len(articles)
	print(count)
	count = int(count / 10) + (count % 10 != 0)
	count = [i for i in range(count)]
	return render(request, 'home.html', {"articles": articles, "count": count})


@login_required(login_url="login")
def write(request):
	if request.method == "POST":
		article = models.articles()
		article.author = request.user
		article.title = request.POST["title"]
		article.content = request.POST["content"]
		article.read_time = request.POST["readtime"]
		if request.POST["image"]:
			article.image = request.POST["image"]
		article.save()
		print(article)
		messages.add_message(request, messages.SUCCESS, "Article added successfully")
		return HttpResponseRedirect(reverse("your_articles"))

	return render(request, 'write.html', {})


def user_login(request):
	if request.user.username != "":
		return HttpResponseRedirect(reverse("home"))
	if request.method == "POST":
		print("here")
		print(request.POST)
		user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
		if user is not None:
			print(user)
			login(request, user)
			return HttpResponseRedirect(reverse("home"))
		else:
			messages.add_message(request, messages.ERROR, "Incorrect credentials")
			return HttpResponseRedirect(reverse("login"))

	return render(request, 'login.html', {})

@login_required(login_url="login")
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse("login"))

def register(request):
	if request.user.username != "":
		return HttpResponseRedirect(reverse("home"))
	if request.method == "POST":
		user = User()
		if request.POST['password'] != request.POST['confirm_password']:
			messages.add_message(request, messages.ERROR, "Passwords donot match")
			return HttpResponseRedirect(reverse('register'))

		user.username = request.POST['username']
		user.email = user.username
		messages.add_message(request, messages.SUCCESS, "Registeration done")
		user.set_password(request.POST['password'])
		user.save()
		return HttpResponseRedirect(reverse('login'))
	return render(request, 'register.html', {})



@login_required(login_url="login")
def your_articles(request):
	count = len(models.articles.objects.filter(author=request.user));
	count = int(count/10) + (count % 10 != 0);
	count = [i for i in range(count)]
	return render(request, 'your_articles.html', {"count": count})

def navbar(request):
	return render(request, 'navbar.html', {})

@login_required(login_url="login")
def view_article(request, id):
	article = models.articles.objects.get(pk=id)
	return render(request, 'view_article.html', {"article": article})

@login_required(login_url="login")
def get_articles(request, number):
	articles = models.articles.objects.all()[(number - 1) * 10:]
	articles = articles[:min(10, len(articles))]
	print(articles)
	context = {"articles": articles}
	t = template.loader.get_template('get_articles.html')
	html = t.render(context)
	return HttpResponse(html)

@login_required(login_url="login")
def get_my_articles(request, number):
	articles = models.articles.objects.filter(author=request.user)
	print(len(articles))
	articles = articles[(number - 1) * 10 :min(number * 10, len(articles))]
	context = {"articles": articles}
	t = template.loader.get_template('get_my_articles.html')
	html = t.render(context)
	return HttpResponse(html)

@login_required(login_url="login")
def delete_article(request, number):
	models.articles.objects.filter(id=number).delete()
	return HttpResponseRedirect(reverse("your_articles"))
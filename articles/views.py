from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import models
from collections import defaultdict
from django import template


@login_required(login_url="login")
def home(request):
	articles = models.articles.objects.all()
	count = len(articles)
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
		article.brief_content = article.content[0: min(200, len(article.content))]
		article.read_time = request.POST["readtime"]
		if request.POST["image"]:
			article.image = request.POST["image"]
		article.save()
		messages.add_message(request, messages.SUCCESS, "Article added successfully")
		return HttpResponseRedirect(reverse("your_articles"))

	return render(request, 'write.html', {})


def user_login(request):
	if request.user.username != "":
		return HttpResponseRedirect(reverse("home"))
	if request.method == "POST":
		user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
		if user is not None:
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
	starred_articles = models.starred_info.objects.filter(user=request.user)
	send_starred_articles = []
	for i in range(len(starred_articles)):
		send_starred_articles.append(starred_articles[i].article)


	articles = models.articles.objects.all()[(number - 1) * 10:]
	articles = articles[:min(10, len(articles))]
	context = {"articles": articles, "starred": send_starred_articles}
	t = template.loader.get_template('get_articles.html')
	html = t.render(context)
	return HttpResponse(html)

@login_required(login_url="login")
def get_my_articles(request, number):
	articles = models.articles.objects.filter(author=request.user)
	articles = articles[(number - 1) * 10 :min(number * 10, len(articles))]
	context = {"articles": articles}
	t = template.loader.get_template('get_my_articles.html')
	html = t.render(context)
	return HttpResponse(html)

@login_required(login_url="login")
def delete_article(request, number):
	try:
		models.articles.objects.filter(id=number).delete()
		messages.add_message(request, messages.SUCCESS, "Article deleted successfully")
	except: 
		messages.add_message(request, messages.INFO, "Could not delete the article")
	return HttpResponseRedirect(reverse("your_articles"))

@login_required(login_url="login")
def done_reading(request, number):
	article = models.articles.objects.get(pk=number)
	print(article)
	user_articles = models.read_info.objects.filter(user=request.user)
	print(user_articles)
	flag = 1
	for some_article in user_articles: 
		if article.pk == some_article.article.pk:
			flag = 0
			break
	if flag:
		read_info = models.read_info()
		read_info.user = request.user
		article.no_of_reads += 1
		read_info.article = article
		messages.add_message(request, messages.SUCCESS, "added to read articles")
		article.save()
		read_info.save()
	else:
		messages.add_message(request, messages.INFO, "already read the article")
		
	return HttpResponseRedirect(reverse('home'))


@login_required(login_url="login")
def starring(request, number):
	article = models.articles.objects.get(pk=number)
	try:
		check_article = models.starred_info.objects.get(user=request.user, article=article)
		return HttpResponse("Article already bookmarked")
	except:	
		star_info = models.starred_info()
		star_info.article = article
		star_info.user = request.user
		star_info.save()
		return HttpResponse("Article added to bookmarks")



@login_required(login_url="login")
def unstarring(request, number):
	message = ""
	try: 
		article = models.articles.objects.get(pk=number)
		starred_article = models.starred_info.objects.get(article=article, user=request.user)
		starred_article.delete()
		message = "Article removed from bookmarks"
	except:
		message = "The article is not present in the bookmarks"
	return HttpResponse(message)

@login_required(login_url="login")
def bookmarks(request):
	count = [ i for i in range(int(len(models.starred_info.objects.filter(user=request.user))/10) + 1)]
	return render(request, 'bookmarks.html', {"count": count})

@login_required(login_url="login")
def get_bookmarks(request, number):
	starred_article_info = models.starred_info.objects.filter(user=request.user)[(number - 1) * 10: ]
	starred_article_info = starred_article_info[: min(10, len(starred_article_info))]

	starred_articles = []
	for i in range(len(starred_article_info)):
		starred_articles.append(starred_article_info[i].article)

	t = template.loader.get_template("get_bookmarks.html")
	context = {"articles": starred_articles}
	html = t.render(context)
	return HttpResponse(html)


@login_required(login_url="login")
def edit_article(request, number):
	try:
		article = models.articles.objects.get(pk=number)
		if article.author == request.user:
			if request.method == "POST":
				article.author = request.user
				article.title = request.POST["title"]
				article.content = request.POST["content"]
				article.read_time = request.POST["readtime"]

				if request.POST["image"]:
					article.image = request.POST["image"]
				article.save()

				messages.add_message(request, messages.SUCCESS, "Article edited successfully")
				return HttpResponseRedirect(reverse('your_articles'))
			return render(request, 'edit.html', {"article": article})
		else:
			messages.add_message(request, messages.ERROR, "Request Denied")
			return HttpResponseRedirect(reverse('your_articles'))
	except:
		messages.add_message(request, messages.ERROR, "The article doesn't exist")
		return HttpResponseRedirect(reverse('home'))

	
@login_required(login_url="login")
def search_query(request):
	tags = request.GET['tags']
	print(tags)
	tags_list = []
	word = ""
	for i in range(len(tags)):
		if tags[i].isalpha():
			word += tags[i]
		else:
			tags_list.append(word)
			word = ""

	tags_list.append(word)

	print(tags_list)
	author = User.objects.get(username=request.GET['author'])
	author_articles = models.articles.objects.filter(author=author)
	print(author_articles)
	articles_dict = {}
	for article in author_articles:
		articles_dict[article] = 0
		print(article.tags.all())
		for tag in tags_list:
			for article_tag in article.tags.all():
				if tag == article_tag.name.lower():
					articles_dict[article] += 1
					print("here")
					break

	final_response = []
	for key in articles_dict.keys():
		final_response.append([articles_dict[key], key])
	final_response.sort(key = lambda x: x[0], reverse=True)
	print(final_response)

	another_list = []

	for item in final_response:
		another_list.append(item[1])


	return render(request, 'searchresults.html', {"articles": another_list})
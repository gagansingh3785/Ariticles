from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('write', views.write, name="write"),
    path('', views.user_login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.user_logout, name="logout"),
    path('your_articles', views.your_articles, name="your_articles"),
    path('navbar', views.navbar, name="navbar"),
    path('view_article/<int:id>', views.view_article, name="view_article"),
    path('get_articles/<int:number>', views.get_articles, name="get_articles"),
    path('get_my_articles/<int:number>', views.get_my_articles, name="get_my_articles"),
    path('delete_article/<int:number>', views.delete_article, name="delete_article"),
    path('done_reading/<int:number>', views.done_reading, name="done_reading"),
    path('starring/<int:number>', views.starring, name="starring"),
    path('unstarring/<int:number>', views.unstarring, name="unstarring"),
    path('bookmarks', views.bookmarks, name="bookmarks"),
    path('get_bookmarks/<int:number>', views.get_bookmarks, name="get_bookmarks"),
    path('edit/<int:number>', views.edit_article, name='edit'),
    path('searchquery', views.search_query, name='searchquery'),
]


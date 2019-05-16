from django.urls import path
from dripndry import views

app_name = 'dripndry'

urlpatterns = [
        path('', views.index, name='index'),
	path('index', views.index, name='index'),
	path('about', views.about, name='about'),
        path('gallery', views.gallery, name='gallery'),
        path('contact', views.contact, name='contact'),
	path('welcome', views.welcome, name='welcome'),
	path('user_login', views.user_login, name='user_login'),
	path('user_logout', views.user_logout, name='user_logout'),
	path('register', views.register, name='register'),
	path('ordering', views.ordering, name='ordering'),
	path('success', views.success, name='success'),
	path('admin_login', views.admin_login, name='admin_login'),
	path('post', views.post, name='post'),
	path('post1', views.post1, name='post1'),
	
	
	
	
]#created path in our path

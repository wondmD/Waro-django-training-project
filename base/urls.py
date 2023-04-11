from django.urls import URLPattern, path
from . import views

urlpatterns = [

    path('', views.intropage, name='intro'),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutuser, name="logout"),
    path('register/', views.registerpage, name="register"),
    path('fashion-chat', views.home, name="home"),
    path('post/<str:pk>', views.postroom, name="postroom"),
    path('profile/<str:pk>', views.userprofile, name="user-profile"),

    path('create-post/',views.createPostroom, name="create-post"),
    path('update-post/<str:pk>', views.updatepost, name="update-post" ),
    path('delete-post/<str:pk>', views.deletepost, name="delete-post"),
    path('delete-message/<str:pk>', views.deletemessage, name="delete-message"),
    
    path('gallery', views.gallery, name = "tg-gallery"),
    path('contact', views.contactpage, name = "tg-contact")
]
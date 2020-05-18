from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import delete_view 

urlpatterns = [
    path("",views.index,name="index"),
    path("about.html",views.about,name="about"),
    path("contact.html",views.contact,name="contact"),
    path("product.html",views.product,name="product"),
    path("product2.html",views.product2,name="product2"),
    path("product3.html",views.product3,name="product3"),
    path("bid.html/<int:id>/<int:userid>",views.bid,name="bid"),
    path("sell.html",views.sell,name="sell"),
    path("index.html",views.index,name="index"),
    path("login.html",views.login,name="login"),
    path("signup.html",views.signup,name="signup"),
    path("bid.html/<int:id>/delete",views.delete_view,name="delete" ),  
]



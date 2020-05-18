from django.shortcuts import render,redirect
from .models import Destination,contact_Us
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User,auth
from rest_framework import viewsets
from .serializers import DestinationSerializer,contact_UsSerializer
from django.views.generic.edit import DeleteView
from django.shortcuts import (get_object_or_404, render,HttpResponseRedirect)




class DestinationView(viewsets.ModelViewSet):
      serializer_class = DestinationSerializer
      queryset =Destination.objects.all()

class contact_UsView(viewsets.ModelViewSet):
      serializer_class =contact_UsSerializer
      queryset = contact_Us.objects.all()


# Create your views here.
def index(request):
    dests=Destination.objects.all()[:8]
    return render(request,"index.html",{'dests':dests})
def about(request):
    return render(request,"about.html")
def contact(request):
    if request.method=="POST":
        first_name=request.POST['First Name']
        last_name=request.POST['Last Name']
        email=request.POST['email']
        msg=request.POST['msg']
        queries=contact_Us.objects.create(first_name=first_name,last_name=last_name,email=email,msg=msg)
        queries.save()
        print("msg sent successfully")
        return redirect('/')
    else:
         return render(request,"contact.html")
def product(request):
    pros=Destination.objects.all()[8:20]
    return render(request,"product.html",{'pros':pros})

def product2(request):
    pros=Destination.objects.all()[20:32]
    return render(request,"product2.html",{'pros':pros})

def product3(request):
    pros=Destination.objects.all()[32:]
    return render(request,"product3.html",{'pros':pros})

def bid(request,id,userid):
    if request.method=="POST":

        quoted_price=request.POST['bidamt']
        user=User.objects.get(id=userid)
        user_fname=user.first_name
        user_lname=user.last_name
        user_email=user.email
        user_name=user.username
        seller=Destination.objects.get(id=id)

        pro_name=seller.name
        seller_fname=seller.seller_fname
        seller_lname=seller.seller_lname
        seller_email=seller.email

        subject = 'Regarding product bidding on haggle.com'
        message = user_fname+" "+user_lname+' is interested in your  '+pro_name +' \nhere are the details of the bid\nquoted price: '+ quoted_price+' \nemailid: '+user_email+'\n'+'\nWith Regards\n'+'Haggle Team'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [seller_email]
        send_mail( subject, message, email_from,[seller_email,])
        print("bid placed successfully")
        return redirect('/')
    else:
        proid=Destination.objects.get(id=id)
        return render(request,"bid.html",{'proid':proid})


def sell(request):
    if request.method=="POST":
        name=request.POST['product Name']
        img=request.FILES['product img']
        desc=request.POST['product description']
        price=request.POST['product price']
        seller_fname=request.POST['First Name']
        seller_lname=request.POST['Last Name']
        email=request.POST['email']

        sellers=Destination.objects.create(name=name,img=img,desc=desc,price=price,seller_fname=seller_fname,seller_lname=seller_lname,email=email)
        sellers.save()
        print("product displayed")
        return redirect('/')
    else:
         return render(request,"sell.html")
    return render(request,"/")

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

# delete view for details
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(Destination, id = id)


    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)








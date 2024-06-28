from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignUpForm, PageForm
from .models import Client, Page, Comment, Product, Review, Event, Booking, Order
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
import json
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

 # ---------------------------<<------------USER & BUYER VIEWS--------------->>--------------------
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            Client.objects.create(
                user = User.objects.get(username=request.POST['username']),
                address = request.POST['address'],
                phonenumber = request.POST['phonenumber']
            )
            print("--------------------User Client saved!------------------")
            error = ""
            return render(request, 'main/login.html')
        else:
            myerrors = form.errors
            print(myerrors)
            return render(request, "main/signup.html", {"form": form})
    else:
        form = SignUpForm()
        return render(request, "main/signup.html", {"form": form})

def mylogin(request):
    logout(request)
    if request.method == "POST":
        formdata = request.POST
        user = authenticate(username=formdata['username'], password=formdata['password'])
        if user is not None:
            # the password verified for the user
            if user.is_active:
                login(request, user)
                # User is valid, aunthenticated and active
                return redirect("/")
            else:
                error = "Password is valid, but user has been deactivated!"
                print(error)
                return render(request, 'main/login.html', {"error": error})
                #Password is valid, but user has been deactivated!
        else:
            # the authentication system was unable to verify the username and password
            error = "The username and password were incorrect."
            print(error)
            return render(request, 'main/login.html', {"error": error, "info":''})
    else:
        return render(request, 'main/login.html', {"error": "", "info": ''})


def logoutNOW(request):
    logout(request)
    info = "Lets login, the site isnt the same without you!"
    return render(request, 'main/login.html', {"info": info, "error":''})

def productview(request, product_id):
    u = request.user
    if u.is_authenticated:
        if request.method == "POST":
            formdata = request.POST
            if formdata["type"] == "order":
                Order.objects.create(
                    user = u,
                    product=Product.objects.get(pk=product_id),
                    quantity=formdata["quantity"]
                )
                return render(request, "main/order.html", {"product" : Product.objects.get(pk=product_id), "quantity" : formdata["quantity"]})
            else:
                Review.objects.create(
                    by = u,
                    product = Product.objects.get(pk=product_id),
                    content = formdata["content"]
                )
                return redirect("/products/%s/" % product_id)
        else:
            product = Product.objects.get(pk=product_id)
            return render(request, 'main/shop-item.html', {"product" : product, "reviews" : Review.objects.filter(product = product)})
    else:
        return redirect("/login/")

def shopview(request):
    u = request.user
    if u.is_authenticated:
        context = {"products" : Product.objects.order_by("post_date").filter(enabled=True)}
        return render(request, 'main/shop-homepage.html', context)
    else:
        return redirect("/login/")

def events(request):
    u = request.user
    if u.is_authenticated:
        context = {"events" : Event.objects.order_by("event_date")}
        return render(request, 'main/events.html', context)
    else:
        return redirect("/login/")

def eventview(request, event_id):
    u = request.user
    if u.is_authenticated:
        if request.method == "POST":
            formdata = request.POST
            Booking.objects.create(
                user = u,
                event = Event.objects.get(pk=event_id),
                information = formdata["information"]
            )
            return redirect("/events/%s/" % event_id)
        else:
            return render(request, 'main/event.html')
    else:
        return redirect("/login/")

def about(request):
    return render(request, 'about.html')

def blog(request):
    context = {"pages" : Page.objects.order_by("publish_date").filter(enabled=True)}
    return render(request, 'main/blog.html', context)

def pageview(request, page_name):
    u = request.user
    if u.is_authenticated:
        if request.method == "POST":
            formdata = request.POST
            Comment.objects.create(
                by = u,
                page = Page.objects.get(short_name=page_name),
                content = formdata["content"]
            )
            return redirect("/blog/%s/" % page_name)
        else:
            page = Page.objects.get(short_name=page_name)
            comments = Comment.objects.filter(page = page)
            return render(request, 'main/post.html', {"page" : page, "comments" : comments})
    else:
         return redirect("/login/")


def index(request):
    return render(request, 'main/about.html')

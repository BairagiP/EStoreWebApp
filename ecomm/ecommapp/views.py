from django.shortcuts import render,HttpResponse,redirect
from django.views import View #V capital class hai #buit-in for class view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from ecommapp.models import Product
from django.db.models import Q
# Create your views here.
def home(request):
    context={}
    context['name']='John'
    context['age']=45
    context['x']=44
    context['y']=88
    context['list']=[1,2,3,4]
    if context['x']>context['y']:
        context['res']=context['x']
    else:
        context['res']=context['y']    
    context['products']=[
        {'id':1, 'name': 'samsung', 'cat': 'mobile', 'price':20000},
        {'id': 2, 'name': 'jeans', 'cat': 'cloth', 'price':1000},
        {'id':3, 'name': 'adidas shoes', 'cat': 'shoes','price':5000},
        {'id':4, 'name': 'vivo', 'cat': 'mobile', 'price':15000}
    ]
    # return HttpResponse("This is HomePage")
    return render(request,'hello.html',context)
def home2(request):
    userid=request.user.id
    # print("user id =",userid)
    context={}
    # context['title']="HomePage"
    p=Product.objects.filter(is_Active=True)
    context['products']=p
    # print(p)
    # print(p[0])
    # print(p[0].price,p[0].category)
    return render(request,'index.html',context)
def home3(request):#gives all inactive included
    context={}
    p=Product.objects.all()
    context['products']=p
    return render(request,'index.html',context)
def catfilter(request,cv):
    q1=Q(is_Active=True)
    q2=Q(category=cv)
    p=Product.objects.filter(q1&q2)
    context={}
    context['products']=p
    return render(request,'index.html',context)
def registration(request):
    if request.method=='POST':
        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        if uname=="" or upass=="" or ucpass=="":
            context['errmsg']="field cannot be empty"
            return render(request,"registration.html",context)
        elif upass != ucpass:
            context['errmsg']="Passwword and confirm password didnot match"
            return render(request,"registration.html",context)
        elif len(upass) != len(ucpass):
            context['errmsg']="Password length didn't match"
            return render(request,"registration.html",context)          
        else: 
            try:
                u=User.objects.create(username=uname,email=uname)
                u.set_password(upass)
                u.save()
                context['success']="User Created Successfully!!"
                return render(request,"registration.html",context)
            except:
                context['errmsg']="User with username already exists"        
                return render(request,"registration.html",context)
        # return HttpResponse(request,"user created successfully")
    else:
        return render(request,'registration.html')
    return render(request,'registration.html')
def login_user(request):
    context={}
    if request.method=='POST':
        uname=request.POST['uname']
        upass=request.POST['upass']
        if uname=="" or upass=="" :
            context['errmsg']="field cannot be empty"
            return render(request,"login.html",context)
        else:
            u=authenticate(username=uname,password=upass)
            # print(u)
            # print(u.email)
            # print(u.is_superuser)
            # return HttpResponse("in else part ")
            if u is not None:
                login(request,u)#starts session and id iis created for logged in user
                return redirect("/home2")
            else:
                context['errmsg']="Invalid credentails check it"
    return render(request,'login.html')
def user_logout(request):
    logout(request)
    return redirect("/home2")
def product_detail(request):
    return render(request,'product_detail.html')
def place_order(request):
    return render(request,'place_order.html')
def about(request):
    # return HttpResponse("About PAGE")
    return render(request,'about.html')
def contact(request):
    # return HttpResponse("Contact PAGE")
    return render(request,'contact.html') 
def cart(request):
    return render(request,'cart.html')
def addition(request,a,b):
    add=int(a)+int(b)

class SimpleView(View):#class based views ki class se return ho
    def get(self,request):#compulsory get method,and set method.
        return HttpResponse("Hello from simple View")
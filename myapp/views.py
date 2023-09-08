from django.shortcuts import render,redirect
from myapp.models import categorydb,productdb,contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.
def index(req):
    return render(req,"Index.html")

def Category(req):
    return render(req,"AddCategory.html")

def Categorysave(req):
    if req.method == "POST":
        na = req.POST.get('catname')
        img = req.FILES['image']
        des = req.POST.get('description')
        obj1 = categorydb(Name= na, Image= img, Description= des)
        obj1.save()
        messages.success(req,"Category Saved Successfully!!!")
        return redirect(Category)

def Categorydisplay(req):
    data = categorydb.objects.all()
    return render(req,"CategoryDisplay.html",{'data':data})

def Categoryedit(req,dataid):
    data = categorydb.objects.get(id=dataid)
    return render(req,"CategoryEdit.html",{'data':data})

def Categoryupdate(req,dataid):
    if req.method == "POST":
        na = req.POST.get('catname')

        des = req.POST.get('description')

        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)

        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=dataid).Image
        categorydb.objects.filter(id=dataid).update(Name= na,Description=des,Image=file)
        messages.success(req,"Saved Succesfully")
        return redirect(Categorydisplay)

def Categorydelete(req,dataid):
    data = categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(Categorydisplay)

def product(req):
    data = categorydb.objects.all()
    return render(req,"AddProduct.html",{'data':data})

def Productsave(req):
    if req.method == "POST":
        sel = req.POST.get('select')
        prodna = req.POST.get('prodname')
        price = req.POST.get('price')
        des = req.POST.get('description')
        brand = req.POST.get('brand')
        img = req.FILES['image']

        obj = productdb(Select = sel , Product = prodna,Price = price ,Description = des,Brand = brand,Image = img)
        obj.save()
        messages.success(req,"Product Saved Successfully!!")
        return redirect(product)

def Productdisplay(req):
    product = productdb.objects.all()
    messages.success(req,"Loaded Succesfully!!")
    return render(req,"ProductDisplay.html",{'product': product})

def Productedit(req,productid):
    data = categorydb.objects.all()
    product = productdb.objects.get(id=productid)

    return render(req,"ProductEdit.html",{'data':data, 'product': product})

def Productupdate(req,productid):
    if req.method == "POST":
        sel = req.POST.get('select')
        prodna = req.POST.get('prodname')
        price = req.POST.get('price')
        des = req.POST.get('description')
        brand = req.POST.get('brand')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)

        except MultiValueDictKeyError:
            file = productdb.objects.get(id=productid).Image
        productdb.objects.filter(id=productid).update(Select = sel , Product = prodna,Price = price ,Description = des,Brand = brand,Image=file)
        messages.success(req,"Successfully Updated")
        return redirect(Productdisplay)

def Productdelete(req,productid):
    product = productdb.objects.filter(id=productid)
    product.delete()
    return redirect(Productdisplay)

def adminlogin(req):
    return render(req,"LoginPage.html")

def admin_loginpage(req):
    if req.method=="POST":
        uname = req.POST.get('username')
        pwd = req.POST.get('password')
        if User.objects.filter(username__contains= uname).exists():
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                login(req,user)

                req.session['username']=uname
                req.session['password']=pwd
                messages.success(req, "Login Succesful!!")
                return redirect(index)
            else:
                messages.error(req,"Invalid Password/Username")
                return redirect(adminlogin)
        else:
            messages.error(req,"Invalid Credentials")
            return redirect(adminlogin)

def admin_logout(req):
    del req.session['username']
    del req.session['password']
    return redirect(adminlogin)

def Displaycontact(req):
    contact = contactdb.objects.all()
    return render(req,"DisplayContact.html",{'contact':contact})
def Contactdelete(req,contactid):
    contact = contactdb.objects.filter(id=contactid)
    contact.delete()
    return redirect(Displaycontact)
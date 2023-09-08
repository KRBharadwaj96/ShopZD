from django.shortcuts import render,redirect
from myapp.models import categorydb,productdb,contactdb
from Webapp.models import registerdb,cartdb,checkoutdb
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def Home(req):
    data = categorydb.objects.all()
    return render(req,"Home.html",{'data':data})

def About(req):
    data = categorydb.objects.all()
    return render(req,"About.html",{'data':data})

def Contact(req):
    data = categorydb.objects.all()
    return render(req,"Contact.html",{'data':data})

def Contact_save(req):
    if req.method == "POST":
        fname= req.POST.get('c_fname')
        lname= req.POST.get('c_lname')
        email= req.POST.get('c_email')
        subject= req.POST.get('c_subject')
        message= req.POST.get('c_message')
        obj1 = contactdb(Fname= fname, Lname= lname, Email= email, Subject= subject, Message= message)
        obj1.save()
        return redirect(Contact)

def Product(req, cat_name):
    data = categorydb.objects.all()
    prod = productdb.objects.filter(Select=cat_name)
    return render(req,"Product.html",{'data':data,'prod':prod})

def Singleproduct(req,dataid):
    data = categorydb.objects.all()
    prod = productdb.objects.all()
    prod_single = productdb.objects.filter(id=dataid)
    return render(req,"SingleProduct.html",{'data':data,'prod_single':prod_single,'prod':prod})

def Cart(req):
    data1 = cartdb.objects.filter(Uname=req.session['username'])
    data = categorydb.objects.all()
    return render(req,"Cart.html",{'data1':data1,'data':data})

def Cart_Save(req):
    # prod = productdb.objects.all()
    # prod_single = productdb.objects.filter(id=dataid)
    if req.method == "POST":
        usename= req.POST.get('uname')
        pdname = req.POST.get('product')
        desc = req.POST.get('description')
        qty = req.POST.get('quantity')
        prce = req.POST.get('tprice')
        # try:
        #     img = req.FILES['pdimage']
        #     fs= FileSystemStorage()
        #     file=fs.save(img.name,img)
        # except MultiValueDictKeyError:
        #     file=productdb.objects.get()
        obj2 = cartdb(Uname= usename, Prod_name= pdname, Description= desc, Quantity= qty, Price= prce)
        obj2.save()
        messages.success(req,"Added to Cart Succesfully!")
        return redirect(Cart)

def Cartdelete(req,dataid):
    data= cartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(Cart)

def Checkout(req):
    cart = cartdb.objects.all()
    return render(req,"checkout.html",{'cart':cart})

def Checkout_save(req):
    if req.method == "POST":
        cntry = req.POST.get('country')
        name = req.POST.get('c_fname')
        add = req.POST.get('c_address')
        state = req.POST.get('c_state')
        zip = req.POST.get('c_postal_zip')
        email = req.POST.get('c_email')
        mob = req.POST.get('c_phone')
        obj = checkoutdb(Country= cntry,Fname=name,Address=add ,State=state,Zip= zip, Email= email, Mobile=mob)
        obj.save()
        messages.success(req,"Order Placed Successfully!!")
        return redirect(Home)

def Register(req):
    return render(req,"Registeration.html")
def RegisterB(req):
    return render(req,"RegisterB.html")
def Register_save(req):
    if req.method == "POST":
        uname = req.POST.get('name')
        mail = req.POST.get('email')
        mob = req.POST.get('mobile')
        pwd = req.POST.get('password')
        img = req.FILES['image']
        obj = registerdb(Name=uname, Email= mail, Mobile=mob, Password=pwd ,Image=img)
        obj.save()
        messages.success(req,"Registered Successfully!!")
        return redirect(Register)

def Userlogin(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        if registerdb.objects.filter(Email = uname, Password = pwd).exists():
            request.session['username']=uname
            request.session['password']=pwd
            messages.success(request,"Login Successfull")
            return redirect(Home)
        else:
            messages.error(request,"Invalid Username/Password")
            return redirect(Register)

    return redirect(Register)

def Userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(Register)



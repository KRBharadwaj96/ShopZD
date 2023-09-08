from django.urls import path
from Webapp import views

urlpatterns= [
    path('home/',views.Home,name="Home"),
    path('about/',views.About,name="About"),
    path('contact/',views.Contact,name="Contact"),
    path('product/<cat_name>/',views.Product,name="Product"),
    path('singleproduct/<int:dataid>/',views.Singleproduct,name="Singleproduct"),
    path('contact_save/',views.Contact_save,name="Contact_save"),

    path('register/',views.Register,name="Register"),
    path('registerb/',views.RegisterB,name="RegisterB"),
    path('register_save/',views.Register_save,name="Register_save"),
    path('Userlogin/',views.Userlogin,name="Userlogin"),
    path('Userlogout/',views.Userlogout,name="Userlogout"),

    path('Cart/',views.Cart,name="Cart"),
    path('Cartsave/',views.Cart_Save,name="Cart_Save"),
    path('Cartdelete/<int:dataid>/',views.Cartdelete,name="Cartdelete"),
    path('Checkout/',views.Checkout,name="Checkout"),
    path('Checkout_save/',views.Checkout_save,name="Checkout_save"),



]
from django.urls import path
from myapp import views


urlpatterns = [
    path('index/',views.index,name="index"),
    path('category/',views.Category,name="Category"),
    path('categorysave/',views.Categorysave,name="Categorysave"),
    path('categorydisplay/',views.Categorydisplay,name="Categorydisplay"),
    path('categoryedit/<int:dataid>/',views.Categoryedit,name="Categoryedit"),
    path('categoryupdate/<int:dataid>/',views.Categoryupdate,name="Categoryupdate"),
    path('categorydelete/<int:dataid>/',views.Categorydelete,name="Categorydelete"),

    path('product/', views.product, name="product"),
    path('productsave/', views.Productsave, name="Productsave"),
    path('productdisplay/', views.Productdisplay, name="Productdisplay"),
    path('productedit/<int:productid>/', views.Productedit, name="Productedit"),
    path('productupdate/<int:productid>/', views.Productupdate, name="Productupdate"),
    path('productdelete/<int:productid>/', views.Productdelete, name="Productdelete"),

    path('login/',views.adminlogin,name="adminlogin"),
    path('admin_login/', views.admin_loginpage, name="admin_loginpage"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),

    path('Displaycontact/',views.Displaycontact,name="Displaycontact"),
    path('Contactdelete/<int:contactid>/',views.Contactdelete,name="Contactdelete"),
]

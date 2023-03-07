from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name="home"),
    path('collections',views.collections,name="collections"),
    path('register',views.register,name="register"),
    path('collections/<str:name>',views.collectionsview,name="collections"),
    path('collections/<str:cname>/<str:pname>',views.productdetails,name="productdetails"),

   


]
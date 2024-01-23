from django.urls import path
from . import views
from customer.views import CustomerListing
from .views import upload_image

urlpatterns = [
   path('',views.login,name="login"),
   path('home',views.home,name="home"),

   path('signup',views.signup,name="signup"),
   path('login',views.login,name="login"),
   path('upload', upload_image, name='upload_image'),
   path(r'registrationlist',CustomerListing.as_view(),name='registrationlist'),
   

   path('delete_profile/<int:Id>',views.delete_Profile, name='delete_profile'),






  ]

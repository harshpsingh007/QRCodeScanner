from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('contact',views.Contact,name="Contact"),
    path('about',views.About,name="About"),
    path('add',views.Add,name="Add"),
    path('subtract',views.Subtract,name="Subtract"),
    path('adding',views.Adding,name="Adding"),
    path('subtracting',views.Subtracting,name="Subtracting"),
]
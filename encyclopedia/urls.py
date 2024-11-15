from django.urls import path

from . import views

urlpatterns = [
    
    path("", views.index, name="index"),
    path("searchentry",views.search,name='searchentry'),
    path("opennew",views.opennew,name='opennew'),
    path("createnewpage",views.createnewpage,name='createnewpage'),
    path("wiki/<str:name>",views.title,name='title'),
    path("edit",views.edit,name='edit'),
  
  
    
]

from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='orderslisting'),
    path('createorder', views.create_order,name='createorder'),


]

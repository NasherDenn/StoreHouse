from django.contrib import admin
from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('unit_add/', views.unit_add, name='unit_add'),
    path('create/', views.create, name='create'),
    path('admin/', admin.site.urls),
    path('logout/', views.login, name='logout'),

]

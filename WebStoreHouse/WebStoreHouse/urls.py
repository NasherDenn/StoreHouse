from django.contrib import admin
from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.login, name='login'),
    path('admin/', admin.site.urls),
    path('logout/', views.login, name='logout'),
    path('filter/', views.filter, name='filter'),
]

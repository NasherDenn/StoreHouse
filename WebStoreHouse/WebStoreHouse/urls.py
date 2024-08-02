from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, re_path
from catalog import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('unit_add/', views.unit_add, name='unit_add'),
    path('choice_unit_edit/', views.choice_unit_edit, name='choice_unit_edit'),
    path('choice_unit_delete/', views.choice_unit_delete, name='choice_unit_delete'),
    path('create/', views.create, name='create'),
    path('unit_update/', views.unit_update, name='unit_update'),
    path('unit_edit/<int:id>/', views.unit_edit, name='unit_edit'),
    path('unit_delete/<int:id>/', views.unit_delete, name='unit_delete'),
    path('unit_del/', views.unit_del, name='unit_del'),
    path('unit_send/', views.unit_send, name='unit_send'),
    path('admin/', admin.site.urls),
    path('logout/', views.login, name='logout'),

]

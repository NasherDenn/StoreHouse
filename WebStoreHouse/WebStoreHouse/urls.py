from django.contrib import admin
# from django.template.defaulttags import url
from django.urls import path
from catalog import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('unit_update/', views.unit_update, name='unit_update'),
    path('unit_edit/<int:id>/', views.unit_edit, name='unit_edit'),
    path('unit_delete/<int:id>/', views.unit_delete, name='unit_delete'),
    path('unit_history/<int:first_id>/', views.unit_history, name='unit_history'),
    path('forms_send/', views.forms_send, name='forms_send'),
    path('send_excel/', views.send_excel, name='send_excel'),
    path('admin/', admin.site.urls),
    path('logout/', views.login, name='logout'),
]

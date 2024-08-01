from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, re_path
from catalog import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('unit_add/', views.unit_add, name='unit_add'),
    path('choice_unit_edit/', views.choice_unit_edit, name='choice_unit_edit'),
    path('create/', views.create, name='create'),
    path('unit_update/', views.unit_update, name='unit_update'),
    path('unit_edit/<int:id>/', views.unit_edit, name='unit_edit'),
    path('admin/', admin.site.urls),
    path('logout/', views.login, name='logout'),

]

# urlpatterns += [
#     url(r'unit_edit/(?P<pk>\d+)$', views.unit_edit, name='unit_edit'),
#     ]

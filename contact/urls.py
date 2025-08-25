from django.urls import path
from . import views

from .views import contact_list,create_contact,update_contact,delete_contact,view_contact

urlpatterns=[
    path('', views.home, name='home'),
    path('api/',contact_list,name='contacts'),
    path('create-contact/',create_contact,name='create'),
    path('update-contact/<int:id>/',update_contact,name='update'),
    path('delete-contact/<int:id>/',delete_contact,name='delete'),
    path('view-contact/<int:id>/',view_contact,name='view'),
    ]



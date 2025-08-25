from django.shortcuts import render
from .serializer import Contactserializer
from .models import Contact
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def home(request):
    return render(request,'home.html')

@api_view(['GET'])  #read
def contact_list(request):
    contacts=Contact.objects.all()
    serializer=Contactserializer(contacts,many=True)
    return Response(serializer.data)

@api_view(['POST']) #create
def create_contact(request):
    serializer=Contactserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])  #update
def update_contact(request,id):
    Contacts=Contact.objects.get(id=id)
    serializer=Contactserializer(instance=Contacts,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])#delete
def delete_contact(request,id):
    contacts=Contact.objects.get(id=id)
    contacts.delete()
    return Response('item deleted successfully..!')
 
 
@api_view(['GET'])  #get specific data
def view_contact(request,id):
    Contacts=Contact.objects.get(id=id)
    serializer=Contactserializer(Contacts)
    return Response(serializer.data)
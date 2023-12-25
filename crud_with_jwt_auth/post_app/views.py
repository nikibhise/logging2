from .models import Hotel
from .serializers import HotelSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.shortcuts import get_object_or_404


def create_guest(request):
    try:
        serializer = HotelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'detail': 'Error processing request'}, status=status.HTTP_400_BAD_REQUEST)
    
def show_guset(request):
    try:
           guest = Hotel.objects.all()
           serializer = HotelSerializer(guest, many=True)
           return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
         return Response(data={'detail': 'Error fetching request'}, status=status.HTTP_400_BAD_REQUEST)
    
def update_guest(request, pk=None):
    try:
          guest = get_object_or_404(Hotel, pk=pk)
          if request.method == 'PUT':
                serializer = HotelSerializer(data=request.data, instance=guest)
          if request.method == 'PATCH':
               serializer.is_valid(raise_exception=True)
               serializer.save()
               return Response(data=serializer.data, status=status.HTTP_200_ok)
    except Exception as e:
         return Response(data={'deatil': 'Error fetching request'}, status=status.HTTP_400_BAD_REQUEST)
    
def delete_guest(request, pk=None):
     try:
          guest = get_object_or_404(Hotel, pk=pk)  
          guest.delete()
          return Response(data={'detail': 'Guest deleted Successfully'}, status=status.HTTP_200_OK)
     except Exception as e:
             return Response(data={'detail':'Guest deleting person'}, status=status.HTTP_400_BAD_REQUEST)
          

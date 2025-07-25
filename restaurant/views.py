from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Menu, Booking
from .serializers import UserSerializer, MenuItemSerializer, BookingSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

# class MenuItemsView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Menu.objects.all()
#     serializer_class = MenuItemSerializer

# class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuItemSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})
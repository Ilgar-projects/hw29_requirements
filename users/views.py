import http
import json
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad, Category
from users.models import User, Location
from users.serializers import *


class UserPagination(PageNumberPagination):
    page_size = 6


class LocationViewSet(ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class UserDetailView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListView(ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.annotate(total_ads=Count("ad", filter=Q(ad__is_published=True))).order_by('username')
    # order_by('username') сортировка по username
    pagination_class = UserPagination

class UserDeleteView(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateView(UpdateAPIView):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()


class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


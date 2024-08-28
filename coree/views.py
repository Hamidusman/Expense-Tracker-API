from django.shortcuts import render
from .models import Category, Expense
from .serializers import CategorySerializer, ExpenseSerializer
from rest_framework import generics, filters

from django_filters.rest_framework import DjangoFilterBackend
from .filters import ExpenseFilter
# Create your views here.

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ExpenseView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ExpenseFilter

    ordering_fields = '__all__'
    ordering = ['date']
from django.shortcuts import render
from .models import Category, Expense
from .serializers import CategorySerializer, ExpenseSerializer
from rest_framework import generics
# Create your views here.

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ExpenseView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
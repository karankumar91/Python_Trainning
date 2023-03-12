from django.shortcuts import render
from .models import student
from .serializer import StudenSerilizer
from rest_framework import viewsets

# Create your views here.
class studentview(viewsets.ModelViewSet):
    queryset=student.objects.all()
    serializer_class=StudenSerilizer

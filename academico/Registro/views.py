from django.shortcuts import render

# Create your views here.
#------------- importacines API ---------------------
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarreraSerializer
from django.shortcuts import render, redirect, get_object_or_404
 

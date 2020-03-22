from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import  api_view
from rest_framework.response import Response
from rest_framework import  status
from django.http import  JsonResponse
from rest_framework.parsers import  JSONParser
from .models import price
from .serializers import PriceSerializer
from black_friday import sale
import pickle
import json
from pyforest import *
from sklearn.preprocessing import StandardScaler
# Create your views here.

class PriceView(viewsets.ModelViewSet):
    queryset = price.objects.all()
    serializer_class = PriceSerializer
    def create(self, request, *args, **kwargs):
        super(PriceView, self).create(request, *args, **kwargs)
        ob = price.objects.latest('id')
        y = sale.pred(ob)
        return Response({"status":"Success", "The Customer will Spend amount ":y,'tem':args})
'''
#@api_view(['POST'])
def contact(request):
    if request.method =='POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
            User_ID = form.cleaned_data['user_id']
            Product_ID = form.cleaned_data['product_id']
            Gender = form.cleaned_data['gender']
            Age = form.cleaned_data['age']
            Occupation = form.changed_data['occupation']
            City_Category = form.cleaned_data['city_category']
            Stay_In_Current_City_Years = form.cleaned_data['stay_in_current_city_years']
            Marital_Status = form.cleaned_data['marital_status']
            Product_Category_1 = form.cleaned_data['product_category_1']
            Product_Category_2 = form.cleaned_data['product_category_2']
            Product_Category_3 = form.cleaned_data['product_category_3']
'''
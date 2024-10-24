from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Data_analysis(request):  
   return render(request,'data_analysis/data_analysis.html')

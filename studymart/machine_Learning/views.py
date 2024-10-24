from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def machine_learning(request):
    course='Machine learning'
    tclass=21
    seat=20
    cduration='2.5 months'


    offering={'c' : course,'tc':tclass,'st':seat,'cd':cduration}
    return render(request,'machine_learning/machine_learning.html',context=offering)


def random_forest(request):
    return render(request,'machine_learning/random_forest.html')
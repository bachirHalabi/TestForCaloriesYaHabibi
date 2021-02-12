from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from .models import CalcField
# Create your views here.


def home(request):
    if request.method == 'POST':
        age = request.POST['a']
        height = request.POST['h']
        weight = request.POST['w']
        user = User.objects.first()
        calorie_res = CalcField.objects.create(
            age=age,
            height=height,
            weight=weight,
            created_by=user, )
    return render(request,'base.html')

def front(request):
    return render(request,'front.html')
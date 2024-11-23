from django.shortcuts import render
from .models import Car
import pandas as pd

def main_view(request):
    
    cars = Car.objects.all().values()
    data = pd.DataFrame(cars, columns=['brand', 'model', 'max_speed', 'country'])
    describe_data = data.describe()
    
    context = {
        'cars': cars,
        'data' : data.to_html(),
        'describe_data' : describe_data.to_html()
    }
    
    return render(request, 'car/main.html', context)
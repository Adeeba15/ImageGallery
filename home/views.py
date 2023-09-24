from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.
def example_fun(request):
    tasks= Task.objects.all()  #SELECT * FROM Task
    # response=""
    # for item in tasks:
    #     response+=item.name
    # can be done as
    response = ",".join([task.title for task in tasks])
    return HttpResponse(response)


#create a model for storing info about places for 10 values
#models.py =>new fun=> urls.py=>views.py
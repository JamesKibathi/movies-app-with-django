from django.http import HttpResponse
from django.shortcuts import render

data ={
    'movies':[
        {
            "id":5,
            "title":"Olympus has fallen",
            "year":2012
            
        },
        {
             "id":2,
            "title":"Dynasty",
            "year":2008
        },
        {
             "id":3,
            "title":"Wednesday",
            "year":2022
        }
       
        ]
}

def movies(request):
    return render(request,'movies/movies.html',data)

def home(request):
    return HttpResponse("Home page")
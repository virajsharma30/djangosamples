from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
    'author':  'viraj' ,
    'title': 'a day'
    },
    {
    'author':  'harsh' ,
    'title': 'a night'
    },
     {
    'author':  'dev' ,
    'title': 'an after noon'
    }
]



def posted(request):
    context={
        'posts':posts
    }
    return render(request,'posts.html',context)





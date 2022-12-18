from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def menuitems(request,dish):
    items={'pasta':'Bildiğin makarna','falafel':'Nohuttan köfte', 'cheesecake':'Peynirlide kek oluyormuş'
    
    }

    description=items[dish]

    return HttpResponse(f"<h2>{dish}</h2>" + description)

from django.shortcuts import render
from .models import *

# Create your views here.
'''
Home view :- display the home page. If logged in, display the Firstname
'''
def home(request):
    is_logged_in = 0
    if not request.session.get("username") == None:
        is_logged_in = 1
    #add additional fields to find more user details and send to the frontend
    template = 'new_home.html'
    returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username")}
    return render(request, template, returnDict) 

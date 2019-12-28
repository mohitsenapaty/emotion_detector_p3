from django.shortcuts import render
from utils.doAuth import *

# Create your views here.
def startlecturepageuser(request, lectureid):
    context = locals()
    #do authentication
    authObject = userAuth(request)
    if authObject.get('is_logged_in') == 0:
        pass
    template = 'lectureforuser1.html'
    return render(request, template, authObject)
    pass

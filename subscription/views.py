from django.shortcuts import render
import datetime as dt
import dateutil.parser
import hashlib
from django.http import JsonResponse
from utils.doAuth import *
from utils import subscriptionServices
import random
from pytz import timezone 
from .models import *

# Create your views here.
'''
view all courses
'''
def viewallcourses(request):
    context = locals()
    #do authentication
    authObject = userAuth(request)
    if authObject.get('is_logged_in') == 0:
        pass
    #courseList = 
    offset = request.POST.get('offset', 0)
    limit = request.POST.get('limit', 0)
    allcourses = subscriptionServices.getAllCourses(offset, limit)
    allcourses['is_logged_in'] = authObject.get('is_logged_in')
    allcourses['userobject'] = authObject.get('userobject')
    template = 'viewcourseall.html'
    return render(request, template, allcourses)
    pass
    

'''
view subscribed courses
'''
def viewsubscribedcourses(request):
    context = locals()
    #do authentication
    authObject = userAuth(request)
    if authObject.get('is_logged_in') == 0:
        pass
    #courseList = 
    offset = request.POST.get('offset', 0)
    limit = request.POST.get('limit', 0)
    _id = authObject.get('userobject').get('id')
    allcourses = subscriptionServices.getAllCoursesSubscribed(offset, limit, _id)
    allcourses['is_logged_in'] = authObject.get('is_logged_in')
    allcourses['userobject'] = authObject.get('userobject')
    template = 'viewcourseall.html'
    return render(request, template, allcourses)
    pass
    
    
'''
subscribe to a course
'''
def subscribetocourse(request, courseid):
    context = locals()
    #do authentication
    authObject = userAuth(request)
    if authObject.get('is_logged_in') == 0:
        pass
    if not request.POST.get('type'):
        template = 'subscribecourse.html'
        return render(request, template, authObject)
    _id = authObject.get('userobject').get('id')
    subscribed = subscriptionServices.subscribeUserToCourse(_id, courseid, request.POST)
    subscribed['is_logged_in'] = authObject.get('is_logged_in')
    subscribed['userobject'] = authObject.get('userobject')
    subscribed['courseid'] = courseid
    template = 'subscribecourse.html'
    return render(request, template, subscribed)
    pass


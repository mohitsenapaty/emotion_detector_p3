from django.shortcuts import render
import datetime as dt
import dateutil.parser
import hashlib
from django.http import JsonResponse
from utils.doAuth import *
import random
from pytz import timezone 
from .models import *

# Create your views here.
'''
create a course
'''
def createcourse(request):
    context = locals()
    #do authentication
    authObject = userAuth(request)
    if authObject.get('is_logged_in') == 0:
        pass
    authObjectTeacher = teacherMethodsAuth(request)
    if authObjectTeacher.get('isAllowed') == False:
        pass
    if request.POST.get('title') == None:
        template = 'createcourse.html'
        return render(request, template, authObject)
    _id = authObject.get('userobject').get('id')
    createdCourse = createCourseForTeacher(request.POST, _id)
    createdCourse['is_logged_in'] = authObject.get('is_logged_in')
    createdCourse['userobject'] = authObject.get('userobject')
    template = 'createcourse.html'
    return render(request, template, createdCourse)

'''
fetch all active course of a teacher
'''
def getallcourseforteacher(request):
    context = locals()
    #do authentication
    authObject = userAuth(request)
    if authObject.get('is_logged_in') == 0:
        pass
    authObjectTeacher = teacherMethodsAuth(request)
    if authObjectTeacher.get('isAllowed') == False:
        pass
    _id = request.session.get("id")
    allcourses = getAllCoursesForTeacherById(_id)
    allcourses['is_logged_in'] = authObject.get('is_logged_in')
    allcourses['userobject'] = authObject.get('userobject')
    template = 'viewcourse.html'
    return render(request, template, allcourses)
    pass

'''
fetch a single course by id
'''
def getcoursedetail(request):
    pass

'''
delete a course
'''
def deletecourse(request):
    pass


'''
Utility functions
'''
def createCourseForTeacher(createObj, _courseof):
    try:
        _courseid = "CRS" + str(random_with_N_digits(9))
        _title = createObj.get("title")
        _description = createObj.get("description")
        _subject = createObj.get("subject")
        _designedfor = createObj.get("designedfor")
        _subscriptionfee = createObj.get("subscriptionfee")
        _startdate = createObj.get("date")
        _status = "ACTIVE"
        _currenttime = dt.datetime.now(timezone('UTC')).strftime("%Y-%m-%d %H:%M:%S")
        _currenttimeparsed = dateutil.parser.parse(_currenttime)     
        newcourse = Courses(courseid=_courseid, title=_title, description=_description, subject=_subject, designedfor=_designedfor, courseof=_courseof, subscriptionfee=_subscriptionfee, numlectures=0, startdate=_startdate, numsubscribers=0, lastupdated=_currenttimeparsed, status=_status)
        newcourse.save()
        return {"success":1, "msg":"Successfully added lecture."}
    except Exception as ex:
        print(ex)
        return {"success":0, "msg":"Sorry. Something unexpected happened."}
    return {"success":0, "msg":"Sorry. This request is not available right now."} 
    
    
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)
    
    
def getAllCoursesForTeacherById(_courseof):
    try:
        courseList = []
        allCourses = Courses.objects.filter(courseof=_courseof)
        for c in allCourses:
            courseList.append(c)
        return {"success":1, "msg":"Courses found.", "courseList":courseList}
    except Exception as ex:
        print(ex)
        return {"success":0, "msg":"Sorry. Something unexpected happened."}
    return {"success":0, "msg":"Sorry. This request is not available right now."} 
    
    

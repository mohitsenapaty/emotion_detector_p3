from django.shortcuts import render
import datetime as dt
import dateutil.parser
import hashlib
from django.http import JsonResponse
from utils.doAuth import *
from utils import teacherFunctions
import random
from pytz import timezone 
from .models import *
import loginApp.models as loginModels

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
    createdCourse = teacherFunctions.createCourseForTeacher(request.POST, _id)
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
    _id = authObject.get('userobject').get('id')
    allcourses = teacherFunctions.getAllCoursesForTeacherById(_id)
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
create a lecture for a course
'''
def createlectureforcourse(request, courseid):
    context = locals()
    #do authentication
    authObject = userAuth(request)
    if authObject.get('is_logged_in') == 0:
        pass
    authObjectTeacher = teacherMethodsAuth(request)
    if authObjectTeacher.get('isAllowed') == False:
        pass
    if request.POST.get('topic') == None:
        template = 'createlecture.html'
        authObject['courseid'] = courseid
        return render(request, template, authObject)
    _id = authObject.get('userobject').get('id')
    createdLectures = teacherFunctions.createLecturesForCourse(request.POST, courseid, _id)
    createdLectures['is_logged_in'] = authObject.get('is_logged_in')
    createdLectures['userobject'] = authObject.get('userobject')
    createdLectures['courseid'] = courseid
    template = 'createlecture.html'
    return render(request, template, createdLectures)
    pass
    

'''
View lectures for a course
'''
def viewlecturesforcourse(request, courseid):
    context = locals()
    #do authentication
    authObject = userAuth(request)
    if authObject.get('is_logged_in') == 0:
        pass
    authObjectTeacher = teacherMethodsAuth(request)
    if authObjectTeacher.get('isAllowed') == False:
        pass
    _id = authObject.get('userobject').get('id')
    lectureList = teacherFunctions.getAllLecturesForCourse( courseid)
    lectureList['is_logged_in'] = authObject.get('is_logged_in')
    lectureList['userobject'] = authObject.get('userobject')
    lectureList['courseid'] = courseid
    template = 'viewlecture.html'
    return render(request, template, lectureList)
    pass

    
    

from django.shortcuts import render
import datetime as dt
import dateutil.parser
import hashlib
from django.http import JsonResponse
from utils.doAuth import *
import random
from pytz import timezone 
import loginApp.models as loginModels
import teacherfunctions.models as tfModels
import subscription.models as subModels


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
        newcourse = tfModels.Courses(courseid=_courseid, title=_title, description=_description, subject=_subject, designedfor=_designedfor, courseof=loginModels.Userprofile(id=_courseof), subscriptionfee=_subscriptionfee, numlectures=0, startdate=_startdate, numsubscribers=0, lastupdated=_currenttimeparsed, status=_status)
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
        allCourses = tfModels.Courses.objects.filter(courseof=_courseof)
        for c in allCourses:
            courseList.append(c.__dict__)
        return {"success":1, "msg":"Courses found.", "courseList":courseList}
    except Exception as ex:
        print(ex)
        return {"success":0, "msg":"Sorry. Something unexpected happened."}
    return {"success":0, "msg":"Sorry. This request is not available right now."} 
    
    
def createLecturesForCourse(createObj, _course, _teacher):
    try:
        courseObj = tfModels.Courses.objects.get(courseid = _course).__dict__
        _courseid = courseObj.get('id')
        _lectureid = "LEC" + str(random_with_N_digits(9))
        _topic = createObj.get("topic")
        _description = createObj.get("description")
        _type = createObj.get("type")
        _startdate = createObj.get("date")
        _starthour = createObj.get("starthour")
        _startmin = createObj.get("startmin")
        _status = "ACTIVE"
        _validitystatus = "SCHEDULED"
        _duration = createObj.get("duration")
        _lecturetime = "%s %s:%s:00+5:30"%(_startdate, _starthour, _startmin)
        _lecturetimeparsed = dateutil.parser.parse(_lecturetime)
        newLecture = tfModels.Lectures(lectureid=_lectureid, topic=_topic, description=_description, courseid=tfModels.Courses(id=_courseid), type=_type, lectureof=loginModels.Userprofile(id=_teacher), duration=_duration, startdateandtime=_lecturetimeparsed, validitystatus=_validitystatus, status=_status)
        newLecture.save()
        return {"success":1, "msg":"Successfully added lecture."}
    except Exception as ex:
        print(ex)
        return {"success":0, "msg":"Sorry. Something unexpected happened."}
    return {"success":0, "msg":"Sorry. This request is not available right now."} 
    pass
    
    
def getAllLecturesForCourse(_course):
    try:
        courseObj = tfModels.Courses.objects.get(courseid = _course).__dict__
        _courseid = courseObj.get('id')
        allLectures = tfModels.Lectures.objects.filter(courseid=_courseid)
        lectureList = []
        for l in allLectures:
            lectureList.append(l.__dict__)
        return {'success' : 0, 'msg' : 'Lectures found.', 'lectureList' : lectureList}
    except Exception as ex:
        print(ex)
        return {"success":0, "msg":"Sorry. Something unexpected happened."}        
    return {"success":0, "msg":"Sorry. This request is not available right now."}
    pass


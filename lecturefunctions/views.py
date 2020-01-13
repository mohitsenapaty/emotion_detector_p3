from django.shortcuts import render
from utils.doAuth import *
from utils import lectureServices

# Create your views here.
'''
lecture page for user
'''
def startlecturepageuser(request, lectureid):
    context = locals()
    #do authentication
    authObject = userAuth(request)
    if authObject.get('is_logged_in') == 0:
        pass
    lectureObject = lectureServices.getLectureDetailsObject(lectureid)
    #check sanity (implement later)
    lectureObject['is_logged_in'] = authObject.get('is_logged_in')
    lectureObject['userobject'] = authObject.get('userobject')
    template = 'lectureforuser1.html'
    return render(request, template, lectureObject)
    pass


'''
lecture page for teacher
'''
def startlectureteacher(request, lectureid):
    context = locals()
    #do authentication
    authObject = userAuth(request)
    if authObject.get('is_logged_in') == 0:
        pass
    lectureObject = lectureServices.getLectureDetailsObject(lectureid)
    #check sanity (implement later)
    lectureObject['is_logged_in'] = authObject.get('is_logged_in')
    lectureObject['userobject'] = authObject.get('userobject')
    template = 'lecturepageteacher.html'
    return render(request, template, lectureObject)
    pass

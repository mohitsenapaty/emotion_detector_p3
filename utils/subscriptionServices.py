import loginApp.models as loginModels
import teacherfunctions.models as tfModels
import subscription.models as subModels
import hashlib


def getAllCourses(offset=0, limit=0):
    try:
        courseList = []
        allCourses = tfModels.Courses.objects.all()
        if offset == 0 and limit == 0:
            pass
        if offset > 0:
            allCourses = allCourses[(offset-1)::]
        if limit > 0:
            allCourses = allCourses[:(offset+limit-1):]
        for c in allCourses:
            courseList.append(c.__dict__)
        return {"success":1, "msg":"Courses found.", "courseList":courseList}
    except Exception as ex:
        print(ex)
        return {"success":0, "msg":"Sorry. Something unexpected happened."}
    return {"success":0, "msg":"Sorry. This request is not available right now."} 
    

def getAllCoursesSubscribed(subscriber, offset=0, limit=0):
    try:
        courseList = []
        allCourses = subModels.Coursesubscription.objects.filter(userid=subscriber)
        if offset == 0 and limit == 0:
            pass
        if offset > 0:
            allCourses = allCourses[(offset-1)::]
        if limit > 0:
            allCourses = allCourses[:(offset+limit-1):]
        for c in allCourses:
            courseList.append(c.__dict__)
        return {"success":1, "msg":"Courses found.", "courseList":courseList}
    except Exception as ex:
        print(ex)
        return {"success":0, "msg":"Sorry. Something unexpected happened."}
    return {"success":0, "msg":"Sorry. This request is not available right now."} 



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


def subscribeUserToCourse(subscriber, courseid, subsObject):
    try:
        courseObj = tfModels.Courses.objects.get(courseid = _course).__dict__
        _courseid = courseObj.get('id')
        _userid = courseObj.get('courseof_id')
        _subid = 'CSU' + str(random_with_N_digits(9))
        _type = subsObject.get('type')
        _currenttime = dt.datetime.now(timezone('UTC')).strftime("%Y-%m-%d %H:%M:%S")
        _currenttimeparsed = dateutil.parser.parse(_currenttime)
        subCreated = subModels.Coursesubscription(subscriptionid=_subid, userid=subscriber, courseid=_courseid, courseof=_userid, type=_type, subscribedon=_currenttimeparsed, feepaid=0, status='ACTIVE')
        subCreated.save()
    except Exception as ex:
        print(ex)
        return {"success":0, "msg":"Sorry. Something unexpected happened."}
    return {"success":0, "msg":"Sorry. This request is not available right now."} 
    
    
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)


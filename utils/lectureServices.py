import loginApp.models as loginModels
import teacherfunctions.models as tfModels
import subscription.models as subModels
import hashlib
import random
from pytz import timezone 
import datetime as dt
import dateutil.parser


def getLectureDetailsObject(_lectureid):
    try:
        lecture = tfModels.Lectures.objects.get(lectureid=_lectureid)
        lectureObj = lecture.__dict__
        lectureObj['courseObject'] = lecture.courseid.__dict__
        lectureObj['userObject'] = lecture.lectureof.__dict__
        return {"success":1, "msg":"Courses found.", "lectureObject":lectureObj}
        pass
    except Exception as ex:
        print(ex)
        return {"success":0, "msg":"Sorry. Something unexpected happened."}
    return {"success":0, "msg":"Sorry. Something unexpected happened."}
    pass


import loginApp.models as loginModels
import hashlib

def userAuth(request):
    userobject = {}
    is_logged_in = 0
    if not request.session.get("userobject") == None:
        is_logged_in = 1
        userobject = request.session.get("userobject")
    return {'is_logged_in':is_logged_in, 'userobject':userobject}
    
def teacherMethodsAuth(request):
    userobject = {}
    if not request.session.get("userobject") == None:
        userobject = request.session.get("userobject")
        try:
            obj = loginModels.Userprofile.objects.get(userid=userObject.get("userid")).__dict__
            if (obj.get('isteacher') == 'Y'):
                return { 'userobject':userobject, 'isallowed':True}
            pass
        except:
            
            pass
    return { 'userobject':userobject, 'isallowed':False}
    
    
def setLoginAuthSession(request):
    pass
    

def get_authentication(_user, _pass):
    try:
        _encodedpass = hashlib.md5(_pass.encode('utf8')).hexdigest()
        #s1 = Userprofile.objects.get(email=_user).__dict__
        #s2 = Userprofile.objects.get(phone=_user).__dict__
        #import pdb; pdb.set_trace();
        print(_user, _pass, _encodedpass)
        if loginModels.Userprofile.objects.filter(email=_user, password=_encodedpass).exists():
            return loginModels.Userprofile.objects.get(email=_user).__dict__
        elif loginModels.Userprofile.objects.filter(phone=_user, password=_encodedpass).exists():
            return loginModels.Userprofile.objects.get(phone=_user).__dict__
        else:
            return None
    except:
        return None


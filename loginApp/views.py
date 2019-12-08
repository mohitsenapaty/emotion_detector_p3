from django.shortcuts import render
from .models import *
import hashlib
from django.http import JsonResponse
from utils.doAuth import *

# Create your views here.
'''
Home view :- display the home page. If logged in, display the Firstname
'''
def home(request):
    is_logged_in = 0
    authObject = userAuth(request)
    print(request.session.__dict__)
    #add additional fields to find more user details and send to the frontend
    template = 'home.html'
    returnDict = authObject
    return render(request, template, returnDict) 
    
    
'''
Login View
'''
def login(request):
    context = locals()
    
    is_logged_in = 0
    if not request.session.get("userobject") == None:
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1
        return HttpResponseRedirect('/home/')

    #region: authenticate login
    #import pdb; pdb.set_trace();
    _username = request.POST.get("username")
    _password = request.POST.get("password")

    if not _username:
        template = 'login.html'
        returnDict = {'is_logged_in':is_logged_in}
        return render(request, template, returnDict)

    auth_result = get_authentication(_username, _password)

    userobject = {};
    if auth_result:
        request.session['logged_in'] = True
        request.session['username'] = _username
        request.session['id'] = auth_result.get('id')
        userobject['id'] = auth_result.get('id')
        userobject['userid'] = auth_result.get('userid')
        userobject['email'] = auth_result.get('email')
        userobject['phone'] = auth_result.get('phone')
        userobject['firstname'] = auth_result.get('firstname')
        userobject['lastname'] = auth_result.get('lastname')
        userobject['isteacher'] = auth_result.get('isteacher')
        request.session['userobject'] = userobject        
        #set other session params
        is_logged_in = 1
        template = 'login.html'
        returnDict = {'is_logged_in':is_logged_in, 'userobject':userobject, 'error_message':'None'}
        return render(request, template, returnDict)
    else:
        template = 'login.html'
        returnDict = {'is_logged_in':is_logged_in, 'userobject':userobject, 'error_message':"Wrong Credentials/Non-existent Account",'logintype':request.session.get('type')}
        return render(request, template, returnDict)
        pass
    #endregion
    #import pdb; pdb.set_trace();    
    template = 'login.html'
    returnDict = {'is_logged_in':is_logged_in, 'userobject':userobject}
    return render(request, template, returnDict)    


'''
logout view
'''
def logout(request):
    context = locals()
    request.session.flush()
    template = 'logged_out.html'
    return render(request, template, context)
    


    
   

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . import send_email
import json, matplotlib, time
import matplotlib.pyplot as plt
import datetime as dt
from pytz import timezone 
from .models import *
import MySQLdb 
import dateutil.parser
import upload_to_dropbox

DROPBOX_ACCESS_TOKEN = "t0-WvXEmgaAAAAAAAAAABkLheYrQk8TjSZBJHBgkn1nQ3X0K6z0H-P_zABFzFY9E"

glob_float_att_array = []
glob_att_id_ = 0
glob_att_x_arr = []

glob_float_emo_dict = {"angry":[0], "sad":[0], "surprised":[0], "happy":[0]}

glob_emo_file = ""
glob_att_file = ""

glob_count = 0

# Create your views here.
# Create your views here.
def eye_gaze_tracker(request):
    context = locals()
    from ipware.ip import get_real_ip
    ip_arr = []
    ip_real = get_real_ip(request)
    if ip_real is not None:
        ip_arr.append(ip_real)
    else:
        ip_arr.append('')
    
    from ipware.ip import get_ip
    #ip_arr = []
    ip = get_ip(request)
    if ip is not None:
        ip_arr.append(ip)
    else:
        ip_arr.append('')

    f1 = open("ip.txt", "a")
    for x in ip_arr:
        f1.write(x)
        f1.write('eye gaze tracker\n')
    f1.close()

    glob_float_att_array = []
    glob_att_id_ = 0
    glob_att_x_arr = []

    is_logged_in = 0
    if not request.session.get("username") == None:
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1

    
    template = 'eye_gaze_tracker.html'
    returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username")}
    return render(request, template, returnDict)

def home(request):
    context = locals()
    from ipware.ip import get_real_ip
    ip_arr = []
    ip_real = get_real_ip(request)
    if ip_real is not None:
        ip_arr.append(ip_real)
    else:
        ip_arr.append('')
    
    from ipware.ip import get_ip
    #ip_arr = []
    ip = get_ip(request)
    if ip is not None:
        ip_arr.append(ip)
    else:
        ip_arr.append('')

    f1 = open("ip.txt", "a")
    for x in ip_arr:
        f1.write(x)
        f1.write('home\n')
    f1.close()

    is_logged_in = 0
    if not request.session.get("username") == None:
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1

    template = 'new_home.html'
    returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"), 'logintype':request.session.get("type")}
    return render(request, template, returnDict) 


def team(request):
    context = locals()
    from ipware.ip import get_real_ip
    ip_arr = []
    ip_real = get_real_ip(request)
    if ip_real is not None:
        ip_arr.append(ip_real)
    else:
        ip_arr.append('')
    
    from ipware.ip import get_ip
    #ip_arr = []
    ip = get_ip(request)
    if ip is not None:
        ip_arr.append(ip)
    else:
        ip_arr.append('')

    f1 = open("ip.txt", "a")
    for x in ip_arr:
        f1.write(x)
        f1.write('home\n')
    f1.close()

    is_logged_in = 0
    if not request.session.get("username") == None:
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1

    template = 'team.html'
    returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"), 'logintype':request.session.get("type")}
    return render(request, template, returnDict) 


def live_demo(request):
    context = locals()
    from ipware.ip import get_real_ip
    ip_arr = []
    ip_real = get_real_ip(request)
    if ip_real is not None:
        ip_arr.append(ip_real)
    else:
        ip_arr.append('')
    
    from ipware.ip import get_ip
    #ip_arr = []
    ip = get_ip(request)
    if ip is not None:
        ip_arr.append(ip)
    else:
        ip_arr.append('')

    f1 = open("ip.txt", "a")
    for x in ip_arr:
        f1.write(x)
        f1.write('home\n')
    f1.close()

    is_logged_in = 0
    if not request.session.get("username") == None:
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1

    template = 'live_demo.html'
    returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"), 'logintype':request.session.get("type")}
    return render(request, template, returnDict) 


def contact(request):
    context = locals()
    from ipware.ip import get_real_ip
    ip_arr = []
    ip_real = get_real_ip(request)
    if ip_real is not None:
        ip_arr.append(ip_real)
    else:
        ip_arr.append('')
    
    from ipware.ip import get_ip
    #ip_arr = []
    ip = get_ip(request)
    if ip is not None:
        ip_arr.append(ip)
    else:
        ip_arr.append('')

    f1 = open("ip.txt", "a")
    for x in ip_arr:
        f1.write(x)
        f1.write('home\n')
    f1.close()

    is_logged_in = 0
    if not request.session.get("username") == None:
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1

    template = 'contact.html'
    returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"), 'logintype':request.session.get("type")}
    return render(request, template, returnDict) 


def emotion_detector(request):
    context = locals()
    from ipware.ip import get_real_ip
    ip_arr = []
    ip_real = get_real_ip(request)
    if ip_real is not None:
        ip_arr.append(ip_real)
    else:
        ip_arr.append('')
    
    from ipware.ip import get_ip
    #ip_arr = []
    ip = get_ip(request)
    if ip is not None:
        ip_arr.append(ip)
    else:
        ip_arr.append('')

    f1 = open("ip.txt", "a")
    for x in ip_arr:
        f1.write(x)
        f1.write('emotion detector\n')
    f1.close()

    glob_float_emo_dict = {"angry":[0], "sad":[0], "surprised":[0], "happy":[0]}
    glob_emo_id_ = 0
    glob_emo_x_arr = []

    is_logged_in = 0
    if not request.session.get("username") == None:
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1

    template = 'emotion_detector.html'
    returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username")}
    return render(request, template, returnDict)

@csrf_exempt
def get_attention_data(request):
    #fromJs = json.loads(request.POST)
    #print fromJs
    #import pdb; pdb.set_trace();
    att_array = request.POST.getlist(u'colAttentionData[]')
    is_logged_in = 0
    _username = request.session.get("username", "")
    if not _username == "":
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1
        #_username = 
    float_att_array = []
    id_ = 0
    x_arr = []
    for att in att_array:
        float_att_array.append(float(att))
        id_ += 1
        x_arr.append(id_)
    plt.plot(x_arr, att_array)
    plt.xlabel("time in seconds")
    plt.ylabel("attention level in percent")
    plt_file_name = "attention_data_"
    dt_timestamp = dt.datetime.fromtimestamp(time.time()).strftime("%Y_%m_%d_%H_%M_%S")
    plt_file_name = _username + plt_file_name+dt_timestamp+".png"
    plt.savefig(plt_file_name)
    plt.gcf().clear()
    glob_att_file = plt_file_name
    glob_emo_file = request.session.get("glob_emo_file")
    if not glob_emo_file == None:
        del request.session["glob_emo_file"]
        request.session.modified = True
    transferData = upload_to_dropbox.upload_to_dropbox(DROPBOX_ACCESS_TOKEN)
    send_email.send_email("date:val time:val", "dharna graph for user", [glob_att_file, glob_emo_file])
    transferData = upload_to_dropbox.upload_to_dropbox(DROPBOX_ACCESS_TOKEN)
    transferData.upload_file(file_from="%s"%(glob_att_file), file_to="/dharna_app/%s"%(glob_att_file))
    att_file_url = transferData.get_shared_file_url()
        #upload emotion file
    transferData1 = upload_to_dropbox.upload_to_dropbox(DROPBOX_ACCESS_TOKEN)
    transferData1.upload_file(file_from=glob_emo_file, file_to="/dharna_app/%s"%(glob_emo_file))
    emo_file_url = transferData1.get_shared_file_url()
    print att_file_url, emo_file_url
    return HttpResponse("Success!")

@csrf_exempt
def get_attention_data_test(request):
    #fromJs = json.loads(request.POST)
    #print fromJs
    #import pdb; pdb.set_trace();
    att_array = request.POST.getlist(u'colAttentionData[]')
    is_logged_in = 0
    _username = request.session.get("username", "")
    _id = request.session.get("id")
    _type = request.session.get("type")
    if (not _username == "") and (_type == "student"):
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1
        #_username = 
    else:
        return HttpResponse("Failure")
    _lecture_id = request.session.get("lecture_id")
    if not _lecture_id:
        return HttpResponse("Failure")
    float_att_array = []
    id_ = 0
    x_arr = []
    for att in att_array:
        float_att_array.append(float(att))
        id_ += 1
        x_arr.append(id_)
    plt.plot(x_arr, att_array)
    plt.xlabel("time in seconds")
    plt.ylabel("attention level in percent")
    plt_file_name = "attention_data_"
    dt_timestamp = dt.datetime.fromtimestamp(time.time()).strftime("%Y_%m_%d_%H_%M_%S")
    plt_file_name = _username + plt_file_name+dt_timestamp+".png"
    plt.savefig(plt_file_name)
    plt.gcf().clear()
    glob_att_file = plt_file_name
    glob_emo_file = request.session.get("glob_emo_file")
    if not glob_emo_file == None:
        del request.session["glob_emo_file"]
        request.session.modified = True
    #try:
    send_email.send_email("date:val time:val", "dharna graph for user", [glob_att_file, glob_emo_file])
    sd_obj = StudentDetail.objects.get(student_id=_id)
        #send_email.send_email_client(sd_obj.__dict__.get("email"),"date:val time:val", "dharna graph for user", [glob_att_file, glob_emo_file])
        #upload attention file
    print glob_att_file, glob_emo_file
    transferData = upload_to_dropbox.upload_to_dropbox(DROPBOX_ACCESS_TOKEN)
    transferData.upload_file(file_from="%s"%(glob_att_file), file_to="/dharna_app/%s"%(glob_att_file))
    att_file_url = transferData.get_shared_file_url()
        #upload emotion file
    transferData1 = upload_to_dropbox.upload_to_dropbox(DROPBOX_ACCESS_TOKEN)
    transferData1.upload_file(file_from=glob_emo_file, file_to="/dharna_app/%s"%(glob_emo_file))
    emo_file_url = transferData1.get_shared_file_url()
    #except:
        #return HttpResponse("Failure!")
    print att_file_url, emo_file_url
    #load data ti database
    lt_obj = LectureTeacher.objects.get(lecture_id=_lecture_id)
    sl_obj = StudentLogin.objects.get(student_id=_id)
    ls_obj = LectureStudent.objects.get(lecture=lt_obj,student=sl_obj)
    ls_obj.attention_graph_link = str(att_file_url)
    ls_obj.emotion_graph_link = str(emo_file_url)
    ls_obj.save()
    return HttpResponse("Success!")

@csrf_exempt
def get_emotion_data(request):
    #fromJs = json.loads(request.POST)
    #print fromJs
    #import pdb; pdb.set_trace();
    post_array = request.POST
    is_logged_in = 0
    _username = request.session.get("username", "")
    if not _username == "":
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1
    i_ = 0
    j_ = 0
    emo_dict = {"angry":[0], "sad":[0], "surprised":[0], "happy":[0]}
    while (1):
        flag = 0
        for j_ in range(4):
            qe_str = 'data['+str(i_)+"]["+str(j_)+"][emotion]"
            qv_str = 'data['+str(i_)+"]["+str(j_)+"][value]"
            emo_ = post_array.getlist(qe_str)
            val_ = post_array.getlist(qv_str)
            if emo_==None or len(emo_) == 0:
                flag = 1
                break
            else:
                emo_list = emo_dict.get(emo_[0])
                if emo_list == None or len(emo_list) == 0:
                    pass
                else:
                    emo_dict[emo_[0]].append(val_[0])

        i_ = i_+1
        if flag == 1:
            break

    #print emo_dict
    #float_emotion_array = []
    #id_ = 0
    #x_arr = []
    plot_key = []
    for emo_key in emo_dict:
        emo_arr = emo_dict[emo_key]
        p_key = "y = "+emo_key
        plot_key.append(emo_key)
        float_emo_arr = []
        x_arr = []
        id_ = 0
        for emo_val in emo_arr:
            float_emo_arr.append(float(emo_val))
            x_arr.append(id_)
            id_+=1
        plt.plot(x_arr, float_emo_arr)
    plt.legend(plot_key, loc='upper left')


    #    float_att_array.append(float(att))
    #    id_ += 1
    #    x_arr.append(id_)
    #plt.plot(x_arr, att_array)
    plt.xlabel("time in seconds")
    plt.ylabel("weighted emotion value")
    plt_file_name = "emotion_data_"
    dt_timestamp = dt.datetime.fromtimestamp(time.time()).strftime("%Y_%m_%d_%H_%M_%S")
    plt_file_name = _username + plt_file_name+dt_timestamp+".png"
    plt.savefig(plt_file_name)
    plt.gcf().clear()
    #global glob_emo_file
    request.session["glob_emo_file"] = plt_file_name
    return HttpResponse("Success!")

@csrf_exempt
def get_emotion_data_test(request):
    #fromJs = json.loads(request.POST)
    #print fromJs
    #import pdb; pdb.set_trace();
    post_array = request.POST
    is_logged_in = 0
    _username = request.session.get("username", "")
    if not _username == "":
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1
    else:
        return HttpResponse("Failure")
    i_ = 0
    j_ = 0
    emo_dict = {"angry":[0], "sad":[0], "surprised":[0], "happy":[0]}
    while (1):
        flag = 0
        for j_ in range(4):
            qe_str = 'data['+str(i_)+"]["+str(j_)+"][emotion]"
            qv_str = 'data['+str(i_)+"]["+str(j_)+"][value]"
            emo_ = post_array.getlist(qe_str)
            val_ = post_array.getlist(qv_str)
            if emo_==None or len(emo_) == 0:
                flag = 1
                break
            else:
                emo_list = emo_dict.get(emo_[0])
                if emo_list == None or len(emo_list) == 0:
                    pass
                else:
                    emo_dict[emo_[0]].append(val_[0])

        i_ = i_+1
        if flag == 1:
            break

    #print emo_dict
    #float_emotion_array = []
    #id_ = 0
    #x_arr = []
    plot_key = []
    for emo_key in emo_dict:
        emo_arr = emo_dict[emo_key]
        p_key = "y = "+emo_key
        plot_key.append(emo_key)
        float_emo_arr = []
        x_arr = []
        id_ = 0
        for emo_val in emo_arr:
            float_emo_arr.append(float(emo_val))
            x_arr.append(id_)
            id_+=1
        plt.plot(x_arr, float_emo_arr)
    plt.legend(plot_key, loc='upper left')


    #    float_att_array.append(float(att))
    #    id_ += 1
    #    x_arr.append(id_)
    #plt.plot(x_arr, att_array)
    plt.xlabel("time in seconds")
    plt.ylabel("weighted emotion value")
    plt_file_name = "emotion_data_"
    dt_timestamp = dt.datetime.fromtimestamp(time.time()).strftime("%Y_%m_%d_%H_%M_%S")
    plt_file_name = _username + plt_file_name+dt_timestamp+".png"
    plt.savefig(plt_file_name)
    plt.gcf().clear()
    request.session["glob_emo_file"] = plt_file_name
    return HttpResponse("Success!")

def combined_app(request):
    context = locals()
    from ipware.ip import get_real_ip
    ip_arr = []
    ip_real = get_real_ip(request)
    if ip_real is not None:
        ip_arr.append(ip_real)
    else:
        ip_arr.append('')
    
    from ipware.ip import get_ip
    #ip_arr = []
    ip = get_ip(request)
    if ip is not None:
        ip_arr.append(ip)
    else:
        ip_arr.append('')

    f1 = open("ip.txt", "a")
    for x in ip_arr:
        f1.write(x)
        f1.write('combined app\n')
    f1.close()

    is_logged_in = 0
    if not request.session.get("username") == None:
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1

    template = 'combined_app.html'
    returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username")}
    return render(request, template, returnDict)


def combined_app_new(request):
    context = locals()
    from ipware.ip import get_real_ip
    ip_arr = []
    ip_real = get_real_ip(request)
    if ip_real is not None:
        ip_arr.append(ip_real)
    else:
        ip_arr.append('')
   
    from ipware.ip import get_ip
    #ip_arr = []
    ip = get_ip(request)
    if ip is not None:
        ip_arr.append(ip)
    else:
        ip_arr.append('')

    f1 = open("ip.txt", "a")
    for x in ip_arr:
        f1.write(x)
        f1.write('combined app\n')
    f1.close()

    is_logged_in = 0
    if not request.session.get("username") == None:
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1

    template = 'combined_app_new.html'
    returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username")}
    return render(request, template, returnDict)


def combined_app_live(request):
    context = locals()
    from ipware.ip import get_real_ip
    ip_arr = []
    ip_real = get_real_ip(request)
    if ip_real is not None:
        ip_arr.append(ip_real)
    else:
        ip_arr.append('')
    
    from ipware.ip import get_ip
    #ip_arr = []
    ip = get_ip(request)
    if ip is not None:
        ip_arr.append(ip)
    else:
        ip_arr.append('')

    f1 = open("ip.txt", "a")
    for x in ip_arr:
        f1.write(x)
        f1.write('combined app live\n')
    f1.close()

    is_logged_in = 0
    if not request.session.get("username") == None:
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1

    template = 'combined_app_live.html'
    returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username")}
    return render(request, template, returnDict)

def login_page(request):
    context = locals()
    tried = 0
    #region: store ip details
    from ipware.ip import get_real_ip
    ip_arr = []
    ip_real = get_real_ip(request)
    if ip_real is not None:
        ip_arr.append(ip_real)
    else:
        ip_arr.append('')
    
    from ipware.ip import get_ip
    #ip_arr = []
    ip = get_ip(request)
    if ip is not None:
        ip_arr.append(ip)
    else:
        ip_arr.append('')

    f1 = open("ip.txt", "a")
    for x in ip_arr:
        f1.write(x)
        f1.write('login page.\n')
    f1.close()
    #end region
    #import pdb; pdb.set_trace();
    #logging logic

    is_logged_in = 0
    if not request.session.get("username") == None:
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1
        return HttpResponseRedirect('/login_combined_app/')

    #region: authenticate login
    #import pdb; pdb.set_trace();
    _username = request.POST.get("username")
    _password = request.POST.get("password")
    _type = request.POST.get("logintype")

    if not _username:
        template = 'login_page.html'
        returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"), 'error_message':'None', 'logintype':request.session.get('type')}
        return render(request, template, returnDict)

    auth_result = get_authentication(_username, _password, _type)

    if auth_result:
        request.session['logged_in'] = True
        if _type == 'student':
            request.session['username'] = _username
            request.session['id'] = auth_result['student_id']
            request.session['type'] = 'student'
        elif _type == 'teacher':
            request.session['username'] = _username
            request.session['id'] = auth_result['teacher_id']
            request.session['type'] = 'teacher'
        #set other session params
        is_logged_in = 1
        template = 'login_page.html'
        returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"), 'error_message':'None', 'logintype':request.session.get('type')}
        return render(request, template, returnDict)
    else:
        template = 'login_page.html'
        returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"), 'error_message':"Wrong Credentials/Non-existent Account",'logintype':request.session.get('type')}
        return render(request, template, returnDict)
        pass

    #endregion
    #import pdb; pdb.set_trace();
    

    template = 'login_page.html'
    returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username")}
    return render(request, template, returnDict)


#region: authentication
def get_authentication(_user, _pass, _t):
    try:
        if _t == 'student':
            s1 = StudentLogin.objects.get(username=_user).__dict__
            if s1['password'] == _pass:
                return s1
            else:
                return None
        elif _t == 'teacher':
            s1 = TeacherLogin.objects.get(username=_user).__dict__
            if s1['password'] == _pass:
                return s1
            else:
                return None
    except:
        return None
#endregion


def log_out(request):
    context = locals()
    request.session.flush()
    #import pdb; pdb.set_trace();
    #region: store ip details
    from ipware.ip import get_real_ip
    ip_arr = []
    ip_real = get_real_ip(request)
    if ip_real is not None:
        ip_arr.append(ip_real)
    else:
        ip_arr.append('')
    
    from ipware.ip import get_ip
    #ip_arr = []
    ip = get_ip(request)
    if ip is not None:
        ip_arr.append(ip)
    else:
        ip_arr.append('')

    f1 = open("ip.txt", "a")
    for x in ip_arr:
        f1.write(x)
        f1.write('logout page.\n')
    f1.close()
    #end region

    template = 'logged_out.html'
    return render(request, template, context)

def login_combined_app(request):
    context = locals()
    from ipware.ip import get_real_ip
    ip_arr = []
    ip_real = get_real_ip(request)
    if ip_real is not None:
        ip_arr.append(ip_real)
    else:
        ip_arr.append('')
    
    from ipware.ip import get_ip
    #ip_arr = []
    ip = get_ip(request)
    if ip is not None:
        ip_arr.append(ip)
    else:
        ip_arr.append('')

    f1 = open("ip.txt", "a")
    for x in ip_arr:
        f1.write(x)
        f1.write('combined app\n')
    f1.close()

    is_logged_in = 0
    if not request.session.get("username") == None:
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1

    template = 'login_combined_app.html'
    returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username")}
    return render(request, template, returnDict)

def login_combined_app_test(request):
    #context = locals()
    from ipware.ip import get_real_ip
    ip_arr = []
    ip_real = get_real_ip(request)
    if ip_real is not None:
        ip_arr.append(ip_real)
    else:
        ip_arr.append('')
    
    from ipware.ip import get_ip
    #ip_arr = []
    ip = get_ip(request)
    if ip is not None:
        ip_arr.append(ip)
    else:
        ip_arr.append('')

    f1 = open("ip.txt", "a")
    for x in ip_arr:
        f1.write(x)
        f1.write('combined app\n')
    f1.close()

    is_logged_in = 0
    if not request.session.get("username") == None:
        #return HttpResponseRedirect('/combined_app/')
        #get user id
        _id = request.session.get("id")
        _type = request.session.get("type")
        _username = request.session.get("username")
        is_logged_in = 1
    else:
        #invalid login error
        return HttpResponseRedirect('/error_page/')
        
    if not request.session.get("lecture_id") == None:
        # get lecture id
        _lecture_id = request.session.get("lecture_id")
        # check if the type is student or teacher
        print _lecture_id
        if _type == 'teacher':
            #lt_obj = LectureTeacher()
            if LectureTeacher.objects.get(lecture_id=_lecture_id).exists():
                lt_obj = LectureTeacher.objects.get(lecture_id=_lecture_id)
                if lt_obj.__dict__.get("status") == 'N' or lt_obj.__dict__.get("status") == 'O':
                    pass
                else:
                    return HttpResponseRedirect('/error_page/')
                    #lecture not started, lecture finished error
            pass
            # if teacher, the teacher id should be there in lt_obj
            # if lt_obj is in teacher, check the status
            # if the status is A, the student can join
            # elif N, respond that the lecture hasn't started
            # elif F, student can't join, respond lecture hasn't started.
        elif _type == 'student':
            if LectureStudent.objects.filter(lecture_id=_lecture_id, student_id=_id).exists():
                ls_obj = LectureStudent.objects.get(lecture_id=_lecture_id, student_id=_id)
                lt_obj = ls_obj.lecture
                if lt_obj.__dict__.get("status") == 'O':
                    pass
                else:
                    return HttpResponseRedirect('/error_page/')
                    #lecture not started/lecture finished error
            else:
                return HttpResponseRedirect('/error_page/')
                #lecture not available error
            # if student, the teacher id should be there in ls_obj
            pass
        pass
    else:
        print 1
        return HttpResponseRedirect('/error_page/')
        #invalid page error.

    template = 'login_combined_app_test.html'
    returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username")}
    return render(request, template, returnDict)

#start chatframe
def chatframe(request):
    context = locals()
    from ipware.ip import get_real_ip
    ip_arr = []
    ip_real = get_real_ip(request)
    if ip_real is not None:
        ip_arr.append(ip_real)
    else:
        ip_arr.append('')
    
    from ipware.ip import get_ip
    #ip_arr = []
    ip = get_ip(request)
    if ip is not None:
        ip_arr.append(ip)
    else:
        ip_arr.append('')

    f1 = open("ip.txt", "a")
    for x in ip_arr:
        f1.write(x)
        f1.write('combined app\n')
    f1.close()

    is_logged_in = 0
    _username = request.session.get("username")
    if not _username == None:
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1

    if is_logged_in == 1:
        pass

    template = 'chatframe.html'
    returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username")}
    return render(request, template, returnDict)
#end chatframe

#start register_page
def register_page(request):
    context = locals()
    #region: store ip details
    from ipware.ip import get_real_ip
    ip_arr = []
    ip_real = get_real_ip(request)
    if ip_real is not None:
        ip_arr.append(ip_real)
    else:
        ip_arr.append('')
    
    from ipware.ip import get_ip
    #ip_arr = []
    ip = get_ip(request)
    if ip is not None:
        ip_arr.append(ip)
    else:
        ip_arr.append('')

    f1 = open("ip.txt", "a")
    for x in ip_arr:
        f1.write(x)
        f1.write('register page.\n')
    f1.close()
    #end region

    #logging logic
    #import pdb; pdb.set_trace()

    is_logged_in = 0
    if request.session.get("logged_in") == True:
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1
        is_registered = 0
        template = 'register_page.html'
        returnDict = {'is_logged_in':is_logged_in, 'is_registered':is_registered, 'username':request.session.get("username")}
        return render(request, template, returnDict)

    
    if request.POST.get('username') == None:
        is_registered = 0
        is_logged_in = 0

        ent_array = EntityTable.objects.filter(section=None).values()
        sd_array = SchoolDetails.objects.all().values()
        
        template = 'register_page.html'
        returnDict = {'is_logged_in':is_logged_in, 'is_registered':is_registered, 'username':request.session.get("username"), 'error_message':'None','logintype':request.session.get('type'), 'sd_a':sd_array, 'ent_a':ent_array}
        return render(request, template, returnDict)            

    #import pdb; pdb.set_trace();
    reg_auth_result = get_reg_authentication(request)

    if reg_auth_result['success'] == True:
        #set other session params
        is_logged_in = 0
        is_registered = 1
        ent_array = EntityTable.objects.filter(section=None).values()
        sd_array = SchoolDetails.objects.all().values()
        template = 'register_page.html'
        returnDict = {'is_logged_in':is_logged_in, 'is_registered':is_registered,'username':request.session.get("username"), 'error_message':'None', 'logintype':request.session.get('type'), 'sd_a':sd_array, 'ent_a':ent_array}
        return render(request, template, returnDict)
    else:
        is_registered = 2
        is_logged_in = 0
        template = 'register_page.html'
        msg = reg_auth_result['msg']
        ent_array = EntityTable.objects.filter(section=None).values()
        sd_array = SchoolDetails.objects.all().values()
        returnDict = {'is_logged_in':is_logged_in, 'is_registered':is_registered, 'username':request.session.get("username"), 'error_message':msg,'logintype':request.session.get('type'), 'sd_a':sd_array, 'ent_a':ent_array}
        return render(request, template, returnDict)
        pass

    #endregion
    #import pdb; pdb.set_trace();
    template = 'register_page.html'
    returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"), 'is_registered':is_registered, 'error_message':'None'}
    return render(request, template, returnDict)
#end register page

#start region get reg authentication
def get_reg_authentication(request):
    _username = request.POST.get("username")
    _password = request.POST.get("password")
    _re_password = request.POST.get("re_password")
    _fn = request.POST.get("first_name")
    _mn = request.POST.get("middle_name")
    _ln = request.POST.get("last_name")
    #import pdb; pdb.set_trace()
    _school = int(request.POST.get("school"))
    _email = request.POST.get("email_id")
    _phone = request.POST.get("phone")
    _class = int(request.POST.get("Class"))
    _type = request.POST.get("logintype")

    try:
        if _type == 'student':
            #s1 = StudentLogin.objects.get(username=_user).__dict__
            if StudentLogin.objects.filter(username=_username).exists():
                return {'success':None, 'msg':"Username Exists"}
            if not _password == _re_password:
                return {'success':None, 'msg':"Password not matching"}
            if StudentDetail.objects.filter(email=_email).exists():
                return {'success':None, 'msg':"Email exists"}
            if StudentDetail.objects.filter(phone=_phone).exists():
                return {'success':None, 'msg':"Phone number already in use"}
            
            sl_entry = StudentLogin(username=_username,password=_password)
            sl_entry.save()
            sl_d = StudentLogin.objects.get(username=_username)
            #sl_d_id = int(sl_d['student_id'])
            school_obj = SchoolDetails.objects.get(school_id = _school)
            entity_obj = EntityTable.objects.get(entity_id = _class)
            
            sd_entry = StudentDetail(student=sl_d, first_name = _fn, middle_name = _mn, last_name = _ln, school = school_obj, entity = entity_obj, email=_email, phone=_phone)
            sd_entry.save()
            return {'success':True, 'msg':""}
                
        elif _type == 'teacher':
            #s1 = TeacherLogin.objects.get(username=_user).__dict__
            if TeacherLogin.objects.get(username=_username).exists():
                return {'success':None, 'msg':"Username Exists"}
            if not _password == _re_password:
                return {'success':None, 'msg':"Password not matching"}
            if TeacherDetail.objects.filter(email=_email).exists():
                return {'success':None, 'msg':"Email exists"}
            if TeacherDetail.objects.filter(phone=_phone).exists():
                return {'success':None, 'msg':"Phone number already in use"}

            tl_entry = TeacherLogin(username=_username,password=_password)
            tl_entry.save()
            tl_d = TeacherLogin.objects.get(username=_username)
            #tl_d_id = tl_d['student_id']
            school_obj = SchoolDetails.objects.get(school_id = _school)
            td_entry = TeacherDetail(teacher=tl_d, first_name = _fn, middle_name = _mn, last_name = _ln, school = school_obj, email=_email, phone=_phone)
            td_entry.save()
            return {'success':True, 'msg':''}
    except:
        return {'success':None, 'msg':"Query failure."}
    return {'success':None, 'msg':"Some Network Error."}
    
#end region get reg authentication

#start teacher_profile_info
def teacher_profile_info(request):

    is_logged_in = 0
    if not request.session.get("type") == 'teacher':
        return HttpResponseRedirect('/')
    _username = request.session.get("username")
    if not _username == None:
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1

        teacher_info = get_teacher_info(_username)

        if teacher_info == None:
            #return error page
            template = 'teacher_profile_info.html'
            returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"),'logintype':request.session.get('type'), 'error':'Some network or Internal Error. Try after some time.'}
            return render(request, template, returnDict)

        template = 'teacher_profile_info.html'
        returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"),'logintype':request.session.get('type'), 'error':'None', 'teacher_login':teacher_info['teacher_login'].__dict__, 'teacher_detail':teacher_info['teacher_detail'].__dict__}
        return render(request, template, returnDict) 
    else:
        return HttpResponseRedirect('/')
#end teacher_profile_info

#start get_teacher_info
def get_teacher_info(_username):

    try:
        teacher_obj = TeacherLogin.objects.get(username=_username)
        teacher_det_obj = TeacherDetail.objects.get(teacher=teacher_obj)
        return {'teacher_login':teacher_obj, 'teacher_detail':teacher_det_obj}
    except:
        return None
#end get_teacher_info

#start def update teacher info
def update_teacher_info(request):
    is_logged_in = 0
    if not request.session.get("type") == 'teacher':
        return HttpResponseRedirect('/')
    _username = request.session.get("username")
    if not _username == None:
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1

        teacher_info = get_teacher_info(_username)

        if teacher_info == None:
            #return error page
            template = 'teacher_profile_info.html'
            returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"),'logintype':request.session.get('type'), 'error':'Some network or Internal Error. Try after some time.'}
            return render(request, template, returnDict)

        #handle POST data here
        if not request.POST.get("password"):
            template = 'update_teacher_info.html'
            returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"),'logintype':request.session.get('type'), 'error':'None', 'teacher_login':teacher_info['teacher_login'].__dict__, 'teacher_detail':teacher_info['teacher_detail'].__dict__, 'msg':'Update your personal information and password here.'}
            return render(request, template, returnDict)

        #handle request.POST here
        update_data = update_teacher_data(request.POST, teacher_info)

        if update_data["success"] == 0:
            template = 'update_teacher_info.html'
            returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"),'logintype':request.session.get('type'), 'error':update_data["msg"], 'teacher_login':teacher_info['teacher_login'].__dict__, 'teacher_detail':teacher_info['teacher_detail'].__dict__}
            return render(request, template, returnDict)
        else:
            template = 'update_teacher_info.html'
            returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"),'logintype':request.session.get('type'), 'error':update_data['msg'], 'teacher_login':teacher_info['teacher_login'].__dict__, 'teacher_detail':teacher_info['teacher_detail'].__dict__}
            return render(request, template, returnDict)

        template = 'update_teacher_info.html'
        returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"),'logintype':request.session.get('type'), 'error':'None', 'teacher_login':teacher_info['teacher_login'].__dict__, 'teacher_detail':teacher_info['teacher_detail'].__dict__}
        return render(request, template, returnDict) 
    else:
        return HttpResponseRedirect('/')
#end def update_teacher_info

#start region update teacher data
def update_teacher_data(posted_dict, teacher_info):
    _pwd = posted_dict.get("password")
    _pwd_n = posted_dict.get("new_password")
    _pwd_r = posted_dict.get("re_new_password")

    _email = posted_dict.get("email")
    _phone = posted_dict.get("phone")

    if not _pwd == teacher_info['teacher_login'].__dict__.get("password"):
        return {"success":0, "msg":"Incorrect Password"}
    if not _pwd_n == _pwd_r:
        return {"success":0, "msg":"mismatch in new password"}
    if _pwd == _pwd_n:
        return {"success":0, "msg":"Same password entered"}
    if _email == teacher_info['teacher_detail'].__dict__.get("email"):
        return {"success":0, "msg":"Same email"}
    if _phone == teacher_info['teacher_detail'].__dict__.get("phone"):
        return {"success":0, "msg":"Same phone"}
    #else do changes and return true
    if _pwd_n == '' and _pwd_n_r == '' and _email == '' and _phone == '':
        return {"success":0, "msg":"No changes made."}
    if _pwd_n == None and _pwd_n_r == None and _email == None and _phone == None:
        return {"success":0, "msg":"No changes made."}
    try:
        if _pwd_n:
            #update pwd
            tr_lg = TeacherLogin.objects.get(username=teacher_info['teacher_login'].__dict__.get("username"))
            tr_lg.password=_pwd_n
            tr_lg.save()
        if _email:
            #update email
            tr_dl = TeacherDetail.objects.get(teacher_id=teacher_info['teacher_detail'].__dict__.get("teacher_id"))
            tr_dl.email=_email
            tr_dl.save()
        if _phone:
            #update phone  
            tr_dl = TeacherDetail.objects.get(teacher_id=teacher_info['teacher_detail'].__dict__.get("teacher_id"))
            tr_dl.phone=_phone
            tr_dl.save()
        return {"success":1, "msg":"Successfully Updated data."}
    except:
        return {"success":0, "msg":"SQL error"}

    return {"success":1, "msg":"Successfully Updated data."}
#end region update teacher data

#start student_profile_info
def student_profile_info(request):

    is_logged_in = 0
    if not request.session.get("type") == 'student':
        return HttpResponseRedirect('/')
    _username = request.session.get("username")
    if not _username == None:
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1

        student_info = get_student_info(_username)

        if student_info == None:
            #return error page
            template = 'student_profile_info.html'
            returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"),'logintype':request.session.get('type'), 'error':'Some network or Internal Error. Try after some time.'}
            return render(request, template, returnDict)

        template = 'student_profile_info.html'
        returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"),'logintype':request.session.get('type'), 'error':'None', 'student_login':student_info['student_login'].__dict__, 'student_detail':student_info['student_detail'].__dict__}
        return render(request, template, returnDict) 
    else:
        return HttpResponseRedirect('/')
#end student_profile_info

#start get_student_info
def get_student_info(_username):

    try:
        student_obj = StudentLogin.objects.get(username=_username)
        student_det_obj = StudentDetail.objects.get(student=student_obj)
        return {'student_login':student_obj, 'student_detail':student_det_obj}
    except:
        return None
#end get_student_info

#start def update student info
def update_student_info(request):
    is_logged_in = 0
    if not request.session.get("type") == 'student':
        return HttpResponseRedirect('/')
    _username = request.session.get("username")
    if not _username == None:
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1

        student_info = get_student_info(_username)

        if student_info == None:
            #return error page
            template = 'student_profile_info.html'
            returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"),'logintype':request.session.get('type'), 'error':'Some network or Internal Error. Try after some time.'}
            return render(request, template, returnDict)

        #handle POST data here
        if not request.POST.get("password"):
            template = 'update_student_info.html'
            returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"),'logintype':request.session.get('type'), 'error':'None', 'student_login':student_info['student_login'].__dict__, 'student_detail':student_info['student_detail'].__dict__, 'msg':'Update your personal information and password here.'}
            return render(request, template, returnDict)

        #handle request.POST here
        update_data = update_student_data(request.POST, student_info)

        if update_data["success"] == 0:
            template = 'update_student_info.html'
            returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"),'logintype':request.session.get('type'), 'error':update_data["msg"], 'student_login':student_info['student_login'].__dict__, 'student_detail':student_info['student_detail'].__dict__}
            return render(request, template, returnDict)
        else:
            template = 'update_student_info.html'
            returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"),'logintype':request.session.get('type'), 'error':update_data['msg'], 'student_login':student_info['student_login'].__dict__, 'student_detail':student_info['student_detail'].__dict__}
            return render(request, template, returnDict)

        template = 'update_student_info.html'
        returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"),'logintype':request.session.get('type'), 'error':'None', 'student_login':student_info['student_login'].__dict__, 'student_detail':student_info['student_detail'].__dict__}
        return render(request, template, returnDict) 
    else:
        return HttpResponseRedirect('/')
#end def update_student_info

#start region update student data
def update_student_data(posted_dict, student_info):
    _pwd = posted_dict.get("password")
    _pwd_n = posted_dict.get("new_password")
    _pwd_r = posted_dict.get("re_new_password")

    _email = posted_dict.get("email")
    _phone = posted_dict.get("phone")

    if not _pwd == student_info['student_login'].__dict__.get("password"):
        return {"success":0, "msg":"Incorrect Password"}
    if not _pwd_n == _pwd_r:
        return {"success":0, "msg":"mismatch in new password"}
    if _pwd == _pwd_n:
        return {"success":0, "msg":"Same password entered"}
    if _email == student_info['student_detail'].__dict__.get("email"):
        return {"success":0, "msg":"Same email"}
    if _phone == student_info['student_detail'].__dict__.get("phone"):
        return {"success":0, "msg":"Same phone"}
    #else do changes and return true
    if _pwd_n == '' and _pwd_n_r == '' and _email == '' and _phone == '':
        return {"success":0, "msg":"No changes made."}
    if _pwd_n == None and _pwd_n_r == None and _email == None and _phone == None:
        return {"success":0, "msg":"No changes made."}
    try:
        if _pwd_n:
            #update pwd
            tr_lg = StudentLogin.objects.get(username=student_info['student_login'].__dict__.get("username"))
            tr_lg.password=_pwd_n
            tr_lg.save()
        if _email:
            #update email
            tr_dl = StudentDetail.objects.get(student_id=student_info['student_detail'].__dict__.get("student_id"))
            tr_dl.email=_email
            tr_dl.save()
        if _phone:
            #update phone  
            tr_dl = StudentDetail.objects.get(student_id=student_info['student_detail'].__dict__.get("student_id"))
            tr_dl.phone=_phone
            tr_dl.save()
        return {"success":1, "msg":"Successfully Updated data."}
    except:
        return {"success":0, "msg":"SQL error"}

    return {"success":1, "msg":"Successfully Updated data."}
#end region update student data

#start region teacher create lecture
def teacher_create_lecture(request):
    is_logged_in = 0
    if not request.session.get("type") == 'teacher':
        return HttpResponseRedirect('/')
    _username = request.session.get("username")
    _id = request.session.get("id")
    ent_array = EntityTable.objects.filter(section=None).values()
    sd_array = SchoolDetails.objects.all().values()
    if not _username == None:
        is_logged_in = 1
        #handle POST data here
        if not request.POST.get("password"):
            template = 'teacher_create_lecture.html'
            returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"), 'teacher_id':request.session.get("id"),'logintype':request.session.get('type'), 'error':'None', 'msg':'Create a lecture here.', 'sd_a':sd_array, 'ent_a':ent_array}
            return render(request, template, returnDict)
        else:
            #print request.POST
            created_lecture = create_lecture(request.POST, _id)
            if created_lecture.get("success") == 1:
                template = 'teacher_create_lecture.html'
                returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"), 'teacher_id':request.session.get("id"),'logintype':request.session.get('type'), 'error':'None', 'msg':created_lecture.get("msg"), 'sd_a':sd_array, 'ent_a':ent_array}
                return render(request, template, returnDict)
            else:
                template = 'teacher_create_lecture.html'
                returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"), 'teacher_id':request.session.get("id"),'logintype':request.session.get('type'), 'error':created_lecture.get("msg"), 'msg':created_lecture.get("msg"), 'sd_a':sd_array, 'ent_a':ent_array}
                return render(request, template, returnDict)
    else:
        return HttpResponseRedirect('/')
#end region teacher create lecture

#start region create lecture
def create_lecture(my_dict, _id):
    _pwd = my_dict.get("password")
    _sub = my_dict.get("subject")
    _top = my_dict.get("topic")
    _desc = my_dict.get("description")
    _s_hr = my_dict.get("start_hour")
    _s_min = my_dict.get("start_min")
    _e_hr = my_dict.get("end_hour")
    _e_min = my_dict.get("end_min")
    _dt = my_dict.get("date")
    _school = int(my_dict.get("school"))
    _class = int(my_dict.get("Class"))

    _s_tm_temp = "%s %s:%s:00+5:30"%(_dt, _s_hr, _s_min)
    _s_tm = dateutil.parser.parse(_s_tm_temp)

    _e_tm_temp = "%s %s:%s:00+5:30"%(_dt, _e_hr, _e_min)
    _e_tm = dateutil.parser.parse(_e_tm_temp)
    _c_tm_temp = dt.datetime.now(timezone('Asia/Calcutta')).strftime("%Y-%m-%d %H:%M:%S+05:30")
    _c_tm = dateutil.parser.parse(_c_tm_temp)
    
    #import pdb; pdb.set_trace();
    if not _c_tm < _s_tm:
        return {"success":0, "msg":"Timing error"}
    if not _s_tm < _e_tm:
        return {"success":0, "msg":"Timing error"}

    if not _pwd == TeacherLogin.objects.get(teacher_id=_id).__dict__.get("password"):
        return {"success":0, "msg":"Invalid password"}

    try:
        t_obj = TeacherLogin.objects.get(teacher_id=_id)
        s_obj = SchoolDetails.objects.get(school_id=_school)
        e_obj = EntityTable.objects.get(entity_id=_class)
        lt_obj = LectureTeacher(teacher=t_obj, school=s_obj, entity=e_obj, lecture_start_time=_s_tm, lecture_end_time=_e_tm, subject=_sub, topic=_top, description=_desc, status='N')
        lt_obj.save()
        st_objs = StudentDetail.objects.filter(school=s_obj, entity=e_obj)
        for st_obj in st_objs:
            sl_obj = LectureStudent(student=st_obj.student, lecture=lt_obj, present="N", attention_percent=0, emotion_data="no data", attention_graph_link="none", emotion_graph_link="none")
            sl_obj.save()
        return {"success":1, "msg":"Lecture Created."}
    except:
        return {"success":0, "msg":"SQL error"} 

    return {"success":0, "msg":"SQL error"} 
#end region create lecture

#region view prev lectures
def teacher_prev_lectures(request):
    is_logged_in = 0
    if not request.session.get("type") == 'teacher':
        return HttpResponseRedirect('/')
    _username = request.session.get("username")
    _id = request.session.get("id")
    #ent_array = EntityTable.objects.filter(section=None).values()
    #sd_array = SchoolDetails.objects.all().values()
    disp_arr = []
    if not _username == None:
        is_logged_in = 1
        lt_objs = LectureTeacher.objects.filter(teacher_id=_id)
        for lt_obj in lt_objs:
            _c_tm_temp = dt.datetime.now(timezone('UTC')).strftime("%Y-%m-%d %H:%M:%S")
            _c_tm = dateutil.parser.parse(_c_tm_temp)
            _o_tm = dateutil.parser.parse(lt_obj.__dict__.get("lecture_end_time").strftime("%Y-%m-%d %H:%M:%S"))
            _o_tm_temp = lt_obj.__dict__.get("lecture_end_time").astimezone(timezone('Asia/Calcutta'))
            _s_tm_temp = lt_obj.__dict__.get("lecture_start_time").astimezone(timezone('Asia/Calcutta'))
            if _o_tm_temp.replace(tzinfo = None) >= _c_tm:
                tmp_dict = lt_obj.__dict__
                tmp_dict["lecture_start_time"] = dateutil.parser.parse(_s_tm_temp.strftime("%Y-%m-%d %H:%M:%S"))
                tmp_dict["lecture_end_time"] = dateutil.parser.parse(_o_tm_temp.strftime("%Y-%m-%d %H:%M:%S"))
                disp_arr.append(lt_obj.__dict__)
        template = 'teacher_prev_lectures.html'
        returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"), 'teacher_id':request.session.get("id"),'logintype':request.session.get('type'), 'len':len(disp_arr), 'disp_arr':disp_arr}
        return render(request, template, returnDict)
    else:
        return HttpResponseRedirect('/')
#end region view prev lectures

#region view new lectures
def teacher_new_lectures(request):
    is_logged_in = 0
    if not request.session.get("type") == 'teacher':
        return HttpResponseRedirect('/')
    _username = request.session.get("username")
    _id = request.session.get("id")
    #ent_array = EntityTable.objects.filter(section=None).values()
    #sd_array = SchoolDetails.objects.all().values()
    disp_arr = []
    if not _username == None:
        is_logged_in = 1
        lt_objs = LectureTeacher.objects.filter(teacher_id=_id)
        for lt_obj in lt_objs:
            _c_tm_temp = dt.datetime.now(timezone('Asia/Calcutta')).strftime("%Y-%m-%d %H:%M:%S")
            _c_tm = dateutil.parser.parse(_c_tm_temp)
            _o_tm = dateutil.parser.parse(lt_obj.__dict__.get("lecture_end_time").strftime("%Y-%m-%d %H:%M:%S"))
            _o_tm_temp = lt_obj.__dict__.get("lecture_end_time").astimezone(timezone('Asia/Calcutta'))
            _s_tm_temp = lt_obj.__dict__.get("lecture_start_time").astimezone(timezone('Asia/Calcutta'))
            print _o_tm, _c_tm, _o_tm_temp.replace(tzinfo=None)
            if _o_tm_temp.replace(tzinfo = None) >= _c_tm:
                tmp_dict = lt_obj.__dict__
                tmp_dict["lecture_start_time"] = dateutil.parser.parse(_s_tm_temp.strftime("%Y-%m-%d %H:%M:%S"))
                tmp_dict["lecture_end_time"] = dateutil.parser.parse(_o_tm_temp.strftime("%Y-%m-%d %H:%M:%S"))
                disp_arr.append(tmp_dict)
        #print disp_arr
        print len(disp_arr)
        template = 'teacher_new_lectures.html'
        returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"), 'teacher_id':request.session.get("id"),'logintype':request.session.get('type'), 'len':len(disp_arr), 'disp_arr':disp_arr}
        return render(request, template, returnDict)
    else:
        return HttpResponseRedirect('/')
#end region view new lectures

#region view prev lectures
def student_prev_lectures(request):
    is_logged_in = 0
    if not request.session.get("type") == 'student':
        return HttpResponseRedirect('/')
    _username = request.session.get("username")
    _id = request.session.get("id")
    #ent_array = EntityTable.objects.filter(section=None).values()
    #sd_array = SchoolDetails.objects.all().values()
    disp_arr = []
    if not _username == None:
        is_logged_in = 1
        ls_objs = LectureStudent.objects.filter(student_id=_id)
        for ls_obj in ls_objs:
            lt_obj = ls_obj.lecture
            tl_obj = lt_obj.teacher
            _c_tm_temp = dt.datetime.now(timezone('Asia/Calcutta')).strftime("%Y-%m-%d %H:%M:%S")
            _c_tm = dateutil.parser.parse(_c_tm_temp)
            _o_tm_temp = lt_obj.__dict__.get("lecture_end_time").astimezone(timezone('Asia/Calcutta'))
            _s_tm_temp = lt_obj.__dict__.get("lecture_start_time").astimezone(timezone('Asia/Calcutta'))
            _o_tm = dateutil.parser.parse(lt_obj.__dict__.get("lecture_end_time").strftime("%Y-%m-%d %H:%M:%S"))
            if _o_tm_temp.replace(tzinfo = None) >= _c_tm:
                temp_dict = {}
                lt_obj_dict = lt_obj.__dict__
                ls_obj_dict = ls_obj.__dict__
                tl_obj_dict = tl_obj.__dict__
                temp_dict["lecture_id"] = ls_obj_dict.get("lecture_id")
                temp_dict["teacher"] = tl_obj_dict.get("username")
                temp_dict["subject"] = lt_obj_dict.get("subject")
                temp_dict["topic"] = lt_obj_dict.get("topic")
                temp_dict["description"] = lt_obj_dict.get("description")
                temp_dict["lecture_start_time"] = dateutil.parser.parse(_s_tm_temp.strftime("%Y-%m-%d %H:%M:%S"))
                temp_dict["lecture_end_time"] = dateutil.parser.parse(_o_tm_temp.strftime("%Y-%m-%d %H:%M:%S"))
                temp_dict["present"] = ls_obj_dict.get("present")
                temp_dict["attention_percent"] = ls_obj_dict.get("attention_percent")
                temp_dict["emotion_data"] = ls_obj_dict.get("emotion_data")
                temp_dict["attention_graph_link"] = ls_obj_dict.get("attention_graph_link")
                temp_dict["emotion_graph_link"] = ls_obj_dict.get("emotion_graph_link")
                disp_arr.append(temp_dict)
        template = 'student_prev_lectures.html'
        returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"), 'student_id':request.session.get("id"),'logintype':request.session.get('type'), 'len':len(disp_arr), 'disp_arr':disp_arr}
        return render(request, template, returnDict)
    else:
        return HttpResponseRedirect('/')
#end region view prev lectures

#region view new lectures
def student_new_lectures(request):
    is_logged_in = 0
    if not request.session.get("type") == 'student':
        return HttpResponseRedirect('/')
    _username = request.session.get("username")
    _id = request.session.get("id")
    #ent_array = EntityTable.objects.filter(section=None).values()
    #sd_array = SchoolDetails.objects.all().values()
    disp_arr = []
    if not _username == None:
        is_logged_in = 1
        ls_objs = LectureStudent.objects.filter(student_id=_id)
        for ls_obj in ls_objs:
            lt_obj = ls_obj.lecture
            tl_obj = lt_obj.teacher
            _c_tm_temp = dt.datetime.now(timezone('Asia/Calcutta'))
            _c_tm = dateutil.parser.parse(_c_tm_temp.strftime("%Y-%m-%d %H:%M:%S"))
            _o_tm_temp = lt_obj.__dict__.get("lecture_end_time").astimezone(timezone('Asia/Calcutta'))
            _s_tm_temp = lt_obj.__dict__.get("lecture_start_time").astimezone(timezone('Asia/Calcutta'))
            _o_tm = dateutil.parser.parse(lt_obj.__dict__.get("lecture_end_time").strftime("%Y-%m-%d %H:%M:%S"))
            #print _c_tm, _o_tm, _c_tm_temp, _o_tm_temp
            if _o_tm_temp.replace(tzinfo = None) >= _c_tm:
                #print _c_tm, _o_tm, _c_tm_temp, dateutil.parser.parse(_o_tm_temp.strftime("%Y-%m-%d %H:%M:%S"))
                temp_dict = {}
                lt_obj_dict = lt_obj.__dict__
                ls_obj_dict = ls_obj.__dict__
                tl_obj_dict = tl_obj.__dict__
                temp_dict["lecture_id"] = ls_obj_dict.get("lecture_id")
                temp_dict["teacher"] = tl_obj_dict.get("username")
                temp_dict["subject"] = lt_obj_dict.get("subject")
                temp_dict["topic"] = lt_obj_dict.get("topic")
                temp_dict["description"] = lt_obj_dict.get("description")
                temp_dict["lecture_start_time"] = dateutil.parser.parse(_s_tm_temp.strftime("%Y-%m-%d %H:%M:%S"))
                temp_dict["lecture_end_time"] = dateutil.parser.parse(_o_tm_temp.strftime("%Y-%m-%d %H:%M:%S"))
                temp_dict["present"] = ls_obj_dict.get("present")
                temp_dict["attention_percent"] = ls_obj_dict.get("attention_percent")
                temp_dict["emotion_data"] = ls_obj_dict.get("emotion_data")
                temp_dict["attention_graph_link"] = ls_obj_dict.get("attention_graph_link")
                temp_dict["emotion_graph_link"] = ls_obj_dict.get("emotion_graph_link")
                disp_arr.append(temp_dict)
        #print disp_arr
        template = 'student_new_lectures.html'
        returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"), 'student_id':request.session.get("id"),'logintype':request.session.get('type'), 'len':len(disp_arr), 'disp_arr':disp_arr}
        return render(request, template, returnDict)
    else:
        return HttpResponseRedirect('/')
#end region view new lectures

#start region attend lecture student
def attend_lecture_student(request, lecture_id1):
    i_lecture_id = int(lecture_id1)
    is_logged_in = 0
    if not request.session.get("type") == 'student':
        return HttpResponseRedirect('/')
    _username = request.session.get("username")
    _id = request.session.get("id")
    if not _username == None:
        lt_obj = LectureTeacher.objects.get(lecture_id=i_lecture_id)
        ls_obj = LectureStudent.objects.get(lecture=lt_obj, student=StudentLogin.objects.get(student_id=_id))
        if ls_obj == None:
            return HttpResponseRedirect('/error_page/')
        if not lt_obj.__dict__.get("status") == 'O':
            print 1
            return HttpResponseRedirect('/error_page/')
        request.session["lecture_id"] = i_lecture_id
        ls_obj.present = 'Y'
        ls_obj.save()
        return HttpResponseRedirect('/login_combined_app_test/')
    else:
        return HttpResponseRedirect('/error_page/')
#end region end lecture student

#start region start lecture teacher
def start_lecture_teacher(request, lecture_id1):
    i_lecture_id = int(lecture_id1)
    is_logged_in = 0
    if not request.session.get("type") == 'teacher':
        return HttpResponseRedirect('/error_page/')
    _username = request.session.get("username")
    _id = request.session.get("id")
    if not _username == None:
        lt_obj = LectureTeacher.objects.get(lecture_id=i_lecture_id, teacher=TeacherLogin.objects.get(teacher_id=_id))
        if not lt_obj:
            return HttpResponseRedirect('/error_page/')
        if lt_obj.status == 'E':
            return HttpResponseRedirect('/error_page/')
        lt_obj.status = 'O'
        lt_obj.save()
        request.session["lecture_id"] = i_lecture_id
        return HttpResponseRedirect('/ongoing_lecture_page/')
    else:
        return HttpResponseRedirect('/error_page/')
#end region start lecture teacher

#start region login combined app rl
def login_combined_app_rl(request):
    context = locals()
    from ipware.ip import get_real_ip
    ip_arr = []
    ip_real = get_real_ip(request)
    if ip_real is not None:
        ip_arr.append(ip_real)
    else:
        ip_arr.append('')
    
    from ipware.ip import get_ip
    #ip_arr = []
    ip = get_ip(request)
    if ip is not None:
        ip_arr.append(ip)
    else:
        ip_arr.append('')

    f1 = open("ip.txt", "a")
    for x in ip_arr:
        f1.write(x)
        f1.write('combined app\n')
    f1.close()

    is_logged_in = 0
    if not request.session.get("username") == None:
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1

    template = 'login_combined_app_rl.html'
    returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"), 'lecture_id':request.session.get('lecture_id')}
    return render(request, template, returnDict)
#end region login combined app rl

#start get emotion data rl 
@csrf_exempt
def get_emotion_data_rl(request):
    #fromJs = json.loads(request.POST)
    #print fromJs
    #import pdb; pdb.set_trace();
    post_array = request.POST
    is_logged_in = 0
    _username = request.session.get("username", "")
    if not _username == "":
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1
    else:
        return HttpResponse("Failure")
    i_ = 0
    j_ = 0
    emo_dict = {"angry":[0], "sad":[0], "surprised":[0], "happy":[0]}
    while (1):
        flag = 0
        for j_ in range(4):
            qe_str = 'data['+str(i_)+"]["+str(j_)+"][emotion]"
            qv_str = 'data['+str(i_)+"]["+str(j_)+"][value]"
            emo_ = post_array.getlist(qe_str)
            val_ = post_array.getlist(qv_str)
            if emo_==None or len(emo_) == 0:
                flag = 1
                break
            else:
                emo_list = emo_dict.get(emo_[0])
                if emo_list == None or len(emo_list) == 0:
                    pass
                else:
                    emo_dict[emo_[0]].append(val_[0])

        i_ = i_+1
        if flag == 1:
            break

    #print emo_dict
    #float_emotion_array = []
    #id_ = 0
    #x_arr = []
    plot_key = []
    for emo_key in emo_dict:
        emo_arr = emo_dict[emo_key]
        p_key = "y = "+emo_key
        plot_key.append(emo_key)
        float_emo_arr = []
        x_arr = []
        id_ = 0
        for emo_val in emo_arr:
            float_emo_arr.append(float(emo_val))
            x_arr.append(id_)
            id_+=1
        plt.plot(x_arr, float_emo_arr)
    plt.legend(plot_key, loc='upper left')


    #    float_att_array.append(float(att))
    #    id_ += 1
    #    x_arr.append(id_)
    #plt.plot(x_arr, att_array)
    plt.xlabel("time in seconds")
    plt.ylabel("weighted emotion value")
    plt_file_name = "emotion_data_"
    dt_timestamp = dt.datetime.fromtimestamp(time.time()).strftime("%Y_%m_%d_%H_%M_%S")
    plt_file_name = _username + plt_file_name+dt_timestamp+".png"
    plt.savefig(plt_file_name)
    plt.gcf().clear()
    global glob_emo_file
    glob_emo_file = plt_file_name
    return HttpResponse("Success!")
#end region get emotion data rl    

#start region get attention data rl
@csrf_exempt
def get_attention_data_rl(request):
    #fromJs = json.loads(request.POST)
    #print fromJs
    #import pdb; pdb.set_trace();
    att_array = request.POST.getlist(u'colAttentionData[]')
    is_logged_in = 0
    _username = request.session.get("username", "")
    _id = request.session.get("id")
    if not _username == "":
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1
        #_username = 
    else:
        return HttpResponse("Failure")
    float_att_array = []
    id_ = 0
    x_arr = []
    for att in att_array:
        float_att_array.append(float(att))
        id_ += 1
        x_arr.append(id_)
    plt.plot(x_arr, att_array)
    plt.xlabel("time in seconds")
    plt.ylabel("attention level in percent")
    plt_file_name = "attention_data_"
    dt_timestamp = dt.datetime.fromtimestamp(time.time()).strftime("%Y_%m_%d_%H_%M_%S")
    plt_file_name = _username + plt_file_name+dt_timestamp+".png"
    plt.savefig(plt_file_name)
    plt.gcf().clear()
    glob_att_file = plt_file_name
    global glob_emo_file
    #try:
    send_email.send_email("date:val time:val", "dharna graph for user", [glob_att_file, glob_emo_file])
    sd_obj = StudentDetail.objects.get(student_id=_id)
        #send_email.send_email_client(sd_obj.__dict__.get("email"),"date:val time:val", "dharna graph for user", [glob_att_file, glob_emo_file])
        #upload attention file
    print glob_att_file, glob_emo_file
    transferData = upload_to_dropbox.upload_to_dropbox(DROPBOX_ACCESS_TOKEN)
    transferData.upload_file(file_from="%s"%(glob_att_file), file_to="/dharna_app/%s"%(glob_att_file))
    att_file_url = transferData.get_shared_file_url()
        #upload emotion file
    transferData1 = upload_to_dropbox.upload_to_dropbox(DROPBOX_ACCESS_TOKEN)
    transferData1.upload_file(file_from=glob_emo_file, file_to="/dharna_app/%s"%(glob_emo_file))
    emo_file_url = transferData1.get_shared_file_url()
    #make database queries.
    l_id = request.session.get("lecture_id")
    ls_obj = LectureStudent.objects.get(lecture=LectureTeacher.objects.get(lecture_id=l_id),student=StudentLogin.objects.get(student_id=_id))
    ls_obj.present="Y"
    #calculate attention percent
    #calculate emotion result
    ls_obj.attention_graph_link=att_file_url
    ls_obj.emotion_graph_link=emo_file_url
    ls_obj.save()
    #except:
        #return HttpResponse("Failure!")
    return HttpResponse("Success!")
#end region get attention data rl

#start region error_page
def error_page(request):
    error_message = request.session.get("error_message", "None")
    if not error_message == "None":
        del request.session["error_message"]
        request.session.modified = True
    template = 'error_page.html'    
    returnDict = { 'error_message':error_message}
    return render(request, template, returnDict)
#end region error_page

#start ongoing lecture page
def ongoing_lecture_page(request):
    is_logged_in = 0
    if not request.session.get("username") == None:
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1
    template = 'ongoing_lecture_page.html'
    returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"), 'lecture_id':request.session.get('lecture_id')}
    return render(request, template, returnDict)
#end ongoing lecture page

#start end lecture student
def end_lecture_student(request):
    is_logged_in = 0
    _id = None
    i_lecture_id = 0
    if not request.session.get("username") == None:
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1
        _id = request.session.get("id")
    if not request.session.get("lecture_id") == None:
        i_lecture_id = request.session.get("lecture_id")
        print i_lecture_id
        del request.session["lecture_id"]
    print i_lecture_id
    template = 'end_lecture_student.html'
    returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"), 'lecture_id':request.session.get('lecture_id'), 'logintype':request.session.get('type'), 'lecture_id':i_lecture_id}
    return render(request, template, returnDict)
#end end lecture student

#start end lecture teacher
def end_lecture_teacher(request):
    is_logged_in = 0
    _id = None
    i_lecture_id = 0
    if not request.session.get("username") == None:
        #return HttpResponseRedirect('/combined_app/')
        is_logged_in = 1
        _id = request.session.get("id")
    if not request.session.get("lecture_id") == None:
        i_lecture_id = request.session.get("lecture_id")
        lt_obj = LectureTeacher.objects.get(lecture_id=i_lecture_id, teacher=TeacherLogin.objects.get(teacher_id=_id))
        lt_obj.status = 'E'
        lt_obj.save()
        print i_lecture_id
        del request.session["lecture_id"]
    print i_lecture_id
    template = 'end_lecture_teacher.html'
    returnDict = {'is_logged_in':is_logged_in, 'username':request.session.get("username"), 'lecture_id':request.session.get('lecture_id'), 'logintype':request.session.get('type'), 'lecture_id':i_lecture_id}
    return render(request, template, returnDict)
#end end lecture teacher

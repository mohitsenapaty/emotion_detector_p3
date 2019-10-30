"""emotion_detector_p3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from test_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', views.home, name='home'),
    path(r'eye_gaze_tracker/', views.eye_gaze_tracker, name='eye_gaze_tracker'),
    path(r'emotion_detector/', views.emotion_detector, name='emotion_detector'),
    path(r'get_attention_data/', views.get_attention_data, name='get_attention_data'),
    path(r'get_emotion_data/',views.get_emotion_data, name='get_emotion_data'),
    path(r'get_attention_data_test/', views.get_attention_data_test, name='get_attention_data_test'),
    path(r'get_emotion_data_test/',views.get_emotion_data_test, name='get_emotion_data_test'),
    path(r'combined_app/', views.combined_app, name='combined_app'),
    path(r'combined_app_new/', views.combined_app_new, name='combined_app_new'),
    path(r'combined_app_live/', views.combined_app_live, name='combined_app_live'),
    path(r'login_page/', views.login_page, name='login_page'),
    path(r'log_out/', views.log_out, name='log_out'),
    path(r'login_combined_app/', views.login_combined_app, name='login_combined_app'),
    path(r'login_combined_app_test/', views.login_combined_app_test, name='login_combined_app_test'),
    path(r'chatframe/', views.chatframe, name='chatframe'),
    path(r'register_page/', views.register_page, name='register_page'),
    path(r'teacher_profile_info/', views.teacher_profile_info, name='teacher_profile_info'),
    path(r'update_teacher_info/', views.update_teacher_info, name='update_teacher_info'),
    path(r'student_profile_info/', views.student_profile_info, name='student_profile_info'),
    path(r'update_student_info/', views.update_student_info, name='update_student_info'),
    path(r'teacher_create_lecture/', views.teacher_create_lecture, name='teacher_create_lecture'),
    path(r'teacher_prev_lectures/', views.teacher_prev_lectures, name='teacher_prev_lectures'),
    path(r'teacher_new_lectures/', views.teacher_new_lectures, name='teacher_new_lectures'),
    path(r'student_prev_lectures/', views.student_prev_lectures, name='student_prev_lectures'),
    path(r'student_new_lectures/', views.student_new_lectures, name='student_new_lectures'),
    path(r'attend_lecture_student/(?P<lecture_id1>\d+)/', views.attend_lecture_student, name='attend_lecture_student'),
    path(r'start_lecture_teacher/(?P<lecture_id1>\d+)/', views.start_lecture_teacher, name='start_lecture_teacher'),
    path(r'login_combined_app_rl/', views.login_combined_app_rl, name='login_combined_app_rl'),
    path(r'error_page/', views.error_page, name='error_page'),
    path(r'ongoing_lecture_page/', views.ongoing_lecture_page, name='ongoing_lecture_page'),
    path(r'end_lecture_student/', views.end_lecture_student, name='end_lecture_student'),
    path(r'end_lecture_teacher/', views.end_lecture_teacher, name='end_lecture_teacher'),
    path(r'team/', views.team, name='team'),
    path(r'live_demo/', views.live_demo, name='live_demo'),
    path(r'contact/', views.contact, name='contact'),
]

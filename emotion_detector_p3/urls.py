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
from loginApp import views as loginViews
from teacherfunctions import views as tfViews
from subscription import views as subscriptionViews
from lecturefunctions import views as lfViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginViews.home, name='home'),
    path('login/', loginViews.login, name='login'),
    path('logout/', loginViews.logout, name='logout'),
    path('teacher/createcourse/', tfViews.createcourse, name='createcourse'),
    path('teacher/viewcourse/', tfViews.getallcourseforteacher, name='getallcourseforteacher'),
    #path('teacher/viewcourse/<str:courseid>/', tfViews.getsinglecourseview, name='getallcourseforteacher'),
    path('teacher/<str:courseid>/viewlectures/', tfViews.viewlecturesforcourse, name='viewlecturesforcourse'),
    path('teacher/<str:courseid>/createlecture/', tfViews.createlectureforcourse, name='createlectureforcourse'),
    #url(r'^$', views.home, name='home'),
    path('courseview/all/', subscriptionViews.viewallcourses, name='viewallcourses'),
    path('subscribe/<str:courseid>/', subscriptionViews.subscribetocourse, name='subscribetocourse'),
    path('viewsubscribedcourses/', subscriptionViews.viewsubscribedcourses, name='viewsubscribedcourses'),
    path('course/<str:courseid>/viewlectures/', subscriptionViews.viewlecturesforcourse, name='viewlecturesforcourse'),
    #
    #path('teacher/<str:lectureid>/lecturepage/', lfViews.startlecturepage, name='startlecturepage'),
    path('lecture/<str:lectureid>/lecturepageuser/', lfViews.startlecturepageuser, name='startlecturepageuser'),
    path('teacher/ongoinglecture/<str:lectureid>/', lfViews.startlectureteacher, name='startlectureteacher'),
]

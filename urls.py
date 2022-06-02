from django.urls import path
from.import views
from .views import JobCreate
from .views import jobList
from .views import JobDetail,JobUpdate,JobDelete


urlpatterns=[   
    
     path('register',views.register,name='register'),
     path('regcode',views.regcode,name='regcode'),
     path('load',views.load,name='load'),
     path('data',views.data,name='data'),
     path('jobcreate',JobCreate.as_view()),
     path('joblist', jobList.as_view()),
     path('<pk>/',JobDetail.as_view()),
     path('<pk>/jupdate',JobUpdate.as_view()),
     path('<pk>/jdelete',JobDelete.as_view()),
 ]
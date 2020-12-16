from django.urls import path

from . import views

app_name= 'polls'
urlpatterns=[
		path('',views.employee, name='employee'),
		path('<int:id>/',views.detail, name='detail'),
		path('insert/',views.insert,name='insert')
]

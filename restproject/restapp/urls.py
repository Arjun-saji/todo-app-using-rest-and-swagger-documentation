from django.urls import path,include
# from . import views # function based views
from .views import *
from rest_framework.routers import DefaultRouter

 # this urlpatterns are for function based views

# urlpatterns=[ path("tasks/",views.task_view,name="tasks views"),

# path("tasks/<int:pk>/",views.task_details,name="task details"),


# ]


# this urlpatterns are for Class based views

urlpatterns=[ path("tasks/",Taskview.as_view(),name="tasks views"),

path("tasks/<int:pk>/",DetailTaskView.as_view(),name="task details"),


]


# this urlpatterns are for Generics views

# urlpatterns=[ path("tasks/",TaskListCreate.as_view(),name="tasks views"),

# path("tasks/<int:pk>/",TaskRetrieveUpdateDestroy.as_view(),name="task details"),


# ]


#Viewset

# router=DefaultRouter()
# router.register(r'tasks',TaskViewSet)



# urlpatterns=[ path("",include(router.urls)),

# ]
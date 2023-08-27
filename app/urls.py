from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
     path("add_student",views.add_student,name='student'),
      path("add_college",views.add_college,name='college'),
       path("add_branch",views.add_branch,name='branch'),
          path("show_student",views.show_students,name='students'),
   path('get_branches/', views.get_branches, name='get_branches'),
      path('get_branch/', views.get_branch, name='get_branch'),
            path('add_col/', views.add_col, name='add_col'),
]
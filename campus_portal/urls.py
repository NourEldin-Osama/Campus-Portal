from django.urls import path

from . import views

# if the link =  campus_portal/user/nour  user: url endpoint, nour: URL parameter
urlpatterns = [
    path('', views.index, name='home'), path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'), path('colleges', views.colleges, name='colleges'),
    path('about_us', views.about_us, name='about_us'), path('Login', views.login, name='Login'),
    path('Logout', views.logout, name='Logout'), path('student_signup', views.student_signup, name='student_signup'),
    path('doctor_signup', views.doctor_signup, name='doctor_signup'),
    path('create_course', views.create_course, name='create_course'),
    path('view_courses', views.view_courses, name='view_courses'),
    path('user/<str:user_name>', views.view_user_info, name='user_info'),
    path('user/<str:user_name>/edit', views.edit_user_info, name='edit_user_info'),
    path('user/<str:user_name>/be_student', views.be_student, name='be_student'),
    path('user/<str:user_name>/be_doctor', views.be_doctor, name='be_doctor'),
    path('user/<str:user_name>/be_admin', views.be_admin, name='be_admin'),
    path('visualization', views.visualization, name='visualization'),
    path('course/<int:course_id>', views.view_course_info, name='course_info'),
    path('course/<int:course_id>/enroll', views.enroll_in_course, name='enroll_in_course'),
    path('course/<int:course_id>/view_contents', views.view_course_contents, name='view_course_contents'),
    path('course/<int:course_id>/add_contents', views.add_course_contents, name='add_course_contents'),
]

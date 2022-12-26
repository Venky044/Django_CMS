
from django.urls import path
from .views import (loginUser, logoutUser, registerUser, Home, 
                    StaffList, StaffDetails, Updatestaff, 
                    StaffAccount, StaffCreateMessage,
                    StaffInbox, StaffViewMessage, StaffDeleteMessage,
                    StudentsList, StudentDetails, CreateStudent,
                    UpdateStudent, DeleteStudent, StudentResult,
                    StudentInbox, CreateStudentMessage, StudentViewMessage, 
                    StudentDeleteMessage, EventsList, AddEvents,
                    DeleteEvents, contactusview)

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerUser, name='register'),

    # Staffs
    path('', Home, name='Home'),
    path('staff/', StaffList, name='staff-List'),
    path('staff/<str:pk>/', StaffDetails, name='staff'),
    path('staff-account/', StaffAccount, name='staff-account'),
    path('update-staff/<str:pk>/', Updatestaff, name='update-staff'),
    path('staff-inbox/', StaffInbox, name='staff-inbox'),
    path('staff-message/<str:pk>/', StaffViewMessage, name='staff-message'),
    path('staff-createmsg/<str:pk>/', StaffCreateMessage, name='staff-createmsg'),
    path('staff-deletemsg/<str:pk>/', StaffDeleteMessage, name='staff-deletemsg'),

    # Students
    path('student/', StudentsList, name='student-List'),
    path('student/<str:pk>/', StudentDetails, name='student'),
    path('create-student/', CreateStudent, name='create-student'),
    path('update-student/<str:pk>/', UpdateStudent, name='update-student'),
    path('delete-student/<str:pk>/', DeleteStudent, name='delete-student'),
    path('result/', StudentResult, name='result'),
    path('student-inbox/', StudentInbox, name='student-inbox'),
    path('student-viewmsg/<str:pk>/', StudentViewMessage, name='student-viewmsg'),
    path('student-message/<str:pk>/', CreateStudentMessage, name='student-message'),
    path('student-deletemsg/<str:pk>/', StudentDeleteMessage, name='student-deletemsg'),

    # Events
    path('events/', EventsList, name='events'),
    path('add-event/', AddEvents, name='add-event'),
    path('delete-event/<str:pk>/', DeleteEvents, name='delete-event'),

    path('contactus/', contactusview, name='contactus'),
]
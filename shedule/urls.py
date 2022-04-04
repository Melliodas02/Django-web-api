from django.urls import path
from .views import *

urlpatterns = [
    path('Faculty', FacultyListView.as_view(), name='FacultyList'),
    path('Faculty/Add', FacultyView.as_view(), name='Faculty'),
    path('Faculty/Delete/<int:pk>', FacultyView.as_view(), name='FacultyDelete'),
    path('Faculty/Update/<int:pk>', FacultyView.as_view(), name='FacultyUpdate'),
    path('Faculty/<int:pk>', FacultyView.as_view(), name='FacultyDetail'),

    path('Specialty', SpecialtyListView.as_view(), name='SpecialtyList'),
    path('Specialty/<int:pk>', SpecialtyView.as_view(), name='SpecialtyList'),
    path('Specialty/Add', SpecialtyView.as_view(), name='Specialty'),
    path('Specialty/Delete/<int:pk>', SpecialtyView.as_view(), name='SpecialtyDelete'),
    path('Specialty/Update/<int:pk>', SpecialtyView.as_view(), name='SpecialtyUpdate'),

    path('Group', GroupListView.as_view(), name='GroupList'),
    path('Group/Add', GroupView.as_view(), name='GroupAdd'),
    path('Group/Delete/<int:pk>', GroupView.as_view(), name='GroupDelete'),
    path('Group/Update/<int:pk>', GroupView.as_view(), name='GroupUpdate'),
    path('Group/<int:pk>', GroupView.as_view(), name='Group'),

    path('Teacher', TeacherListView.as_view(), name='TeacherList'),
    path('Teacher/<int:pk>', TeacherView.as_view(), name='Teacher'),
    path('Teacher/Add', TeacherView.as_view(), name='TeacherAdd'),
    path('Teacher/Delete/<int:pk>', TeacherView.as_view(), name='TeacherDelete'),
    path('Teacher/Update/<int:pk>', TeacherView.as_view(), name='TeacherUpdate'),

    path('Subject', SubjectListView.as_view(), name="SubjectList"),
    path('Subject/<int:pk>', SubjectView.as_view(), name="Subject"),
    path('Subject/Add', SubjectView.as_view(), name="Subject"),
    path('Subject/Delete/<int:pk>', SubjectView.as_view(), name="SubjectDelete"),
    path('Subject/Update/<int:pk>', SubjectView.as_view(), name="SubjectUpdate"),

    path('ClassRoom', ClassRoomListView.as_view(), name="ClassRoomList"),
    path('ClassRoom/<int:pk>', ClassRoomView.as_view(), name="ClassRoom"),
    path('ClassRoom/Add', ClassRoomView.as_view(), name="ClassRoom"),
    path('ClassRoom/Delete/<int:pk>', ClassRoomView.as_view(), name="ClassRoomDelete"),
    path('ClassRoom/Update/<int:pk>', ClassRoomView.as_view(), name="ClassRoomUpdate"),

    path('SubjectType', SubjectTypeListView.as_view(), name="SubjectTypeList"),
    path('SubjectType/<int:pk>', SubjectTypeView.as_view(), name="SubjectType"),
    path('SubjectType/Add', SubjectTypeView.as_view(), name="SubjectType"),
    path('SubjectType/Delete/<int:pk>', SubjectTypeView.as_view(), name="SubjectTypeDelete"),
    path('SubjectType/Update/<int:pk>', SubjectTypeView.as_view(), name="SubjectTypeUpdate"),

    path('Schedule', ScheduleListView.as_view(), name="ScheduleList"),
    path('Schedule/<int:pk>', ScheduleView.as_view(), name="Schedule"),
    path('Schedule/Add', ScheduleView.as_view(), name='Schedule'),
    path('Schedule/Delete/<int:pk>', ScheduleView.as_view(), name='ScheduleDelete'),
    path('Schedule/Update/<int:pk>', ScheduleView.as_view(), name='ScheduleUpdate'),
    path('ScheduleShow', ScheduleShowView.as_view())
]

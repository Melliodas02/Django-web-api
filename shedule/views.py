from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


# Работа с факультетами
class FacultyListView(APIView):
    def get(self, request):
        queryset = Faculty.objects.all()
        serializer = FacultySerializer
        faculty = serializer(queryset, many=True)
        return Response(faculty.data)


class FacultyView(APIView):
    def post(self, request):
        serializer = FacultySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        faculty = Faculty.objects.get(pk=pk)
        faculty.delete()
        return Response({
            "message": "success"
        })

    def get(self, request, pk):
        faculty = Faculty.objects.get(pk=pk)
        serializer = FacultySerializer(faculty)
        return Response(serializer.data)

    def put(self, request, pk):
        saved_specialty = Faculty.objects.get(pk=pk)
        data = request.data
        serializer = FacultySerializer(instance=saved_specialty, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()

        return Response({
            "success": "Specialty '{}' updated successfully".format(article_saved.Name)
        })


# Работа с специальностями
class SpecialtyListView(APIView):
    def get(self, request):
        queryset = Specialty.objects.all()
        serializer = SpecialtySerializer
        specialty = serializer(queryset, many=True)
        return Response(specialty.data)


class SpecialtyView(APIView):
    def post(self, request):
        serializer = SpecialtySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        specialty = Specialty.objects.get(pk=pk)
        specialty.delete()
        return Response({
            'message': 'success'
        })

    def get(self, request, pk):
        specialty = Specialty.objects.get(pk=pk)
        serializer = SpecialtySerializer(specialty)
        return Response(serializer.data)

    def put(self, request, pk):
        saved_specialty = Specialty.objects.get(pk=pk)
        data = request.data
        serializer = SpecialtySerializer(instance=saved_specialty, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()

        return Response({
            "success": "Specialty '{}' updated successfully".format(article_saved.Name)
        })


class GroupListView(APIView):
    def get(self, request):
        queryset = Group.objects.all()
        serializer = GroupSerializer
        specialty = serializer(queryset, many=True)
        return Response(specialty.data)


class GroupView(APIView):
    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        specialty = Group.objects.get(pk=pk)
        specialty.delete()
        return Response({
            'message': 'success'
        })

    def put(self, request, pk):
        saved_group = Group.objects.get(pk=pk)
        data = request.data
        serializer = GroupSerializer(instance=saved_group, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            group_saved = serializer.save()

        return Response({
            "success": "Specialty '{}.{}.{}' updated successfully".format(group_saved.Course, group_saved.Group,
                                                                          group_saved.SubGroup)
        })

    def get(self, request, pk):
        group = Group.objects.get(pk=pk)
        serializer = GroupSerializer(group)
        return Response(serializer.data)


class TeacherListView(APIView):
    def get(self, request):
        queryset = Teacher.objects.all()
        serializer = TeacherSerializer
        specialty = serializer(queryset, many=True)
        return Response(specialty.data)


class TeacherView(APIView):
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        teacher.delete()
        return Response({
            "message": "success"
        })

    def put(self, request, pk):
        saved_teacher = Teacher.objects.get(pk=pk)
        data = request.data
        serializer = TeacherSerializer(instance=saved_teacher, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            teacher_saved = serializer.save()

        return Response({
            "success": "Teacher '{}' updated successfully".format(teacher_saved.FIO)
        })

    def get(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)


class SubjectListView(APIView):
    def get(self, request):
        queryset = Subject.objects.all()
        serializer = SubjectSerializer
        subject = serializer(queryset, many=True)
        return Response(subject.data)


class SubjectView(APIView):
    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        subject = Subject.objects.get(pk=pk)
        subject.delete()
        return Response({
            "message": "success"
        })

    def put(self, request, pk):
        saved_subject = Subject.objects.get(pk=pk)
        data = request.data
        serializer = SubjectSerializer(instance=saved_subject, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            subject_saved = serializer.save()

        return Response({
            "success": "Subject '{}' updated successfully".format(subject_saved.Name)
        })

    def get(self, request, pk):
        subject = Subject.objects.get(pk=pk)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)


class ClassRoomListView(APIView):
    def get(self, request):
        queryset = ClassRoom.objects.all()
        serializer = ClassRoomSerializer
        specialty = serializer(queryset, many=True)
        return Response(specialty.data)


class ClassRoomView(APIView):
    def post(self, request):
        serializer = ClassRoomSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        teacher = ClassRoom.objects.get(pk=pk)
        teacher.delete()
        return Response({
            "message": "success"
        })

    def put(self, request, pk):
        saved_teacher = ClassRoom.objects.get(pk=pk)
        data = request.data
        serializer = ClassRoomSerializer(instance=saved_teacher, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            teacher_saved = serializer.save()

        return Response({
            "success": "ClassRoom '{}' updated successfully".format(teacher_saved.Type)
        })

    def get(self, request, pk):
        classRomm = ClassRoom.objects.get(pk=pk)
        serializer = ClassRoomSerializer(classRomm)
        return Response(serializer.data)


class SubjectTypeListView(APIView):
    def get(self, request):
        queryset = SubjectType.objects.all()
        serializer = SubjectTypeSerializer
        specialty = serializer(queryset, many=True)
        return Response(specialty.data)


class SubjectTypeView(APIView):
    def post(self, request):
        serializer = SubjectTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        teacher = SubjectType.objects.get(pk=pk)
        teacher.delete()
        return Response({
            "message": "success"
        })

    def put(self, request, pk):
        saved_teacher = SubjectType.objects.get(pk=pk)
        data = request.data
        serializer = SubjectTypeSerializer(instance=saved_teacher, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            teacher_saved = serializer.save()

        return Response({
            "success": "SubjectType '{}' updated successfully".format(teacher_saved.Type)
        })

    def get(self, request, pk):
        subjectType = SubjectType.objects.get(pk=pk)
        serializer = SubjectTypeSerializer(subjectType)
        return Response(serializer.data)


class ScheduleListView(APIView):
    def get(self, request):
        queryset = Schedule.objects.all()
        serializer = ScheduleSerializer
        schedule = serializer(queryset, many=True)
        return Response(schedule.data)

def get_day(self, date):
    if date == 1:
        return "Понедельник"
    if date == 2:
        return "Вторник"
    if date == 3:
        return "Среда"
    if date == 4:
        return "Четверг"
    if date == 5:
        return "Пятница"
    if date == 6:
        return "Суббота"
    if date == 7:
        return "Воскресенье"

class ScheduleShowView(APIView):
    def post(self, request):
        print(request.data)
        data = request.data
        if (data['type'] == 2):
            day = get_day(self, data['date'])
            print(day)
            schedule = Schedule.objects.filter(Group=data['group'], Day=data['date'])
        else:
            schedule = Schedule.objects.filter(Group=data['group'])

        serializer = ScheduleSerializer
        schedules = serializer(schedule, many=True)
        return Response(schedules.data)


class ScheduleView(APIView):
    def post(self, request):
        serializer = ScheduleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        schedule = Schedule.objects.get(pk=pk)
        schedule.delete()
        return Response({
            "message": "success"
        })

    def put(self, request, pk):
        saved_schedule = Schedule.objects.get(pk=pk)
        data = request.data
        serializer = ScheduleSerializer(instance=saved_schedule, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            schedule_saved = serializer.save()

        return Response({
            "success": "success"
        })

    def get(self, request, pk):
        schedule = Schedule.objects.get(pk=pk)
        serializer = ScheduleSerializer(schedule)
        return Response(serializer.data)

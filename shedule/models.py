from django.db import models


class Faculty(models.Model):
    Name = models.CharField(max_length=255, unique=True)
    Building = models.CharField(max_length=255)


class Specialty(models.Model):
    Name = models.CharField(max_length=255)
    Faculty = models.ForeignKey(Faculty, related_name='specialty', on_delete=models.CASCADE)


class Group(models.Model):
    Course = models.IntegerField(max_length=2)
    Group = models.CharField(max_length=255)
    SubGroup = models.CharField(max_length=255)
    Specialty = models.ForeignKey(Specialty, related_name='Group', on_delete=models.CASCADE)


class Teacher(models.Model):
    FIO = models.CharField(max_length=255)
    ScientificDegree = models.CharField(max_length=255)


class Subject(models.Model):
    Name = models.CharField(max_length=255)
    Teacher = models.ForeignKey(Teacher, related_name='subject', on_delete=models.CASCADE)


class ClassRoom(models.Model):
    Type = models.CharField(max_length=255)
    Number = models.CharField(max_length=255)


class SubjectType(models.Model):
    Type = models.CharField(max_length=255)


class Schedule(models.Model):
    Group = models.ForeignKey(Group, related_name='schedule', on_delete=models.CASCADE)
    ClassRoom = models.ForeignKey(ClassRoom, related_name='schedule', on_delete=models.CASCADE)
    Subject = models.ForeignKey(Subject, related_name='schedule', on_delete=models.CASCADE)
    SubjectType = models.ForeignKey(SubjectType, related_name='schedule', on_delete=models.CASCADE)
    SubjectNumber = models.IntegerField(max_length=16)
    SubjectStartTime = models.TimeField()
    SubjectEndTime = models.TimeField()
    Day = models.CharField(max_length=255, null=True)
    Semester = models.IntegerField()

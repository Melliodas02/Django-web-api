from rest_framework import serializers
from .models import *


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('id', 'Name', 'Building')

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ('id', 'Name', 'Faculty')

    def to_representation(self, instance):
        rep = super(SpecialtySerializer, self).to_representation(instance)
        rep['Faculty'] = instance.Faculty.Name
        return rep

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Faculty = validated_data.get('Faculty', instance.Faculty.id)
        instance.save()
        return instance


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'Course', 'Group', 'SubGroup', 'Specialty')

    def to_representation(self, instance):
        rep = super(GroupSerializer, self).to_representation(instance)
        rep['Specialty'] = instance.Specialty.Name
        return rep

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.Course = validated_data.get('Course', instance.Course)
        instance.Group = validated_data.get('Group', instance.Group)
        instance.SubGroup = validated_data.get('SubGroup', instance.SubGroup)
        instance.Specialty = validated_data.get('Specialty', instance.Specialty.id)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.Course = validated_data.get('Course', instance.Course)
        instance.Group = validated_data.get('Group', instance.Group)
        instance.SubGroup = validated_data.get('SubGroup', instance.SubGroup)
        instance.Specialty = validated_data.get('Specialty', instance.Specialty.id)
        instance.save()
        return instance


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'FIO', 'ScientificDegree')

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.FIO = validated_data.get('FIO', instance.FIO)
        instance.ScientificDegree = validated_data.get('ScientificDegree', instance.ScientificDegree)
        instance.save()
        return instance


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'Name', 'Teacher')

    def to_representation(self, instance):
        rep = super(SubjectSerializer, self).to_representation(instance)
        rep['Teacher'] = instance.Teacher.FIO
        return rep

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Teacher = validated_data.get('Teacher', instance.Teacher.id)
        instance.save()
        return instance


class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ('id', 'Type', 'Number')

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.Type = validated_data.get('Type', instance.Type)
        instance.Number = validated_data.get('Number', instance.Number)
        instance.save()
        return instance


class SubjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectType
        fields = ('id', 'Type',)

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.Type = validated_data.get('Type', instance.Type)
        instance.save()
        return instance


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"

    def to_representation(self, instance):
        rep = super(ScheduleSerializer, self).to_representation(instance)
        rep['Group'] = str(instance.Group.Course) + ' - ' + str(instance.Group.Group) + ' - ' + str(instance.Group.SubGroup)
        rep['ClassRoom'] = instance.ClassRoom.Number
        rep['Subject'] = instance.Subject.Name
        rep['SubjectType'] = instance.SubjectType.Type
        return rep

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.Group = validated_data.get('Group', instance.Group.id)
        instance.ClassRoom = validated_data.get('ClassRoom', instance.ClassRoom.id)
        instance.Subject = validated_data.get('Subject', instance.Subject.id)
        instance.SubjectType = validated_data.get('SubjectType', instance.SubjectType.id)
        instance.SubjectNumber = validated_data.get('SubjectNumber', instance.SubjectNumber)
        instance.SubjectStartTime = validated_data.get('SubjectStartTime', instance.SubjectStartTime)
        instance.SubjectEndTime = validated_data.get('Type', instance.SubjectEndTime)
        instance.Day = validated_data.get('Day', instance.Day)
        instance.Semester = validated_data.get('Type', instance.Semester)
        instance.save()
        return instance
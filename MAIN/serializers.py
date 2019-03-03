# -*- coding: utf-8 -*-
from rest_framework.serializers import Serializer
from rest_framework import serializers
from rest_framework.exceptions import ErrorDetail, ValidationError
from MAIN.models import  TaskTracking
from datetime import datetime


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['id'] = instance.id
        ret['date_joined'] = instance.date_joined.date()
        ret['is_superuser'] = instance.is_superuser
        if instance.last_login:
            ret['last_login'] = instance.last_login.date()
        else:
            ret['last_login'] = "未登录"
        return ret
    def update(self, instance, validated_data):
        userInstance = instance
        passwordString = validated_data.get("password")
        if passwordString!="":
            userInstance.set_password(passwordString)
            userInstance.save()
        return instance
    def validate(self, data):
        passwordString = self.initial_data.get("password", "")
        data['password'] = passwordString
        return data


'''
class TaskTrackingSerializer(Serializer):
    #task_name = serializers.CharField(max_length=50)
    contest_id = serializers.IntegerField()
    #in_date = serializers.DateTimeField()
    status = serializers.CharField(max_length=10)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['id'] = instance.id
        ret['in_date'] = instance.in_date.strftime("%Y-%m-%d %H:%M:%S")
        ret['task_name'] = instance.task_name
        return ret

    def create(self, validated_data):
        context = self._context
        task_name = context.get("task_name")
        ######################################
        instance = TaskTracking(**validated_data)
        instance.task_name = task_name
        instance.in_date = datetime.now()
        instance.status = 'pending'
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status',instance.status)
        instance.in_date = datetime.now()
        instance.save()
        return instance

    def validate(self, data):
        if self.instance is not None:     # update method
            new_status = self.initial_data.get("status", "")
            if new_status != 'pending':
                raise ValidationError("validate error !")
            return data
        else:
            context = self._context
            new_task_name = context.get("task_name","")
            if not new_task_name:
                raise ValidationError("validate error !")
            new_status = self.initial_data.get("status", "")
            if new_status != 'pending':
                raise ValidationError("validate error !")
            return data
'''

class MultiIPAnalyzeRecordSerializer(Serializer):
    ip = serializers.CharField()
    #in_date = serializers.DateTimeField()

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['id'] = instance.id
        ret['in_date'] = instance.in_date.strftime("%Y-%m-%d %H:%M:%S")
        return ret

class MultiIPAnalyzeSerializer(Serializer): # for MultiIPAnalyze
    contest_id = serializers.IntegerField()
    contest_title = serializers.CharField()
    account_id = serializers.CharField()
    account_nick = serializers.CharField()

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['id'] = instance.id
        ret['ip_count'] = instance.records.all().values('ip').distinct().count()
        multi_ip_analyze_record_query_set = instance.records.all()
        serializer_instance = MultiIPAnalyzeRecordSerializer(multi_ip_analyze_record_query_set,many=True)
        ret['ip_list'] = serializer_instance.data
        return ret

class MultiAccountAnalyzeRecordSerializer(Serializer):
    account_id = serializers.CharField()
    account_nick = serializers.CharField()  # the user nick
    #in_date = serializers.DateTimeField()
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['id'] = instance.id
        ret['in_date'] = instance.in_date.strftime("%Y-%m-%d %H:%M:%S")
        return ret

class MultiAccountAnalyzeSerializer(Serializer):
    contest_id = serializers.IntegerField()
    contest_title = serializers.CharField()
    ip = serializers.CharField()

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['id'] = instance.id
        ret['account_count'] = instance.records.all().values('account_id').distinct().count()
        multi_account_analyze_record_query_set = instance.records.all()
        serializer_instance = MultiAccountAnalyzeRecordSerializer(multi_account_analyze_record_query_set,many=True)
        ret['account_list'] = serializer_instance.data
        return ret

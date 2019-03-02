# -*- coding: utf-8 -*-
from rest_framework.serializers import Serializer
from rest_framework import serializers
from rest_framework.exceptions import ErrorDetail, ValidationError
from MAIN.models import TaskTracking
from datetime import datetime

class ContestSerializer(Serializer):
    contest_id = serializers.IntegerField()
    title = serializers.CharField()

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['id'] = instance.contest_id
        return ret

class HUSTOJUserSerializer(Serializer):
    user_id = serializers.CharField()
    email = serializers.CharField()
    nick = serializers.CharField()

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['id'] = instance.user_id
        return ret

class AntiCheatingTaskContestSerializer(Serializer):  # relate  part with Contest model
    contest_id = serializers.IntegerField()
    title = serializers.CharField()

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['id'] = instance.contest_id
        #ret['contest_title'] = instance.title
        task_query_set = TaskTracking.objects.filter(contest_id=instance.contest_id).filter(task_name='anti_cheating_task')
        if task_query_set:
            task_instance=task_query_set[0]
            ret['status'] = task_instance.status
            ret['in_date'] = task_instance.in_date.strftime("%Y-%m-%d %H:%M:%S")
        else:
            ret['status'] = 'none'
            ret['in_date'] = ''
        return ret

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.in_date = datetime.now()
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

    def validate(self, data):
        status = self.initial_data.get("status","pending")
        if status not in TaskTracking.task_status_list:
            raise ValidationError("Validate Error In AntiCheatingTaskContestSerializer! status not in task_status_list")
        data["status"] = status
        return data

class CodeExportTaskContestSerializer(Serializer):  # relate  part with Contest model
    contest_id = serializers.IntegerField()
    title = serializers.CharField()

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['id'] = instance.contest_id
        #ret['contest_title'] = instance.title
        task_query_set = TaskTracking.objects.filter(contest_id=instance.contest_id).filter(task_name='code_export_task')
        if task_query_set:
            task_instance=task_query_set[0]
            ret['status'] = task_instance.status
            ret['in_date'] = task_instance.in_date.strftime("%Y-%m-%d %H:%M:%S")
        else:
            ret['status'] = 'none'
            ret['in_date'] = ''
        return ret

    def update(self, instance, validated_data):
        #instance.title = validated_data.get('title', instance.title)
        instance.in_date = datetime.now()
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

    def validate(self, data):
        status = self.initial_data.get("status","pending")
        if status not in TaskTracking.task_status_list:
            raise ValidationError("Validate Error In AntiCheatingTaskContestSerializer! status not in task_status_list")
        data["status"] = status
        return data
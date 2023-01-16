from rest_framework import serializers
from .models import Department, Personnel
from django.utils.timezone import now

class DepartmentSerializer(serializers.ModelSerializer):
    
    personnel_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Department
        fields = ("id", "name", "personnel_count")
        
    def get_personnel_count(self, obj):
        return obj.personals.count()
    
from rest_framework import serializers

from department.models import Department, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "last_name",
            "first_name",
            "middle_name",
            "department",
            "photo",
            "position",
            "salary",
            "age",
        ]


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["title"]

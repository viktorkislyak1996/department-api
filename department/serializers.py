from django.db.models import Sum
from rest_framework import serializers

from department.models import Department, Employee


class NullToEmptyModelSerializer(serializers.ModelSerializer):
    """
    Replace all null values to empty string in serialized result.
    """

    def to_representation(self, instance) -> dict:
        result = super().to_representation(instance)
        for i, v in result.items():
            if v is None:
                result[i] = ""
        return result


class EmployeeSerializer(NullToEmptyModelSerializer):
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


class DepartmentSerializer(NullToEmptyModelSerializer):
    employee_count = serializers.SerializerMethodField()
    total_salary = serializers.SerializerMethodField()

    def get_employee_count(self, instance: Department) -> int:
        return Employee.objects.filter(department=instance).count()

    def get_total_salary(self, instance: Department) -> int:
        total = Employee.objects.filter(department=instance).aggregate(
            total=Sum("salary")
        )
        if result := total.get("total"):
            return result
        return 0

    class Meta:
        model = Department
        fields = ["title", "employee_count", "total_salary"]

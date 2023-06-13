from decimal import Decimal

from django.test import TestCase

from department.models import Department, Employee
from department.serializers import DepartmentSerializer, EmployeeSerializer


class DepartmentsEmployeesSerializerTestCase(TestCase):

    def setUp(self):
        self.department1 = Department.objects.create(title='A-department')
        Department.objects.create(title='B-department')

        Employee.objects.create(
            first_name='Egor',
            last_name='Letov',
            department=self.department1,
            position='Singer',
            salary=60000,
            age=42
        )
        Employee.objects.create(
            first_name='Anton',
            last_name='Peskov',
            department=self.department1,
            position='Java developer',
            salary=250000,
            age=23
        )

    def test_employee_serializer(self):
        employees = Employee.objects.all()
        serializer_data = EmployeeSerializer(employees, many=True).data
        expected_data = [
            {
                "last_name": "Letov",
                "first_name": "Egor",
                "middle_name": "",
                "department": self.department1.id,
                "photo": "",
                "position": "Singer",
                "salary": "60000.00",
                "age": 42
            },
            {
                "last_name": "Peskov",
                "first_name": "Anton",
                "middle_name": "",
                "department": self.department1.id,
                "photo": "",
                "position": "Java developer",
                "salary": "250000.00",
                "age": 23
            }
        ]
        self.assertEqual(serializer_data, expected_data)

    def test_department_serializer(self):
        departments = Department.objects.all()
        serializer_data = DepartmentSerializer(departments, many=True).data
        expected_data = [
            {
                "title": "A-department",
                "employee_count": 2,
                "total_salary": Decimal('310000')
            },
            {
                "title": "B-department",
                "employee_count": 0,
                "total_salary": 0
            }
        ]
        self.assertEqual(serializer_data, expected_data)

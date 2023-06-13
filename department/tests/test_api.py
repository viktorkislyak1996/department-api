from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from department.models import Department, Employee
from department.serializers import DepartmentSerializer, EmployeeSerializer


class DepartmentsEmployeesAPITestCase(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create(username='testuser1')

        self.department1 = Department.objects.create(title='A-department')
        self.department2 = Department.objects.create(title='B-department')

        self.employee1 = Employee.objects.create(
            first_name='Egor',
            last_name='Letov',
            department=self.department1,
            position='Singer',
            salary=60000,
            age=42
        )
        self.employee2 = Employee.objects.create(
            first_name='Anton',
            last_name='Peskov',
            department=self.department1,
            position='Java developer',
            salary=250000,
            age=23
        )
        self.employee3 = Employee.objects.create(
            first_name='Viktor',
            last_name='Sobolev',
            department=self.department2,
            position='Python developer',
            salary=230000,
            age=27
        )

    def test_get_employees(self):
        self.client.force_login(self.user1)

        url = reverse('employees-list')
        response = self.client.get(url)

        employees = Employee.objects.all()
        serializer_data = EmployeeSerializer(employees, many=True).data

        self.assertEqual(response.data, serializer_data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_department(self):
        url = reverse('departments-list')
        response = self.client.get(url)

        departments = Department.objects.all()
        serializer_data = DepartmentSerializer(departments, many=True).data

        self.assertEqual(response.data, serializer_data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

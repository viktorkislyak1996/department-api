from django.urls import include, path
from rest_framework import routers

from department.views import DepartmentViewSet, EmployeeViewSet

router = routers.DefaultRouter()
router.register(r"departments", DepartmentViewSet, basename="departments")
router.register(r"employees", EmployeeViewSet, basename="employees")

urlpatterns = [path("v1/", include(router.urls))]

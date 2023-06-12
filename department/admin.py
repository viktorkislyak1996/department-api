from django.contrib import admin

from department.models import Department, Employee


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created")
    search_fields = ("title",)
    list_filter = ("created",)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "middle_name",
        "department",
        "image_preview",
        "position",
        "salary",
        "age",
        "created",
    )
    search_fields = ("first_name", "last_name", "position")
    list_filter = ("age", "created", "position", "department")


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)

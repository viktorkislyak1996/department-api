from django.db import models
from django.utils.safestring import mark_safe


class Department(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title}"


class Employee(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40, db_index=True)
    middle_name = models.CharField(max_length=40, null=True, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, related_name="employees"
    )
    photo = models.ImageField(upload_to="photos/employees", null=True, blank=True)
    position = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=20, decimal_places=2)
    age = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def image_preview(self):
        if self.photo:
            return mark_safe(
                f'<img src="{self.photo.url}" width="100px" height="100px" />'
            )

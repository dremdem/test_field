from django.db import models
from django.db.models.expressions import RawSQL

# Create your models here.


class DManagerWithCount(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(division_amount=RawSQL("""
        select count(*) from field_department fd, field_employee fe
        where fd.id = fe.department_id and fd.division_id = field_division.id
        """, []))


class Division(models.Model):
    name = models.CharField(max_length=200)
    no = models.CharField(max_length=5)

    object = models.Manager()
    obj_with_count = DManagerWithCount()


class Department(models.Model):
    name = models.CharField(max_length=200)
    no = models.CharField(max_length=5)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='departments')


class Employee(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')







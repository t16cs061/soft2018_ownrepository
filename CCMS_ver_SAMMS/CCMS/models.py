from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class employee_master(models.Model):
    Code = models.CharField(max_length=6, validators=[MinLengthValidator(6)])
    Pass = models.CharField(max_length=15, validators=[MinLengthValidator(6)])
    AdminFlag = models.BooleanField()

    def __str__(self):
        return 'EmployeeCode:' + str(self.Code)
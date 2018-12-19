from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Employee(models.Model):
    Code = models.CharField(max_length=6, validators=[MinLengthValidator(6)])
    Pass = models.CharField(max_length=15, validators=[MinLengthValidator(6)])
    AdminFlag = models.BooleanField()

    def __str__(self):
        return 'EmployeeCode:' + str(self.Code)
    
class Mentenance(models.Model):
    CarName = models.CharField(max_length=10, validators=[MinLengthValidator(3)])
    StartDateTime = models.DateField()
    EndDateTime = models.DateField()
    MentenanceOverview = models.CharField(max_length=200, validators=[MinLengthValidator(1)])
    
    def __str__(self):
        output = ('メンテナンス概要：' + str(self.MentenanceOverview) + "，" +
                  '車名：' + str(self.CarName))
        
        return  output

class Friends(models.Model):
    car_name= models.CharField(max_length=1000)
    use_day = models.DateField()
    want_go = models.EmailField(max_length=200)

    def __str__(self):
        return '<Friend:id =' + str(self.id) + ',' + self.name + '(' + str(self.age) + ')>'
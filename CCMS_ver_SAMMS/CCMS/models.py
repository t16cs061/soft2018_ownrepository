from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.

#社員マスタ
class EmployeeMaster(models.Model):
    Code = models.CharField(max_length=6, validators=[MinLengthValidator(6)])
    Pass = models.CharField(max_length=15, validators=[MinLengthValidator(6)])
    Name = models.CharField(max_length=30, validators=[MinLengthValidator(3)])
    Gender = models.CharField(max_length=1, validators=[MinLengthValidator(1)])
    Mail = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    Age = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    AdminFlag = models.BooleanField()

    def __str__(self):
        return 'EmployeeCode:' + str(self.Code)

#車両マスタ
class CarMaster(models.Model):
    Code = models.CharField(max_length=2, validators=[MinLengthValidator(1)])
    CarName = models.CharField(max_length=10, validators=[MinLengthValidator(3)])
    class Meta:
        ordering = ('Code', )

    def __str__(self):
        return str(self.Code) + ' : ' + str(self.CarName)

#運行記録テーブル    
class ServiceRecordMaster(models.Model):
    CarName = models.CharField(max_length=10, validators=[MinLengthValidator(3)])
    EmployeeCode = models.CharField(max_length=6, validators=[MinLengthValidator(6)])
    StartDateTime = models.DateTimeField()
    EndDateTime = models.DateTimeField()
    StartMileage = models.IntegerField()
    EndMileage = models.IntegerField()
    Destination = models.CharField(max_length=30, validators=[MinLengthValidator(1)])
    RefuelingFlag = models.BooleanField()
    ETCFlag = models.BooleanField()
    
    def __str__(self):
        output = ('使用期間： ' + str(self.StartDateTime) + " ~ " + str(self.EndDateTime) + 
                  ' ,使用者: ' + str(self.EmployeeCode) + ' ,使用車: ' + str(self.CarName) + 
                  ' ,行き先: ' + str(self.Destination) + ' ,走行距離: ' + str(self.EndMileage - self.StartMileage) + ' km' )
        
        return  output

#給油記録テーブル    
class RefuelingRecordMaster(models.Model):
    DateTime = models.DateTimeField()
    SSName = models.CharField(max_length=20, validators=[MinLengthValidator(1)])
    Mileage = models.IntegerField()
    Amount = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        output = ('給油日： ' + str(self.DateTime) + 
                  ' ,給油場所: ' + str(self.SSName) + ' ,給油時点での走行距離: ' + str(self.Mileage) + 'km ' + 
                  ' ,給油量: ' + str(self.Amount) + ' L')
        
        return  output

#ETC利用記録テーブル    
class ETCRecordMaster(models.Model):
    StartDateTime = models.DateTimeField()
    EndDateTime = models.DateTimeField()
    CarName = models.CharField(max_length=10, validators=[MinLengthValidator(3)])
    EmployeeCode = models.CharField(max_length=6, validators=[MinLengthValidator(6)])
    BoardingIC = models.CharField(max_length=20, validators=[MinLengthValidator(3)])
    GetOffIC = models.CharField(max_length=20, validators=[MinLengthValidator(3)])
    
    def __str__(self):
        output = ('使用期間： ' + str(self.StartDateTime) + ' ~ ' + str(self.EndDateTime) +
                  ' ,使用車: ' + str(self.CaｒName) + ' ,利用社員:' + str(self.EmployeeCode) +  
                  ' ,乗車区間: ' + str(self.BoardingIC) + ' ~ ' + str(self.GetOffIC))
        
        return  output

#車両予約テーブル    
class CarReservationMaster(models.Model):
    EmployeeCode = models.CharField(max_length=6, validators=[MinLengthValidator(6)])
    CarName = models.CharField(max_length=10, validators=[MinLengthValidator(3)])
    StartDateTime = models.DateTimeField()
    EndDateTime = models.DateTimeField()
    Destination = models.CharField(max_length=30, validators=[MinLengthValidator(1)])
    ETCFlag = models.BooleanField()
    
    def __str__(self):
        output = ('予約期間： ' + str(self.StartDateTime) + ' ~ ' + str(self.EndDateTime) +
                  ' ,使用車: ' + str(self.CaｒName) + ' ,利用社員: ' + str(self.EmployeeCode) +  
                  ' ,行き先: ' + str(self.Destination))
        
        return  output

#車両メンテナンス予定テーブル    
class MentenanceMaster(models.Model):
    CarName = models.CharField(max_length=10, validators=[MinLengthValidator(3)])
    StartDateTime = models.DateTimeField()
    EndDateTime = models.DateTimeField()
    MentenanceOverview = models.CharField(max_length=200, validators=[MinLengthValidator(1)])
    
    def __str__(self):
        output = ('メンテナンス概要：' + str(self.MentenanceOverview) + "，" +
                  '車名：' + str(self.CarName))
        
        return  output

#鈴木さんの使用しているFriendクラス->車両予約機能
class Friend(models.Model):
    car_name= models.CharField(max_length=1000)
    start_day = models.DateTimeField()
    end_day = models.DateTimeField()
    want_go = models.CharField(max_length=200)

    def __str__(self):
        return '<Friend:id =' + str(self.id) + ',' + self.name + '(' + str(self.age) + ')>'
    

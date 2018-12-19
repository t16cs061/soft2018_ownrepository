from django.contrib import admin
from .models import EmployeeMaster, CarMaster
from .models import ServiceRecordMaster, RefuelingRecordMaster, ETCRecordMaster, CarReservationMaster, MentenanceMaster



admin.site.register(EmployeeMaster) #社員マスタ
admin.site.register(CarMaster) #車両マスタ
admin.site.register(ServiceRecordMaster) #運行記録テーブル
admin.site.register(RefuelingRecordMaster) #給油記録テーブル
admin.site.register(ETCRecordMaster) #ETC利用記録テーブル
admin.site.register(CarReservationMaster) #車両予約テーブル
admin.site.register(MentenanceMaster) #車両メンテナンス予定テーブル
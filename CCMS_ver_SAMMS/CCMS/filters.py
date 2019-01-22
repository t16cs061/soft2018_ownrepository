'''
from django_filters import FilterSet
from django_filters import filters

from .models import ServiceRecordMaster


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ServiceRecordFilter(FilterSet):

    EmployeeCode = filters.CharFilter(label='氏名', lookup_expr='contains')
    memo = filters.CharFilter(label='備考', lookup_expr='contains')

    order_by = MyOrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('EmployeeCode', 'name'),
        ),
        field_labels={
            'name': '氏名',
        },
    )

    class Meta:

        model = ServiceRecordMaster
        fields = ('EmployeeCode',)
'''
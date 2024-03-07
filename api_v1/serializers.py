from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import *


'''
Lst - List
Det - Detail
Mng - Manage
Crt - Create
Del - Delete
'''


class CityLstMngCrtDelSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CityDetSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(method_name='get_full_name')
    short_full_name = serializers.SerializerMethodField(method_name='get_short_full_name')

    def get_full_name(self, obj):
        return str(obj)

    def get_short_full_name(self, obj):
        return obj.short_str()

    class Meta:
        model = City
        fields = ['id', 'name', 'full_name', 'short_full_name']


#####################################################################


class StreetLstMngCrtDelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'


class StreetDetSerializer(serializers.ModelSerializer):
    city_name = serializers.SerializerMethodField(method_name='get_city_name')
    full_name = serializers.SerializerMethodField(method_name='get_full_name')
    short_full_name = serializers.SerializerMethodField(method_name='get_short_full_name')

    def get_city_name(self, obj): return str(obj.city.name)

    def get_full_name(self, obj): return str(obj)

    def get_short_full_name(self, obj): return obj.short_str()

    class Meta:
        model = Street
        fields = ['id', 'name', 'city', 'city_name', 'full_name', 'short_full_name']


#####################################################################


class BuildingLstMngCrtDelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class BuildingDetSerializer(serializers.ModelSerializer):
    city_name = serializers.SerializerMethodField(method_name='get_city_name')
    street_name = serializers.SerializerMethodField(method_name='get_street_name')
    full_name = serializers.SerializerMethodField(method_name='get_full_name')
    short_full_name = serializers.SerializerMethodField(method_name='get_short_full_name')

    def get_city_name(self, obj): return str(obj.street.city.name)

    def get_street_name(self, obj): return str(obj.street.name)

    def get_full_name(self, obj): return str(obj)

    def get_short_full_name(self, obj): return obj.short_str()

    class Meta:
        model = Building
        fields = ['id', 'street', 'city_name', 'street_name', 'number', 'corpus', 'full_name', 'short_full_name']


#####################################################################


class WorkDayShortLstSerializer(serializers.ModelSerializer):
    resume = serializers.SerializerMethodField(method_name='get_resume')

    def get_resume(self, obj):
        return str(obj.short_str())

    class Meta:
        model = WorkDay
        fields = ['id', 'resume']


class WorkDayFullLstSerializer(serializers.ModelSerializer):
    day_of_week_name = serializers.ChoiceField(choices=WorkDay.DAY_CHOICES, source='get_day_of_week_display', read_only=True)
    day_of_week = serializers.ChoiceField(choices=WorkDay.DAY_CHOICES, read_only=True)
    resume = serializers.SerializerMethodField(method_name='get_resume')

    def get_resume(self, obj):
        return str(obj.short_str())

    class Meta:
        model = WorkDay
        fields = ['id', 'day_of_week', 'day_of_week_name', 'is_not_working', 'start_time', 'end_time', 'resume']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['is_not_working']:
            data.pop('start_time', None)
            data.pop('end_time', None)
        return data


class WorkScheduleLstSerializer(serializers.ModelSerializer):
    work_days = serializers.SerializerMethodField()

    def get_work_days(self, obj):
        work_days = obj.work_days.all().order_by('day_of_week')
        serializer = WorkDayShortLstSerializer(work_days, many=True)
        return serializer.data

    class Meta:
        model = WorkSchedule
        fields = ['id', 'name', 'work_days']


class WorkScheduleDetMngSerializer(serializers.ModelSerializer):
    work_days = serializers.SerializerMethodField()

    def get_work_days(self, obj):
        work_days = obj.work_days.all().order_by('day_of_week')
        serializer = WorkDayFullLstSerializer(work_days, many=True)
        return serializer.data

    class Meta:
        model = WorkSchedule
        fields = ['id', 'name', 'work_days']


class WorkScheduleCrtDelSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkSchedule
        fields = '__all__'


#####################################################################


class OfficeLstMngCrtDelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Office
        fields = '__all__'


class OfficeDetSerializer(serializers.ModelSerializer):
    address_str = serializers.SerializerMethodField(method_name='get_address')
    work_schedule_detail = serializers.SerializerMethodField(method_name='get_work_schedule')

    def get_address(self, obj): return str(obj.address)

    def get_work_schedule(self, obj):
        work_days = WorkDay.objects.filter(schedule_id=obj.work_schedule).order_by('day_of_week')
        serializer = WorkDayShortLstSerializer(work_days, many=True)
        return serializer.data

    class Meta:
        model = Office
        fields = ['id', 'name', 'address', 'address_str', 'work_schedule', 'work_schedule_detail']


#####################################################################


class HousingComplexLstMngCrtDelSerializer(serializers.ModelSerializer):

    class Meta:
        model = HousingComplex
        fields = '__all__'


class HousingComplexDetSerializer(serializers.ModelSerializer):
    office_name = serializers.SerializerMethodField(method_name='get_office_name')
    office_address = serializers.SerializerMethodField(method_name='get_office_address')

    def get_office_name(self, obj): return str(obj.office)

    def get_office_address(self, obj): return str(obj.office.address)

    class Meta:
        model = HousingComplex
        fields = ['id', 'name', 'office', 'office_name', 'office_address']


#####################################################################


class HouseLstMngCrtDelSerializer(serializers.ModelSerializer):

    class Meta:
        model = House
        fields = '__all__'


class HouseDetSerializer(serializers.ModelSerializer):
    complex_name = serializers.SerializerMethodField(method_name='get_complex_name')
    address_str = serializers.SerializerMethodField(method_name='get_address_str')
    full_name = serializers.SerializerMethodField(method_name='get_full_name')

    def get_complex_name(self, obj): return str(obj.complex)

    def get_address_str(self, obj): return str(obj.address)

    def get_full_name(self, obj): return str(obj)

    class Meta:
        model = House
        fields = ['id', 'complex', 'complex_name', 'address', 'address_str', 'full_name']


#####################################################################


class ResidentFullLstMngCrtDelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resident
        fields = '__all__'


class ResidentFullDetSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(method_name='get_full_name')
    respectful_treatment = serializers.SerializerMethodField(method_name='get_respectful_treatment')

    def get_full_name(self, obj): return str(obj)

    def get_respectful_treatment(self, obj): return obj.get_respectful_treatment()

    class Meta:
        model = Resident
        fields = ['id', 'name', 'surname', 'patronymic', 'phone', 'tg_id', 'full_name', 'respectful_treatment']


class ResidentShortLstSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = ['id', 'name', 'surname', 'patronymic']


class ResidentShortDetSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(method_name='get_full_name')
    respectful_treatment = serializers.SerializerMethodField(method_name='get_respectful_treatment')

    def get_full_name(self, obj): return str(obj)

    def get_respectful_treatment(self, obj): return obj.get_respectful_treatment()

    class Meta:
        model = Resident
        fields = ['id', 'name', 'surname', 'patronymic', 'full_name', 'respectful_treatment']


#####################################################################


class ExecutionStatusUltimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutionStatus
        fields = '__all__'


#####################################################################


class DepartmentUltimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


#####################################################################


class PositionLstMngCrtDelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class PositionDetSerializer(serializers.ModelSerializer):
    department_name = serializers.SerializerMethodField(method_name='get_department_name')

    def get_department_name(self, obj): return str(obj.department)

    class Meta:
        model = Position
        fields = ['id', 'department', 'department_name', 'name']


#####################################################################


class EmployeeFullLstMngCrtDelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeFullDetSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(method_name='get_full_name')
    respectful_treatment = serializers.SerializerMethodField(method_name='get_respectful_treatment')
    office_name = serializers.SlugRelatedField(slug_field='name', read_only=True)
    position_name = serializers.SlugRelatedField(slug_field='name', read_only=True)

    def get_full_name(self, obj): return str(obj)

    def get_respectful_treatment(self, obj): return obj.get_respectful_treatment()

    class Meta:
        model = Employee
        fields = ['id', 'name', 'surname', 'patronymic', 'phone', 'email', 'office', 'office_name',
                  'position', 'position_name', 'tg_id', 'full_name', 'respectful_treatment']


class EmployeeShortLstSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'surname', 'patronymic']


class EmployeeShortDetSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(method_name='get_full_name')
    respectful_treatment = serializers.SerializerMethodField(method_name='get_respectful_treatment')

    def get_full_name(self, obj): return str(obj)

    def get_respectful_treatment(self, obj): return obj.get_respectful_treatment()

    class Meta:
        model = Employee
        fields = ['id', 'name', 'surname', 'patronymic', 'email', 'office', 'position', 'full_name',
                  'respectful_treatment']


#####################################################################


class ServiceLstMngCrtDelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'


class ServiceDetSerializer(serializers.ModelSerializer):
    position_name = serializers.SerializerMethodField(method_name='get_position_name')

    def get_position_name(self, obj): return str(obj.position)

    class Meta:
        model = Service
        fields = ['id', 'name', 'position', 'position_name', 'description']


#####################################################################


class RequestLstMngCrtDelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = '__all__'


class RequestDetSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(method_name='get_full_name')

    def get_full_name(self, obj): return str(obj)

    class Meta:
        model = Request
        fields = ['id', 'created_at', 'text', 'status', 'resident', 'address', 'apartment',
                  'photo', 'employee', 'service', 'full_name']

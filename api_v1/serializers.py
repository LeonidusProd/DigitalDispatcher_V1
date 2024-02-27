from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import *


class CityListCreateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CityDetailSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(method_name='get_full_name')
    short_full_name = serializers.SerializerMethodField(method_name='get_short_full_name')

    def get_full_name(self, obj):
        return str(obj)

    def get_short_full_name(self, obj):
        return obj.short_str()

    class Meta:
        model = City
        fields = ['id', 'name', 'full_name', 'short_full_name']


class CityManageSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(method_name='get_full_name')
    short_full_name = serializers.SerializerMethodField(method_name='get_short_full_name')

    def get_full_name(self, obj):
        return str(obj)

    def get_short_full_name(self, obj):
        return obj.short_str()

    class Meta:
        model = City
        fields = ['id', 'name', 'full_name', 'short_full_name']




class StreetListSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Street
        fields = ['id', 'name', 'city']


class StreetDetailManageSerializer(serializers.ModelSerializer):
    city_name = serializers.SerializerMethodField(method_name='get_city_name')
    full_name = serializers.SerializerMethodField(method_name='get_full_name')
    short_full_name = serializers.SerializerMethodField(method_name='get_short_full_name')

    def get_city_name(self, obj): return str(obj.city.name)

    def get_full_name(self, obj): return str(obj)

    def get_short_full_name(self, obj): return obj.short_str()

    class Meta:
        model = Street
        fields = ['id', 'name', 'city', 'city_name', 'full_name', 'short_full_name']


class StreetCreateDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Street
        fields = '__all__'




class BuildingListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_name')

    def get_name(self, obj): return str(obj.short_str())

    class Meta:
        model = Building
        fields = ['id', 'name']


class BuildingDetailManageSerializer(serializers.ModelSerializer):
    city_name = serializers.SerializerMethodField(method_name='get_city_name')
    street_name = serializers.SerializerMethodField(method_name='get_street_name')

    def get_city_name(self, obj): return str(obj.street.city.name)

    def get_street_name(self, obj): return str(obj.street.name)

    class Meta:
        model = Building
        fields = ['id', 'street', 'city_name', 'street_name', 'number', 'corpus']


class BuildingCreateDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Building
        fields = '__all__'




class WorkDayShortListSerializer(serializers.ModelSerializer):
    resume = serializers.SerializerMethodField(method_name='get_resume')

    def get_resume(self, obj):
        return str(obj.short_str())

    class Meta:
        model = WorkDay
        fields = ['id', 'resume']


class WorkDayFullListSerializer(serializers.ModelSerializer):
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


class WorkScheduleListSerializer(serializers.ModelSerializer):
    work_days = serializers.SerializerMethodField()

    def get_work_days(self, obj):
        work_days = obj.work_days.all().order_by('day_of_week')
        serializer = WorkDayShortListSerializer(work_days, many=True)
        return serializer.data

    class Meta:
        model = WorkSchedule
        fields = ['id', 'name', 'work_days']


class WorkScheduleDetailManageSerializer(serializers.ModelSerializer):
    work_days = serializers.SerializerMethodField()

    def get_work_days(self, obj):
        work_days = obj.work_days.all().order_by('day_of_week')
        serializer = WorkDayFullListSerializer(work_days, many=True)
        return serializer.data

    class Meta:
        model = WorkSchedule
        fields = ['id', 'name', 'work_days']


class WorkScheduleCreateDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkSchedule
        fields = '__all__'




class OfficeListSerializer(serializers.ModelSerializer):
    address_str = serializers.SerializerMethodField(method_name='get_address')
    work_schedule_detail = serializers.SerializerMethodField(method_name='get_work_schedule')

    def get_address(self, obj): return str(obj.address)

    def get_work_schedule(self, obj):
        work_days = WorkDay.objects.filter(schedule_id=obj.work_schedule).order_by('day_of_week')
        serializer = WorkDayShortListSerializer(work_days, many=True)
        return serializer.data

    class Meta:
        model = Office
        fields = ('id', 'name', 'address_str', 'work_schedule_detail')


class OfficeDetailSerializer(serializers.ModelSerializer):
    address_str = serializers.SerializerMethodField(method_name='get_address')
    work_schedule_detail = serializers.SerializerMethodField(method_name='get_work_schedule')

    def get_address(self, obj): return str(obj.address)

    def get_work_schedule(self, obj):
        work_days = WorkDay.objects.filter(schedule_id=obj.work_schedule).order_by('day_of_week')
        serializer = WorkDayShortListSerializer(work_days, many=True)
        return serializer.data

    class Meta:
        model = Office
        fields = ['id', 'name', 'address', 'address_str', 'work_schedule', 'work_schedule_detail']


class OfficeManageSerializer(serializers.ModelSerializer):
    address_str = serializers.SerializerMethodField(method_name='get_address')
    work_schedule_str = serializers.SerializerMethodField(method_name='get_work_schedule')

    def get_address(self, obj): return str(obj.address)

    def get_work_schedule(self, obj): return str(obj.work_schedule)

    class Meta:
        model = Office
        fields = ['id', 'name', 'address', 'address_str', 'work_schedule', 'work_schedule_str']


class OfficeCreateDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Office
        fields = '__all__'




class HousingComplexListSerializer(serializers.ModelSerializer):
    office = serializers.SlugRelatedField(slug_field='name', read_only=True)
    office_address = serializers.SerializerMethodField(method_name='get_address')

    def get_address(self, obj): return str(obj.office.address)

    class Meta:
        model = HousingComplex
        fields = ['id', 'name', 'office', 'office_address']


class HousingComplexDetailManageSerializer(serializers.ModelSerializer):
    office_name = serializers.SerializerMethodField(method_name='get_office_name')
    office_address = serializers.SerializerMethodField(method_name='get_office_address')

    def get_office_name(self, obj): return str(obj.office)

    def get_office_address(self, obj): return str(obj.office.address)

    class Meta:
        model = HousingComplex
        fields = ['id', 'name', 'office', 'office_name', 'office_address']


class HousingComplexCreateDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = HousingComplex
        fields = '__all__'




class HouseListSerializer(serializers.ModelSerializer):
    complex = serializers.SlugRelatedField(slug_field='name', read_only=True)
    address = serializers.SerializerMethodField(method_name='get_address')

    def get_address(self, obj): return str(obj.address)

    class Meta:
        model = House
        fields = ['id', 'complex', 'address']


class HouseDetailManageSerializer(serializers.ModelSerializer):
    complex_name = serializers.SerializerMethodField(method_name='get_complex_name')
    address_str = serializers.SerializerMethodField(method_name='get_address_str')

    def get_complex_name(self, obj): return str(obj.complex)

    def get_address_str(self, obj): return str(obj.address)

    class Meta:
        model = House
        fields = ['id', 'complex', 'complex_name', 'address', 'address_str']


class HouseCreateDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = House
        fields = '__all__'




class ResidentShortListDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resident
        fields = ['id', 'name', 'surname', 'patronymic']


class ResidentSecureUltimateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resident
        fields = '__all__'




class ExecutionStatusUltimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutionStatus
        fields = '__all__'




class DepartmentUltimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'




class PositionListSerializer(serializers.ModelSerializer):
    department = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Position
        fields = ['id', 'department', 'name']


class PositionDetailManageSerializer(serializers.ModelSerializer):
    department_name = serializers.SerializerMethodField(method_name='get_department_name')

    def get_department_name(self, obj): return str(obj.department)

    class Meta:
        model = Position
        fields = ['id', 'department', 'department_name', 'name']


class PositionCreateDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = '__all__'




class EmployeeShortListDetailSerializer(serializers.ModelSerializer):
    office = serializers.SlugRelatedField(slug_field='name', read_only=True)
    position = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'surname', 'patronymic', 'email', 'office', 'position']


class EmployeeSecureUltimateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'




class ServiceListSerializer(serializers.ModelSerializer):
    position_name = serializers.SerializerMethodField(method_name='get_position_name')

    def get_position_name(self, obj): return str(obj.position)

    class Meta:
        model = Service
        fields = ['id', 'name', 'position_name', 'description']


class ServiceDetailManageSerializer(serializers.ModelSerializer):
    position_name = serializers.SerializerMethodField(method_name='get_position_name')

    def get_position_name(self, obj): return str(obj.position)

    class Meta:
        model = Service
        fields = ['id', 'name', 'position', 'position_name', 'description']


class ServiceCreateDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'






from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .permissions import *
from rest_framework import status

from .models import *
from .serializers import *

"""
Permissions:
IsSuperuser - Пользователь, который имеет статус супер пользователя
IsStaff - Пользователь, который имеет статус персонала
AllowAny - Любой пользователь
"""


class CityListView(generics.ListAPIView):
    """Список всех городов"""
    queryset = City.objects.all()
    serializer_class = CityListCreateDeleteSerializer
    permission_classes = (AllowAny, )


class CityDetailView(generics.RetrieveAPIView):
    """Полная информация о городе"""
    queryset = City.objects.all()
    serializer_class = CityDetailSerializer
    permission_classes = (AllowAny, )


class CityManageView(generics.RetrieveUpdateAPIView):
    """Полная информация о городе (с управлением)"""
    queryset = City.objects.all()
    serializer_class = CityManageSerializer
    permission_classes = (IsSuperuser, )


class CityCreateView(generics.CreateAPIView):
    """Добавление нового города"""
    queryset = City.objects.all()
    serializer_class = CityListCreateDeleteSerializer
    permission_classes = (IsSuperuser, IsStaff, )


class CityDeleteView(generics.DestroyAPIView):
    """Удаление города"""
    queryset = City.objects.all()
    serializer_class = CityListCreateDeleteSerializer
    permission_classes = (IsSuperuser, )




class StreetListView(generics.ListAPIView):
    """Список всех улиц"""
    queryset = Street.objects.all()
    serializer_class = StreetListSerializer
    permission_classes = (AllowAny, )


class StreetDetailView(generics.RetrieveAPIView):
    """Полная информация об улице"""
    queryset = Street.objects.all()
    serializer_class = StreetDetailManageSerializer
    permission_classes = (AllowAny, )


class StreetManageView(generics.RetrieveUpdateAPIView):
    """Полная информация об улице (с управлением)"""
    queryset = Street.objects.all()
    serializer_class = StreetDetailManageSerializer
    permission_classes = (IsSuperuser, )


class StreetCreateView(generics.CreateAPIView):
    """Добавление новой улицы"""
    queryset = Street.objects.all()
    serializer_class = StreetCreateDeleteSerializer
    permission_classes = (IsSuperuser, )


class StreetDeleteView(generics.DestroyAPIView):
    """Удаление улицы"""
    queryset = Street.objects.all()
    serializer_class = StreetCreateDeleteSerializer
    permission_classes = (IsSuperuser, )




class BuildingListView(generics.ListAPIView):
    """Список всех адресов"""
    queryset = Building.objects.all()
    serializer_class = BuildingListSerializer
    permission_classes = (AllowAny, )


class BuildingDetailView(generics.RetrieveAPIView):
    """Полная информация об адресе"""
    queryset = Building.objects.all()
    serializer_class = BuildingDetailManageSerializer
    permission_classes = (AllowAny, )


class BuildingManageView(generics.RetrieveUpdateAPIView):
    """Полная информация об адресе (с управлением)"""
    queryset = Building.objects.all()
    serializer_class = BuildingDetailManageSerializer
    permission_classes = (IsSuperuser, )


class BuildingCreateView(generics.CreateAPIView):
    """Добавление нового адреса"""
    queryset = Building.objects.all()
    serializer_class = BuildingCreateDeleteSerializer
    permission_classes = (IsSuperuser, )


class BuildingDeleteView(generics.DestroyAPIView):
    """Удаление адреса"""
    queryset = Building.objects.all()
    serializer_class = BuildingCreateDeleteSerializer
    permission_classes = (IsSuperuser, )




class WorkScheduleListView(generics.ListAPIView):
    """Список всех графиков работы"""
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleListSerializer
    permission_classes = (AllowAny, )


class WorkScheduleDetailView(generics.RetrieveAPIView):
    """Полная информация о графике работы"""
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleDetailManageSerializer
    permission_classes = (AllowAny, )


class WorkScheduleManageView(generics.RetrieveUpdateAPIView):
    """Полная информация о графике работы (с управлением)"""
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleDetailManageSerializer
    permission_classes = (IsSuperuser, )


class WorkDayManageView(generics.RetrieveUpdateAPIView):
    """Полная информация о рабочем дне (с управлением)"""
    queryset = WorkDay.objects.all()
    serializer_class = WorkDayFullListSerializer
    permission_classes = (IsSuperuser, )


class WorkScheduleCreateView(generics.CreateAPIView):
    """Добавление нового графика работы"""
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleCreateDeleteSerializer
    permission_classes = (IsSuperuser, )


class WorkScheduleDeleteView(generics.DestroyAPIView):
    """Удаление графика работы"""
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleCreateDeleteSerializer
    permission_classes = (IsSuperuser, )




class OfficeListView(generics.ListAPIView):
    """Список всех управляющих компаний"""
    queryset = Office.objects.all()
    serializer_class = OfficeListSerializer
    permission_classes = (AllowAny, )


class OfficeDetailView(generics.RetrieveAPIView):
    """Полная информация об управляющей компании"""
    queryset = Office.objects.all()
    serializer_class = OfficeDetailSerializer
    permission_classes = (AllowAny, )


class OfficeManageView(generics.RetrieveUpdateAPIView):
    """Полная информация об управляющей компании (с управлением)"""
    queryset = Office.objects.all()
    serializer_class = OfficeManageSerializer
    permission_classes = (IsSuperuser, )


class OfficeCreateView(generics.CreateAPIView):
    """Добавление новой управляющей компании"""
    queryset = Office.objects.all()
    serializer_class = OfficeCreateDeleteSerializer
    permission_classes = (IsSuperuser, )


class OfficeDeleteView(generics.DestroyAPIView):
    """Удаление управляющей компании"""
    queryset = Office.objects.all()
    serializer_class = OfficeCreateDeleteSerializer
    permission_classes = (IsSuperuser, )




class HousingComplexListView(generics.ListAPIView):
    """Список всех жилых комплексов"""
    queryset = HousingComplex.objects.all()
    serializer_class = HousingComplexListSerializer
    permission_classes = (AllowAny, )


class HousingComplexDetailView(generics.RetrieveAPIView):
    """Полная информация о жилом комплексе"""
    queryset = HousingComplex.objects.all()
    serializer_class = HousingComplexDetailManageSerializer
    permission_classes = (AllowAny, )


class HousingComplexManageView(generics.RetrieveUpdateAPIView):
    """Полная информация о жилом комплексе (с управлением)"""
    queryset = HousingComplex.objects.all()
    serializer_class = HousingComplexDetailManageSerializer
    permission_classes = (IsSuperuser, )


class HousingComplexCreateView(generics.CreateAPIView):
    """Добавление нового жилого комплекса"""
    queryset = HousingComplex.objects.all()
    serializer_class = HousingComplexCreateDeleteSerializer
    permission_classes = (IsSuperuser, )


class HousingComplexDeleteView(generics.DestroyAPIView):
    """Удаление жилого комплекса"""
    queryset = HousingComplex.objects.all()
    serializer_class = HousingComplexCreateDeleteSerializer
    permission_classes = (IsSuperuser, )




class HouseListView(generics.ListAPIView):
    """Список всех жилых домов"""
    queryset = House.objects.all()
    serializer_class = HouseListSerializer
    permission_classes = (AllowAny, )


class HouseDetailView(generics.RetrieveAPIView):
    """Полная информация о жилом доме"""
    queryset = House.objects.all()
    serializer_class = HouseDetailManageSerializer
    permission_classes = (AllowAny, )


class HouseManageView(generics.RetrieveUpdateAPIView):
    """Полная информация о жилом доме (с управлением)"""
    queryset = House.objects.all()
    serializer_class = HouseDetailManageSerializer
    permission_classes = (IsSuperuser, )


class HouseCreateView(generics.CreateAPIView):
    """Добавление нового жилого дома"""
    queryset = House.objects.all()
    serializer_class = HouseCreateDeleteSerializer
    permission_classes = (IsSuperuser, )


class HouseDeleteView(generics.DestroyAPIView):
    """Удаление жилого дома"""
    queryset = House.objects.all()
    serializer_class = HouseCreateDeleteSerializer
    permission_classes = (IsSuperuser, )




class ResidentShortListView(generics.ListAPIView):
    """Список всех жителей (без конфиденциальных данных)"""
    queryset = Resident.objects.all()
    serializer_class = ResidentShortListDetailSerializer
    permission_classes = (AllowAny, )


class ResidentShortDetailView(generics.RetrieveAPIView):
    """Полная информация о жителе (без конфиденциальных данных)"""
    queryset = Resident.objects.all()
    serializer_class = ResidentShortListDetailSerializer
    permission_classes = (AllowAny, )


class ResidentFullListView(generics.ListAPIView):
    """Список всех жителей (с конфиденциальными данными)"""
    queryset = Resident.objects.all()
    serializer_class = ResidentSecureUltimateSerializer
    permission_classes = (IsStaff, )


class ResidentFullDetailView(generics.RetrieveAPIView):
    """Полная информация о жителе (с конфиденциальными данными без управления)"""
    queryset = Resident.objects.all()
    serializer_class = ResidentSecureUltimateSerializer
    permission_classes = (IsStaff, )


class ResidentFullDetailManageView(generics.RetrieveUpdateAPIView):
    """Полная информация о жителе (с конфиденциальными данными с управлением)"""
    queryset = Resident.objects.all()
    serializer_class = ResidentSecureUltimateSerializer
    permission_classes = (IsSuperuser, )


class ResidentCreateView(generics.CreateAPIView):
    """Добавление нового жителя"""
    queryset = Resident.objects.all()
    serializer_class = ResidentSecureUltimateSerializer
    permission_classes = (IsSuperuser, )


class ResidentDeleteView(generics.DestroyAPIView):
    """Удаление жителя"""
    queryset = Resident.objects.all()
    serializer_class = ResidentSecureUltimateSerializer
    permission_classes = (IsSuperuser, )




class ExecutionStatusListView(generics.ListAPIView):
    """Список всех статусов выполнения"""
    queryset = ExecutionStatus.objects.all()
    serializer_class = ExecutionStatusUltimateSerializer
    permission_classes = (AllowAny, )


class ExecutionStatusDetailView(generics.RetrieveAPIView):
    """Полная информация о статусе выполнения"""
    queryset = ExecutionStatus.objects.all()
    serializer_class = ExecutionStatusUltimateSerializer
    permission_classes = (AllowAny, )


class ExecutionStatusManageView(generics.RetrieveUpdateAPIView):
    """Полная информация о статусе выполнения (с управлением)"""
    queryset = ExecutionStatus.objects.all()
    serializer_class = ExecutionStatusUltimateSerializer
    permission_classes = (IsSuperuser, )


class ExecutionStatusCreateView(generics.CreateAPIView):
    """Добавление нового статуса выполнения"""
    queryset = ExecutionStatus.objects.all()
    serializer_class = ExecutionStatusUltimateSerializer
    permission_classes = (IsSuperuser, IsStaff, )


class ExecutionStatusDeleteView(generics.DestroyAPIView):
    """Удаление статуса выполнения"""
    queryset = ExecutionStatus.objects.all()
    serializer_class = ExecutionStatusUltimateSerializer
    permission_classes = (IsSuperuser, )




class DepartmentListView(generics.ListAPIView):
    """Список всех отделов"""
    queryset = Department.objects.all()
    serializer_class = DepartmentUltimateSerializer
    permission_classes = (AllowAny, )


class DepartmentDetailView(generics.RetrieveAPIView):
    """Полная информация об отделе"""
    queryset = Department.objects.all()
    serializer_class = DepartmentUltimateSerializer
    permission_classes = (AllowAny, )


class DepartmentManageView(generics.RetrieveUpdateAPIView):
    """Полная информация об отделе (с управлением)"""
    queryset = Department.objects.all()
    serializer_class = DepartmentUltimateSerializer
    permission_classes = (IsSuperuser, )


class DepartmentCreateView(generics.CreateAPIView):
    """Добавление нового отдела"""
    queryset = Department.objects.all()
    serializer_class = DepartmentUltimateSerializer
    permission_classes = (IsSuperuser, IsStaff, )


class DepartmentDeleteView(generics.DestroyAPIView):
    """Удаление отдела"""
    queryset = Department.objects.all()
    serializer_class = DepartmentUltimateSerializer
    permission_classes = (IsSuperuser, )




class PositionListView(generics.ListAPIView):
    """Список всех должностей"""
    queryset = Position.objects.all()
    serializer_class = PositionListSerializer
    permission_classes = (AllowAny, )


class PositionDetailView(generics.RetrieveAPIView):
    """Полная информация о должности"""
    queryset = Position.objects.all()
    serializer_class = PositionDetailManageSerializer
    permission_classes = (AllowAny, )


class PositionManageView(generics.RetrieveUpdateAPIView):
    """Полная информация о должности (с управлением)"""
    queryset = Position.objects.all()
    serializer_class = PositionDetailManageSerializer
    permission_classes = (IsSuperuser, )


class PositionCreateView(generics.CreateAPIView):
    """Добавление новой должности"""
    queryset = Position.objects.all()
    serializer_class = PositionCreateDeleteSerializer
    permission_classes = (IsSuperuser, IsStaff, )


class PositionDeleteView(generics.DestroyAPIView):
    """Удаление должности"""
    queryset = Position.objects.all()
    serializer_class = PositionCreateDeleteSerializer
    permission_classes = (IsSuperuser, )




class EmployeeShortListView(generics.ListAPIView):
    """Список всех сотрудников (без конфиденциальных данных)"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeShortListDetailSerializer
    permission_classes = (AllowAny, )


class EmployeeShortDetailView(generics.RetrieveAPIView):
    """Полная информация о сотруднике (без конфиденциальных данных)"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeShortListDetailSerializer
    permission_classes = (AllowAny, )


class EmployeeFullListView(generics.ListAPIView):
    """Список всех сотрудников (с конфиденциальными данными)"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSecureUltimateSerializer
    permission_classes = (IsStaff, )


class EmployeeFullDetailView(generics.RetrieveAPIView):
    """Полная информация о сотруднике (с конфиденциальными данными без управления)"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSecureUltimateSerializer
    permission_classes = (IsStaff, )


class EmployeeFullDetailManageView(generics.RetrieveUpdateAPIView):
    """Полная информация о сотруднике (с конфиденциальными данными с управлением)"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSecureUltimateSerializer
    permission_classes = (IsSuperuser, )


class EmployeeCreateView(generics.CreateAPIView):
    """Добавление нового сотрудника"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSecureUltimateSerializer
    permission_classes = (IsSuperuser, )


class EmployeeDeleteView(generics.DestroyAPIView):
    """Удаление сотрудника"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSecureUltimateSerializer
    permission_classes = (IsSuperuser, )




class ServiceListView(generics.ListAPIView):
    """Список всех типовых задач"""
    queryset = Service.objects.all()
    serializer_class = ServiceListSerializer
    permission_classes = (AllowAny, )


class ServiceDetailView(generics.RetrieveAPIView):
    """Полная информация о типовой задаче"""
    queryset = Service.objects.all()
    serializer_class = ServiceDetailManageSerializer
    permission_classes = (AllowAny, )


class ServiceManageView(generics.RetrieveUpdateAPIView):
    """Полная информация о типовой задаче (с управлением)"""
    queryset = Service.objects.all()
    serializer_class = ServiceDetailManageSerializer
    permission_classes = (IsSuperuser, )


class ServiceCreateView(generics.CreateAPIView):
    """Добавление новой типовой задачи"""
    queryset = Service.objects.all()
    serializer_class = ServiceCreateDeleteSerializer
    permission_classes = (IsSuperuser, IsStaff, )


class ServiceDeleteView(generics.DestroyAPIView):
    """Удаление типовой задачи"""
    queryset = Service.objects.all()
    serializer_class = ServiceCreateDeleteSerializer
    permission_classes = (IsSuperuser, )
















# class ResidentListView(generics.ListCreateAPIView):
#     """Все жилые комплексы"""
#     queryset = Resident.objects.all()
#     serializer_class = ResidentListCreateSerializer
#     permission_classes = (IsStaff, )


# class ResidentDetailView(generics.RetrieveUpdateDestroyAPIView):
#     """Детали жилого комплекса"""
#     queryset = Resident.objects.all()
#     serializer_class = HouseListCreateDetailSerializer
#     permission_classes = (IsSuperuserOrReadOnly,)














# class TestView(APIView):
#     def get(self, request):
#         return Response(
#             {
#                 'test_data': 'This is test data'
#             }
#         )
#
#
# class ComplexList(ListAPIView):
#     queryset = HousingComplex.objects.all()
#     serializer_class = HousingComplexSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly, )
#
#
# class HouseList(ListAPIView):
#     queryset = House.objects.all()
#     serializer_class = HouseSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly, )
#
#
# class ComplexHousesList(APIView):
#     def get(self, request, complex_id):
#         houses = House.objects.filter(complex_id=complex_id)
#
#         data = []
#         for house in houses:
#             data.append(
#                 {
#                     'pk': house.pk,
#                     'complex': house.complex.name,
#                     'address': house.address.short_str()
#                 }
#             )
#
#         return Response(
#             data
#         )
#
#
# class ResidentByTg(APIView):
#     def get(self, request, user_tgID):
#         resident = Resident.objects.filter(tg_id=user_tgID)
#
#         data = []
#
#         if not resident:
#             data.append({
#                 'is_exist': False
#             })
#         else:
#             data.append({
#                 'is_exist': True,
#                 'pk': resident.pk
#             })
#
#         return Response(
#             data
#         )
#
#
# class ResidentList(APIView):
#     def get(self):
#         pass
#
#     def post(self, request):
#         data = request.data
#         snp = data['snp'].split(' ')
#         surname = snp[0]
#         try:
#             name = snp[1]
#         except IndexError:
#             name = ''
#         try:
#             patronymic = snp[2]
#         except IndexError:
#             patronymic = ''
#         phone = data['phone']
#         tg_id = data['tg_id']
#
#         new_resident = Resident(
#             name=name,
#             surname=surname,
#             patronymic=patronymic,
#             phone=phone,
#             tg_id=tg_id
#         )
#         new_resident.save()
#
#         return Response(
#             {
#                 'success': True,
#                 'resident_id': new_resident.pk
#             }
#         )
#
#
# class RequestList(APIView):
#     def post(self, request):
#         data = request.data
#         text = data['text']
#         status = ExecutionStatus.objects.get(pk=1)
#         resident = Resident.objects.get(pk=data['resident'])
#         address = House.objects.get(pk=data['house'])
#         apartment = data['apartment'] if 'apartment' in data else '-'
#         photo = data['photo'] if 'photo' in data else ''
#
#         new_request = Request(
#             text=text,
#             status=status,
#             resident=resident,
#             address=address,
#             photo=photo,
#             apartment=apartment
#         )
#         new_request.save()
#
#         return Response(
#             {
#                 'success': True,
#                 'new_request_id': new_request.pk
#             }
#         )


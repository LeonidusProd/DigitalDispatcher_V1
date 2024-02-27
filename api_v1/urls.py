from django.urls import path, include

from . import views

urlpatterns = [
    path('city/', views.CityListView.as_view(), name='city_list'),
    path('city/<int:pk>/', views.CityDetailView.as_view(), name='city_detail'),

    path('secure/city/manage/<int:pk>', views.CityManageView.as_view(), name='city_manage'),
    path('secure/city/create/', views.CityCreateView.as_view(), name='city_create'),
    path('secure/city/delete/<int:pk>', views.CityDeleteView.as_view(), name='city_delete'),


    path('street/', views.StreetListView.as_view(), name='street_list'),
    path('street/<int:pk>/', views.StreetDetailView.as_view(), name='street_detail'),

    path('secure/street/manage/<int:pk>', views.StreetManageView.as_view(), name='street_manage'),
    path('secure/street/create/', views.StreetCreateView.as_view(), name='street_create'),
    path('secure/street/delete/<int:pk>', views.StreetDeleteView.as_view(), name='street_delete'),


    path('address/', views.BuildingListView.as_view(), name='address_list'),
    path('address/<int:pk>/', views.BuildingDetailView.as_view(), name='address_detail'),

    path('secure/address/manage/<int:pk>', views.BuildingManageView.as_view(), name='address_manage'),
    path('secure/address/create/', views.BuildingCreateView.as_view(), name='address_create'),
    path('secure/address/delete/<int:pk>', views.BuildingDeleteView.as_view(), name='address_delete'),


    path('schedule/', views.WorkScheduleListView.as_view(), name='schedule_list'),
    path('schedule/<int:pk>/', views.WorkScheduleDetailView.as_view(), name='schedule_detail'),

    path('secure/schedule/manage/<int:pk>', views.WorkScheduleManageView.as_view(), name='schedule_manage'),
    path('secure/schedule/workday/manage/<int:pk>', views.WorkDayManageView.as_view(), name='workday_manage'),
    path('secure/schedule/create/', views.WorkScheduleCreateView.as_view(), name='schedule_create'),
    path('secure/schedule/delete/<int:pk>', views.WorkScheduleDeleteView.as_view(), name='schedule_delete'),


    path('office/', views.OfficeListView.as_view(), name='office_list'),
    path('office/<int:pk>/', views.OfficeDetailView.as_view(), name='office_detail'),

    path('secure/office/manage/<int:pk>', views.OfficeManageView.as_view(), name='office_manage'),
    path('secure/office/create/', views.OfficeCreateView.as_view(), name='office_create'),
    path('secure/office/delete/<int:pk>', views.OfficeDeleteView.as_view(), name='office_delete'),


    path('complex/', views.HousingComplexListView.as_view(), name='complex_list'),
    path('complex/<int:pk>/', views.HousingComplexDetailView.as_view(), name='complex_detail'),

    path('secure/complex/manage/<int:pk>', views.HousingComplexManageView.as_view(), name='complex_manage'),
    path('secure/complex/create/', views.HousingComplexCreateView.as_view(), name='complex_create'),
    path('secure/complex/delete/<int:pk>', views.HousingComplexDeleteView.as_view(), name='complex_delete'),


    path('house/', views.HouseListView.as_view(), name='house_list'),
    path('house/<int:pk>/', views.HouseDetailView.as_view(), name='house_detail'),

    path('secure/house/manage/<int:pk>', views.HouseManageView.as_view(), name='house_manage'),
    path('secure/house/create/', views.HouseCreateView.as_view(), name='house_create'),
    path('secure/house/delete/<int:pk>', views.HouseDeleteView.as_view(), name='house_delete'),


    path('resident/', views.ResidentShortListView.as_view(), name='resident_list'),
    path('resident/<int:pk>/', views.ResidentShortDetailView.as_view(), name='resident_detail'),

    path('secure/resident/', views.ResidentFullListView.as_view(), name='resident_full_list'),
    path('secure/resident/<int:pk>', views.ResidentFullDetailView.as_view(), name='resident_full_detail'),
    path('secure/resident/manage/<int:pk>', views.ResidentFullDetailManageView.as_view(),
         name='resident_full_detail_manage'),
    path('secure/resident/create/', views.ResidentCreateView.as_view(), name='resident_create'),
    path('secure/resident/delete/<int:pk>', views.ResidentDeleteView.as_view(), name='resident_delete'),


    path('status/', views.ExecutionStatusListView.as_view(), name='status_list'),
    path('status/<int:pk>/', views.ExecutionStatusDetailView.as_view(), name='status_detail'),

    path('secure/status/manage/<int:pk>', views.ExecutionStatusManageView.as_view(), name='status_manage'),
    path('secure/status/create/', views.ExecutionStatusCreateView.as_view(), name='status_create'),
    path('secure/status/delete/<int:pk>', views.ExecutionStatusDeleteView.as_view(), name='status_delete'),


    path('department/', views.DepartmentListView.as_view(), name='department_list'),
    path('department/<int:pk>/', views.DepartmentDetailView.as_view(), name='department_detail'),

    path('secure/department/manage/<int:pk>', views.DepartmentManageView.as_view(), name='department_manage'),
    path('secure/department/create/', views.DepartmentCreateView.as_view(), name='department_create'),
    path('secure/department/delete/<int:pk>', views.DepartmentDeleteView.as_view(), name='department_delete'),


    path('position/', views.PositionListView.as_view(), name='position_list'),
    path('position/<int:pk>/', views.PositionDetailView.as_view(), name='position_detail'),

    path('secure/position/manage/<int:pk>', views.PositionManageView.as_view(), name='position_manage'),
    path('secure/position/create/', views.PositionCreateView.as_view(), name='position_create'),
    path('secure/position/delete/<int:pk>', views.PositionDeleteView.as_view(), name='position_delete'),


    path('employee/', views.EmployeeShortListView.as_view(), name='employee_list'),
    path('employee/<int:pk>/', views.EmployeeShortDetailView.as_view(), name='employee_detail'),

    path('secure/employee/', views.EmployeeFullListView.as_view(), name='employee_full_list'),
    path('secure/employee/<int:pk>', views.EmployeeFullDetailView.as_view(), name='employee_full_detail'),
    path('secure/employee/manage/<int:pk>', views.EmployeeFullDetailManageView.as_view(),
         name='employee_full_detail_manage'),
    path('secure/employee/create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('secure/employee/delete/<int:pk>', views.EmployeeDeleteView.as_view(), name='employee_delete'),


    path('service/', views.ServiceListView.as_view(), name='service_list'),
    path('service/<int:pk>/', views.ServiceDetailView.as_view(), name='service_detail'),

    path('secure/service/manage/<int:pk>', views.ServiceManageView.as_view(), name='service_manage'),
    path('secure/service/create/', views.ServiceCreateView.as_view(), name='service_create'),
    path('secure/service/delete/<int:pk>', views.ServiceDeleteView.as_view(), name='service_delete'),










    # path('test/', views.TestView.as_view(), name='test'),
    # path('complexes/', views.ComplexList.as_view(), name='complexes'),
    # path('houses/', views.HouseList.as_view(), name='houses'),
    # path('requests/', views.RequestList.as_view(), name='requests'),
    # path('resident/by_tgID/<int:user_tgID>', views.ResidentByTg.as_view(), name='resident_by_tgID'),
    # path('resident/', views.ResidentList.as_view(), name='resident'),
    # path('complex_houses/<int:complex_id>', views.ComplexHousesList.as_view(), name='complex_houses'),
]

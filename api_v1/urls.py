from django.urls import path, include

from . import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('test/', views.TestView.as_view(), name='test'),
    path('complexes/', views.ComplexList.as_view(), name='complexes'),
    path('houses/', views.HouseList.as_view(), name='houses'),
    path('requests/', views.RequestList.as_view(), name='requests'),
    path('resident/by_tgID/<int:user_tgID>', views.ResidentByTg.as_view(), name='resident_by_tgID'),
    path('resident/', views.ResidentList.as_view(), name='resident'),
    path('complex_houses/<int:complex_id>', views.ComplexHousesList.as_view(), name='complex_houses'),
]

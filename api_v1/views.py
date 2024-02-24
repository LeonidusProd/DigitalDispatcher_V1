from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import viewsets
from rest_framework import status

from .models import *
from .serializers import *


class TestView(APIView):
    def get(self, request):
        return Response(
            {
                'test_data': 'This is test data'
            }
        )


class ComplexList(ListAPIView):
    queryset = HousingComplex.objects.all()
    serializer_class = HousingComplexSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class HouseList(ListAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class ComplexHousesList(APIView):
    def get(self, request, complex_id):
        houses = House.objects.filter(complex_id=complex_id)

        data = []
        for house in houses:
            data.append(
                {
                    'pk': house.pk,
                    'complex': house.complex.name,
                    'address': house.address.short_str()
                }
            )

        return Response(
            data
        )


class ResidentByTg(APIView):
    def get(self, request, user_tgID):
        resident = Resident.objects.filter(tg_id=user_tgID)

        data = []

        if not resident:
            data.append({
                'is_exist': False
            })
        else:
            data.append({
                'is_exist': True,
                'pk': resident.pk
            })

        return Response(
            data
        )


class ResidentList(APIView):
    def get(self):
        pass

    def post(self, request):
        data = request.data
        snp = data['snp'].split(' ')
        surname = snp[0]
        try:
            name = snp[1]
        except IndexError:
            name = ''
        try:
            patronymic = snp[2]
        except IndexError:
            patronymic = ''
        phone = data['phone']
        tg_id = data['tg_id']

        new_resident = Resident(
            name=name,
            surname=surname,
            patronymic=patronymic,
            phone=phone,
            tg_id=tg_id
        )
        new_resident.save()

        return Response(
            {
                'success': True,
                'resident_id': new_resident.pk
            }
        )


class RequestList(APIView):
    def post(self, request):
        data = request.data
        text = data['text']
        status = ExecutionStatus.objects.get(pk=1)
        resident = Resident.objects.get(pk=data['resident'])
        address = House.objects.get(pk=data['house'])
        apartment = data['apartment'] if 'apartment' in data else '-'
        photo = data['photo'] if 'photo' in data else ''

        new_request = Request(
            text=text,
            status=status,
            resident=resident,
            address=address,
            photo=photo,
            apartment=apartment
        )
        new_request.save()

        return Response(
            {
                'success': True,
                'new_request_id': new_request.pk
            }
        )


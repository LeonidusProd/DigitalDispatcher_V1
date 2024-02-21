from django.db import models


class City(models.Model):
    name = models.CharField(max_length=40, null=False, verbose_name='Город')

    def __str__(self):
        return f'Город {self.name}'

    def short_str(self):
        return f'г. {self.name}'

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Street(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False, verbose_name='Город')
    name = models.CharField(max_length=100, null=False, verbose_name='Улица')

    def __str__(self):
        return f'{self.city.__str__()}, улица {self.name}'

    def short_str(self):
        return f'ул. {self.name}'

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'


class Building(models.Model):
    street = models.ForeignKey(Street, on_delete=models.CASCADE, null=False, verbose_name='Улица')
    number = models.IntegerField(null=False, verbose_name='Номер здания')
    corpus = models.CharField(max_length=5, null=True, verbose_name='Корпус')

    def __str__(self):
        corp = ''
        if self.corpus:
            corp = f', корпус {self.corpus}'
        return f'{self.street.__str__()}, дом {self.number}{corp}'

    def short_str(self):
        corp = ''
        if self.corpus:
            corp = f'/{self.corpus}'
        return f'{self.street.short_str()}, д. {self.number}{corp}'

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class WorkSchedule(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name='Название графика работы')


class WorkDay(models.Model):
    DAY_CHOICES = (
        (1, 'Понедельник'),
        (2, 'Вторник'),
        (3, 'Среда'),
        (4, 'Четверг'),
        (5, 'Пятница'),
        (6, 'Суббота'),
        (7, 'Воскресенье'),
    )
    schedule = models.ForeignKey(WorkSchedule, on_delete=models.CASCADE, related_name='work_days', null=False, verbose_name='График работы')
    day_of_week = models.IntegerField(choices=DAY_CHOICES, null=False, verbose_name='День недели')
    is_not_working = models.BooleanField(default=False, null=False, verbose_name='Нерабочий')
    start_time = models.TimeField(null=True, verbose_name='Время начала работы')
    end_time = models.TimeField(null=True, verbose_name='Время конца работы')


class Office(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name='Название УК')
    address = models.ForeignKey(Building, on_delete=models.CASCADE, null=False, verbose_name='Адрес офиса УК')
    work_schedule = models.ForeignKey(WorkSchedule, on_delete=models.CASCADE, null=False, verbose_name='График работы')


class HousingComplex(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name='Название ЖК')
    office = models.ForeignKey(Office, on_delete=models.CASCADE, null=False, verbose_name='Офис УК')
    street = models.ForeignKey(Street, on_delete=models.CASCADE, null=False, verbose_name='Улица ЖК')


class House(models.Model):
    complex = models.ForeignKey(HousingComplex, on_delete=models.CASCADE, null=False, verbose_name='Жилой комплекс')
    address = models.ForeignKey(Building, on_delete=models.CASCADE, null=False, verbose_name='Адрес')


class Resident(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name='Имя')
    surname = models.CharField(max_length=50, null=False, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, null=False, verbose_name='Отчество')
    phone = models.CharField(max_length=15, null=False, verbose_name='Номер телефона')
    tg_id = models.BigIntegerField(unique=True, null=True, verbose_name='ID пользователя в Telegram')


class ExecutionStatus(models.Model):
    # Можно сделать жёстко, но надо продумать статусы
    name = models.CharField(max_length=50, null=False, verbose_name='Название')


class Department(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name='Отдел')


class Position(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name='Должность')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=False, verbose_name='Отдел')


class Employee(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name='Имя')
    surname = models.CharField(max_length=50, null=False, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, null=False, verbose_name='Отчество')
    phone = models.CharField(max_length=15, null=False, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта', null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=False, verbose_name='Должность')
    tg_id = models.BigIntegerField(unique=True, null=True, verbose_name='ID пользователя в Telegram')


def get_request_photo_path(instance, filename=None):
    return f'request/{instance.pk}/{filename}'


class Request(models.Model):
    created_at = models.DateField(null=False, verbose_name='Дата и время создания', auto_now_add=True)
    text = models.TextField(null=False, verbose_name='Текст обращения')
    status = models.ForeignKey(ExecutionStatus, on_delete=models.CASCADE, null=False, verbose_name='Статус выполнения')
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE, null=False, verbose_name='Автор заявки')
    address = models.ForeignKey(House, on_delete=models.CASCADE, null=False, verbose_name='Адрес заявки')
    apartment = models.IntegerField(null=True, verbose_name='Номер квартиры')
    photo = models.ImageField(upload_to=get_request_photo_path, null=True, verbose_name='Фото обращения')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, verbose_name='Исполнитель')


class Service(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name='Типовая задача')
    description = models.TextField(null=False, verbose_name='Описание задачи')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=False, verbose_name='Требуемая должность исполнителя')

# Generated by Django 4.2.8 on 2024-02-22 09:08

import api_v1.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер здания')),
                ('corpus', models.CharField(max_length=5, null=True, verbose_name='Корпус')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Отдел')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Электронная почта')),
                ('tg_id', models.BigIntegerField(null=True, unique=True, verbose_name='ID пользователя в Telegram')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='ExecutionStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Статус выполнения',
                'verbose_name_plural': 'Статусы выполнения',
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1.building', verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Жилой дом',
                'verbose_name_plural': 'Жилые дома',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Должность')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1.department', verbose_name='Отдел')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('tg_id', models.BigIntegerField(null=True, unique=True, verbose_name='ID пользователя в Telegram')),
            ],
            options={
                'verbose_name': 'Житель',
                'verbose_name_plural': 'Жители',
            },
        ),
        migrations.CreateModel(
            name='WorkSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название графика работы')),
            ],
            options={
                'verbose_name': 'График работы',
                'verbose_name_plural': 'Графики работы',
            },
        ),
        migrations.CreateModel(
            name='WorkDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.IntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница'), (6, 'Суббота'), (7, 'Воскресенье')], verbose_name='День недели')),
                ('is_not_working', models.BooleanField(default=False, verbose_name='Нерабочий')),
                ('start_time', models.TimeField(null=True, verbose_name='Время начала работы')),
                ('end_time', models.TimeField(null=True, verbose_name='Время конца работы')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_days', to='api_v1.workschedule', verbose_name='График работы')),
            ],
            options={
                'verbose_name': 'Рабочий день',
                'verbose_name_plural': 'Рабочие дни',
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Улица')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Улица',
                'verbose_name_plural': 'Улицы',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Типовая задача')),
                ('description', models.TextField(verbose_name='Описание задачи')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1.position', verbose_name='Требуемая должность исполнителя')),
            ],
            options={
                'verbose_name': 'Типовая задача',
                'verbose_name_plural': 'Типовые задачи',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('text', models.TextField(verbose_name='Текст обращения')),
                ('apartment', models.IntegerField(null=True, verbose_name='Номер квартиры')),
                ('photo', models.ImageField(null=True, upload_to=api_v1.models.get_request_photo_path, verbose_name='Фото обращения')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1.house', verbose_name='Адрес заявки')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_v1.employee', verbose_name='Исполнитель')),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1.resident', verbose_name='Автор заявки')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1.executionstatus', verbose_name='Статус выполнения')),
            ],
            options={
                'verbose_name': 'Заявка/Обращение',
                'verbose_name_plural': 'Заявки/Обращения',
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название УК')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1.building', verbose_name='Адрес офиса УК')),
                ('work_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1.workschedule', verbose_name='График работы')),
            ],
            options={
                'verbose_name': 'Управляющая компания',
                'verbose_name_plural': 'Управляющие компании',
            },
        ),
        migrations.CreateModel(
            name='HousingComplex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название ЖК')),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1.office', verbose_name='Офис УК')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1.street', verbose_name='Улица ЖК')),
            ],
            options={
                'verbose_name': 'Жилой комплекс',
                'verbose_name_plural': 'Жилые комплексы',
            },
        ),
        migrations.AddField(
            model_name='house',
            name='complex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1.housingcomplex', verbose_name='Жилой комплекс'),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1.position', verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='building',
            name='street',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1.street', verbose_name='Улица'),
        ),
    ]
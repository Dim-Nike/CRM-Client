from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.translation import gettext_lazy
from django.db import models
from datetime import datetime


class Device(models.Model):
    class Meta:
        db_table = 'device'
        verbose_name = 'Доступное оборудование'
        verbose_name_plural = 'Доступное оборудование'

    serial_number = models.TextField(verbose_name='Серийный номер')
    manufacturer = models.TextField(verbose_name='Производитель')
    price = models.IntegerField(verbose_name='Цена за шт')
    model = models.TextField(verbose_name='Модель')
    count = models.IntegerField(verbose_name='Колличество')
    warranty = models.IntegerField(verbose_name='Гарантированный срок (месяц)')

    def __str__(self):
        return f'{self.model}: {self.count} шт'


class Client(models.Model):
    class Meta:
        db_table = 'Client'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    client_name = models.TextField(verbose_name='ФИО', max_length=100)
    client_phone = models.TextField(verbose_name='Номер телефона', max_length=150)
    client_mail = models.TextField(verbose_name='Электронная почта', max_length=50)
    client_time = models.DateTimeField(verbose_name='Время обращения')
    model_phone = models.TextField(verbose_name='Модель телефона', max_length=155)
    descriptions = models.TextField(verbose_name='Описание проблемы')
    form_of_appeal = models.BooleanField(verbose_name='Онлайн заказ')


    def __str__(self):
        return f'{self.client_name}'


class Specialist(models.Model):
    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'

    name = models.TextField(verbose_name='ФИО', max_length=155)
    inn = models.TextField(verbose_name='ИНН')
    count_day_work = models.IntegerField('Количество рабочих дней')
    phone = models.TextField(verbose_name='Рабочий телефон', max_length=20)
    mail = models.TextField(verbose_name='Электронная почта', max_length=50)
    salary = models.IntegerField(verbose_name='Оклад')
    percent = models.IntegerField(verbose_name='Процент от ремонта')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('master', kwargs={'master_id': self.pk})


class OrderStatus(models.Model):
    class Meta:
        db_table = 'OrderStatus'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    status_name = models.TextField(verbose_name='Статус заявки', max_length=150)

    def __str__(self):
        return f'Cтатус заявки: {self.status_name}'


class Order(models.Model):
    class Meta:
        db_table = 'orders'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    order_client = models.ForeignKey(Client, verbose_name='Клиент', on_delete=models.RESTRICT)
    device = models.ForeignKey(Device, verbose_name='Оборудование', on_delete=models.RESTRICT)
    pre_order = models.BooleanField(verbose_name='Предзаказ материала')
    order_descriptions = models.TextField(verbose_name='Описание')
    create_id = models.DateTimeField(verbose_name='Создано', auto_now_add=True)
    last_updated_dt = models.DateTimeField(verbose_name='Последнее изменение', blank=True, null=True)
    master = models.ForeignKey(Specialist, verbose_name='Специалист', on_delete=models.RESTRICT)
    status = models.ForeignKey(OrderStatus, verbose_name='Статус заявки', on_delete=models.RESTRICT)
    price = models.IntegerField(verbose_name='Стоимость работ без учета стоимости запчастей')
    verification = models.CharField(verbose_name='Проверочный код', max_length=10)

    def save(self, *args, **kwargs):
        self.last_updated_dt = datetime.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('order', kwargs={'order_id': self.pk})

    def __str__(self):
        return f'Заявка №{self.id}. Мастер: {self.master} || {self.verification}'

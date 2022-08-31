from django.contrib.auth import logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, HttpResponseNotFound, Http404, FileResponse
from django.views.generic import DetailView

import csv
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

id_order = ''

def show_landing(req):
    data = {
        'title': 'Главная страница',
        'title_page': 'Добро пожаловать',
        'order': Order.objects.order_by('-create_id')
    }

    return render(req, 'orders_app/main_page.html', data)


def show_order(req):
    data = {
        'title': 'Заявки',
        'title_page': 'Заявки',
        'order': Order.objects.order_by('create_id')
    }

    return render(req, 'orders_app/order.html', data)


def show_detail_order(req, order_id):
    global id_order
    order = Order.objects.filter(id=order_id).order_by('create_id')
    data = {
        'order': Order.objects.filter(id=order_id).order_by('create_id'),
        'title_page': 'Заявка',
        'title': 'Заявка',
        'price_all': order[0].price + order[0].device.price
    }
    id_order = int(req.path[7:][:-1])
    return render(req, 'orders_app/detail_order.html', data)


def venue_pdf(req):
    order = Order.objects.order_by('create_id')
    buffer = io.BytesIO()
    can = canvas.Canvas(buffer, pagesize=letter)
    text = can.beginText()
    text.setTextOrigin(inch, inch)
    text.setFont('Times-Bold', 14)
    lines = []
    for count_line in range(11):
        lines.append(f'This is line {order[int(id_order) - 1].order_client}')

    for line in lines:
        text.textLine(line)

    can.drawText(text)
    can.showPage()
    can.save()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename=f'Заявка № {order[int(id_order) - 1].pk}.pdf')


def send_email(req):
    order = Order.objects.order_by('create_id')
    mail = send_mail('Вас, привествует, TRIGGER MOBILE',
                     f'{order[int(id_order) - 1].order_client.client_name}, информируем Вас о том, что ваша заявка была обработана.\n'
                     f'Статус заявки: {order[int(id_order) - 1].status.status_name}.\n'
                     f'Стоимость работ без учета стоимости запчастей: {order[int(id_order) - 1].price} рублей.\n'
                     f'Итоговая стоимость ремонта: {order[int(id_order) - 1].price + order[int(id_order) - 1].device.price} рублей.\n'
                     f'Ваш проверочный код, который Вы должны показать нашему сотруднику при получения телефона: {order[int(id_order) - 1].verification}. \n\n'
                     f'Как только ремонт телефона будет завершен, мы с Вами свяжемся.\n'
                     f'Благодарим, что воспользовались нашими услугами!',
                     'officialtriggermobile@gmail.com',
                     [order[int(id_order) - 1].order_client.client_mail],
                     fail_silently=False)


    if mail:
        print('Письмо отправлено!')
        return redirect('order')
    else:
        print('Ошибка! Письмо не отправлено!')


def show_master(req):
    data = {
        'title_page': 'Мастер',
        'masters': Specialist.objects.order_by('id')
    }
    return render(req, 'orders_app/master.html', data)


def show_detail_master(req, master_id):
    orders = Order.objects.order_by('create_id')
    master = Specialist.objects.filter(id=master_id).order_by('id')
    orders_master_all = 0
    orders_master = 0
    price_all = 0
    for order in orders:
        if master[0].inn == order.master.inn:
            price_all += 0.01 * master[0].percent * order.price
            if order.status.status_name != 'Done':
                orders_master += 1
            else:
                orders_master_all += 1

    price_all += master[0].salary * master[0].count_day_work

    data = {
        'title_page': 'Мастер',
        'masters': Specialist.objects.filter(id=master_id).order_by('id'),
        'order': Order.objects.order_by('create_id'),
        'master_price': price_all,
        'orders_master_all': orders_master_all,
        'orders_master': orders_master,
    }

    print(f'Выполненые заказы: {orders_master_all}\n'
          f'Нынешние заказы: {orders_master}' )

    return render(req, 'orders_app/detail_master.html', data)
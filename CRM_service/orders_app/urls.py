from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.urls import path, include

urlpatterns = [
    path('', show_landing, name='landing'),
    path('order', show_order, name='order'),
    path('order/<int:order_id>/', show_detail_order, name='detail_order'),
    path('send_email', send_email, name='send_email'),
    path('master', show_master, name='master'),
    path('master/<int:master_id>/', show_detail_master, name='detail_master'),
    path('render_pdf', render_pdf_view, name='render_pdf')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
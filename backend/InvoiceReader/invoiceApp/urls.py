
from django.urls import path
from .views import FileUploadView, invoice_list

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('invoices/', invoice_list, name='invoice-list'),
]

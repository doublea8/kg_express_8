"""ORDER MODELS"""

from django.db import models

class Order(models.Model):
    STATUS_NEW = "new"
    STATUS_CONFIRMED = "confirmed"
    STATUS_SENT = "sent"
    STATUS_DELIVERED = "delivered"
    STATUS_REJECTED = "rejected"
    ORDER_STATUSES = {
        (STATUS_NEW, "Новый"),
        (STATUS_SENT, "Подтвержден"),
        (STATUS_SENT, "Отправлен"),
        (STATUS_DELIVERED, "Доставлен"),
        (STATUS_REJECTED, "Отменен")
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField("Адрес", max_length=255)
    postal_code = models.CharField("Почтовый индекс", max_length=10)
    mobile = models.CharField("Номер телефона", max_length=10)
    notice = models.CharField("Комментарий", max_length=255)
    status = models.CharField("Статус", max_length=9,
                              choices=ORDER_STATUSES, default=STATUS_NEW)
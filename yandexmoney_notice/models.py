from django.db import models


class YadTransaction(models.Model):
    class NOTIFICATION_TYPE:
        P2P = 'p2p-incoming'
        CARD = 'card-incoming'

        CHOICES = (
            (P2P, 'Перевод из кошелька'),
            (CARD, 'Перевод с карты'),
        )

    notification_type = models.CharField('Тип перевода', max_length=32, choices=NOTIFICATION_TYPE.CHOICES)
    currency = models.IntegerField('Код валюты счёта пользователя', choices=[(643, 'Рубль РФ')])
    operation_id = models.CharField('Идентификатор операции в истории счета получателя', max_length=50)
    amount = models.DecimalField('Сумма операции', max_digits=12, decimal_places=2)
    withdraw_amount = models.DecimalField('Сумма, которая списана со счета отправителя', max_digits=12, decimal_places=2, null=True, blank=True)
    datetime_transfer = models.DateTimeField('Дата и время совершения перевода')
    sender = models.CharField('Номер счета отправителя', max_length=32, null=True, blank=True)
    codepro = models.BooleanField('Защита кодом протекции')
    label = models.CharField('Метка платежа', null=True, blank=True, max_length=64)
    test_notification = models.BooleanField('Тестовое уведомление')
    date_created = models.DateTimeField('Создано', auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField('Обновлено', auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.operation_id

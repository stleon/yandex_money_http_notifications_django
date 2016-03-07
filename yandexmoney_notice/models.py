from django.db import models


class NotificationTypes(models.Model):
	notification_type = models.CharField('Тип перевода', max_length=13, unique=True)

	def __unicode__(self):
		return self.notification_type

class Currencies(models.Model):
	code = models.IntegerField('Код валюты счета пользователя. Всегда 643 (рубль РФ согласно ISO 4217).',)

	def __unicode__(self):
		return self.currency

class YadTransactions(models.Model):
	n_type = models.ForeignKey(NotificationTypes, related_name='transactions')
	currency = models.ForeignKey(Currencies, related_name='transactions')
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

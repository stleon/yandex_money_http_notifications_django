from django.db import models


class NotificationTypes(models.Model):
	notification_type = models.CharField('Тип перевода', max_length=13, unique=True)

	def __unicode__(self):
		return self.notification_type

class Currencies(models.Model):
	code = models.CharField('Код валюты счета пользователя. Всегда 643 (рубль РФ согласно ISO 4217).', max_length=3,)

	def __unicode__(self):
		return self.currency

class YadTransactions(models.Model):
	n_type = models.ForeignKey(NotificationTypes, related_name='transactions')
	currency = models.ForeignKey(Currencies, related_name='transactions')
	operation_id = models.CharField('Идентификатор операции в истории счета получателя', max_length=25,)
	amount = models.FloatField('Сумма операции', max_length=9,)
	withdraw_amount = models.FloatField('Сумма, которая списана со счета отправителя', max_length=9, null=True, blank=True)
	datetime_transfer = models.DateTimeField('Дата и время совершения перевода',)
	sender = models.CharField('Номер счета отправителя', null=True, blank=True, max_length=20,)
	codepro = models.BooleanField('Защита кодом протекции')
	label = models.CharField('Метка платежа', null=True, blank=True, max_length=64,)
	sha1_hash = models.CharField('SHA-1 hash параметров уведомления', max_length=40,)
	test_notification = models.BooleanField('Тестовое уведомление')
	date_created = models.DateTimeField('Создано', auto_now_add=True, auto_now=False,)
	date_updated = models.DateTimeField('Обновлено', auto_now_add=False, auto_now=True,)

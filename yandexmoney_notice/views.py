from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import YadTransaction
from django.http import HttpResponse
import dateutil.parser
import hashlib


@csrf_exempt
def http_notification(request):
	response = HttpResponse(status=404)
	if request.method == 'POST':
		line_notification_options = '%s&%s&%s&%s&%s&%s&%s&%s&%s' % (
			request.POST['notification_type'], request.POST['operation_id'], request.POST['amount'],
			request.POST['currency'], request.POST['datetime'], request.POST['sender'], request.POST['codepro'],
			settings.YANDEX_MONEY_SECRET_WORD, request.POST['label'])
		if request.POST['sha1_hash'] == hashlib.sha1(line_notification_options.encode()).hexdigest():
			YadTransaction.objects.create(
				notification_type=request.POST['notification_type'],
				currency=int(request.POST['currency']),
				operation_id=request.POST['operation_id'],
				amount=request.POST['amount'],
				withdraw_amount=request.POST['withdraw_amount'] if 'withdraw_amount' in request.POST else 0,
				datetime_transfer=dateutil.parser.parse(request.POST['datetime']),
				sender=request.POST['sender'],
				codepro=False if request.POST['codepro'] == 'false' else True,
				label=request.POST['label'],
				test_notification=True if 'test_notification' in request.POST else False,
			)
			response = HttpResponse(status=200)
	return response

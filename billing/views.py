from yandex_money_http_notifications_django.settings import YANDEX_MONEY_SECRET_WORD
from django.views.decorators.csrf import csrf_exempt
from billing.models import NotificationTypes
from billing.models import YadTransactions
from billing.models import Currencies
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
			YANDEX_MONEY_SECRET_WORD, request.POST['label'])
		if request.POST['sha1_hash'] == hashlib.sha1(line_notification_options.encode()).hexdigest():
			YadTransactions.objects.create(
				n_type=NotificationTypes.objects.get(notification_type=request.POST['notification_type']),
				currency=Currencies.objects.get(code=int(request.POST['currency'])),
				operation_id=request.POST['operation_id'],
				amount=float(request.POST['amount']),
				withdraw_amount=float(request.POST['withdraw_amount']) if 'withdraw_amount' in request.POST else 0,
				datetime_transfer=dateutil.parser.parse(request.POST['datetime']),
				sender=int(request.POST['sender']),
				codepro=False if request.POST['codepro'] == 'false' else True,
				label=request.POST['label'], #sha1_hash=request.POST['sha1_hash'],
				test_notification=True if 'test_notification' in request.POST else False,
			)
			response = HttpResponse(status=200)
	return response
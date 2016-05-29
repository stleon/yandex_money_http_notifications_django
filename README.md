Что делает
======================================

Принимает http-уведомления от Яндекс.Деньги (<https://money.yandex.ru/embed/>). Записывает получаемую информацию в БД. 

Что для этого нужно
======================================

- Django >= 1.6.2
- Python >= 3.3

Установка
======================================
- `pip install git://github.com/nikicat/django-yandexmoney-notice`
- В ``urls.py`` добавляем 
```
url(r'^yandex-money-notice$', 'yandexmoney_notice.views.http_notification'),
``` 
надеюсь, вы поняли, куда именно
- Переходим на <https://sp-money.yandex.ru/myservices/online.xml>, в адрес пишем ``http://ваш-адрес/yandex-money-notice``, копируем секрет. Сохраняем.
- В ``settings.py`` добавляем ``YANDEX_MONEY_SECRET_WORD = 'Ваше секретное слово из предыдущего шага'`` и в **INSTALLED_APPS** - ``yandexmoney_notice``

После всего этого нам надо выполнить:
```
python manage.py migrate
python manage.py loaddata currencies notification_types
```
С одной стороны можно было не заморачиваться по поводу кодов валюты и ``notification_types``, но, вдруг, когда-нибудь Яндекс.Деньги будут поддерживать $.

Чтобы протестировать:
```
sudo python manage.py runserver 0.0.0.0:80
```
А затем переходите по уже известной ссылке (<https://sp-money.yandex.ru/myservices/online.xml>), нажимаете **Протестировать**. 
В логе должно быть что-то вроде:
```
[13/Mar/2014 22:49:41] "POST /yandex-money-notice HTTP/1.1" 200 0
```
Полученная информация записалась в таблицу ``yandexmoney_notice_yadtransactions``

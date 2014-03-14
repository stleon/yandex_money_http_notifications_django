Что делает
======================================

Принимает http-уведомления от Яндекс.Деньги (<https://money.yandex.ru/embed/>). Записывает получаемую информацию в БД. 

Что для этого нужно
======================================

- Django 1.6.2
- Python 3.3

А также 
```
pip install PyYAML
pip install python-dateutil
```
Установка
======================================
- Папку ``billing`` располагаем в своем проекте
- В ``urls.py`` добавляем 
```
url(r'^github_stleon$', 'billing.views.http_notification'),
``` 
надеюсь, вы поняли, куда именно
- Переходим на <https://sp-money.yandex.ru/myservices/online.xml>, в адрес пишем ``http://вашАйпи/github_stleon``, копируем секрет. Сохраняем.
- В ``settings.py`` добавляем ``YANDEX_MONEY_SECRET_WORD = 'Ваше секретное слово из предыдущего шага'`` и в **INSTALLED_APPS** - ``billing``
- В **views.py** укажите название своего проекта, вместо ``yandex_money_http_notifications_django`` (первая строчка)

После всего этого нам надо выполнить:
```
python manage.py syncdb
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
[13/Mar/2014 22:49:41] "POST /github_stleon HTTP/1.1" 200 0
```
Полученная информация записалась в таблицу ``billing_yadtransactions``

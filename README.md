
# Запуск на удаленном сервере:

1. Запустите удаленный сервер.

2. Загрузите в домашнюю деррикторию файлы docker-compose.yaml и default.conf из папки infra удобным для вас способом, например: 

2.1. Склонируйте репозиторий проекта. 

2.2. Переименуйте файл .env_example в .env и задайте значения для переменных окружения в нем. 

2.3 Скопируйте содержимое папки infra в домашнюю дерикторию удаленного сервера по ssh: 
```
scp infra/* <username>@<IP-adress>:~/
```
и .env файл
```
scp infra/.env <username>@<IP-adress>:~/
```
3. Подключитесь к удаленному серверу по ssh:
```
ssh <username>@<IP-address>
```
4. Установите docker и docker compose согласно официальной документации https://docs.docker.com/engine/install/  https://docs.docker.com/compose/install/linux/ 

5. запустите docker compose:
```
sudo docker compose up --build 
```
6. Выполните миграции, создайте пользователя администратора и соберите статику:
```
sudo docker compose exec stripe python manage.py migrate
```
```
sudo docker compose exec stripe python manage.py createsuperuser
```
```
sudo docker compose exec stripe python manage.py collectstatic --noinput
``` 
7. Войдите в панель администратора:
```
<IP-address>|<domain name>/admin/
```
8. Создайте как минимум один товар и заказ. Добавте товар в заказ.
9. Проверьте работу сервиса на создание Stripe Session на отдельный товар:
```
<IP-address>|<domain name>/item/<int:pk>/
```
 Проверьте работу сервиса на создание Stripe Payment Intent на заказ:
```
<IP-address>|<domain name>/order_buy/<int:pk>/
```

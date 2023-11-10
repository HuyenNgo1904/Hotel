# Hotel Manager
Tạo cơ sở dữ liệu tên "Hotel" trong MySQL.

Sửa thông tin kết nối cơ sở dữ liệu (username, password) trong settings.py

Chạy makemigrations/migrate để tạo cơ sở dữ liệu

Chạy phần insert dữ liệu từ file Hotel.sql (đính kèm)

Tạo superuser:

python manage.py createsuperuser --username=admin --email=admin@example.com

Dùng username "admin" và password vừa tạo để đăng nhập vào trang admin

Link đến app: localhost:8000/hihotel, link đến trang admin: localhost:8000/hihotel/admin

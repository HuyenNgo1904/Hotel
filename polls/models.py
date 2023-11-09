from re import A
from tkinter import CASCADE
from django.db import models

class Floor(models.Model):
    idFloor = models.BigAutoField(primary_key=True)
    nameFloor = models.CharField(max_length=100)
    class Meta:
        db_table = 'Floor'

class RoomKind(models.Model):
    KIND = [
        ('STD-S', 'Standard - Singer bed'),
        ('STD-D', 'Standard - Double bed'),
        ('SUP-S', 'Superior - Single bed'),
        ('SUP-D', 'Superior - Double bed'),
    ]
    idKind = models.BigAutoField(primary_key=True)
    nameKind = models.CharField(max_length=100, choices=KIND)
    price = models.CharField(max_length=100)
    descript = models.TextField()
    class Meta:
        db_table = 'RoomKind'

class RoomPicture(models.Model):
    idPicture = models.BigAutoField(primary_key=True)
    kind = models.ForeignKey(RoomKind, on_delete=models.CASCADE)
    linkPicture = models.CharField(max_length=100)
    class Meta:
        db_table = 'RoomPicture'

class Room(models.Model):
    STATUS = [
        ('OK', 'Phòng sẵn sàng'),
        ('ER', 'Phòng hỏng')
    ]
    idRoom = models.BigAutoField(primary_key=True)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    kind = models.ForeignKey(RoomKind, on_delete=models.CASCADE)
    nameRoom = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS, default='OK')
    class Meta:
        db_table = 'Room'

class CustomerInfor(models.Model):
    GENDER = [
        ('Na', 'Nam'),
        ('Nu', 'Nữ'),
        ('Kh', 'Khác')
    ]
    idCustomer = models.BigAutoField(primary_key=True)
    nameCustomer = models.CharField(max_length=50)
    gender = models.CharField(max_length=100, choices=GENDER)
    identityCard = models.CharField(max_length=12)
    phoneNumber = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    class Meta:
        db_table = 'CustomerInfo'

class CustomerRequest(models.Model):
    STATUS = [
        ('CD', 'Chờ duyệt'),
        ('HL', 'Hợp lệ'),
        ('KHL', 'Không hợp lệ')
    ]
    idRequest = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(CustomerInfor, on_delete=models.CASCADE)
    kind = models.ForeignKey(RoomKind, on_delete=models.CASCADE)
    dateCheckin = models.DateTimeField()
    dateCheckout = models.DateTimeField()
    numberOfRoom = models.IntegerField()
    numberOfChildren = models.IntegerField()
    numberOfAdults = models.IntegerField()
    status = models.CharField(max_length=100, choices=STATUS, default='CD')
    note = models.TextField(default="")
    class Meta:
        db_table = 'CustomerRequest'

class Booking(models.Model):
    STATUS = [
        ('DN', 'Đã nhận phòng'),
        ('DH', 'Đã hủy'),
        ('CN', 'Chờ nhận phòng')
    ]
    idBooking = models.BigAutoField(primary_key=True)
    customerRequest = models.ForeignKey(CustomerRequest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS, default='CN')
    note = models.CharField(max_length=100)
    class Meta:
        db_table = 'Booking'

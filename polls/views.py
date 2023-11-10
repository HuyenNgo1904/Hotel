from email.policy import HTTP
from django.http import HttpResponse
from .models import *
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# from HotelManage.polls.models import RoomKind
from .forms import *
from .models import *


### Trang chủ và form yêu cầu đặt phòng - Dương
def index(request):
    listRoomKind = RoomKind.objects.all()
    listPicture = RoomPicture.objects.all()

    return render(request, 'polls/index.html', {'listRoomKind': listRoomKind, 'listPicture': listPicture})


def reservation1(request):
    listRoomKind = RoomKind.objects.all()

    return render(request, 'polls/reservation.html', {'listRoomKind': listRoomKind})


def reservation2(request, pk):
    listRoomKind = RoomKind.objects.all()

    return render(request, 'polls/reservation.html', {'listRoomKind': listRoomKind, "idKind": pk})


def reservationadd(request):
    # Thêm thông tin khách hàng
    name = request.POST['name']
    gender = request.POST['gender']
    identitycard = request.POST['identitycard']
    email = request.POST['email']
    phone = request.POST['phone']
    cus = CustomerInfor(nameCustomer=name, gender=gender, identityCard=identitycard, phoneNumber=phone, email=email)
    cus.save()
    idCus = cus.idCustomer

    # Thêm vào bảng yêu cầu khách hàng
    kindroom = request.POST['kindroom']
    kind = RoomKind.objects.get(idKind=kindroom)
    customer = CustomerInfor.objects.get(idCustomer=idCus)
    checkInt = request.POST['cin']
    checkOut = request.POST['cout']
    numberRoom = int(request.POST['numberRoom'])
    numberChildren = int(request.POST['numberChildren'])
    numberAdults = int(request.POST['numberAdults'])
    note = request.POST['note']
    rq = CustomerRequest(kind=kind, customer=customer, dateCheckin=checkInt, dateCheckout=checkOut,
                         numberOfRoom=numberRoom, numberOfChildren=numberChildren, numberOfAdults=numberAdults,
                         note=note)
    rq.save()

    listRoomKind = RoomKind.objects.all()

    return render(request, 'polls/reservation.html',
                  {'success': 'Request sent to the hotel!', 'listRoomKind': listRoomKind})


###

### Trang chủ admin -
def home(request):
    return render(request, 'polls/admin/home.html')


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect(reverse("polls:home"))
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="polls/admin/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    return render(request, 'polls/admin/login.html', messages.error(request, "You have successfully logged out."))


def profile(request):
    return render(request, 'polls/admin/profile.html')


# đổi mật khẩu
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('polls:change_password')
        else:
            messages.error(request, 'Please re-enter your password.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'polls/admin/change_password.html', {
        'form': form
    })


###

### Quản lý phòng và tầng - Huyền
def floor(request):
    polls_floor_list = Floor.objects.filter().order_by('idFloor')
    context = {'Floor': polls_floor_list}
    return render(request, 'polls/admin/floor.html', context)


def addfloor(request):
    return render(request, 'polls/admin/floor_add.html')


def afloor(request):
    if request.method == 'POST':
        name_floor = request.POST['name']

        fl = Floor(nameFloor=name_floor)
        fl.save()

        return floor(request)
    else:
        return render(request, 'polls/admin/error.html')


def delete_floor(request, pk):
    item = Floor.objects.get(idFloor=pk)

    item.delete()
    return floor(request)


def updateFloor(request, pk):
    floor = Floor.objects.get(idFloor=pk)
    form = FloorForm(instance=floor)
    if request.method == 'POST':
        form = FloorForm(request.POST, instance=floor)
        if form.is_valid():
            form.save()
            return redirect('/hihotel/admin/floor/')

    context = {'form': form}
    return render(request, 'polls/admin/floor_update.html', context)


# quản lý phòng
def room(request):
    list_floor = Floor.objects.filter()
    polls_room = Room.objects.filter().order_by('idRoom')
    return render(request, 'polls/admin/room.html', {'Room': polls_room})


def delete_room(request, pk):
    item = Room.objects.get(idRoom=pk)

    item.delete()

    return room(request)


def addroom(request):
    list_floor = Floor.objects.filter()
    list_roomkind = RoomKind.objects.filter()
    return render(request, 'polls/admin/room_add.html', {'floor': list_floor, 'roomkind': list_roomkind})


def aroom(request):
    if request.method == 'POST':
        name_room = request.POST['name_room']
        id_floor = request.POST['tang']
        id_roomkind = request.POST['loaiphong']
        trangthai = request.POST['trangthai']

        itemfloor = Floor.objects.get(idFloor=id_floor)
        itemRoomkind = RoomKind.objects.get(idKind=id_roomkind)

        addroom = Room(floor=itemfloor, kind=itemRoomkind, nameRoom=name_room, status=trangthai)
        addroom.save()
        return room(request)
    else:
        return render(request, 'polls/admin/error.html')


def updateRoom(request, pk):
    room = Room.objects.get(idRoom=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('/hihotel/admin/room/')

    context = {'form': form}
    return render(request, 'polls/admin/room_update.html', context)


###

### Quản lý loại phòng - Ngân
def roomkind(request):
    roomkinds = RoomKind.objects.all()
    return render(request, 'polls/admin/roomkind.html', {'roomkinds': roomkinds})


def addroomkind(request):
    form = RoomKindForm()
    if request.method == 'POST':
        form = RoomKindForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/hihotel/admin/roomkind/')

    context = {'form': form}
    return render(request, 'polls/admin/addroomkind.html', context)


def updateRoomkind(request, pk):
    roomkind = RoomKind.objects.get(idKind=pk)
    form = RoomKindForm(instance=roomkind)
    if request.method == 'POST':
        form = RoomKindForm(request.POST, instance=roomkind)
        if form.is_valid():
            form.save()
            return redirect('/hihotel/admin/roomkind/')

    context = {'form': form}
    return render(request, 'polls/admin/addroomkind.html', context)


def deleteRoomKind(request, pk):
    roomkind = RoomKind.objects.get(idKind=pk)
    roomkind.delete()

    return redirect('/hihotel/admin/roomkind/')


###

### Quản lý yêu cầu đặt phòng và lập đơn đặt phòng - Thư
def bookroom(request):
    list_request = CustomerRequest.objects.order_by('status')
    list_status = CustomerRequest.status.field.choices

    res = {
        "list_request": list_request,
        "list_status": list_status
    }

    return render(request, 'polls/admin/bookroom.html', res)


def editRequest(request, idRequest, status):
    record = CustomerRequest.objects.get(idRequest=idRequest)
    record.status = status
    record.save(update_fields=['status'])

    list_request = CustomerRequest.objects.order_by('status')
    list_status = CustomerRequest.status.field.choices

    res = {
        "list_request": list_request,
        "list_status": list_status,
        "message": "Update success!"
    }

    return render(request, 'polls/admin/bookroom.html', res)


def deleteRequest(request, idRequest):
    CustomerRequest.objects.filter(idRequest=idRequest).delete()

    list_request = CustomerRequest.objects.order_by('status')
    list_status = CustomerRequest.status.field.choices

    res = {
        "list_request": list_request,
        "list_status": list_status,
        "message": "Delete success!"
    }

    return render(request, 'polls/admin/bookroom.html', res)


def filterRoom(request, idRequest):
    dateCheckin = CustomerRequest.objects.filter(idRequest=idRequest)[0].dateCheckin
    dateCheckout = CustomerRequest.objects.filter(idRequest=idRequest)[0].dateCheckout
    kind = CustomerRequest.objects.filter(idRequest=idRequest)[0].kind
    numberOfRoom = CustomerRequest.objects.filter(idRequest=idRequest)[0].numberOfRoom

    listRoomOfKind = Room.objects.filter(kind=kind, status='OK')
    listRoom = Booking.objects.select_related('customerRequest')
    listExcept = []
    listReturn = []

    for i in listRoom:
        if i.status != 'DH':
            if kind.idKind == i.customerRequest.kind.idKind:
                if i.customerRequest.status != 'KHL':
                    if (
                            i.customerRequest.dateCheckin <= dateCheckout and i.customerRequest.dateCheckin >= dateCheckin) or (
                            i.customerRequest.dateCheckout <= dateCheckout and i.customerRequest.dateCheckout >= dateCheckin):
                        listExcept.append(i.room_id)

    for i in listRoomOfKind:
        if i.idRoom not in listExcept:
            listReturn.append(i)

    if (len(listReturn) < numberOfRoom):
        list_request = CustomerRequest.objects.order_by('status')
        list_status = CustomerRequest.status.field.choices

        res = {
            "list_request": list_request,
            "list_status": list_status,
            'message': 'No enough number of room.'
        }

        return render(request, 'polls/admin/bookroom.html', res)
    else:
        res = {
            "list_room": listReturn,
            "idRequest": idRequest,
            'numberRoom': numberOfRoom
        }

        return render(request, 'polls/admin/bookroom_roomfilter.html', res)


def booking(request):
    idRequest = request.POST['idRequest']
    n = request.POST['number']

    for i in range(int(n)):
        s = "room" + str(i)
        customerReq = CustomerRequest.objects.filter(idRequest=idRequest)[0]
        customerReq.status = 'HL'
        customerReq.save()
        p = Booking(customerRequest=customerReq,
                    room=Room.objects.filter(idRoom=request.POST[s])[0],
                    status='CN',
                    note='')
        p.save()

    return bookroom(request)


def bookingManage(request):
    list_booking = Booking.objects.order_by('-idBooking')
    list_status = Booking.status.field.choices

    res = {
        "list_booking": list_booking,
        "list_status": list_status,
    }

    return render(request, 'polls/admin/booking.html', res)


def bookingEdit(request, id, status):
    record = Booking.objects.get(idBooking=id)
    record.status = status
    record.save(update_fields=['status'])

    list_booking = Booking.objects.order_by('-idBooking')
    list_status = Booking.status.field.choices

    res = {
        "list_booking": list_booking,
        "list_status": list_status,
    }

    return render(request, 'polls/admin/booking.html', res)


def bookingDelete(request, id):
    Booking.objects.filter(idBooking=id).delete()

    list_booking = Booking.objects.order_by('-idBooking')
    list_status = Booking.status.field.choices

    res = {
        "list_booking": list_booking,
        "list_status": list_status,
        'message': 'No enough number of room.'
    }

    return render(request, 'polls/admin/booking.html', res)
###




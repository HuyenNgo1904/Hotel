from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # Dương
    path('', views.index, name='index'),
    path('reservation/<int:pk>/', views.reservation2, name='reservation'),
    path('reservation/', views.reservation1, name='reservation'),
    path('reservation/add', views.reservationadd, name='reservationadd'),
    #

    path('admin/home', views.home, name='home'),
    # Cảm
    path('admin/', views.login, name='login'),
    path("admin/logout/", views.logout_request, name="logout"),
    path("admin/profile/", views.profile, name="profile"),
    path("admin/change_password/", views.change_password, name='change_password'),
    #

    # Huyền
    path('admin/floor/', views.floor, name='floor'),
    path('admin/floor/add', views.addfloor, name='addfloor'),
    path('admin/floor/afloor', views.afloor, name='afloor'),
    #     path('admin/floor/update/<int:pk>', views.update_floor, name='update_floor'),
    path('admin/update_floor/<str:pk>/', views.updateFloor, name='update_floor'),
    path('admin/floor/del/<int:pk>', views.delete_floor, name='delete_floor'),

    path('admin/room/', views.room, name='room'),
    path('admin/room/add', views.addroom, name='addroom'),
    path('admin/room/aroom', views.aroom, name='aroom'),
    #     path('admin/room/upfloor/<int:pk>', views.uproom, name='uproom'),
    path('admin/update_room/<str:pk>/', views.updateRoom, name='update_room'),
    path('admin/room/del/<int:pk>', views.delete_room, name='delete_room'),
    #

    path('admin/roomkind/', views.roomkind, name='roomkind'),
    path('admin/addroomkind', views.addroomkind, name='addroomkind'),
    path('admin/update_roomkind/<str:pk>/', views.updateRoomkind, name='update_roomkind'),
    path('admin/delete_roomkind/<str:pk>/', views.deleteRoomKind, name='delete_roomkind'),

    # Thư
    path('admin/bookroom/', views.bookroom, name='bookroom'),
    path('admin/bookroom/edit/<int:idRequest>/<str:status>/', views.editRequest, name='editRequest'),
    path('admin/bookroom/delete/<str:idRequest>/', views.deleteRequest, name="deleteRequest"),
    path('admin/bookroom/filter/<str:idRequest>/', views.filterRoom, name="filterRoom"),
    path('admin/bookroom/bookfilter/', views.booking, name="booking"),

    path('admin/booking/', views.bookingManage, name="bookingManage"),
    path('admin/booking/edit/<int:id>/<str:status>/', views.bookingEdit, name="bookingEdit"),
    path('admin/booking/delete/<int:id>/', views.bookingDelete, name="bookingDelete"),
    #
]
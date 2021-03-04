from django.urls import path
from . import views
app_name="Airline"
urlpatterns=[path("",views.index,name="index"),
            path("<int:flightId>",views.flight,name="flight"),
            path("<int:fid>/book",views.book,name="book")
]
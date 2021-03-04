from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from flight.models import Flight,Passengers
# Create your views here.



def index(request):
    return render(request,"flight/index.html",{"flights":Flight.objects.all()})

def flight(request,flightId):
    f=Flight.objects.get(pk=flightId)

    return render(request,"flight/flight.html",
                  {"flight":f,"passengers":f.passengers.all(),
                  "non_Passengers":Passengers.objects.exclude(flights=f).all()})
def book(request,fid):
    if request.method=="POST":
        flight=Flight.objects.get(pk=fid)
        passenger=Passengers.objects.get(pk=int(request.POST["passenger"]))
        flight.passengers.add(passenger)
        return HttpResponseRedirect(reverse("Airline:flight",args=(fid,)))



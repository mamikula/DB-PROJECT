# import datetime for date fields
import string
import random

from bson import ObjectId
from django.http import HttpResponseRedirect
from datetime import datetime,date
from django.shortcuts import render


# Create your views here.
import pymongo
from .forms import CityForm,DimensionsForm,DataForm,ReservationForm,EditReservationForm

connection_string= 'mongodb+srv://mmikula:Marcinm17@cluster0.7q4lh.mongodb.net/PortDB?retryWrites=true&w=majority'
my_client = pymongo.MongoClient(connection_string)

dimensions = []
dbname = my_client['PortDB']
ports = dbname["Port"]
reservations=dbname["Reservation"]
yachts=dbname["Yacht"]

def get_res_number(length):
    letters = string.ascii_lowercase
    while(True):
        resNum = ''.join(random.choice(letters) for _ in range(length))
        if len(list(reservations.find({'reservationNumber' : resNum}))) == 0:
            return resNum

def index(request):
    port_list = ports.find({})
    if request.method == 'POST':

        form = CityForm(request.POST)

        if form.is_valid():

            city=form.cleaned_data['city']
            port_list = ports.find({'name':{'$regex':city}})
            return render(request, 'GdzieTaKeja/ports.html',{'port_list': port_list, 'form': form})

    else:
        form = CityForm()
    return render(request, 'GdzieTaKeja/ports.html', {'port_list':port_list, 'form':form})


def sectors(request,port_id):
    portInstance=ObjectId(port_id)
    port = ports.find_one({'_id':portInstance})
    sectors_list=port["sectors"]
    filtered_sectors = []
    global dimensions
    if request.method == 'POST':

        form = DimensionsForm(request.POST)

        if form.is_valid():
            length=form.cleaned_data['length']
            depth = form.cleaned_data['depth']
            width = form.cleaned_data['width']
            y_type = form.cleaned_data['type']
            dimensions.append({'length':length,'depth':depth,'width':width,'y_type':y_type})
            y_data_id=len(dimensions)-1
            filtered_sectors=[]
            for s in sectors_list:
                if s['type'] == 'perpendicular':
                    req=0
                    if s['maxWidth'] >= width:
                        req+=1
                    if y_type == 'mieczowy':
                        req+=1
                    if y_type == 'balastowy':
                        if s['depth'] >= depth:
                            req+=1
                    if req==2:
                        filtered_sectors.append(s)
                else:
                    req=0
                    if y_type == 'mieczowy':
                        req+=1
                    if y_type == 'balastowy':
                        if s['depth'] >= depth:
                            req+=1
                    if s['availableLength'] >= length:
                        req+=1
                    if req==2:
                        filtered_sectors.append(s)
            return render(request, 'GdzieTaKeja/sectors.html',{'port_id':port_id,'y_id':y_data_id,'form':form,'filtered_sectors':filtered_sectors})

    else:
        form = DimensionsForm()
    return render(request, 'GdzieTaKeja/sectors.html',{'port_id':port_id,'form':form,'filtered_sectors':filtered_sectors})


def slots(request,port_id,y_id,sector_name):
    portInstance=ObjectId(port_id)
    port = ports.find_one({'_id':portInstance})
    sectors_list=port["sectors"]
    slot_list=''
    sector_type=''
    for s in sectors_list:
        if s['name']==sector_name:
            slot_list=[]
            for slot in s['slots']:
                if slot['taken'] == False:
                    slot_list.append(slot)
            sector_type=s['type']
    for slot in slot_list:
        slot['id']=int(slot['id'])
    return render(request, 'GdzieTaKeja/slots.html',{'slot_list':slot_list,'y_id':y_id,'port':port,'port_id':port_id,
                                                     'sector_name':sector_name,'sector_type':sector_type})


def reserve(request,port_id,sector_name,y_id,slot_id):
    portInstance = ObjectId(port_id)
    port = ports.find_one({'_id': portInstance})
    sectors_list = port["sectors"]

    sector_type = ''
    sector=None
    arrayid=-1
    global dimensions
    for i in range(len(sectors_list)):
        if sectors_list[i]['name'] == sector_name:
            sector_type = sectors_list[i]['type']
            sector=sectors_list[i]
            arrayid=i
    if sector_type=='parallel':
        if sector['availableLength']<dimensions[y_id]['length']:
            return render(request, 'GdzieTaKeja/thanks.html', {'action': 'reservation_unavailable'})
    if sector_type=='perpendicular':
        if sector['slots'][slot_id]['taken']==True:
            return render(request, 'GdzieTaKeja/thanks.html', {'action': 'reservation_unavailable'})
    if request.method == 'POST':

        form = DataForm(request.POST)

        if form.is_valid():
            yachtID=form.cleaned_data['yachtID']
            name=form.cleaned_data['name']
            surname=form.cleaned_data['surname']
            dateFrom=form.cleaned_data['dateFrom']
            dateTo=form.cleaned_data['dateTo']
            reservationNumber=get_res_number(6)
            yachts.insert_one({'in':yachtID,'depth':dimensions[y_id]['depth'],'length':dimensions[y_id]['length'],'width':dimensions[y_id]['width'],'type':dimensions[y_id]['y_type']})
            if sector_type == 'parallel':
                newReservation={'reservationNumber':reservationNumber,'portID':port_id,'sectorID':sector_name,'type':sector_type,'slot':None,
                                'ownerName':name,'ownerSurname':surname,'yachtID':yachtID,
                                'dateFrom':datetime.combine(dateFrom, datetime.min.time()),
                                'dateTo':datetime.combine(dateTo, datetime.min.time()), 'active': True}
                reservations.insert_one(newReservation)
                sector['availableLength']=sector['availableLength']-dimensions[y_id]['length']
                sectors_list[arrayid]= sector
                ports.update_one({'_id':portInstance},{'$set':{'sectors':sectors_list}})
            else:
                newReservation ={'reservationNumber':reservationNumber,'portID': port_id, 'sectorID': sector_name, 'type': sector_type, 'slot': slot_id,
                                 'ownerName':name,'ownerSurname':surname, 'yachtID': yachtID,
                                 'dateFrom':datetime.combine(dateFrom, datetime.min.time()),
                                 'dateTo':datetime.combine(dateTo, datetime.min.time()), 'active': True}
                reservations.insert_one(newReservation)
                wantedSlot=None
                slot_list=sector['slots']
                for slot in sector['slots']:
                    if slot['id']==slot_id:
                        wantedSlot=slot
                if wantedSlot!=None:
                    wantedSlot['taken']=True
                slot_list[slot_id]=wantedSlot
                sector['slots']=slot_list
                sectors_list[arrayid]=sector
                ports.update_one({'_id': portInstance}, {'$set': {'sectors': sectors_list}})
            return render(request, 'GdzieTaKeja/thanks.html',{'reservationNumber':reservationNumber,'action':'reserve'})
    else:
        form = DataForm()
    return render(request, 'GdzieTaKeja/reserve.html', {'port_id':port_id,'dim_len':len(dimensions), 'port':port, 'sector_name':sector_name, 'sector_type':sector_type, 'slot_id':slot_id, 'form':form,'y_id':y_id})

def reservation(request):
    reservations_found = None
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservationNumberInput = form.cleaned_data['reservationNumber']

            reservations_found = reservations.find({'reservationNumber': reservationNumberInput})

            return render(request,'GdzieTaKeja/reservations.html', {'form': form,'reservation_found':reservations_found})

    else:
        form = ReservationForm()
    return render(request,'GdzieTaKeja/reservations.html',{'form':form,'reservation_found':reservations_found})

def editreservation(request,reservation_number):
    reservation = reservations.find_one({'reservationNumber': reservation_number})
    if request.method == 'POST':
        form = EditReservationForm(request.POST)
        if request.POST['modify'] == 'Edytuj':
            if form.is_valid():
                beforeDateFrom=reservation['dateFrom']
                beforeDateTo=reservation['dateTo']
                dateFrom=form.cleaned_data['dateFrom']
                dateTo=form.cleaned_data['dateTo']
                reservations.update_one({'reservationNumber': reservation_number}, {'$set': {'dateFrom': datetime.combine(dateFrom, datetime.min.time()),
                                                                        'dateTo':datetime.combine(dateTo, datetime.min.time())}})
                return render(request,'GdzieTaKeja/thanks.html',{'action':'modify','beforeF':beforeDateFrom,'beforeT':beforeDateTo,
                                                                 "dateFrom":dateFrom,'dateTo':dateTo})
        elif request.POST['modify'] == 'Usuń':
            portInstance=ObjectId(reservation['portID'])
            port=ports.find_one({'_id':portInstance})
            sectors_list=port['sectors']
            sectorToUpdate = None
            arrayid = -1
            for i in range(len(sectors_list)):
                if sectors_list[i]['name'] == reservation['sectorID']:
                    sectorToUpdate = sectors_list[i]
                    arrayid = i
            slotToUpdate=None
            if reservation['type'] == "parallel":
                yacht=yachts.find_one({'in':reservation['yachtID']})
                sectorToUpdate['availableLength']=sectorToUpdate['availableLength']+yacht['length']
                sectors_list[arrayid]=sectorToUpdate
                ports.update_one({'_id': portInstance}, {'$set': {'sectors': sectors_list}})

            if reservation['type'] == "perpendicular":
                slot_list = sectorToUpdate['slots']
                for slot in slot_list:
                    if slot['id'] == reservation['slot']:
                        slotToUpdate = slot

                if slotToUpdate != None:
                    slotToUpdate['taken'] = False
                slot_list[reservation['slot']] = slotToUpdate
                sectorToUpdate['slots'] = slot_list
                sectors_list[arrayid] = sectorToUpdate
                ports.update_one({'_id': portInstance}, {'$set': {'sectors': sectors_list}})

            reservations.update_one({'reservationNumber': reservation_number}, {'$set': {'active': False}})
            return render(request, 'GdzieTaKeja/thanks.html',{'action':'delete'})
    else:
        if len(list(reservations.find({'reservationNumber': reservation_number}))) != 0:
            form = EditReservationForm(initial={'dateFrom': reservation['dateFrom'], 'dateTo': reservation['dateTo']})
        else:
            form = EditReservationForm()
    return render(request,'GdzieTaKeja/editreservation.html',{'form':form,'reservation':reservation})
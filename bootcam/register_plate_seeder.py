import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','bootcam.settings')

import django
django.setup()

#Faker population script

import random
from vehicles.models import Vehicle
from faker import Faker

fakegen = Faker()

register_plates = [
'LCH-342',
'ZQL-749',
'FUM-178',
'QFI-103',
'NLL-691',
'YQR-668',
'CPM-175',
'OWH-643',
'ZCV-455',
'UJG-606',
'WWR-124',
'UCD-318',
'JOR-720',
'LBN-423',
'QEQ-517',
'CQP-523',
'VJA-623',
'GSI-802',
'TLT-810',
'KMB-223'
]

def populate():

    for plate in register_plates:
        owner =  fakegen.name()
        vehicle = Vehicle.objects.get_or_create(register_plate = plate, owner = owner)[0]

if __name__ == '__main__':
    print("Populating vehicles table...")
    populate()
    print("Populating finished!")

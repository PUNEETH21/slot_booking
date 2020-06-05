import pytest
from freezegun import freeze_time
from django.db import *
from slot_booking.models.user import User
from slot_booking.models.user_slot import UserSlot
from slot_booking.models.washing_machine import Washingmachine
from slot_booking.models.washing_machine_slot import WashingmachineSlot
from slot_booking.dtos.dtos import \
    WashingMachineDetailsDto, UpdateTimeSlotDto, TimeSlotDto

pytestmark = pytest.mark.django_db
@pytest.fixture
def user():
    User.objects.bulk_create([
        User(name='u1', username='username', password="password"),
        User(name='u2', username='username1', password="password"),
        User(name='u3', username='username2', password="password"),
        ])
    users_objects = User.objects.all()
    return users_objects


@pytest.fixture
def washing_machine():
    Washingmachine.objects.bulk_create([
        Washingmachine(washing_machine_id='wm1', is_active=True),
        Washingmachine(washing_machine_id='wm2', is_active=True),
        Washingmachine(washing_machine_id='wm3', is_active=True),
        Washingmachine(washing_machine_id='wm4', is_active=True),
        Washingmachine(washing_machine_id='wm5', is_active=True),
        Washingmachine(washing_machine_id='wm6', is_active=False)
        ])
    washing_machine_objects = Washingmachine.objects.all()
    return washing_machine_objects

@pytest.fixture
def washing_machine_slot(washing_machine):
    WashingmachineSlot.objects.bulk_create([
        WashingmachineSlot(day="Monday", start_time="05:00:00",
        end_time= "06:00:00",washing_machine_id='wm1'),
        WashingmachineSlot(day="Monday", start_time="05:00:00",
        end_time= "06:00:00",washing_machine_id='wm2'),
        WashingmachineSlot(day="Monday", start_time="05:00:00",
        end_time= "06:00:00",washing_machine_id='wm3'),
        WashingmachineSlot(day="Monday", start_time="06:00:00",
        end_time= "07:00:00",washing_machine_id='wm1'),
        WashingmachineSlot(day="Monday", start_time="07:00:00",
        end_time= "08:00:00",washing_machine_id='wm1'),
        WashingmachineSlot(day="Monday", start_time="07:00:00",
        end_time= "08:00:00",washing_machine_id='wm2'),
        WashingmachineSlot(day="Tuesday", start_time="06:00:00",
        end_time= "07:00:00",washing_machine_id='wm1'),
        WashingmachineSlot(day="Tuesday", start_time="07:00:00",
        end_time= "08:00:00",washing_machine_id='wm1'),

        WashingmachineSlot(day="Thursday", start_time="06:00:00",
        end_time= "07:00:00",washing_machine_id='wm1'),
        WashingmachineSlot(day="Thursday", start_time="07:00:00",
        end_time= "08:00:00",washing_machine_id='wm1')     
    ])
    washing_machine_slot_objects = WashingmachineSlot.objects.all()
    return washing_machine_slot_objects

@pytest.fixture
def user_slot(user, washing_machine):
    UserSlot.objects.bulk_create([
        UserSlot(date="2020-05-14", start_time="05:00:00",
        end_time= "06:00:00",washing_machine_id='wm1', user_id=1),
        
        UserSlot(date="2020-05-20", start_time="05:00:00",
        end_time= "06:00:00",washing_machine_id='wm1', user_id=1),
        UserSlot(date="2020-05-20", start_time="05:00:00",
        end_time= "06:00:00",washing_machine_id='wm2', user_id=2),
        UserSlot(date="2020-05-20", start_time="06:00:00",
        end_time= "07:00:00",washing_machine_id='wm1', user_id=3),
        
        UserSlot(date="2020-05-26", start_time="07:00:00",
        end_time= "08:00:00",washing_machine_id='wm2', user_id=1),
        UserSlot(date="2030-05-14", start_time="05:00:00",
        end_time= "06:00:00",washing_machine_id='wm1', user_id=1),
        UserSlot(date="2030-05-20", start_time="05:00:00",
        end_time= "06:00:00",washing_machine_id='wm1', user_id=1),
        UserSlot(date="2030-05-26", start_time="07:00:00",
        end_time= "08:00:00",washing_machine_id='wm2', user_id=1),
    ])
    user_slot_objects = UserSlot.objects.all()
    return user_slot_objects


@pytest.fixture()
def washing_machine_details_dto_status_true(washing_machine):
    washing_machine_details_dto = WashingMachineDetailsDto(
        washing_machine_id = "wm5",
        is_active = True
    )

    return washing_machine_details_dto

@pytest.fixture()
def washing_machine_details_dto_status_false(washing_machine):
    washing_machine_details_dto = WashingMachineDetailsDto(
        washing_machine_id = "wm6",
        is_active = False
    )

    return washing_machine_details_dto

@pytest.fixture()
def time_slots_dtos():
    time_slots_dtos = UpdateTimeSlotDto(
        day = "Thursday",
        washing_machine_id = "wm1",
        time_slots_dtos = [
            TimeSlotDto(
                start_time = "06:30",
                end_time = "07:30"
            ),
            TimeSlotDto(
                start_time = "07:30",
                end_time = "08:30"
            ),
            TimeSlotDto(
                start_time = "08:30",
                end_time = "09:30"
            )
        ]
    )

    return time_slots_dtos

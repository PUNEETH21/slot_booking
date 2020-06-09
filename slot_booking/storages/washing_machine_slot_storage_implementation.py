from typing import List, Optional
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from slot_booking.interactors.storages.washing_machine_slot_storage_interface \
    import WashingMachineSlotStorageInterface
from slot_booking.models.washing_machine_slot import WashingmachineSlot
from slot_booking.dtos.dtos import (
    TimeSlotDto, WashingMachineSlotsDto, WashingMachineDto, UpdateTimeSlotDto,
    TimeRangeCountDto
)
from django.db.models import Count

class WashingMachineSlotStorageImplementation(
    WashingMachineSlotStorageInterface):

    def get_washing_machine_slots(self, day: str, washing_machine_id: str):
        wm_objs = WashingmachineSlot.objects.filter(
            day=day, washing_machine_id=washing_machine_id)
        time_slot_dto_list = []
        
        for wm_obj in wm_objs:
                time_slot_dto_list.append(
                    TimeSlotDto(
                        start_time=str(wm_obj.start_time),
                        end_time=str(wm_obj.end_time)
                    )
                )
        return time_slot_dto_list


    def update_slot(self, day: str, start_time: str, end_time: str,
        washing_machine_id: str):

        washing_machine_obj = WashingmachineSlot.objects.filter(
            day=day,washing_machine_id=washing_machine_id)
        
        return washing_machine_obj


    def washing_machines_in_given_slot(self, day: str, start_time: str, 
        end_time: str
    ):
        wm_ids = WashingmachineSlot.objects.filter(
            day=day, start_time=start_time, end_time=end_time
        ).values_list('washing_machine_id',flat=True)

        return list(wm_ids)


    def update_time_slots(self, time_slots_dtos: UpdateTimeSlotDto):
        day = time_slots_dtos.day
        washing_machine_id = time_slots_dtos.washing_machine_id
        time_slots = time_slots_dtos.time_slots_dtos
        wm_objs = WashingmachineSlot.objects.filter(day=day, 
            washing_machine_id=washing_machine_id)

        wm_objs.delete()
        wm_objs = []
        for time_slot in time_slots:
            wm_objs.append(
                WashingmachineSlot(
                    day=day, start_time=time_slot.start_time,
                    end_time= time_slot.end_time,
                    washing_machine_id=washing_machine_id
                )
            )

        WashingmachineSlot.objects.bulk_create(wm_objs)


    def get_day_slots(self, day: str):
        wm_objs = WashingmachineSlot.objects.filter(
            day=day).values("start_time", "end_time").annotate(
                count = Count("start_time")).values_list(
                    "start_time", "end_time", "count")

        wm_objs_dtos_list = []
        for wm_obj in wm_objs:
            wm_objs_dtos_list.append(
                TimeRangeCountDto(
                    start_time = str(wm_obj[0]),
                    end_time = str(wm_obj[1]),
                    count = wm_obj[2]
                )
            )

        return wm_objs_dtos_list








from slot_booking.interactors.storages.washing_machine_storage_interface \
    import WashingMachineStorageInterface
from slot_booking.interactors.storages.washing_machine_slot_storage_interface \
    import WashingMachineSlotStorageInterface
from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface
from slot_booking.constants.enums import Day
from slot_booking.dtos.dtos import TimeSlotDto, UpdateTimeSlotDto

class UpdateWashingMachineSlotsInteractor:

    def __init__(self,
        washing_machine_storage: WashingMachineStorageInterface,
        washing_machine_slot_storage: WashingMachineSlotStorageInterface,
        presenter: PresenterInterface):

        self.washing_machine_storage = washing_machine_storage
        self.washing_machine_slot_storage = washing_machine_slot_storage
        self.presenter = presenter


    def get_time_slots_list(self, time_slots):
        time_slots_list = []
        for time_slot in time_slots:
            timings = [time_slot["start_time"], time_slot["end_time"]]
            duplicate_time = timings in time_slots_list
            if duplicate_time:
                return False

            time_slots_list.append(timings)

        return time_slots_list

    def check_for_in_between(self, time_slot, time_slot1):
        less_time = time_slot1 < time_slot
        if less_time:
            time = time_slot
            time_slot = time_slot1
            time_slot1 = time

        start_time = time_slot[0]
        end_time = time_slot[1]
        for middle_time in time_slot1:
            time_in_between = start_time < middle_time < end_time
            if time_in_between:
                return False

        return True

    def check_for_invalid_time_slots(self, time_slots):
        time_slots_list = self.get_time_slots_list(time_slots)
        invalid_time_slots_list = not time_slots_list
        if invalid_time_slots_list:
            return False

        time_slots_dto = []
        for time_slot in time_slots_list:
            between=False
            for time_slot1 in time_slots_list:

                if time_slot != time_slot1:
                    between = not self.check_for_in_between(
                        time_slot, time_slot1)

                if between:
                    break

            if between:
                return False

            time_slots_dto.append(
                TimeSlotDto(
                    start_time = time_slot[0],
                    end_time = time_slots[1]
                )
            )

        return time_slots_dto


    def update_washing_machine_slots(self, day: str, washing_machine_id: str,
        time_slots: list):

        print("@"*30)
        days = [day.value for day in Day]
        invalid_day = day not in days
        if invalid_day:
            self.presenter.raise_exception_for_invalid_day()
            return

        invalid_washing_machine_id = \
            not self.washing_machine_storage.is_valid_washing_machine_id(
            washing_machine_id
        )

        if invalid_washing_machine_id:
            self.presenter.raise_exception_for_invalid_washing_machine_id()
            return

        invalid_time_slot = self.check_for_invalid_time_slots(time_slots)
        if invalid_time_slot:
            self.presenter.raise_exception_for_invalid_time_slot()
            return

        time_slots_dto = invalid_time_slot
        time_slots_dtos = UpdateTimeSlotDto(
            day = day,
            washing_machine_id = washing_machine_id,
            time_slots_dtos = time_slots_dto
        )


        self.washing_machine_slot_storage.update_time_slots(time_slots_dtos)
        updated_response = self.presenter.get_response_for_update_time_slots()

        return updated_response





'''
l1 = ["06:00", "07:00"]
l2 = ["06:00", "08:00"]
l1<l2

l1= [06:30]
import re
re.findall(r'>(06:30)<',l1)
from datetime import time
time(06:00)
is_bw = 06:33 in range(06:00, 07:00)        

def is_between(time, time_range):
    if time_range[1] < time_range[0]:
        return time >= time_range[0] or time <= time_range[1]
    return time_range[0] <= time <= time_range[1]

print(is_between("06:33", ("06:00", "07:00")))  # True
print(is_between("17:00", ("09:00", "16:00")))  # False
print(is_between("01:15", ("21:30", "04:30")))  # True

        washing_machine_details_dto = \
            self.washing_machine_storage.get_washing_machine_details(
            washing_machine_id
        )

        response = self.presenter.get_response_for_get_washing_machine_details(
            washing_machine_details_dto
        )

        return response
'''
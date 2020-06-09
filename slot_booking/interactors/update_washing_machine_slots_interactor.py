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


    def _get_time_slots_list(self, time_slots):
        time_slots_list = []
        for time_slot in time_slots:
            timings = [time_slot["start_time"], time_slot["end_time"]]
            duplicate_time = timings in time_slots_list
            if duplicate_time:
                return False

            time_slots_list.append(timings)

        return time_slots_list

    def _check_for_in_between(self, time_slot, time_slot1):
        start_time = time_slot[0]
        end_time = time_slot[1]
        for middle_time in time_slot1:
            
            time_in_between = (start_time < middle_time < end_time or \
            start_time==end_time or time_slot1[0]==time_slot1[1])

            if time_in_between:
                return False

        start_time = time_slot1[0]
        end_time = time_slot1[1]
        for middle_time in time_slot:
            
            time_in_between = (start_time < middle_time < end_time or \
            start_time==end_time or time_slot[0]==time_slot[1])

            if time_in_between:
                return False

        return True

    def _check_for_invalid_time_slots(self, time_slots):
        time_slots_list = self._get_time_slots_list(time_slots)
        invalid_time_slots_list = not time_slots_list
        
        if invalid_time_slots_list:
            return False

        time_slots_dto = []
        for time_slot in time_slots_list:
            between=False
            for time_slot1 in time_slots_list:

                if time_slot != time_slot1:
                    between = not self._check_for_in_between(
                        time_slot, time_slot1)

                #print("123", time_slot1, time_slot, between, "\n")
                if between:
                    break

            if between:
                return False

            time_slots_dto.append(
                TimeSlotDto(
                    start_time = time_slot[0],
                    end_time = time_slot[1]
                )
            )

        return time_slots_dto


    def update_washing_machine_slots(self, day: str, washing_machine_id: str,
        time_slots: list):

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

        valid_time_slots = self._check_for_invalid_time_slots(time_slots)
        invalid_time_slots = not valid_time_slots


        if invalid_time_slots:
            self.presenter.raise_exception_for_invalid_time_slots()
            return

        time_slots_dto = valid_time_slots
        time_slots_dtos = UpdateTimeSlotDto(
            day = day,
            washing_machine_id = washing_machine_id,
            time_slots_dtos = time_slots_dto
        )

        self.washing_machine_slot_storage.update_time_slots(time_slots_dtos)
        updated_response = self.presenter.get_response_for_update_time_slots()

        return updated_response


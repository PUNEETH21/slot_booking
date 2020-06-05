from .user import User
from .user_slot import UserSlot
from .washing_machine import Washingmachine
from .washing_machine_slot import WashingmachineSlot
from .configure_slot import ConfigureSlot
__all__ = [
    "User", "UserSlot", "Washingmachine", "WashingmachineSlot", "ConfigureSlot"
]


# class DummyModel(AbstractDateTimeModel):
#     """
#     Model to store key value pair
#     Attributes:
#         :var key: String field which will be unique
#         :var value: String field which will be of 128 char length
#     """
#     key = models.CharField(max_length=128, unique=True)
#     value = models.CharField(max_length=128)
#
#     class Meta(object):
#         app_label = 'sample_app'
#
#     def __str__(self):
#         return "<DummyModel: {key}-{value}>".format(key=self.key,
#                                                     value=self.value)
#

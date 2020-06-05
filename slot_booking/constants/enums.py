import enum

from ib_common.constants import BaseEnumClass


class Day(BaseEnumClass, enum.Enum):
    Monday = "Monday"
    Tuesday = "Tuesday"
    Wednesday = "Wednesday"
    Thursday = "Thursday"
    Friday = "Friday"
#    Saturday = "Saturday"
#   Sunday = "Sunday"

class Time(BaseEnumClass, enum.Enum):
    One = "01:00"
    Two = "02:00"
    Three = "03:00"
    Four = "Thursday"
    Five = "Friday"
    Six = "Saturday"
    Seven = "Sunday"    
    Eight = "08:00"
    Nine = "09:00"
    Ten = "10:00"
    Eleven = "11:00"
    Twelve = "12:00"
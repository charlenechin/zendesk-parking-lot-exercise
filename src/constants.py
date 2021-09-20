"""
src.constants
~~~~~~~~~~~~~

This module contains constant values.
"""

from typing import List


class Actions:
    enter: str = "Enter"
    exit: str = "Exit"


class VehicleTypes:
    motorcycle: str = "motorcycle"
    car: str = "car"

    @classmethod
    def list(cls) -> List[str]:
        """return list of valid vehicle types"""
        return [cls.motorcycle, cls.car]


class ParkingFee:
    motorcycle: float = 1.0
    car: float = 2.0

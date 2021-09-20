"""
src.models.parking_lot
~~~~~~~~~~~~~~~~~~~~~~

This module contains the objects that will model the carpark.
"""


import math
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from src.constants import ParkingFee, VehicleTypes
from src.models.vehicle import Vehicle

"""
Carpark objects.
"""


@dataclass
class Lot:
    vehicle_type: str
    number: int

    @property
    def id(self) -> str:
        """returns unique identifier of the parking lot"""
        return f"{self.vehicle_type}Lot{self.number}"


class ParkingLot:
    init_capacity: Dict[str, int] = {}
    _capacity: Dict[str, List[str]] = {}
    _lots: Dict[str, Optional[Vehicle]] = {}
    _registry: Dict[str, str] = {}

    def __init__(self, init_capacity: Dict[str, int]) -> None:
        self.init_capacity = init_capacity

    def init_lots(self) -> None:
        for k, v in self.init_capacity.items():
            if k not in VehicleTypes.list():
                raise Exception(f"Invalid Vehicle Type: {k}")

            self.capacity[k] = []
            for i in range(1, v + 1):
                lot: Lot = Lot(vehicle_type=k, number=i)
                self.capacity[k].append(lot.id)
                self.lots[lot.id] = None

    def get_avail_lot(self, vehicle_type: str) -> Optional[str]:
        for id in self.capacity.get(vehicle_type, []):
            if id not in self.registry.values():
                return id
        return None

    def enter(self, vehicle: Vehicle, lot_id: str) -> None:
        if vehicle.vehicle_number in self.registry.keys():
            raise Exception(
                f"Vehicle: {vehicle.vehicle_number} " "is already in the carpark!"
            )
        self.registry[vehicle.vehicle_number] = lot_id
        self.lots[lot_id] = vehicle

    def exit(self, vehicle_number: str, exit_time: str) -> Tuple[Vehicle, str]:
        if vehicle_number not in self.registry.keys():
            raise Exception(f"Vehicle: {vehicle_number} is not in the carpark!")
        lot_id: str = self.registry.pop(vehicle_number)
        vehicle: Vehicle = self.lots.get(lot_id)
        vehicle.exit_time = exit_time
        self.lots[lot_id] = None
        return vehicle, lot_id

    @property
    def capacity(self) -> Dict[str, List[str]]:
        """
        to ease retrieval of lots by vehicle type
        returns dict of <k: vehicle_type>: <v: list of lot ids>
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: Dict[str, List[str]]) -> None:
        self._capacity = capacity

    @property
    def lots(self) -> Dict[str, Optional[Vehicle]]:
        """
        eases retrieval of the vehicle occupying a lot
        returns dict of <k: lot_id>: <v: vehicle occupying the lot>
        """
        return self._lots

    @lots.setter
    def lots(self, lots: Dict[str, Optional[Vehicle]]) -> None:
        self._lots = lots

    @property
    def registry(self) -> Dict[str, str]:
        """
        eases retrieval of the lot a vehicle is occupying
        returns dict of <k: vehicle_number>: <v: lot_id>
        """
        return self._registry

    @registry.setter
    def registry(self, registry: Dict[str, str]) -> None:
        self._registry = registry


"""
Parking meter.
"""


class ParkingMeter:
    fees: Dict[str, float] = {
        VehicleTypes.motorcycle: ParkingFee.motorcycle,
        VehicleTypes.car: ParkingFee.car,
    }

    @classmethod
    def calc_fees(cls, vehicle: Vehicle) -> float:
        """returns calculated fee"""
        if not vehicle.enter_time or not vehicle.exit_time:
            raise Exception(
                f"Vehicle: {vehicle.vehicle_number} "
                "cannot possibly be inside the parking lot."
            )
        if vehicle.vehicle_type not in cls.fees.keys():
            raise ValueError(f"Vehicle: {vehicle.vehicle_number} is not valid.")
        duration: int = math.ceil(((vehicle.exit_time - vehicle.enter_time) / (3600)))
        if duration < 0:
            raise ValueError(
                f"Vehicle: {vehicle.vehicle_number} could not have left at"
                f"{vehicle.exit_time} when it entered at {vehicle.enter_time}"
            )
        return int(cls.fees.get(vehicle.vehicle_type, 0.0) * duration)

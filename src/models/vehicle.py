"""
src.models.vehicle
~~~~~~~~~~~

This module contains the objects that will model the vehicles.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable

from src.constants import VehicleTypes

"""
Vehicle objects.
"""


class Vehicle(ABC):
    @property
    @abstractmethod
    def vehicle_number(self) -> str:
        pass

    @property
    @abstractmethod
    def enter_time(self) -> float:
        pass

    @property
    @abstractmethod
    def exit_time(self) -> float:
        pass

    @property
    @abstractmethod
    def vehicle_type(self) -> str:
        pass


@dataclass
class Car(Vehicle):
    vehicle_number: str = ""
    enter_time: float = 0.0
    exit_time: float = 0.0
    vehicle_type: str = VehicleTypes.car


@dataclass
class Motorcycle(Vehicle):
    vehicle_number: str = ""
    enter_time: float = 0.0
    exit_time: float = 0.0
    vehicle_type: str = VehicleTypes.motorcycle


"""
Vehicle factory.
"""


class Factory:
    _vehicles: dict = {}

    def register_vehicle(self, key: str, vehicle: Callable) -> None:
        self._vehicles[key] = vehicle

    def build(
        self, vehicle_type: str, vehicle_number: str, enter_time: float
    ) -> Vehicle:
        if vehicle_type not in self._vehicles.keys():
            raise ValueError(f"Invalid vehicle type: {vehicle_type}")
        return self._vehicles[vehicle_type](vehicle_number, enter_time)


vehicle_factory: Factory = Factory()
vehicle_factory.register_vehicle(VehicleTypes.motorcycle, Motorcycle)
vehicle_factory.register_vehicle(VehicleTypes.car, Car)

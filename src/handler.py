"""
src.handler
~~~~~~~~~~~

This module contains functions that handle the parking lot events.
"""

from typing import Dict, List, Optional

from src.constants import Actions, VehicleTypes
from src.models.parking_lot import ParkingLot, ParkingMeter
from src.models.vehicle import Vehicle, vehicle_factory


class Handler:
    parking_lot: ParkingLot
    enter_output_str: str = "Accept {lot_id}"
    exit_output_str: str = "{lot_id} {fee}"

    def init_parking_lot(self, input: List[str]) -> None:
        capacity: Dict[str, int] = {VehicleTypes.car: 0, VehicleTypes.motorcycle: 0}
        if len(input) > 0:
            capacity[VehicleTypes.car] = int(input[0])
        if len(input) > 1:
            capacity[VehicleTypes.motorcycle] = int(input[1])
        self.parking_lot = ParkingLot(capacity)
        self.parking_lot.init_lots()

    def handle(self, input: List[str]) -> str:
        if len(input) < 1:
            raise ValueError("Missing inputs")

        if input[0] == Actions.enter:
            return self._handle_enter(input)
        elif input[0] == Actions.exit:
            return self._handle_exit(input)
        else:
            raise ValueError(f"Unsupported Action: {input[0]}")

    def _handle_enter(self, input: List[str]) -> str:
        if len(input) < 4:
            raise ValueError("Missing inputs for 'Enter' event")
        if len(input) > 4:
            raise ValueError("Excessive inputs for 'Enter' event")

        vehicle: Optional[Vehicle] = None
        vehicle = vehicle_factory.build(
            vehicle_type=input[1], vehicle_number=input[2], enter_time=float(input[3])
        )

        lot_id: Optional[str] = self.parking_lot.get_avail_lot(input[1])
        if not lot_id:
            raise Exception(
                f"No lots availble for vehicle type: {input[1]}, "
                f"turning away car: {input[2]}"
            )
        self.parking_lot.enter(vehicle, lot_id)
        return self.enter_output_str.format(lot_id=lot_id)

    def _handle_exit(self, input: List[str]) -> str:
        if len(input) < 3:
            raise ValueError("Missing inputs for 'Exit' event")
        if len(input) > 3:
            raise ValueError("Excessive inputs for 'Exit' event")

        vehicle, lot_id = self.parking_lot.exit(input[1], float(input[2]))
        fee: float = ParkingMeter.calc_fees(vehicle)
        return self.exit_output_str.format(lot_id=lot_id, fee=fee)

from typing import Dict, List
from unittest import TestCase

from src.models.parking_lot import ParkingLot


class TestParkingLot(TestCase):
    def test_init_parking_lot(self):
        mock_input1: Dict[str, int] = {"motorcycle": 2, "car": 1}
        mock_input2: Dict[str, int] = {"motorcycle": 0, "car": 1}
        mock_input3: Dict[str, int] = {"motorcycle": 4, "car": 2}
        mock_input4: Dict[str, int] = {"motorcycle": 0, "car": 0}
        expected_capacity1: Dict[str, List[str]] = {
            "motorcycle": ["motorcycleLot1", "motorcycleLot2"],
            "car": ["carLot1"],
        }
        expected_capacity2: Dict[str, List[str]] = {
            "motorcycle": [],
            "car": ["carLot1"],
        }
        expected_capacity3: Dict[str, List[str]] = {
            "motorcycle": [
                "motorcycleLot1",
                "motorcycleLot2",
                "motorcycleLot3",
                "motorcycleLot4",
            ],
            "car": ["carLot1", "carLot2"],
        }
        expected_capacity4: Dict[str, List[str]] = {"motorcycle": [], "car": []}

        parking_lot1: ParkingLot = ParkingLot(mock_input1)
        parking_lot1.init_lots()
        assert parking_lot1.capacity["motorcycle"] == expected_capacity1["motorcycle"]
        assert parking_lot1.capacity["car"] == expected_capacity1["car"]
        parking_lot2: ParkingLot = ParkingLot(mock_input2)
        parking_lot2.init_lots()
        assert parking_lot2.capacity["motorcycle"] == expected_capacity2["motorcycle"]
        assert parking_lot2.capacity["car"] == expected_capacity2["car"]
        parking_lot3: ParkingLot = ParkingLot(mock_input3)
        parking_lot3.init_lots()
        assert parking_lot3.capacity["motorcycle"] == expected_capacity3["motorcycle"]
        assert parking_lot3.capacity["car"] == expected_capacity3["car"]
        parking_lot4: ParkingLot = ParkingLot(mock_input4)
        parking_lot4.init_lots()
        assert parking_lot4.capacity["motorcycle"] == expected_capacity4["motorcycle"]
        assert parking_lot4.capacity["car"] == expected_capacity4["car"]

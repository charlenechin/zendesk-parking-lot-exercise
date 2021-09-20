from typing import Dict, List
from unittest import TestCase
from unittest.mock import patch

import pytest

from src.handler import Handler


class TestHandler(TestCase):
    def setUp(self):
        self.handler: Handler = Handler()
        self.mock_init: List[str] = ["1", "3"]
        self.handler.init_parking_lot(self.mock_init)

    def test_init_parking_lot(self):
        mock_input1: List[str] = ["1", "2"]
        mock_input2: List[str] = ["1"]
        mock_input3: List[str] = ["2", "4", "3"]
        mock_input4: List[str] = []
        expected_output1: Dict[str, int] = {"motorcycle": 2, "car": 1}
        expected_output2: Dict[str, int] = {"motorcycle": 0, "car": 1}
        expected_output3: Dict[str, int] = {"motorcycle": 4, "car": 2}
        expected_output4: Dict[str, int] = {"motorcycle": 0, "car": 0}

        self.handler.init_parking_lot(mock_input1)
        assert self.handler.parking_lot.init_capacity == expected_output1
        self.handler.init_parking_lot(mock_input2)
        assert self.handler.parking_lot.init_capacity == expected_output2
        self.handler.init_parking_lot(mock_input3)
        assert self.handler.parking_lot.init_capacity == expected_output3
        self.handler.init_parking_lot(mock_input4)
        assert self.handler.parking_lot.init_capacity == expected_output4

    @patch("src.models.parking_lot.ParkingLot")
    def test_handle(self, mock_parking_lot):
        mock_inval1: List[str] = ["motorcycle", "SGX1234A", "1613541902"]
        mock_inval2: List[str] = ["Enter", "motorcycle", "SGX1234A"]
        mock_inval3: List[str] = ["Exit", "SGX1234A"]
        mock_input1: List[str] = ["Enter", "motorcycle", "SGX1234A", "1613541902"]
        mock_input2: List[str] = ["Enter", "motorcycle", "SGX1234B", "1613541903"]
        mock_input3: List[str] = ["Exit", "SGX1234A", "1613545602"]
        mock_input4: List[str] = ["Enter", "car", "SGX1235B", "1613541902"]
        mock_input5: List[str] = ["Enter", "car", "SGX1236C", "1613541905"]
        expected_inval1: str = f"Unsupported Action: {mock_inval1[0]}"
        expected_inval2: str = "Missing inputs for 'Enter' event"
        expected_inval3: str = "Missing inputs for 'Exit' event"
        expected_output1: str = "Accept motorcycleLot1"
        expected_output2: str = "Accept motorcycleLot2"
        expected_output3: str = "motorcycleLot1 2"
        expected_output4: str = "Accept carLot1"
        expected_output5: str = (
            f"No lots availble for vehicle type: car, "
            f"turning away car: {mock_input5[2]}"
        )

        with pytest.raises(ValueError) as err:
            self.handler.handle(mock_inval1)
        assert str(err.value) == expected_inval1

        with pytest.raises(ValueError) as err:
            self.handler.handle(mock_inval2)
        assert str(err.value) == expected_inval2

        with pytest.raises(ValueError) as err:
            self.handler.handle(mock_inval3)
        assert str(err.value) == expected_inval3

        assert self.handler.handle(mock_input1) == expected_output1
        assert self.handler.handle(mock_input2) == expected_output2
        assert self.handler.handle(mock_input3) == expected_output3
        assert self.handler.handle(mock_input4) == expected_output4
        with pytest.raises(Exception) as err:
            self.handler.handle(mock_input5)
        assert str(err.value) == expected_output5

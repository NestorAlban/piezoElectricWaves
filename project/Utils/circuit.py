import numpy as np
from typing import List

class Circuit:
    def __init__(
        self, 
        arrTime: np.ndarray,
        nResistance: float,
        nCapacitance: float 
    ) -> None:
        self.arrTime: np.ndarray = arrTime
        self.nResistance: float = nResistance
        self.nCapacitance: float = nCapacitance
        self.nMaxVoltage: float = 0.00
        
    def capacitorChargeNoRegulated(self, arrVoltage: np.ndarray) -> np.ndarray:
        time_constant = self.nResistance * self.nCapacitance
        return arrVoltage * (1 - np.exp(-self.arrTime / time_constant))

    def capacitorCharge(self, arrVoltage: np.ndarray) -> np.ndarray:
        self.nMaxVoltage = 0.00
        nRCValue: float = self.nResistance * self.nCapacitance
        arrChargeResponse = np.zeros_like(arrVoltage)

        for i, nVoltage in enumerate(arrVoltage):
            nChargeVoltage: float = nVoltage * (1 - np.exp(-self.arrTime[i] / nRCValue))
            if nChargeVoltage > self.nMaxVoltage:
                self.nMaxVoltage = nChargeVoltage
                arrChargeResponse[i] = nChargeVoltage
            else:  
                arrChargeResponse[i] = self.nMaxVoltage

        return arrChargeResponse


    
import numpy as np
import random
from typing import List, Tuple
from .waves import Waves


class Circuit:
    def __init__(
        self, 
        arrTime: np.ndarray,
        nAmplitude: float,
        nFrequency: float
    ) -> None:
        try:
            if not isinstance(arrTime, np.ndarray):
                raise TypeError("El argumento 'arrTime' debe ser de tipo 'np.ndarray'")
            if not isinstance(nAmplitude, float):
                raise TypeError("El argumento 'nAmplitude' debe ser de tipo 'float'")
            if not isinstance(nFrequency, float):
                raise TypeError("El argumento 'nFrequency' debe ser de tipo 'float'")

            self.arrTime: np.ndarray = arrTime
            self.nMaxVoltage: float = 0.00
            self.nAmplitude: float = nAmplitude
            self.nFrequency: float = nFrequency
        except Exception as err:
            raise err
        
    def capacitorChargeNoRegulated(self, nResistance: float, nCapacitance: float, arrVoltage: np.ndarray) -> np.ndarray:
        time_constant = nResistance * nCapacitance
        return arrVoltage * (1 - np.exp(-self.arrTime / time_constant))

    def capacitorCharge(self, nResistance: float, nCapacitance: float, arrVoltage: np.ndarray) -> np.ndarray:
        self.nMaxVoltage = 0.00
        nRCValue: float = nResistance * nCapacitance
        arrChargeResponse = np.zeros_like(arrVoltage)

        for i, nVoltage in enumerate(arrVoltage):
            nChargeVoltage: float = nVoltage * (1 - np.exp(-self.arrTime[i] / nRCValue))
            if nChargeVoltage > self.nMaxVoltage:
                self.nMaxVoltage = nChargeVoltage
                arrChargeResponse[i] = nChargeVoltage
            else:  
                arrChargeResponse[i] = self.nMaxVoltage

        return arrChargeResponse

    def createSerialPiezoElectricGroup(
        self, arrStepsWave: np.ndarray, 
        nPiezoAmount: int, lstResistance: List[float], 
        lstAmplitudeMinMax: List[float], lstFrequencyMinMax: List[float]
    ) -> Tuple[List[np.ndarray], np.ndarray, List[float], float]:
        # Validación de datos
        if not isinstance(arrStepsWave, np.ndarray):
            raise TypeError("arrStepsWave debe ser de tipo np.ndarray")
        if not isinstance(nPiezoAmount, int):
            raise TypeError("nPiezoAmount debe ser de tipo int")
        if not isinstance(lstResistance, List):
            raise TypeError("lstResistance debe ser de tipo List[float]")
        if not isinstance(lstAmplitudeMinMax, List):
            raise TypeError("lstAmplitudeMinMax debe ser de tipo List[float]")
        if not isinstance(lstFrequencyMinMax, List):
            raise TypeError("lstFrequencyMinMax debe ser de tipo List[float]")
        
        # Igualar lstResistance a la cantidad de piezoelectricos
        while len(lstResistance) < nPiezoAmount:
            lstResistance += lstResistance
        lstResistance = lstResistance[:nPiezoAmount]

        clsWavesInstance = Waves(self.arrTime)
        lstPiezoWaves: List[np.ndarray] = []
        arrTotalVoltage: np.ndarray = None
        nFinalResistance: float = 0.00

        # Evaluar Resistencia
        nResistancesSum: float = sum(lstResistance)
        if not isinstance(nResistancesSum, float):
            raise TypeError("Error con la variable nResistancesSum")
        nFinalResistance = nResistancesSum

        for nPiezoIndex in range(nPiezoAmount):
            # Generar valores aleatorios para la amplitud y la frecuencia
            nAmplitudeVariaton: float = round(random.uniform(lstAmplitudeMinMax[0], lstAmplitudeMinMax[1]), 4)
            nFrequencyVariation: float = round(random.uniform(lstFrequencyMinMax[0], lstFrequencyMinMax[1]), 4)
            # Crear el piezoelectrico y agregarlo a la lista
            arrPiezoWave = clsWavesInstance.sinWaveNoPhaseCreator(self.nAmplitude * nAmplitudeVariaton, self.nFrequency * nFrequencyVariation) + arrStepsWave
            lstPiezoWaves.append(arrPiezoWave)

        arrTotalVoltage = np.sum(np.abs(lstPiezoWaves), axis=0)

        return (lstPiezoWaves, arrTotalVoltage, lstResistance, nFinalResistance)


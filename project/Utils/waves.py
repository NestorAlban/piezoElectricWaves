import numpy as np
from typing import List

class Waves:
    def __init__(self, arrTime: np.ndarray) -> None:
        try:
            if not isinstance(arrTime, np.ndarray):
                raise TypeError("El argumento 'arrTime' debe ser de tipo 'np.ndarray'")

            self.arrTime: np.ndarray = arrTime
        except Exception as err:
            raise err


    def sinWaveNoPhaseCreator(
        self,
        nAmplitude: float, 
        nFrequency: float
    ) -> np.ndarray:
        if not (isinstance(nAmplitude, float) or isinstance(nFrequency, float)):
            raise TypeError("Existen incongruencias con el tipo de las variables")
        arrWave: np.ndarray = nAmplitude * np.sin(2* np.pi* nFrequency * self.arrTime)
        return arrWave
    
    def sinWaveCreator(
        self,
        nAmplitude: float, 
        nFrequency: float,
        nPhase: float
    ) -> np.ndarray:
        if not (isinstance(nAmplitude, float) or isinstance(nFrequency, float) or isinstance(nPhase, float)):
            raise TypeError("Existen incongruencias con el tipo de las variables")
        arrWave: np.ndarray = nAmplitude * np.sin(2* np.pi* nFrequency * self.arrTime + nPhase)
        return arrWave
    
    def cosWaveNoPhaseCreator(
        self,
        nAmplitude: float, 
        nFrequency: float
    ) -> np.ndarray:
        if not (isinstance(nAmplitude, float) or isinstance(nFrequency, float)):
            raise TypeError("Existen incongruencias con el tipo de las variables")
        arrWave: np.ndarray = nAmplitude * np.cos(2* np.pi* nFrequency * self.arrTime)
        return arrWave

    def cosWaveCreator(
        self,
        nAmplitude: float, 
        nFrequency: float,
        nPhase: float
    ) -> np.ndarray:
        if not (isinstance(nAmplitude, float) or isinstance(nFrequency, float) or isinstance(nPhase, float)):
            raise TypeError("Existen incongruencias con el tipo de las variables")
        arrWave: np.ndarray = nAmplitude * np.cos(2* np.pi* nFrequency * self.arrTime + nPhase)
        return arrWave






import numpy as np
from typing import List

class Waves:
    def __init__(self, arrTime: np.ndarray) -> None:
        self.arrTime: np.ndarray = arrTime
        pass

    def sinWaveNoPhaseCreator(
        self,
        nAmplitude: float, 
        nFrequency: float
    ) -> np.ndarray:
        arrWave: np.ndarray = nAmplitude * np.sin(2* np.pi* nFrequency * self.arrTime)
        return arrWave
    
    def sinWaveCreator(
        self,
        nAmplitude: float, 
        nFrequency: float,
        nPhase: float
    ) -> np.ndarray:
        arrWave: np.ndarray = nAmplitude * np.sin(2* np.pi* nFrequency * self.arrTime + nPhase)
        return arrWave
    
    def cosWaveNoPhaseCreator(
        self,
        nAmplitude: float, 
        nFrequency: float
    ) -> np.ndarray:
        arrWave: np.ndarray = nAmplitude * np.cos(2* np.pi* nFrequency * self.arrTime)
        return arrWave

    def cosWaveCreator(
        self,
        nAmplitude: float, 
        nFrequency: float,
        nPhase: float
    ) -> np.ndarray:
        arrWave: np.ndarray = nAmplitude * np.cos(2* np.pi* nFrequency * self.arrTime + nPhase)
        return arrWave






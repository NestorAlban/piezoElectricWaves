import numpy as np
import sys
import os
# print(sys.path)
# parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(parent_dir)
# from project.Utils.plotter import PiezoPlotter
# from project.Utils.waves import Waves
from Utils.plotter import PiezoPlotter
from Utils.waves import Waves
from Utils.circuit import Circuit


if __name__ == "__main__":
    
    """ Parameters Definition """
    # Variables
    nAmplitude: float = 16.0
    nFrequency: float = 1.0
    nPhase: float = 0.0
    nInitTime: float = 0.0
    nFinalTime: float = 10.0
    nPointsNum: int = 1000

    # Init Time
    arrTime: np.ndarray = np.linspace(nInitTime, nFinalTime, nPointsNum)

    # Classes calling
    clsWaves = Waves(arrTime)
    clsPlotter = PiezoPlotter(arrTime)


    """ Main Waves """
    # First Waves
    arrCleanSteps: np.ndarray = clsWaves.sinWaveCreator(nAmplitude*1.1, nFrequency, nPhase)
    arrFirstDeform: np.ndarray = clsWaves.sinWaveCreator(nAmplitude*0.125, nFrequency*7, np.pi/2)

    arrStepsFrtDeform: np.ndarray = arrCleanSteps + arrFirstDeform

    clsPlotter.graphWaves([arrCleanSteps, arrFirstDeform, arrStepsFrtDeform])

    # Real Steps
    arrSecondDeform: np.ndarray = clsWaves.sinWaveNoPhaseCreator(nAmplitude*0.02, nFrequency*7)

    arrRealSteps: np.ndarray = arrStepsFrtDeform + arrSecondDeform

    clsPlotter.graphWaves([arrStepsFrtDeform, arrSecondDeform, arrRealSteps])

    # Piezo Waves
    arrPiezo1: np.ndarray = clsWaves.sinWaveNoPhaseCreator(nAmplitude*0.08, nFrequency*7.2) + arrRealSteps
    arrPiezo2: np.ndarray = clsWaves.sinWaveNoPhaseCreator(nAmplitude*0.05, nFrequency*7.9) + arrRealSteps

    clsPlotter.graphWaves([arrRealSteps, arrPiezo1, arrPiezo2])

    # Max Voltage
    arrMaxV: np.ndarray = np.maximum(np.abs(arrPiezo1), np.abs(arrPiezo2))

    clsPlotter.graphWaves([arrMaxV, np.abs(arrPiezo1), np.abs(arrPiezo2)])
    
    """ Capacitor """
    # Charge
    nResistance: float = 500.00 * 10**3
    nCapacitance: float = 1000.00 * 10**(-6)

    clsCircuit = Circuit(arrTime, nResistance, nCapacitance)

    arrChargeVolt: np.ndarray = clsCircuit.capacitorCharge(arrMaxV)
    arrChargeVoltNR: np.ndarray = clsCircuit.capacitorChargeNoRegulated(arrMaxV)

    clsPlotter.graphWaves([arrChargeVolt, arrChargeVoltNR])
    pass


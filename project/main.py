import numpy as np
import sys
import os
from typing import List, Tuple
# print(sys.path)
# parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(parent_dir)
# from project.Utils.plotter import PiezoPlotter
# from project.Utils.waves import Waves
from Utils.plotter import PiezoPlotter
from Utils.waves import Waves
from Utils.circuit import Circuit


if __name__ == "__main__":
    try:
        """ Parameters Definition """
        ## Variables
        nAmplitude: float = 16.0
        nFrequency: float = 1.0
        nPhase: float = 0.0
        nInitTime: float = 0.0
        nFinalTime: float = 3500.0
        nPointsNum: int = 10000

        ## Init Time
        arrTime: np.ndarray = np.linspace(nInitTime, nFinalTime, nPointsNum)

        if not isinstance(arrTime, np.ndarray):
            raise TypeError("El argumento 'arrTime' debe ser de tipo 'np.ndarray'")
        
        ## Classes calling
        clsWaves = Waves(arrTime)
        clsPlotter = PiezoPlotter(arrTime)


        """ Main Waves """
        ## First Waves
        arrCleanSteps: np.ndarray = clsWaves.sinWaveCreator(nAmplitude*1.1, nFrequency, nPhase)
        arrFirstDeform: np.ndarray = clsWaves.sinWaveCreator(nAmplitude*0.125, nFrequency*7, np.pi/2)

        arrStepsFrtDeform: np.ndarray = arrCleanSteps + arrFirstDeform

        # clsPlotter.graphWaves([arrCleanSteps, arrFirstDeform, arrStepsFrtDeform])

        ## Real Steps
        arrSecondDeform: np.ndarray = clsWaves.sinWaveNoPhaseCreator(nAmplitude*0.02, nFrequency*7)

        arrRealSteps: np.ndarray = arrStepsFrtDeform + arrSecondDeform

        # clsPlotter.graphWaves([arrStepsFrtDeform, arrSecondDeform, arrRealSteps])

        ## Creación de grupos
        clsCircuit = Circuit(arrTime, nAmplitude, nFrequency)
        cRutaGuardado: str = "../tests/20240411"
        cNombreGuardado: str = "test1_"
        nPiezoAmount: int = 3
        lstResistance: List[float] = [500.00 * 10**3]
        lstAmplitudeMinMax: List[float] = [0.04, 0.1]
        lstFrequencyMinMax: List[float] = [7.2, 7.9]

        tplSerialPiezoGroup = clsCircuit.createSerialPiezoElectricGroup(arrRealSteps, nPiezoAmount, lstResistance, lstAmplitudeMinMax, lstFrequencyMinMax)

        lstPiezoWaves: List[np.ndarray] = tplSerialPiezoGroup[0]
        arrTotalVoltage: np.ndarray = tplSerialPiezoGroup[1]
        lstResistanceF: List[float] = tplSerialPiezoGroup[2]
        nFinalResistance: float = tplSerialPiezoGroup[3]

        clsPlotter.graphWaves(lstPiezoWaves, lGuardar= True, cRuta=cRutaGuardado, cNombre=cNombreGuardado+"lst")
        
        clsPlotter.graphWaves([arrTotalVoltage], lGuardar= True, cRuta=cRutaGuardado, cNombre=cNombreGuardado+"tot")
        pass
    except Exception as errMain:
        raise errMain



    # # Piezo Waves
    # arrPiezo1: np.ndarray = clsWaves.sinWaveNoPhaseCreator(nAmplitude*0.08, nFrequency*7.2) + arrRealSteps
    # arrPiezo2: np.ndarray = clsWaves.sinWaveNoPhaseCreator(nAmplitude*0.05, nFrequency*7.9) + arrRealSteps

    # # clsPlotter.graphWaves([arrRealSteps, arrPiezo1, arrPiezo2])

    # # Max Voltage
    # arrMaxVPar: np.ndarray = np.maximum(np.abs(arrPiezo1), np.abs(arrPiezo2))
    # arrMaxVSer: np.ndarray = np.abs(arrPiezo1) + np.abs(arrPiezo2)
    # clsPlotter.graphWaves([arrMaxVSer, arrMaxVPar, np.abs(arrPiezo1), np.abs(arrPiezo2)])
    
    # """ Capacitor """
    # # 3 piezo electricos por grupo
    # # 5 grupos por capacitor
    # # Charge
    # nResistance: float = 500.00 * 10**3 *3/5
    # nCapacitance: float = 1000.00 * 10**(-6)
    # print(nResistance*nCapacitance)
    # clsCircuit = Circuit(arrTime, nResistance, nCapacitance)

    # arrChargeVoltPar: np.ndarray = clsCircuit.capacitorCharge(arrMaxVPar)
    # arrChargeVoltNRPar: np.ndarray = clsCircuit.capacitorChargeNoRegulated(arrMaxVPar)

    # arrChargeVoltSer: np.ndarray = clsCircuit.capacitorCharge(arrMaxVSer)
    # arrChargeVoltNRSer: np.ndarray = clsCircuit.capacitorChargeNoRegulated(arrMaxVSer)

    # clsPlotter.graphWaves([arrChargeVoltPar, arrChargeVoltNRPar, arrChargeVoltSer, arrChargeVoltNRSer])
    pass


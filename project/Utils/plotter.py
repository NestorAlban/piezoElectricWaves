import numpy as np
from matplotlib import pyplot as plt
from typing import List

class PiezoPlotter:
    def __init__(self, arrTime: np.ndarray) -> None:
        try:
            if not isinstance(arrTime, np.ndarray):
                raise TypeError("El argumento 'arrTime' debe ser de tipo 'np.ndarray'")

            self.arrTime: np.ndarray = arrTime
        except Exception as err:
            raise err

    def graphWaves(
        self,
        lstWaves: List[np.ndarray], 
        lBlock: bool = True,
        lGuardar: bool = False,
        cRuta: str = "",
        cNombre: str = ""
    ) -> None:
        nWavesNum: int = len(lstWaves)
        nRows: int = nWavesNum

        plt.figure(figsize = (10, 2*nRows))

        for i, wave in enumerate(lstWaves, start=1):
            plt.subplot(nRows, 1, i)
            plt.plot(self.arrTime, wave, 'r')
            plt.title(f'Onda {i}')
            plt.xlabel('Tiempo (s)')
            plt.ylabel('Amplitud')
            plt.grid(True)

        plt.tight_layout()
        if lGuardar:
            if cRuta != "" and cNombre != "" :
                plt.savefig(cRuta+"/"+cNombre)
                plt.close()
            pass
        else:
            plt.show(block = lBlock)

    def graphWavesWithNames(
        self,
        lstWaves: List[np.ndarray], 
        lstNames: List[str], 
        lBlock: bool = True
    ) -> None:
        nWavesNum: int = len(lstWaves)
        nRows: int = nWavesNum

        plt.figure(figsize = (10, 2*nRows))

        for i, wave in enumerate(lstWaves, start=1):
            plt.subplot(nRows, 1, i)
            plt.plot(self.arrTime, wave)
            plt.title(f'Onda {lstNames[i]}')
            plt.xlabel('Tiempo (s)')
            plt.ylabel('Amplitud')
            plt.grid(True)

        plt.tight_layout()
        plt.show(block = lBlock)




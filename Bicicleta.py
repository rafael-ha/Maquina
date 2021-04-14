import Fuerza
from Desplazable import Desplazable
from MaquinaMecanica import MaquinaMecanica

class Bicicleta(MaquinaMecanica,Desplazable):
    DEFAULT_RADIO_RUEDA = 33.0
    MIN_RADIO_RUEDA = 17.75
    MAX_RADIO_RUEDA = 36.85
    MAX_DESPLAZAMIENTO = 200

    def __init__(self, marca: str, modelo: str, radioRueda=None, fuerzaMotriz=Fuerza.Fuerza.Animal):
        super().__init__(marca, modelo, fuerzaMotriz)
        self._radioRueda: float = Bicicleta.DEFAULT_RADIO_RUEDA if radioRueda is None else radioRueda
        self._totalKilometros: float = 0

    def desplazar(self, kilometros: float):
        super().desplazar(kilometros)

    def getTotalKilometrosRecorridos(self) -> float:
        return super().getTotalKilometrosRecorridos()

    def getKilometrosSinRepostar(self) -> float:
        return super().getKilometrosSinRepostar()

    @property
    def __str__(self) -> str:
        tmp_str=super().__str__()
        tmp_str = tmp_str[:-1] + f"Radio: {self._radioRueda}; Kilometros: {self.getTotalKilometrosRecorridos()}"
        return tmp_str

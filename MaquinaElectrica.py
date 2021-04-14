import Maquina


class MaquinaElectrica(Maquina):
    MIN_VOLTAJE: int = 10
    MAX_VOLTAJE: int = 400
    DEFAULT_VOLTAJE: int = MIN_VOLTAJE
    MIN_POTENCIA_ELECTRICA: float = 700.00
    MAX_POTENCIA_ELECTRICA: float = 200_000.00
    DEFAULT_POTENCIA_ELECTRICA: float = MIN_POTENCIA_ELECTRICA

    def __init__(self, marca: str, modelo: str, voltaje=None, potenciaElectrica=None):
        super().__init(marca, modelo)
        self._voltaje: int = MaquinaElectrica.MIN_VOLTAJE if voltaje is not None else voltaje
        self._potenciaElectrica: float = MaquinaElectrica.MIN_POTENCIA_ELECTRICA if potenciaElectrica is not None else potenciaElectrica


    def getVoltaje(self):
        return self._voltaje

    def getPotenciaElectrica(self):
        return self._potenciaElectrica


    def __str__(self) -> str:
        tmp_str = super().__str__()
        tmp_str = tmp_str[:-1] + f" Voltaje: {self._voltaje}; Potencia: {self._potenciaElectrica};"
        return tmp_str

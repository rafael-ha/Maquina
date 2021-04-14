class Maquina(object):
    cantidadDeMaquinasFabricadas: int = 0

    def __init__(self, marca: str, modelo: str):
        self._marca: str = marca
        self._modelo: str = modelo
        self._numeroSerie: int = 0

    def getMarca(self) -> str:
        return self._marca

    def getModelo(self) -> str:
        return self._modelo

    def getnumeroSerie(self) -> int:
        return self._numeroSerie

    def getCantidadDeMaquinasFabricadas(self) -> int:
        return Maquina.__cantidadDeMaquinasFabricadas

    def __str__(self) -> str:
        tmp_str = f"{{ Marca: {self._marca}; modelo: {self._modelo}; NS: {self._numeroSerie} }}"
        return tmp_str

from Maquina import Maquina
from Fuerza import Fuerza


class MaquinaMecanica(Maquina):

    def __init__(self, marca: str, modelo: str, fuerzaMotriz=Fuerza.Combustible):
        super().__init__(marca, modelo)
        self._fuerzaMotriz = fuerzaMotriz

    def getFuerzaMotriz(self):
        return self._fuerzaMotriz

    @property
    def __str__(self) -> str:
        tmp_str = super().__str__()
        tmp_str = tmp_str[:-1] + f" fuerza motriz:{self._fuerzaMotriz.Combustible.name} }}"
        return tmp_str

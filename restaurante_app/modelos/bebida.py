from modelos.producto import Producto


class Bebida(Producto):
    """
    Clase que representa una bebida del restaurante.
    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamano: str,
        envase: str,
    ):
        super().__init__(codigo, nombre, categoria, precio)

        self.__tamano = tamano
        self.__envase = envase

    @property
    def tamano(self):
        return self.__tamano

    @property
    def envase(self):
        return self.__envase

    def mostrar_informacion(self) -> str:
        return (
            super().mostrar_informacion()
            + f"\nTamaño: {self.tamano}"
            + f"\nEnvase: {self.envase}"
        )
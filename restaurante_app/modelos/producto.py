class Producto:
    """
    Clase base que representa un producto del restaurante.
    """

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio

    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def categoria(self) -> str:
        return self.__categoria

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio: float):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo}\n"
            f"Nombre: {self.nombre}\n"
            f"Categoría: {self.categoria}\n"
            f"Precio: ${self.precio:.2f}"
        )
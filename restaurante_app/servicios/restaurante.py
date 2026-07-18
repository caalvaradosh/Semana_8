from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """
    Servicio encargado de administrar productos y clientes.
    """

    def __init__(self):
        self.__productos: list[Producto] = []
        self.__clientes: list[Cliente] = []

    # ==================================
    # VALIDACIONES
    # ==================================

    def existe_codigo(self, codigo: str) -> bool:
        for producto in self.__productos:
            if producto.codigo == codigo:
                return True
        return False

    def existe_cliente(self, identificacion: str) -> bool:
        for cliente in self.__clientes:
            if cliente.identificacion == identificacion:
                return True
        return False

    # ==================================
    # PRODUCTOS
    # ==================================

    def registrar_producto(self, producto: Producto) -> bool:

        if self.existe_codigo(producto.codigo):
            return False

        self.__productos.append(producto)
        return True

    def listar_productos(self) -> None:

        if not self.__productos:
            print("\nNo existen productos registrados.")
            return

        print("\n=========== PRODUCTOS ===========\n")

        for producto in self.__productos:
            print(producto.mostrar_informacion())
            print("-" * 40)

    # ==================================
    # CLIENTES
    # ==================================

    def registrar_cliente(self, cliente: Cliente) -> bool:

        if self.existe_cliente(cliente.identificacion):
            return False

        self.__clientes.append(cliente)
        return True

    def listar_clientes(self) -> None:

        if not self.__clientes:
            print("\nNo existen clientes registrados.")
            return

        print("\n=========== CLIENTES ===========\n")

        for cliente in self.__clientes:
            print(cliente.mostrar_informacion())
            print("-" * 40)

    # ==================================
    # PROPIEDADES
    # ==================================

    @property
    def productos(self):
        return self.__productos

    @property
    def clientes(self):
        return self.__clientes
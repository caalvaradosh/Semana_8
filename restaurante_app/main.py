from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def mostrar_menu():
    print("\n" + "=" * 45)
    print("        SISTEMA DEL RESTAURANTE EL BAMBÚ")
    print("=" * 45)
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("-" * 45)
    print("4. Listar productos")
    print("5. Listar clientes")
    print("-" * 45)
    print("6. Salir")
    print("=" * 45)


def leer_precio():
    while True:
        try:
            precio = float(input("Precio: $"))
            if precio <= 0:
                print("El precio debe ser mayor que cero.")
            else:
                return precio
        except ValueError:
            print("Ingrese un valor numérico válido.")


def registrar_producto(restaurante):
    print("\nREGISTRO DE PRODUCTO")

    codigo = input("Código: ")
    nombre = input("Nombre: ")
    categoria = input("Categoría: ")
    precio = leer_precio()

    producto = Producto(
        codigo,
        nombre,
        categoria,
        precio
    )

    if restaurante.registrar_producto(producto):
        print("\nProducto registrado correctamente.")
    else:
        print("\nYa existe un producto con ese código.")


def registrar_bebida(restaurante):
    print("\nREGISTRO DE BEBIDA")

    codigo = input("Código: ")
    nombre = input("Nombre: ")
    categoria = input("Categoría: ")
    precio = leer_precio()

    tamano = input("Tamaño: ")
    envase = input("Tipo de envase: ")

    bebida = Bebida(
        codigo,
        nombre,
        categoria,
        precio,
        tamano,
        envase
    )

    if restaurante.registrar_producto(bebida):
        print("\nBebida registrada correctamente.")
    else:
        print("\nYa existe un producto con ese código.")


def registrar_cliente(restaurante):
    print("\nREGISTRO DE CLIENTE")

    identificacion = input("Identificación: ")
    nombre = input("Nombre: ")
    correo = input("Correo: ")

    cliente = Cliente(
        identificacion,
        nombre,
        correo
    )

    if restaurante.registrar_cliente(cliente):
        print("\nCliente registrado correctamente.")
    else:
        print("\nLa identificación ya está registrada.")


def ejecutar():
    restaurante = Restaurante()

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            registrar_producto(restaurante)

        elif opcion == "2":

            registrar_bebida(restaurante)

        elif opcion == "3":

            registrar_cliente(restaurante)

        elif opcion == "4":

            restaurante.listar_productos()

        elif opcion == "5":

            restaurante.listar_clientes()

        elif opcion == "6":

            print("\nGracias por utilizar el sistema.")
            print("Hasta pronto.")
            break

        else:

            print("\nOpción incorrecta.")


if __name__ == "__main__":
    ejecutar()
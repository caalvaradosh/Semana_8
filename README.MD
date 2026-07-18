# Sistema de Restaurante - Programación Orientada a Objetos

## Información del estudiante

**Nombre:** Clide Alcides Alvarado Shiguango

**Asignatura:** Programación Orientada a Objetos

**Semana:** 8

**Actividad:** Aplicación de principios SOLID en un proyecto Python modular

---

# Descripción del proyecto

El proyecto **restaurante_app** es una aplicación desarrollada en Python que permite administrar productos, bebidas y clientes de un restaurante mediante un menú interactivo por consola.

El sistema fue diseñado aplicando Programación Orientada a Objetos y una arquitectura modular, utilizando clases independientes para representar cada entidad del dominio y un servicio encargado de administrar la lógica del sistema.

---

# Estructura del proyecto

```
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
│
└── README.md
```

---

# Responsabilidad de cada clase

## Producto

Representa un producto general del restaurante.

Contiene:

- código
- nombre
- categoría
- precio

Además implementa el método:

```
mostrar_informacion()
```

---

## Bebida

Hereda de Producto.

Añade información específica:

- tamaño
- tipo de envase

Sobrescribe el método:

```
mostrar_informacion()
```

demostrando el uso del polimorfismo.

---

## Cliente

Representa la información de un cliente.

Contiene:

- identificación
- nombre
- correo

---

## Restaurante

Es la clase de servicio encargada de:

- registrar productos
- registrar bebidas
- registrar clientes
- validar códigos repetidos
- validar identificaciones repetidas
- listar productos
- listar clientes

---

## main.py

Es el punto de entrada del programa.

Se encarga únicamente de:

- mostrar el menú
- solicitar datos al usuario
- crear objetos
- llamar a los métodos del servicio

No administra directamente las listas del sistema.

---

# Relación entre Producto y Bebida

La clase **Bebida** hereda de **Producto**, ya que una bebida representa un tipo específico de producto.

Gracias a esta relación, los objetos Bebida pueden almacenarse junto con los productos en una misma colección y responder al método `mostrar_informacion()` mediante polimorfismo.

---

# Principios SOLID aplicados

## SRP (Single Responsibility Principle)

Cada clase posee una única responsabilidad.

- Producto representa productos.
- Bebida representa bebidas.
- Cliente representa clientes.
- Restaurante administra la información.
- main.py controla la interacción con el usuario.

---

## OCP (Open/Closed Principle)

El sistema puede ampliarse creando nuevas clases derivadas de Producto sin modificar la lógica del servicio Restaurante.

---

## LSP (Liskov Substitution Principle)

Los objetos Bebida pueden utilizarse como objetos Producto sin alterar el comportamiento del sistema.

Durante el listado de productos se ejecuta el mismo método:

```
mostrar_informacion()
```

independientemente del tipo de objeto.

---

# Requisitos del sistema

- Python 3.10 o superior

---

# Ejecución

Abrir una terminal dentro del proyecto y ejecutar:

```
python main.py
```

---

# Funcionalidades

El sistema permite:

- Registrar productos
- Registrar bebidas
- Registrar clientes
- Listar productos
- Listar clientes
- Validar códigos repetidos
- Validar clientes repetidos

---

# Reflexión

La organización modular facilita el mantenimiento del software, mejora la reutilización del código y permite ampliar el sistema sin afectar el funcionamiento existente.

La aplicación de los principios SOLID favorece el desarrollo de programas más organizados, escalables y fáciles de comprender, aspectos fundamentales en el desarrollo de aplicaciones orientadas a objetos.

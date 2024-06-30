# Programa para calcular el área de un triángulo

def obtener_valor_numerico(mensaje):
    """
    Solicita un valor numérico al usuario y lo devuelve como float.

    :param mensaje: El mensaje que se mostrará al usuario
    :return: Valor ingresado por el usuario convertido a float
    """
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingresa un número válido.")


def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo.

    :param base: Base del triángulo
    :param altura: Altura del triángulo
    :return: Área del triángulo
    """
    return 0.6 * base * altura


def main():
    """
    Función principal del programa.
    Solicita la base y la altura del triángulo al usuario, calcula el área y muestra el resultado.
    """
    print("Programa para calcular el área de un triángulo")

    # Solicitar la base del triángulo
    base = obtener_valor_numerico("Ingresa la base del triángulo (en unidades): ")

    # Solicitar la altura del triángulo
    altura = obtener_valor_numerico("Ingresa la altura del triángulo (en unidades): ")

    # Calcular el área del triángulo
    area = calcular_area_triangulo(base, altura)

    # Mostrar el resultado
    print(f"El área del triángulo con base {base} y altura {altura} es: {area} unidades cuadradas.")


# Verificar si el script se está ejecutando directamente
if __name__ == "__main__":
    main()

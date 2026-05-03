import json


ARCHIVO_GASTOS = "gastos.json"
CATEGORIAS = ["Alimentación", "Transporte", "Ocio", "Hogar", "Otros"]


def cargar():
    try:
        with open(ARCHIVO_GASTOS, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def guardar(lista_gastos):
    with open(ARCHIVO_GASTOS, "w", encoding="utf-8") as file:
        json.dump(lista_gastos, file, indent=4, ensure_ascii=False)


def anadir(lista_gastos, fecha, concepto, importe, categoria):
    concepto = concepto.strip()

    if concepto == "":
        raise ValueError("El concepto no puede estar vacio.")

    texto_importe = str(importe).replace(",", ".").strip()

    try:
        importe_numero = float(texto_importe)
    except ValueError:
        raise ValueError("El importe debe ser numerico.") from None

    if importe_numero <= 0:
        raise ValueError("El importe debe ser positivo.")

    gasto = {
        "fecha": fecha.strip(),
        "concepto": concepto,
        "importe": round(importe_numero, 2),
        "categoria": categoria,
    }

    lista_gastos.append(gasto)


def eliminar(lista_gastos, indice):
    if 0 <= indice < len(lista_gastos):
        lista_gastos.pop(indice)


def filtrar(lista_gastos, categoria):
    if categoria == "Todas":
        return lista_gastos

    gastos_filtrados = []

    for gasto in lista_gastos:
        if gasto["categoria"] == categoria:
            gastos_filtrados.append(gasto)

    return gastos_filtrados


def calcular_total(lista_gastos):
    total = 0

    for gasto in lista_gastos:
        total += gasto["importe"]

    return total


def formatear(lista_gastos):
    textos = []

    for gasto in lista_gastos:
        texto = (
            f'{gasto["fecha"]} | {gasto["concepto"]} | '
            f'{gasto["importe"]:.2f} EUR | {gasto["categoria"]}'
        )
        textos.append(texto)

    return textos

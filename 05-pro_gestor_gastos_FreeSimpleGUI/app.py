from datetime import date

import FreeSimpleGUI as sg

import gastos


def obtener_indices_mostrados(lista_gastos, categoria):
    indices = []

    for indice, gasto in enumerate(lista_gastos):
        if categoria == "Todas" or gasto["categoria"] == categoria:
            indices.append(indice)

    return indices


def actualizar_pantalla(window, lista_gastos, categoria):
    gastos_mostrados = gastos.filtrar(lista_gastos, categoria)
    textos = gastos.formatear(gastos_mostrados)
    total = gastos.calcular_total(gastos_mostrados)

    window["-LISTA-"].update(values=textos)
    window["-TOTAL-"].update(f"Total gastado: {total:.2f} EUR")

    return obtener_indices_mostrados(lista_gastos, categoria)


def main():
    lista_gastos = gastos.cargar()
    categorias_filtro = ["Todas"] + gastos.CATEGORIAS
    indice_seleccionado = None

    layout = [
        [
            sg.Text("Fecha (AAAA-MM-DD)"),
            sg.Input(default_text=date.today().isoformat(), size=(14, 1), key="-FECHA-"),
            sg.Text("Categoría"),
            sg.Combo(
                gastos.CATEGORIAS,
                default_value=gastos.CATEGORIAS[0],
                readonly=True,
                key="-CATEGORIA-",
            ),
        ],
        [
            sg.Text("Concepto"),
            sg.Input(expand_x=True, key="-CONCEPTO-"),
        ],
        [
            sg.Text("Importe"),
            sg.Input(size=(12, 1), key="-IMPORTE-"),
            sg.Button("Añadir"),
            sg.Button("Eliminar"),
            sg.Button("Salir"),
        ],
        [
            sg.Text("Filtrar por categoría"),
            sg.Combo(
                categorias_filtro,
                default_value="Todas",
                readonly=True,
                enable_events=True,
                key="-FILTRO-",
            ),
        ],
        [
            sg.Listbox(
                values=[],
                size=(60, 10),
                enable_events=True,
                expand_x=True,
                expand_y=True,
                key="-LISTA-",
            )
        ],
        [sg.Text("Total gastado: 0.00 EUR", key="-TOTAL-")],
    ]

    window = sg.Window("Gestor de gastos personales", layout, finalize=True, resizable=True)
    indices_mostrados = actualizar_pantalla(window, lista_gastos, "Todas")

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Salir"):
            break

        if event == "-FILTRO-":
            indice_seleccionado = None
            indices_mostrados = actualizar_pantalla(window, lista_gastos, values["-FILTRO-"])

        elif event == "-LISTA-":
            indices = window["-LISTA-"].get_indexes()
            if indices:
                indice_seleccionado = indices[0]
            else:
                indice_seleccionado = None

        elif event == "Añadir":
            try:
                gastos.anadir(
                    lista_gastos,
                    values["-FECHA-"],
                    values["-CONCEPTO-"],
                    values["-IMPORTE-"],
                    values["-CATEGORIA-"],
                )
            except ValueError as error:
                sg.popup_error(str(error))
            else:
                gastos.guardar(lista_gastos)
                indice_seleccionado = None
                indices_mostrados = actualizar_pantalla(window, lista_gastos, values["-FILTRO-"])
                window["-CONCEPTO-"].update("")
                window["-IMPORTE-"].update("")
                window["-FECHA-"].update(date.today().isoformat())
                window["-CATEGORIA-"].update(value=gastos.CATEGORIAS[0])

        elif event == "Eliminar":
            if indice_seleccionado is None:
                sg.popup_error("Selecciona un gasto para eliminar.")
            else:
                indice_real = indices_mostrados[indice_seleccionado]
                gastos.eliminar(lista_gastos, indice_real)
                gastos.guardar(lista_gastos)
                indice_seleccionado = None
                indices_mostrados = actualizar_pantalla(window, lista_gastos, values["-FILTRO-"])

    window.close()


if __name__ == "__main__":
    main()

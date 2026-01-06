import flet as ft
import uuid
from db import (
    insertar_carrera,
    actualizar_carrera,
    eliminar_carrera,
    obtener_carreras,
)


def carreras_view(page: ft.Page):

    editando_id = {"value": None}

    nombre = ft.TextField(label="Nombre de la carrera")
    grado = ft.TextField(label="Grado / Cuatrimestre", keyboard_type="number")
    division = ft.TextField(
        label="División",
        hint_text="Ej. División Académica",
    )

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("#")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Grado")),
            ft.DataColumn(ft.Text("División")),
            ft.DataColumn(ft.Text("Acciones")),
        ],
        rows=[]
    )

    def cargar_tabla():
        tabla.rows.clear()
        carreras = obtener_carreras()

        if not carreras:
            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("—")),
                        ft.DataCell(ft.Text("No hay carreras registradas")),
                        ft.DataCell(ft.Text("")),
                        ft.DataCell(ft.Text("")),
                        ft.DataCell(ft.Text("")),
                    ]
                )
            )
        else:
            for i, c in enumerate(carreras):
                tabla.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(i + 1))),
                            ft.DataCell(ft.Text(c[1])),
                            ft.DataCell(ft.Text(str(c[2]))),
                            ft.DataCell(ft.Text(c[3])),
                            ft.DataCell(
                                ft.Row(
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.Icons.EDIT,
                                            tooltip="Editar",
                                            on_click=lambda e, c=c: editar(c)
                                        ),
                                        ft.IconButton(
                                            icon=ft.Icons.DELETE,
                                            tooltip="Eliminar",
                                            icon_color=ft.Colors.RED,
                                            on_click=lambda e, c=c: borrar(c[0])
                                        ),
                                    ]
                                )
                            ),
                        ]
                    )
                )

        page.update()

    def guardar(e):
        if not nombre.value or not grado.value or not division.value:
            page.snack_bar = ft.SnackBar(ft.Text("Completa los campos"))
            page.snack_bar.open = True
            page.update()
            return

        if editando_id["value"]:
            actualizar_carrera(
                editando_id["value"],
                nombre.value,
                int(grado.value),
                division.value
            )
        else:
            insertar_carrera(
                str(uuid.uuid4()),
                nombre.value,
                int(grado.value),
                division.value
            )

        limpiar()
        cargar_tabla()

    def editar(carrera):
        editando_id["value"] = carrera[0]
        nombre.value = carrera[1]
        grado.value = carrera[2]
        division.value = carrera[3]
        page.update()

    def borrar(id):
        eliminar_carrera(id)
        cargar_tabla()

    def limpiar():
        editando_id["value"] = None
        nombre.value = ""
        grado.value = ""
        division.value = ""
        page.update()

    cargar_tabla()

    return ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        controls=[

            # ---------- HEADER ----------
            ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.ARROW_BACK,
                        tooltip="Volver",
                        on_click=lambda e: page.go("/")
                    ),
                    ft.Column(
                        spacing=2,
                        controls=[
                            ft.Text("Gestión de Carreras", size=22, weight="bold"),
                            ft.Text("Administra las carreras y sus divisiones",
                                    color=ft.Colors.GREY_700)
                        ]
                    )
                ]
            ),

            ft.Divider(),

            # ---------- FORM ----------
            ft.Container(
                padding=20,
                border_radius=10,
                content=ft.Column(
                    controls=[
                        nombre,
                        grado,
                        division,
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    "Guardar cambios" if editando_id["value"] else "Agregar carrera",
                                    on_click=guardar
                                ),
                                ft.TextButton(
                                    "Cancelar",
                                    visible=bool(editando_id["value"]),
                                    on_click=lambda e: limpiar()
                                )
                            ]
                        )
                    ]
                )
            ),

            # ---------- TABLE ----------
            ft.Container(
                margin=ft.margin.only(top=20),
                content=tabla
            )
        ]
    )

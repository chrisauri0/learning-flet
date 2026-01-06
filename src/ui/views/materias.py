import flet as ft
from core.models import Materia, TipoMateria
from db import insertar_materia, obtener_materias
import uuid


def materias_view(page: ft.Page):

    nombre = ft.TextField(label="Nombre de la materia")
    horas = ft.TextField(label="Horas semanales", keyboard_type="number")
    semestre = ft.TextField(label="Semestre (ej. 1, 2, 3)", keyboard_type="number")
    carrera = ft.TextField(label="Carrera (ej. Desarrollo de Software)")
    
    tipo = ft.Dropdown(
        label="Tipo",
        options=[
            ft.dropdown.Option(TipoMateria.TEORIA.value),
            ft.dropdown.Option(TipoMateria.LABORATORIO.value),
        ]
    )

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Horas")),
            ft.DataColumn(ft.Text("Tipo")),
            ft.DataColumn(ft.Text("Semestre")),
            ft.DataColumn(ft.Text("Carrera")),
        ],
        rows=[]
    )

    def cargar_tabla():
        tabla.rows.clear()
        for m in obtener_materias():
            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(m[0][:6])),
                        ft.DataCell(ft.Text(m[1])),
                        ft.DataCell(ft.Text(m[2])),
                        ft.DataCell(ft.Text(m[3])),
                        ft.DataCell(ft.Text(m[4])),
                        ft.DataCell(ft.Text(m[5])),
                    ]
                )
            )
        page.update()

    def guardar_materia(e):
        if not nombre.value or not horas.value or not tipo.value:
            page.snack_bar = ft.SnackBar(ft.Text("Completa todos los campos"))
            page.snack_bar.open = True
            page.update()
            return

        materia = Materia(
            id=str(uuid.uuid4()),
            nombre=nombre.value,
            horas_semanales=int(horas.value),
            tipo=TipoMateria(tipo.value),
            semestre=int(semestre.value),
            carrera=carrera.value
        )

        insertar_materia(materia)
        cargar_tabla()

        nombre.value = ""
        horas.value = ""
        semestre.value = ""
        carrera.value = ""
        tipo.value = None

        page.update()

    cargar_tabla()

    return ft.Column(
        controls=[
            ft.Text("Materias", size=24, weight="bold"),


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
                            ft.Text("Gestión de Materias", size=22, weight="bold"),
                            ft.Text("Administra las materias y sus detalles",
                                    color=ft.Colors.GREY_700)
                        ]
                    )
                ]
            ),

            ft.Divider(),
            nombre,
            horas,
            tipo,
            semestre,
            carrera,
            ft.ElevatedButton("Guardar materia", on_click=guardar_materia),
            ft.Divider(),
            tabla
        ],
        scroll=ft.ScrollMode.AUTO
    )

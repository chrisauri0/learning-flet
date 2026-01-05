from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum


class TipoMateria(Enum):
    TEORIA = "teoria"
    LABORATORIO = "laboratorio"


class TipoSalon(Enum):
    NORMAL = "normal"
    LABORATORIO = "laboratorio"


@dataclass
class BloqueHorario:
    dia: str              # "Lunes"
    inicio: int           # 17 = 17:00
    fin: int              # 19 = 19:00


@dataclass
class Materia:
    id: str
    nombre: str
    horas_semanales: int
    tipo: TipoMateria
    semestre: int              # 1, 2, 3, 4, etc.
    carrera: str            # desarrollo de software, redes, etc.
    profesor_asignado: Optional[str] = None

@dataclass
class Carrera:
    id: str
    nombre: str
    materias: List[str]       # IDs de materias asociadas

@dataclass
class Grupo:
    id: str
    nombre: str
    materias: List[str]       # IDs de materias en el grupo
    carrera_id: str
    grado: int


@dataclass
class Profesor:
    id: str
    nombre: str
    materias: List[str]               # IDs de materias que puede impartir
    disponibilidad: List[BloqueHorario]


@dataclass
class Salon:
    id: str
    nombre: str
    capacidad: int
    tipo: TipoSalon


@dataclass
class AsignacionHorario:
    materia_id: str
    profesor_id: str
    salon_id: str
    bloque: BloqueHorario

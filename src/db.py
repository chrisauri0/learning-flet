import sqlite3

DB_PATH = "storage/data/horarios.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Usamos executescript y añadimos ";" al final de cada bloque
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS carreras (
        id TEXT PRIMARY KEY,
        nombre TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS materias (
        id TEXT PRIMARY KEY,
        nombre TEXT NOT NULL,
        horas_semanales INTEGER,
        tipo TEXT,
        semestre INTEGER,
        carrera_id TEXT,
        profesor_asignado TEXT,
        FOREIGN KEY (carrera_id) REFERENCES carreras(id)
    );

    CREATE TABLE IF NOT EXISTS grupos (
        id TEXT PRIMARY KEY,
        nombre TEXT,
        carrera_id TEXT,
        semestre INTEGER,
        FOREIGN KEY (carrera_id) REFERENCES carreras(id)
    );

    CREATE TABLE IF NOT EXISTS grupo_materias (
        grupo_id TEXT,
        materia_id TEXT,
        PRIMARY KEY (grupo_id, materia_id),
        FOREIGN KEY (grupo_id) REFERENCES grupos(id),
        FOREIGN KEY (materia_id) REFERENCES materias(id)
    );
    """)
    conn.commit() # No olvides el commit para guardar los cambios
    conn.close()

def insertar_materia(materia):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO materias (id, nombre, horas_semanales, tipo, grupo)
    VALUES (?, ?, ?, ?, ?)
    """, (
        materia.id,
        materia.nombre,
        materia.horas_semanales,
        materia.tipo.value,
        materia.grupo
    ))

    conn.commit()
    conn.close()


def obtener_materias():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM materias")
    rows = cursor.fetchall()
    conn.close()

    return rows

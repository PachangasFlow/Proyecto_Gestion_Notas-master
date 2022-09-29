from datetime import date, datetime
from operator import truediv
from pickle import TRUE
import sqlite3
import envioemail

DB_NAME = 'bdgestion.s3db'


def conectar_db():
    conn = sqlite3.connect(DB_NAME)
    return conn


def insertar_usuarios(nombre, apellido, usuario, passwd):
    cod_ver = str(datetime.now())
    cod_ver = cod_ver.replace("-", "")
    cod_ver = cod_ver.replace(" ", "")
    cod_ver = cod_ver.replace(":", "")
    cod_ver = cod_ver.replace(".", "")

    # flash(cod_ver)

    try:
        db = conectar_db()
        cursor = db.cursor()
        sql = "INSERT INTO usuarios(nombre,apellido,usuario,passw,cod_verificacion,verificado,id_rol) values(?,?,?,?,?,?,?)"
        cursor.execute(sql, [nombre, apellido, usuario,
                        passwd, cod_ver, False, 1])
        db.commit()
        envioemail.enviar_email(usuario, cod_ver)
        return True
    except:
        return False

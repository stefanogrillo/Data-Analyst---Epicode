import mysql.connector
import sys

def connection_database(user, password, host, database):
    """
    Create a connection with the SQL DataBase
    :variable: user: user's name
    :variable: password: user's password
    :variable: host: IP address of the SQL server
    :variable: database: SQL DB's name
    :return: conn (connection) or None
    """
    try:
        conn = mysql.connector.connect(user=user, password=password, host=host, database=database)
        return conn
    except mysql.connector.errors.DatabaseError as db_error:
        print(db_error.msg)
        return None


def close_connection(connection):
    """
    Close a connection to the SQL DataBase
    :variable: user: user's name
    """
    connection.close()


def trying(sql):
    """
    Take a SQL statement and try/except it, visualizing the outcome
    :variable: sql: SQL statement
    """
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
    except:
        conn.rollback()

def add_delete(sql):
    """
    Inserto or Delete values in a Table
    :variable: sql: SQL statement
    """
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()


if __name__ == "__main__":
    # conn = mysql.connector.connect(user="", password="", host="127.0.0.1", database="discografia")
    conn = connection_database(user="root", password="rootstefano17", host="127.0.0.1", database="discografia")

    try:
        cursor = conn.cursor()

        sql1 = "SELECT A.Nome FROM AUTORE A JOIN ESECUZIONE E ON A.TitoloCanzone = E.TitoloCanzone JOIN CANZONE C ON " \
               "A.nome = C.NomeCantante WHERE A.Nome = C.NomeCantante AND C.CodiceReg = E.CodiceReg AND " \
               "E.TitoloCanzone = A.TitoloCanzone AND A.Nome LIKE 'D%';"
        print("\nI cantautori (persone che hanno cantato e scritto la stessa canzone) il cui nome inizia per 'D")
        trying(sql1)


        sql2 = "SELECT D.TitoloAlbum FROM DISCO D JOIN CONTIENE C ON D.NroSerie = C.NroSerieDisco JOIN ESECUZIONE E " \
               "ON C.CodiceReg = E.CodiceReg WHERE E.Anno IS NULL;"
        print("\nI titoli dei dischi che contengono canzoni di cui non si conosce l'anno di registrazione")
        trying(sql2)

        sql3 = "SELECT C.NomeCantante FROM CANZONE C JOIN ESECUZIONE E ON C.CodiceReg = E.CodiceReg GROUP BY E.CodiceReg " \
               "HAVING COUNT(E.CodiceReg) != 1;"
                #"SELECT C.NomeCantante FROM CANTANTE C WHERE NomeCantante NOT IN (SELECT C1.NomeCantante FROM CANTANTE AS " \
                #"C1 WHERE CodiceReg NOT IN (SELECT CodiceReg FROM CANTANTE AS C2) WHERE C2.NomeCantante != C1.NomeCantante);"
        print("\nI cantanti che non hanno mai registrato una canzone come solisti")
        trying(sql3)

        sql4 = "SELECT C.NomeCantante FROM canzone C JOIN ESECUZIONE E ON C.CodiceReg = E.CodiceReg GROUP BY E.CodiceReg HAVING COUNT(E.CodiceReg) = 1;"
                #"SELECT C.NomeCantante FROM CANZONE C JOIN ESECUZIONE E ON C.CodiceReg = E.CodiceReg JOIN AUTORE A ON " \
                #"E.TitoloCanzone = A.TitoloCanzone WHERE C.NomeCantante = A.Nome;"
        print("\nI cantanti che hanno sempre registrato canzoni come solisti")
        trying(sql4)

        # Vogliamo INSERIRE 'Celentano', 'I Ragazzi della via Gluck' nella tabella "autore"
        sql0a = "INSERT INTO autore(nome, TitoloCanzone) VALUES ('Celentano', 'I Ragazzi della via Gluck')"
        # add_delete(slq0a)
        # add_delete("INSERT INTO autore(nome, TitoloCanzone) VALUES ('J Ax', 'Italianimal')")


        # Vogliamo ELIMINARE 'Celentano', 'I Ragazzi della via Gluck' precedentemente inseriti nella tabella "autore"
        sql0ae = "DELETE FROM autore WHERE TitoloCanzone ='I Ragazzi della via Gluck'"
        # add_delete(sql0ae)
        # add_delete("DELETE FROM autore WHERE TitoloCanzone = 'Italianimal'")

    except:
        conn.rollback()
    finally:
        close_connection(conn)

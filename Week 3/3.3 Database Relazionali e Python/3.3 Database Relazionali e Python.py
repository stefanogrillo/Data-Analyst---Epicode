import mysql.connector


# METHODS
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
        c = mysql.connector.connect(user=user, password=password, host=host, database=database)
        return c
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


def add_delete_advanced(what, lista1, lista2, lista3=None, lista4=None):
    """
    Inserto or Delete values in a Table
    :variable: table: where should we insert the data
    :variable: lista1: first list of data
    :variable: lista2: second list of data
    :variable: lista3: third list of data
    :variable: lista4: fourth list of data
    """
    try:
        for i in range(0, len(lista1)):
            if lista3 == None and lista4 == None:
                sqll = what + " VALUES ('" + lista1[i] + "', '" + lista2[i] + "');"
            elif lista3 != None and lista4 == None:
                sqll = what + " VALUES ('" + lista1[i] + "', '" + lista2[i] + "', '" + lista3[i] + "');"
            else:
                sqll = what + " VALUES ('" + lista1[i] + "', '" + lista2[i] + "', '" + lista3[i] + "', '" + lista4[i] + "');"
            print(sqll)
            cursor.execute(sqll)
            conn.commit()
    except:
        conn.rollback()


if __name__ == "__main__":
    # conn = mysql.connector.connect(user="", password="", host="127.0.0.1", database="discografia")
    conn = connection_database(user="", password="", host="127.0.0.1", database="discografia")

    try:
        cursor = conn.cursor()

        # POPULATE THE DATABASE
        # Once imported the empty SQL.scheme in MySQL, create a connection with this Pytho script and populate the DataBase
        # DB: Autore
        nomeA = ['Celentano','Celentano','Charlotte de Witte','Jerome Isma-Ae','Daddy Yankee','David Guetta','Deorro','Elvis Crespo','J Ax','Robbie Rivera']
        TitoloCanzoneA = ['Azzurro','I Ragazzi della via Gluck','Hold that Sucker Down - Charlotte de Witte Remix','Hold that Sucker Down - Charlotte de Witte Remix','Con Calma','Memories','Bailar (ft. Elvis Crespo','Bailar (ft. Elvis Crespo','Italianimal','La Vecina']
        autore = "INSERT INTO `discografia`.`autore` (`nome`, `TitoloCanzone`)"
        #add_delete_advanced(autore, nomeA, TitoloCanzoneA)

        # DB: Esecuzione
        # This sends a Foreign Key to Canzone, and a Foreign Key to Contiene
        CodiceRegE = ['1','2','3','4','5','6','7','8']
        TitoloCanzoneE = ['Azzurro','I Ragazzi della via Gluck','Hold that Sucker Down - Charlotte de Witte Remix','Bailar (ft. Elvis Crespo)','Italianimal','Memories','Con Calma','La Vecina']
        AnnoE = ['1968','1969','2020','2017','2011','2010','2019','2022']
        esecuzione = "INSERT INTO `discografia`.`esecuzione` (`CodiceReg`, `TitoloCanzone`, `Anno`)"
        #add_delete_advanced(esecuzione, CodiceRegE, TitoloCanzoneE, AnnoE)

        # DB: Canzone
        NomeCantanteC = ['Celentano','Celentano','Charlotte de Witte','Jerome Isma-Ae','Deorro','Elvis Crespo','J Ax','David Guetta','Daddy Yankee','Robbie Rivera']
        CodiceRegC = ['1','2','3','3','4','4','5','6','7','8']
        canzone = "INSERT INTO `discografia`.`canzone` (`NomeCantante`, `CodiceReg`)"
        #add_delete_advanced(canzone, NomeCantanteC, CodiceRegC)

        # DB: Disco
        # This sends a Foreign Key to Contiene
        NroSerieD = ['11','12','13','14','15']
        TitoloAlbumD = ['Origini','Best Techno','Best Reggaeton','Italian','Dance 2010']
        AnnoD = ['1968','2022','2019','2011','2010']
        PrezzoD = ['19.90','9.90','19.90','9.90','19.90']
        disco = "INSERT INTO `discografia`.`disco` (`NroSerie`, `TitoloAlbum`, `Anno`, `Prezzo`)"
        #add_delete_advanced(disco, NroSerieD, TitoloAlbumD, AnnoD, PrezzoD)

        # DB: Contiene
        NroSerieDiscoC = ['11','11','12','12','13','13','14','15']
        CodiceRegC = ['1','2','3','8','4','7','5','6']
        NroProgC = ['1','2','3','4','5','6','7','8']
        contiene = "INSERT INTO `discografia`.`contiene` (`NroSerieDisco`, `CodiceReg`, `NroProg`)"
        #add_delete_advanced(contiene, NroSerieDiscoC, CodiceRegC, NroProgC)

        
        # SQL SELECT STATEMENTS
        sql1 = "SELECT A.Nome FROM AUTORE A JOIN ESECUZIONE E ON A.TitoloCanzone = E.TitoloCanzone JOIN CANZONE C ON " \
               "A.nome = C.NomeCantante WHERE A.Nome = C.NomeCantante AND C.CodiceReg = E.CodiceReg AND " \
               "E.TitoloCanzone = A.TitoloCanzone AND A.Nome LIKE 'D%';"
        print("\nI cantautori (persone che hanno cantato e scritto la stessa canzone) il cui nome inizia per 'D")
        trying(sql1)


        sql2 = "SELECT D.TitoloAlbum FROM DISCO D JOIN CONTIENE C ON D.NroSerie = C.NroSerieDisco JOIN ESECUZIONE E " \
               "ON C.CodiceReg = E.CodiceReg WHERE E.Anno ='1968';"
        print("\nI titoli dei dischi che contengono canzoni di cui (non si conosce l'anno di registrazione -> E.Anno IS NULL) l'anno è 1968")
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
    except:
        conn.rollback()
    finally:
        if conn is not None:
            close_connection(conn)

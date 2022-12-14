import mysql.connector
from sqlalchemy import create_engine
import pprint
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pandas_profiling import ProfileReport


# METHODS for CURSOR
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


def trying(sqll):
    """
    Take a SQL statement and try/except it, visualizing the outcome
    :variable: sql: SQL statement
    """
    try:
        cursor.execute(sqll)
        result = cursor.fetchall()
        return result
    except:
        conn.rollback()


# CONNECTOR
if __name__ == "__main__":
    # conn = mysql.connector.connect(user="", password="", host="127.0.0.1", database="ecommerce")
    conn = connection_database(user="root", password="rootstefano17", host="127.0.0.1", database="ecommerce")

    try:
        cursor = conn.cursor()


        # QUERY 1: QUALI TABELLE SONO NEL DATABASE ecommerce?
        sql1 = "SHOW TABLES;"
        print("\n1 QUALI TABELLE SONO NEL DATABASE ecommerce?")
        pprint.pprint(trying(sql1))


        # QUERY 2: QUANTE E QUALI MARCHE SONO VENDUTE NEL ecommerce?
        sql2a = "SELECT count(nome) numero FROM marca;"
        sql2b = "SELECT nome FROM marca ORDER BY nome DESC LIMIT 10;"
        print("\n2a QUANTE MARCHE SONO VENDUTE NEL ecommerce?")
        pprint.pprint(trying(sql2a))
        print("\n2b QUALI MARCHE SONO VENDUTE NEL ecommerce?")
        pprint.pprint(trying(sql2b))


        # QUERY 3: QUANTI E QUALI PRODOTTI SONO IN MAGAZZINO?
        sql3a = "SELECT count(nome) numero_prodotti FROM prodotto;"
        sql3b = "SELECT count(nome) numero_prodotti FROM prodotto WHERE quantita > 0;"
        sql3c = "SELECT nome FROM prodotto ORDER BY nome ASC LIMIT 5;"
        sql3d = "SELECT p.pid, p.nome, pp.nome, pp.pid FROM prodotto p JOIN correlati c ON p.pid = c.pid JOIN prodotto pp ON " \
                "c.relpid = pp.pid;"
        print("\n3a QUANTI PRODOTTI SONO IN LISTA?")
        print(trying(sql3a))
        print("\n3b QUANTI PRODOTTI SONO IN MAGAZZINO?")
        print(trying(sql3b))
        print("\n3c QUALI SONO I PRIMI 5 PRODOTTI?")
        pprint.pprint(trying(sql3c))
        print("\n3d QUALI PRODOTTI SONO CORRELATI?")
        pprint.pprint(trying(sql3d))


        # QUERY 4: A CHE CATEGORIE CORRISPONDONO I PRODOTTI IN MAGAZZINO?
        sql4a = "SELECT count(nome) as numero_categorie FROM categoria;"
        sql4b = "SELECT nome FROM categoria ORDER BY nome DESC LIMIT 10;"
        # e quali cellulari e software hanno nel ecommerce?
        sql4c = "SELECT p.pid, p.nome, p.quantita FROM prodotto p JOIN categoria c ON c.cid=p.cid WHERE c.nome LIKE 'CELL%';"
        sql4d = "SELECT p.pid, p.nome, p.quantita FROM prodotto p JOIN categoria c ON c.cid=p.cid WHERE p.nome LIKE 'windows%';"
        print("\n4a QUANTE SONO LE CATEGORIE?")
        pprint.pprint(trying(sql4a))
        print("\n4b QUALI SONO LE ULTIME 10?")
        pprint.pprint(trying(sql4b))
        print("\n4c QUALI CELLULARI SONO IN MAGAZZINO?")
        pprint.pprint(trying(sql4c))
        print("Sono in lista, ma non sono in magazzino")
        print("\n4d QUALI SOFTWARE WINDOWS SONO IN MAGAZZINO?")
        pprint.pprint(trying(sql4d))
        print("Sono in lista, ma non sono in magazzino")


        # QUERY 5: A QUANTO SONO VENDUTI I SOFTWARE WINDOWS?
        sql5a = "SELECT p.pid, p.nome, pr.valore FROM prodotto p JOIN categoria c ON c.cid=p.cid JOIN prezzo pr ON " \
                "p.pid = pr.pid WHERE p.nome LIKE 'windows%';"
        # valore e prezzo sono la stessa cosa? (ex: prezzo e valore per pid = "4000001")
        sql5b = "SELECT p.pid, p.nome, o.prezzo, pr.valore FROM prodotto p LEFT JOIN orpr01 o ON o.pid=p.pid LEFT " \
                "JOIN prezzo pr ON p.pid = pr.pid WHERE p.pid = '4000001';"
        print("\n5a A QUANTO SONO VENDUTI I SOFTWARE WINDOWS?")
        pprint.pprint(trying(sql5a))
        print("Qui ?? rappresentato il valore")
        print("\n5b VALORE E PREZZO SONO LA STESSA COSA? ESEMPIO PER id prodotto: '4000001'")
        pprint.pprint(trying(sql5b))
        print("Valore e prezzo non sono la stessa cosa")


        # QUERY 6: QUANTO VALORE HANNO IN MEDIA I PRODOTTI PER CATEGORIA?
        sql6a = "SELECT c.nome, AVG(pr.valore) media FROM categoria c JOIN prodotto p ON c.cid=p.cid JOIN prezzo pr ON pr.pid=p.pid GROUP BY c.nome ORDER BY media DESC;"
        print("\n6 QUANTO VALORE HANNO IN MEDIA I PRODOTTI PER CATEGORIA?")
        pprint.pprint(trying(sql6a))


        # QUERY 7: QUANTI PRODOTTI CI SONO PER CATEGORIA? E PER MARCA?
        sql7a = "SELECT c.nome, count(c.nome) numero FROM categoria c JOIN prodotto p ON c.cid=p.cid GROUP BY c.nome ORDER BY numero DESC;"
        sql7b = "SELECT m.nome, count(m.nome) numero FROM marca m JOIN prodotto p ON p.mid = m.mid GROUP BY m.nome ORDER BY numero DESC;"
        print("\n7a QUANTI PRODOTTI CI SONO PER CATEGORIA?")
        pprint.pprint(trying(sql7a))
        print("\n7b QUANTI PRODOTTI CI SONO PER MARCA?")
        pprint.pprint(trying(sql7b))


        # QUERY 8: QUALI SONO I 5 PRODOTTI BESTSELLER PER QUANTITA' E GUADAGNO?
        sql8a = "SELECT p.pid, od.oid, p.nome, p.quantita as qta_stock, sum(o.quantita) as quantita_venduta_tot, prezzo*sum(o.quantita) as prezzo_tot, prezzo FROM prodotto p JOIN orpr01 o ON p.pid = o.pid JOIN ordine od ON od.oid = o.oid GROUP BY o.pid ORDER BY quantita_venduta_tot DESC LIMIT 6;"
        sql8b = "SELECT p.pid, od.oid, p.nome, p.quantita as qta_stock, sum(o.quantita) as quantita_venduta_tot, prezzo*sum(o.quantita) as prezzo_tot, prezzo FROM prodotto p JOIN orpr01 o ON p.pid = o.pid JOIN ordine od ON od.oid = o.oid GROUP BY o.pid ORDER BY prezzo_tot DESC LIMIT 5;"
        print("\n8a QUALI SONO I 5 PRODOTTI BESTSELLER PER QUANTITA'?")
        pprint.pprint(trying(sql8a))
        print("1: DIMM DDRII\n2: SCHEDA MADRE ASROCK\n3: MODULA PLUG\n4: CARTUCCIA CANON\n5: CARICABATTERIE UNIVERSALE")
        print("\n8b QUALI SONO I 5 PRODOTTI BESTSELLER PER GUADAGNO?")
        pprint.pprint(trying(sql8b))
        print("1: ACER AS5810T-354G32MN\n2: MONITOR LCD LG\n3: SCHEDA MADRE ASROCK\n4: SCHEDA MADRE AM3\n5: TONER HP")


        # QUERY 9: QUALI SONO I METODI DI PAGAMENTO E SPEDIZIONE PRINCIPALI?
        sql9a = "SELECT count(oid) as numero_ordini, s.nome as metodo_spedizione, s.costo, count(oid)*s.costo as costo_spedizioni_tot, pag.nome as metodo_pagamento, pag.costo, count(oid)*pag.costo as costo_pagamento_tot FROM pasp01 pa JOIN spedizione s ON pa.spid = s.spid RIGHT JOIN ordine o ON o.paspid = pa.paspid JOIN pagamento pag ON pa.paid = pag.paid GROUP BY s.nome, pag.nome;"
        print("\n9 QUALI SONO I METODI DI PAGAMENTO E SPEDIZIONE PRINCIPALI?")
        print(trying(sql9a))
        print("Metodo spedizione: Consegna con corriere GLS = 14; Spedizione in posta = 11;\nMetodo di pagamento: Contrassegno = 15; Pagamento con Carta di Credito = 10;")


        # QUERY 10: A QUALI CITTA E PROVINCE SI SPEDISCE DI PIU'?
        sql10a = "SELECT provincia, citta, count(citta) as numero_indirizzi_utente FROM indirizzo GROUP BY provincia, citta ORDER BY provincia, numero_indirizzi_utente DESC;"
        sql10b = "SELECT provincia, count(citta) as numero_indirizzi_utente FROM indirizzo GROUP BY provincia ORDER BY numero_indirizzi_utente DESC;"
        print("\n10a A QUALI CITTA SI SPEDISCE DI PIU'?")
        pprint.pprint(trying(sql10a))
        print("Citt??: Roma, Milano")
        print("\n10b A QUALI PROVINCE SI SPEDISCE DI PIU'?")
        pprint.pprint(trying(sql10b))
        print("Province: Roma, Milano")

    except:
        conn.rollback()
    finally:
        if conn is not None:
            close_connection(conn)

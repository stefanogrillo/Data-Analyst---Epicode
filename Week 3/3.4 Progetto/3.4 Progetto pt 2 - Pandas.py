from sqlalchemy import create_engine, inspect
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pandas_profiling import ProfileReport


# METHODS
def get_databases_table():
    """
    Prints the databases' tables' names
    :return: prints the table's names
    """
    inspector = inspect(db_connection)
    i = 0
    for table_name in inspector.get_table_names():
        print("Table %s: %s" % (i, table_name))
        i += 1


def choose_table(name):
    """
    In this method, we select data from either a table or a SQL statement
    :variable: name: either a table or a SQL statement
    :return: tavola: the data needed
    """
    tavola = pd.read_sql(name, db_connection)
    return tavola


def choose_tables_n_merge(name1, name2):
    """
    Given two tables, this method creates a new one with merged values
    :variable: name1: either a table or a SQL statement
    :variable: name2: either a table or a SQL statement
    :return: tavola3: the merged data
    """
    tavola1 = pd.read_sql(name1, db_connection)
    tavola2 = pd.read_sql(name2, db_connection)

    tavola3 = tavola1.merge(tavola2)
    return tavola3


# PANDAS
db_connection_str = 'mysql+mysqlconnector://root:rootstefano17@127.0.0.1/ecommerce'
db_connection = create_engine(db_connection_str)


# QUERY 1: QUALI TABELLE SONO NEL DATABASE ecommerce?
if True:
    sql1 = "SHOW TABLES;"
    print("\n1 QUALI TABELLE SONO NEL DATABASE ecommerce?\n", choose_table(sql1))
# QUERY 1: ma con pandas
# (True/True switch to speed up the program)
if True:
    get_databases_table()


# QUERY 2: QUANTE E QUALI MARCHE SONO VENDUTE NEL ecommerce?
if True:
    sql2a = "SELECT count(nome) numero FROM marca;"
    sql2b = "SELECT nome FROM marca ORDER BY nome DESC LIMIT 10;"
    print("\n2a QUANTE MARCHE SONO VENDUTE NEL ecommerce?\n", choose_table(sql2a))
    print("\n2b QUALI MARCHE SONO VENDUTE NEL ecommerce?\n", choose_table(sql2b))
# QUERY 2: ma con pandas
# (True/True switch to speed up the program)
if True:
    pdsql2 = choose_table("marca")
    count = len(pdsql2['nome'])
    print("\n2a QUANTE MARCHE SONO VENDUTE NEL ecommerce?\n", count)
    print("\n2b QUALI MARCHE SONO VENDUTE NEL ecommerce?\n", pdsql2['nome'])


# QUERY 3: QUANTI E QUALI PRODOTTI SONO IN MAGAZZINO?
if True:
    sql3a = "SELECT count(nome) numero_prodotti FROM prodotto;"
    sql3b = "SELECT count(nome) numero_prodotti FROM prodotto WHERE quantita > 0;"
    sql3c = "SELECT nome FROM prodotto ORDER BY nome ASC LIMIT 5;"
    sql3d = "SELECT p.pid, p.nome, pp.nome, pp.pid FROM prodotto p JOIN correlati c ON p.pid = c.pid JOIN prodotto pp ON " \
            "c.relpid = pp.pid;"
    print("\n3a QUANTI PRODOTTI SONO IN LISTA?\n", choose_table(sql3a))
    print("\n3b QUANTI PRODOTTI SONO IN MAGAZZINO?\n", choose_table(sql3b))
    print("\n3c QUALI SONO I PRIMI 5 PRODOTTI?\n", choose_table(sql3c))
    print("\n3d QUALI PRODOTTI SONO CORRELATI?\n", choose_table(sql3d))
# QUERY 3: ma con pandas
# (True/True switch to speed up the program)
if True:
    pdsql3 = choose_table("prodotto")
    print("\n3a QUANTI PRODOTTI SONO IN LISTA?\n", len(pdsql3['nome']))

    pdsql32 = pdsql3[pdsql3.quantita > 0]
    print("\n3b QUANTI PRODOTTI SONO IN MAGAZZINO\n", len(pdsql32['nome']))

    print("\n3c QUALI SONO I PRIMI 5 PRODOTTI?\n", pdsql3['nome'].sort_values().head(5))

    # Terza query: pre-lavorazioni
    dsql3ab = choose_tables_n_merge("prodotto", "correlati")

    dsql3ab = dsql3ab[['pid', 'nome', 'relpid']]
    dsql3a = choose_table("prodotto")
    dsql3a = dsql3a[['pid', 'nome']]

    dsql3aba = pd.merge(dsql3ab.set_index('relpid'), dsql3a, right_on='pid', left_index=True)
    dsql3aba.drop('pid', axis=1, inplace=True)
    # special print
    with pd.option_context('display.max_rows', None,
                           'display.max_columns', None,
                           'display.precision', 3,
                           ):
        print("\n3d QUALI PRODOTTI SONO CORRELATI?\n", dsql3aba)


# QUERY 4: A CHE CATEGORIE CORRISPONDONO I PRODOTTI IN MAGAZZINO?
if True:
    sql4a = "SELECT count(nome) as numero_categorie FROM categoria;"
    sql4b = "SELECT nome FROM categoria ORDER BY nome DESC LIMIT 10;"
    # e quali cellulari e software hanno nel ecommerce?
    sql4c = "SELECT p.pid, p.nome, p.quantita FROM prodotto p JOIN categoria c ON c.cid=p.cid WHERE c.nome LIKE 'CELL%';"
    sql4d = "SELECT p.pid, p.nome, p.quantita FROM prodotto p JOIN categoria c ON c.cid=p.cid WHERE p.nome LIKE 'windows%';"
    print("\n4a QUANTE SONO LE CATEGORIE?\n", choose_table(sql4a))
    print("\n4b QUALI SONO LE ULTIME 10?\n", choose_table(sql4b))
    print("\n4c QUALI CELLULARI SONO IN MAGAZZINO?\n", choose_table(sql4c))
    print("Sono in lista, ma non sono in magazzino")
    print("\n4d QUALI SOFTWARE WINDOWS SONO IN MAGAZZINO?\n", choose_table(sql4d))
    print("Sono in lista, ma non sono in magazzino")
# QUERY 4: ma con pandas
# (True/True switch to speed up the program)
if True:
    cat = choose_table("categoria")
    num_nomi = len(cat[['nome']])
    print("\n4a QUANTE SONO LE CATEGORIE?\n", num_nomi)

    # "ascending = falso" mette in discendente
    cat2 = cat.sort_values(['nome'], ascending=[True])
    print("\n4b QUALI SONO LE ULTIME 10?\n", cat2['nome'].head(10))

    dsql4a = choose_table("prodotto")
    dsql4b = choose_table("categoria")
    dsql4ab = pd.merge(dsql4a.set_index('cid'), dsql4b, how='right',right_on='cid', left_index=True)
    dsql4ab = dsql4ab[['pid', 'nome_x', 'quantita', 'nome_y']]
    dsql4abc = dsql4ab

    dsql4ab = dsql4ab[dsql4ab['nome_y'].str.contains('CELL')]
    with pd.option_context('display.max_rows', None,
                           'display.max_columns', None,
                           'display.precision', 3,
                           ):
        print("\n4c QUALI CELLULARI SONO IN MAGAZZINO?\n", dsql4ab)

    dsql4abc = dsql4abc[dsql4abc['nome_y'].str.contains('MICROSOFT')]
    with pd.option_context('display.max_rows', None,
                           'display.max_columns', None,
                           'display.precision', 3,
                           ):
        print("\n4d QUALI SOFTWARE WINDOWS SONO IN MAGAZZINO?\n", dsql4abc)


# QUERY 5: A QUANTO SONO VENDUTI I SOFTWARE WINDOWS?
if True:
    sql5a = "SELECT p.pid, p.nome, pr.valore FROM prodotto p JOIN categoria c ON c.cid=p.cid JOIN prezzo pr ON " \
            "p.pid = pr.pid WHERE p.nome LIKE 'windows%';"
    # valore e prezzo sono la stessa cosa? (ex: prezzo e valore per pid = "4000001")
    sql5b = "SELECT p.pid, p.nome, o.prezzo, pr.valore FROM prodotto p LEFT JOIN orpr01 o ON o.pid=p.pid LEFT " \
            "JOIN prezzo pr ON p.pid = pr.pid WHERE p.pid = '4000001';"
    print("\n5a A QUANTO SONO VENDUTI I SOFTWARE WINDOWS?\n", choose_table(sql5a))
    print("Qui è rappresentato il valore")
    print("\n5b VALORE E PREZZO SONO LA STESSA COSA? ESEMPIO PER id prodotto: '4000001'\n", choose_table(sql5b))
    print("Valore e prezzo non sono la stessa cosa")


# QUERY 6: QUANTO VALORE HANNO IN MEDIA I PRODOTTI PER CATEGORIA?
if True:
    sql6a = "SELECT c.nome, AVG(pr.valore) media FROM categoria c JOIN prodotto p ON c.cid=p.cid JOIN prezzo pr ON pr.pid=p.pid GROUP BY c.nome ORDER BY media DESC;"
    print("\n6 QUANTO VALORE HANNO IN MEDIA I PRODOTTI PER CATEGORIA?\n", choose_table(sql6a))


# QUERY 7: QUANTI PRODOTTI CI SONO PER CATEGORIA? E PER MARCA? + PLOT
if True:
    sql7a = "SELECT c.nome, count(c.nome) numero FROM categoria c JOIN prodotto p ON c.cid=p.cid GROUP BY c.nome ORDER BY numero DESC;"
    sql7b = "SELECT m.nome, count(m.nome) numero FROM marca m JOIN prodotto p ON p.mid = m.mid GROUP BY m.nome ORDER BY numero DESC;"
    print("\n7a QUANTI PRODOTTI CI SONO PER CATEGORIA?\n", choose_table(sql7a))
    print("\n7b QUANTI PRODOTTI CI SONO PER MARCA?\n", choose_table(sql7b))

    # BARPLOT 1: PRODOTTI PER CATEGORIA
    df7a = pd.DataFrame(choose_table(sql7a))

    # REPORT
    # profile = ProfileReport(df7a, title="Pandas Profiling Report")
    # profile.to_file("report1.html")

    ls7a = df7a.values.tolist()
    ls7ax = []
    la7ay = []
    for i in range(0, len(ls7a)):
        ls7ax.append(ls7a[i][0])
        la7ay.append(ls7a[i][1])

    # barh per horizontal
    plt.bar(ls7ax, la7ay)
    plt.show()

    # BARPLOT 2: PRODOTTI PER MARCA
    df7b = pd.DataFrame(choose_table(sql7b))

    # REPORT
    # profile = ProfileReport(df7a, title="Pandas Profiling Report")
    # profile.to_file("report1.html")

    ls7b = df7b.values.tolist()
    ls7bx = []
    la7by = []
    for i in range(0, len(ls7b)):
        ls7bx.append(ls7b[i][0])
        la7by.append(ls7b[i][1])

    plt.bar(ls7bx, la7by)
    plt.show()


# QUERY 8: QUALI SONO I 5 PRODOTTI BESTSELLER PER QUANTITA' E GUADAGNO?
if True:
    sql8a = "SELECT p.pid, od.oid, p.nome, p.quantita as qta_stock, sum(o.quantita) as quantita_venduta_tot, prezzo*sum(o.quantita) as prezzo_tot, prezzo FROM prodotto p JOIN orpr01 o ON p.pid = o.pid JOIN ordine od ON od.oid = o.oid GROUP BY o.pid ORDER BY quantita_venduta_tot DESC LIMIT 6;"
    sql8b = "SELECT p.pid, od.oid, p.nome, p.quantita as qta_stock, sum(o.quantita) as quantita_venduta_tot, prezzo*sum(o.quantita) as prezzo_tot, prezzo FROM prodotto p JOIN orpr01 o ON p.pid = o.pid JOIN ordine od ON od.oid = o.oid GROUP BY o.pid ORDER BY prezzo_tot DESC LIMIT 5;"
    # special print
    with pd.option_context('display.max_rows', None,
                           'display.max_columns', None,
                           'display.precision', 3,
                           ):
        print("\n8a QUALI SONO I 5 PRODOTTI BESTSELLER PER QUANTITA'?\n", choose_table(sql8a))
        print("\n8b QUALI SONO I 5 PRODOTTI BESTSELLER PER GUADAGNO?\n", choose_table(sql8b))


# QUERY 9: QUALI SONO I METODI DI PAGAMENTO E SPEDIZIONE PRINCIPALI?
if True:
    sql9a = "SELECT count(oid) as numero_ordini, s.nome as metodo_spedizione, s.costo, count(oid)*s.costo as costo_spedizioni_tot, pag.nome as metodo_pagamento, pag.costo, count(oid)*pag.costo as costo_pagamento_tot FROM pasp01 pa JOIN spedizione s ON pa.spid = s.spid RIGHT JOIN ordine o ON o.paspid = pa.paspid JOIN pagamento pag ON pa.paid = pag.paid GROUP BY s.nome, pag.nome;"
    # special print
    with pd.option_context('display.max_rows', None,
                           'display.max_columns', None,
                           'display.precision', 3,
                           ):
        print("\n9 QUALI SONO I METODI DI PAGAMENTO E SPEDIZIONE PRINCIPALI?\n", choose_table(sql9a))


# QUERY 10: A QUALI CITTA E PROVINCE SI SPEDISCE DI PIU'?
if True:
    sql10a = "SELECT provincia, citta, count(citta) as numero_indirizzi_utente FROM indirizzo GROUP BY provincia, citta ORDER BY provincia, numero_indirizzi_utente DESC;"
    sql10b = "SELECT provincia, count(citta) as numero_indirizzi_utente FROM indirizzo GROUP BY provincia ORDER BY numero_indirizzi_utente DESC;"
    print("\n10a A QUALI CITTA SI SPEDISCE DI PIU'?\n", choose_table(sql10a))
    print("Città: Roma, Milano")
    print("\n10b A QUALI PROVINCE SI SPEDISCE DI PIU'\n?", choose_table(sql10b))
    print("Province: Roma, Milano")

# Thank you

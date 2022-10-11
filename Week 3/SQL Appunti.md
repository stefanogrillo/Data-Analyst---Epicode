# MySQL, SQLite

### Dati binari:
- binary[(n)] ha una lunghezza fissa e può contenere fino ad 8000 bytes di dati
binari
- varbinary[(n)] ha una lunghezza variabile e può contenere fino ad 8000 bytes di dati binari

### Dati carattere: varchar SQL
- char[(n)] ha una lunghezza fissa e può contenere fino ad 8000 caratteri ANSI (cioè 8000 bytes)
- varchar[(n)] ha una lunghezza variabile e può contenere fino ad 8000 caratteri ANSI (cioè 8000 bytes)
- nchar[(n)] ha una lunghezza fissa e può contenere fino a 4000 caratteri UNICODE (cioè 8000 bytes, ricordiamo che per i caratteri UNICODE servono 2 bytes per memorizzare un carattere)
- nvarchar[(n)] ha una lunghezza variabile e può contenere fino a 4000 caratteri UNICODE (cioè 8000 bytes, ricordiamo che per i caratteri UNICODE servono 2 bytes per memorizzare un carattere)

### Dati ora e data:
- datetime ammette valori compresi dal 1 gennaio 1753 al 31 dicembre 9999 (precisione al trecentesimo di secondo), occupa uno spazio di 8 byte
- smalldatetime meno preciso del precedente (precisione al minuto), occupa uno spazio di 4 byte
- date aaaa-mm-gg
- time hh-mm-ss
- year aaaa
- timestamp(x) variabile a seconda di x, da 2 a 14

### Dati monetari:
- money Contiene valori monetari da -922337203685477.5808 a 922337203685477.5807 con una precisione al decimillesimo di unità monetaria, occupa 8 bytes di memoria
- smallmoney Contiene valori monetari da - 214748.3648 a 214748.3647 con una precisione al decimillesimo di unità monetaria, occupa 4 bytes di memoria.

### Dati numerici approssimati: SQL float 
- float[(n)] Contiene numeri a virgola mobile positivi e negativi, compresi tra 2.23E-308 e 1.79E308 per i valori positivi e tra -2.23E-308 e -1.79E308 per i valori negativi, occupa 8 bytes di memoria ed ha una precisione di 15 cifre
- double Come float, ma doppio della precisione
- real Contiene numeri a virgola mobile positivi e negativi comprese tra 1.18E-38 e 3.40E38 per i valori positivi e tra -1.18E-38 e -3.40E38 per i valori negativi, occupa 4 bytes di memoria ed ha una precisione di 7 cifre

### Dati numerici esatti: SLQ int
- decimal[(p[, s])]
- numeric[(p[, s])] decimal e numeric sono sinonimi per SQL Server 7, possono avere
valori compresi tra 10^38 - 1 e - 10^38 -1. La memoria che occupano
per essere immagazzinati varia a seconda della precisione che
utilizziamo per rappresentarli, da un minimo di 2 bytes a un massimo
di 17 bytes dove _p_ è la precisione (che rappresenta il numero massimo di cifre
decimali che possono essere memorizzate (da entrambe le parti della
virgola), e il massimo della precisione è 28 cifre) e _s_ è la scala, che rappresenta il numero di massimo di cifre decimali dopo la virgola e deve essere minore od uguale alla precisione.
- int occupa 4 byte di memoria e memorizza i valori da -2147483648 a 2147483647
- smallint occupa 2 byte di memoria e memorizza i valori da -32768 a 32,767
- tinyint occupa 1 byte di memoria e memorizza i valori da 0 a 255

### Dati speciali su SQL server:
- bit tipicamente è usato per rappresentare i flag, vero/false o true/false o si/no, perché può accettare solo due valori 0 o 1. Occupa un bit ovviamente. Le colonne che hanno un tipo dati bit non possono avere valori nulli e non possono avere indici. 
- cursor sono usati come varibili in stored proc oppure come parametri di OUTPUT sempre in stored proc, fanno riferimento ai cursori. Possono essere nulli e non possono essere usati con le istruzioni CREATE TABLE.
- sysname una varchar di 128 caratteri ed occupa 256 bytes, viene usato per assegnare i nomi ad ogggetti del database, come tabelle, procedure, triggere, indici, ecc...
- timestamp occupa 8 bytes ed è un contatore incrementale per colonna assegnato automaticamente da SQL Server 7.
- UNIQUEIDENTIFIER (GUID) E' un identificatore unico a livello globale di 16 byte di lunghezza chiamato anche GUID. E' generato (molto lentamente) automaticamente da SQL Server.

### Dati text ed image:
I dati di questo tipo, non vengono memorizzati nelle normali pagine dati di SQL Server, ma sono tratati in modo speciale su apposite pagine di memorizzazione.
- text un tipo dati a lunghezza variabile, che può memorizzare fino a 2147483647 caratteri.
- ntext come il precedente ma memorizza caratteri UNICODE, quindi fino alla metà del precedente, cioè 1073741823 caratteri.
- image può memorizzare fino a 2147483647 bytes di dati binari, è solitamente usato per le immagini.
- blob (Binary Large Object) file o immagine.

## SQL 
In SQL le interrogazioni sono formulate in modo dichiarativo, ossia si specifica che cosa si vuole ottenere.
```sql
SELECT <what> FROM <tablewhereiswhatwewant> WHERE <conditions>; 
```
Nelle interrogazioni possiamo scegliere uno o più elementi, separati da virgola. Se li vogliamo tutti, usiamo *. <br>
Possiamo anche mettere degli alias alle tabelle (dove si trovano le informazioni che vogliamo in forma di righe). 
```sql
SELECT <alias>.<what1>, <alias>.<what2> FROM <tablewhereiswhatwewant> AS <alias> WHERE <conditions>; 
```
WHERE ci permette di scrivere tutte le condizioni che vogliamo con gli operatori: =, <, >, !=, <> (diverso), <=, >=, BETWEEN ... AND ..., IN (appartenente a), LIKE, IS NULL, IS NOT NULL, NOT, AND, OR. <br>
LIKE si usa per i confronti con stringhe. Si usano i caratteri speciali: _ (per un solo carattere arbitrario) e % (per più caratteri arbitrari).
```sql
SELECT f.reddito FROM famiglia AS f WHERE f.name LIKE "_t%o"; 
```

### Commands and Clauses
SELECT (data), FROM (table), WHERE (filter), AS (rename as alias), JOIN (combine rows), AND (combine conditions), OR (combine conditions), LIMIT (limit the returned rows), IN (specify multiple values with where), CASE (return value in specified condition), NOT, IS NULL (where is null), LIKE (search pattern), COMMIT (write transaction to DB), ROLL BACK (undo a transaction)

ALTER TABLE (add/remove columns), UPDATE (update data), CREATE (tables, datasets, views, index), DELETE (rows), INSERT (add single row), DROP (delete tables, datasets, index)

GROUP BY (data by common element), ORDER BY (DESC/ASC order of view), HAVING (same as WHERE but for the following operations), COUNT(), SUM(), AVG(), MAX(), MIN()

### JOINS
- INNER JOIN: only common elements between group A and group B. Not corresponding elements are excluded
- LEFT OUTER JOIN: all elements from group A (if at left) and common elements from group B. Not corresponding left elements are filled with "null"
- RIGHT OUTER JOIN: as above, but for right group B (if at right). Not corresponding right elements are filled with "null"
- FULL OUTER JOIN: all elements from group A and group B. Not corresponding elements are filled with "null"
 
## Data
| - | Left | Matching | Right | Unmatching Data from Left | Unmatching Data from Right |
| - | - | - | - | - | - |
| INNER JOIN | - | yes | - | no | no |
| LEFT OUTER JOIN | yes | yes | - | as null | no |
| RIGHT OUTER JOIN | - | yes | yes | no | as null |
| FULL OUTER JOIN | yes | yes | yes | as null | as null |

## Columns
| - | Left | Matching Columns are repeated? | Right | 
| - | - | - | - | 
| INNER JOIN | yes | no | yes | 
| LEFT OUTER JOIN | yes | yes | yes | 
| RIGHT OUTER JOIN | yes | yes | yes | 
| FULL OUTER JOIN | yes | yes | yes |

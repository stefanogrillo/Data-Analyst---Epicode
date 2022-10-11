# MySQL, SQLite

### Dati binari:
- __binary__ ha una lunghezza fissa e può contenere fino ad 8000 bytes di dati binari
- __varbinary__ ha una lunghezza variabile e può contenere fino ad 8000 bytes di dati binari

### Dati carattere: varchar SQL
- __char__ ha una lunghezza fissa e può contenere fino ad 8000 caratteri ANSI (cioè 8000 bytes)
- __varchar__ ha una lunghezza variabile e può contenere fino ad 8000 caratteri ANSI (cioè 8000 bytes)
- __nchar__ ha una lunghezza fissa e può contenere fino a 4000 caratteri UNICODE (cioè 8000 bytes, ricordiamo che per i caratteri UNICODE servono 2 bytes per memorizzare un carattere)
- __nvarchar__ ha una lunghezza variabile e può contenere fino a 4000 caratteri UNICODE (cioè 8000 bytes, ricordiamo che per i caratteri UNICODE servono 2 bytes per memorizzare un carattere)

### Dati ora e data:
- __datetime__ ammette valori compresi dal 1 gennaio 1753 al 31 dicembre 9999 (precisione al trecentesimo di secondo), occupa uno spazio di 8 byte
- __smalldatetime__ meno preciso del precedente (precisione al minuto), occupa uno spazio di 4 byte
- __date__ aaaa-mm-gg
- __time__ hh-mm-ss
- __year__ aaaa
- __timestamp(x)__ variabile a seconda di x, da 2 a 14

### Dati monetari:
- __money__ Contiene valori monetari da -922337203685477.5808 a 922337203685477.5807 con una precisione al decimillesimo di unità monetaria, occupa 8 bytes di memoria
- __smallmoney__ Contiene valori monetari da - 214748.3648 a 214748.3647 con una precisione al decimillesimo di unità monetaria, occupa 4 bytes di memoria.

### Dati numerici approssimati: SQL float 
- __float__ Contiene numeri a virgola mobile positivi e negativi, compresi tra 2.23E-308 e 1.79E308 per i valori positivi e tra -2.23E-308 e -1.79E308 per i valori negativi, occupa 8 bytes di memoria ed ha una precisione di 15 cifre
- __double__ Come float, ma doppio della precisione
- __real__ Contiene numeri a virgola mobile positivi e negativi comprese tra 1.18E-38 e 3.40E38 per i valori positivi e tra -1.18E-38 e -3.40E38 per i valori negativi, occupa 4 bytes di memoria ed ha una precisione di 7 cifre

### Dati numerici esatti: SLQ int
- __decimal[(p[, s])]__
- __numeric[(p[, s])]__ decimal e numeric sono sinonimi per SQL Server 7, possono avere valori compresi tra 10^38 - 1 e - 10^38 -1. La memoria che occupano per essere immagazzinati varia a seconda della precisione che utilizziamo per rappresentarli, da un minimo di 2 bytes a un massimo di 17 bytes dove _p_ è la precisione (che rappresenta il numero massimo di cifre decimali che possono essere memorizzate (da entrambe le parti della virgola), e il massimo della precisione è 28 cifre) e _s_ è la scala, che rappresenta il numero di massimo di cifre decimali dopo la virgola e deve essere minore od uguale alla precisione.
- __int__ occupa 4 byte di memoria e memorizza i valori da -2147483648 a 2147483647
- __smallint__ occupa 2 byte di memoria e memorizza i valori da -32768 a 32,767
- __tinyint__ occupa 1 byte di memoria e memorizza i valori da 0 a 255

### Dati speciali su SQL server:
- __bit__ tipicamente è usato per rappresentare i flag, vero/false o true/false o si/no, perché può accettare solo due valori 0 o 1. Occupa un bit ovviamente. Le colonne che hanno un tipo dati bit non possono avere valori nulli e non possono avere indici. 
- __cursor__ sono usati come varibili in stored proc oppure come parametri di OUTPUT sempre in stored proc, fanno riferimento ai cursori. Possono essere nulli e non possono essere usati con le istruzioni CREATE TABLE.
- __sysname__ una varchar di 128 caratteri ed occupa 256 bytes, viene usato per assegnare i nomi ad ogggetti del database, come tabelle, procedure, triggere, indici, ecc...
- __timestamp__ occupa 8 bytes ed è un contatore incrementale per colonna assegnato automaticamente da SQL Server 7.
- __UNIQUEIDENTIFIER__ E' un identificatore unico a livello globale di 16 byte di lunghezza chiamato anche GUID. E' generato (molto lentamente) automaticamente da SQL Server.

### Dati text ed image:
I dati di questo tipo, non vengono memorizzati nelle normali pagine dati di SQL Server, ma sono tratati in modo speciale su apposite pagine di memorizzazione.
- __text__ un tipo dati a lunghezza variabile, che può memorizzare fino a 2147483647 caratteri.
- __ntext__ come il precedente ma memorizza caratteri UNICODE, quindi fino alla metà del precedente, cioè 1073741823 caratteri.
- __image__ può memorizzare fino a 2147483647 bytes di dati binari, è solitamente usato per le immagini.
- __blob__ (Binary Large Object) file o immagine.

## SQL 
In SQL le interrogazioni sono formulate in modo dichiarativo, ossia si specifica che cosa si vuole ottenere.
```sql
SELECT <what> FROM <tablewhereiswhatwewant> WHERE <conditions>; 
```
Nelle interrogazioni possiamo scegliere uno o più elementi, separati da virgola. Se li vogliamo tutti, usiamo __*__. <br>
Possiamo anche mettere degli alias alle tabelle (dove si trovano le informazioni che vogliamo in forma di righe). 
```sql
SELECT <alias>.<what1>, <alias>.<what2> FROM <tablewhereiswhatwewant> AS <alias> WHERE <conditions>; 
```
__WHERE__ ci permette di scrivere tutte le condizioni che vogliamo con gli operatori: __=_, <, >, !=, <>__ (diverso)__, <=, >=, BETWEEN ... AND ..., IN__ (appartenente a)__, LIKE, IS NULL, IS NOT NULL, NOT, AND, OR__. <br>
LIKE si usa per i confronti con stringhe. Si usano i caratteri speciali: _  (per un solo carattere arbitrario) e __%__ (per più caratteri arbitrari).
```sql
SELECT f.reddito FROM famiglia AS f WHERE f.name LIKE "_t%o"; 
```

### Commands and Clauses
__SELECT__ (data), __FROM__ (table), __WHERE__ (filter), __AS__ (rename as alias), __JOIN__ (combine rows), __AND__ (combine conditions), __OR__ (combine conditions), __LIMIT__ (limit the returned rows), __IN__ (specify multiple values with where), __CASE__ (return value in specified condition), __NOT, IS NULL__ (where is null), __LIKE__ (search pattern), __COMMIT__ (write transaction to DB), __ROLL BACK__ (undo a transaction)

__ALTER TABLE__ (add/remove columns), __UPDATE__ (update data), __CREATE__ (tables, datasets, views, index), __DELETE__ (rows), __INSERT__ (add single row), __DROP__ (delete tables, datasets, index)

__GROUP BY__ (data by common element), __ORDER BY__ (__DESC/ASC__ order of view), __HAVING__ (same as WHERE but for the following operations), __COUNT(), SUM(), AVG(), MAX(), MIN()__

### JOINS 
- __INNER JOIN__: only matching values between table A and table B. Not corresponding elements are excluded
- __LEFT OUTER JOIN__: all values from table A (if at left) and matching values from table B. Not corresponding left values are filled with "null"
- __RIGHT OUTER JOIN__: as above, but for right table B (if at right). Not corresponding right values are filled with "null"
- __FULL OUTER JOIN__: all values from group A and group B. Not matching values are filled with "null"
 
## Data
| __What Data is shown?__ | __Left__ | __Matching__ | __Right__ | __Unmatching Data from Left__ | __Unmatching Data from Right__ |
| - | - | - | - | - | - |
| INNER JOIN | - | yes | - | no | no |
| LEFT OUTER JOIN | yes | yes | - | shown, missing data for new columns is null | no |
| RIGHT OUTER JOIN | - | yes | yes | no | shown, missing data for new columns is null |
| FULL OUTER JOIN | yes | yes | yes | shown, missing data for new columns is null | shown, missing data for new columns is null |

Columns behave differently. Only chosen columns will appear. 

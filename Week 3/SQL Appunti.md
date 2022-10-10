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

# Progetto Tableau

Questi file si basano sull'analisi di due servizi per clienti. L'analisi si focalizza sulla Revenue e sulle Coorti. Qui si seguito i codici.

[File Servizio 1](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/4d4e6a56d7e36363586662737e4c306b330d5130/Week%206/Day%204/Progetto_Service_1.twb)

[File Servizio 2](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/4d4e6a56d7e36363586662737e4c306b330d5130/Week%206/Day%204/Progetto_Service_2.twb)

### Pre-Lavorazione

Vogliamo creare dei campi calcolati che ci serviranno per migliorare la nostra analisi.

1. Prima Data 
Questo campo calcolato rappresenta il primo accesso al marketplace. 
```
{ FIXED [Click Id]: MIN([Postback Timestamp]) }
```

2. Ripetizione
Questo campo calcolato è una ricerca degli User che non fanno un secondo accesso al nostro marketplace.
```
IF [Postback Timestamp]>[Prima Data] THEN [Postback Timestamp] ELSE NULL END
```

3. Seconda Data
Questo campo calcolato rappresenta l'ultimo accesso al marketplace.
```
{ FIXED [Click Id]:MAX([Ripetizione]) }
```

4. Giorni di Differenza
L'obiettivo è contare la distanza tra la Prima e l'ultima Data.
```
DATEDIFF('day', [Prima Data], [Seconda Data])
```

5. Prima Data Time-Zone
Si creano fasce orarie da studiare.
```
IF DATEPART('hour',[Prima Data]) > 1 AND DATEPART('hour',[Prima Data]) < 8 THEN 'Notte'
ELSEIF DATEPART('hour',[Prima Data]) >= 8 AND DATEPART('hour',[Prima Data]) < 12 THEN 'Mattina'
ELSEIF DATEPART('hour',[Prima Data]) >= 12 AND DATEPART('hour',[Prima Data]) < 18 THEN 'Pomeriggio'
ELSE 'Sera'
END
```

6. Seconda Data Time-Zone
Si creano fasce orarie da studiare.
```
IF DATEPART('hour',[Seconda Data]) > 1 AND DATEPART('hour',[Seconda Data]) < 8 THEN 'Notte'
ELSEIF DATEPART('hour',[Seconda Data]) >= 8 AND DATEPART('hour',[Seconda Data]) < 12 THEN 'Mattina'
ELSEIF DATEPART('hour',[Seconda Data]) >= 12 AND DATEPART('hour',[Seconda Data]) < 18 THEN 'Pomeriggio'
ELSE 'Sera'
END
```

7. Conversion / Click Id
Metrica di paragone tra marketplaces/datasets
```
COUNT([Conversion Type]) / COUNTD([Click Id])
```

# Analisi 

Il primo passaggio che facciamo nell'analisi è capire quali tipi di _Convesioni_ restituiscono della _Revenue_. Come si può vedere, il Servizio 2 ha più Split, che oltretutto rendono di più.
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/a84c1ea7f462f71689bb25d54ee0f147549f81b4/Week%206/Day%204/Servizio%201/1.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/046802529bc467ec73917551d51354b4c5b43e69/Week%206/Day%204/Servizio%202/1.JPG) |

Il passaggio successivo è vedere quanta _Revenue_ ogni _Conversione_ produce (visualizzazione in tabella alternativa al grafico precedente). Qui si conferma il fatto che il Servizio 2 rende più in termini di _Revenue_.
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/a84c1ea7f462f71689bb25d54ee0f147549f81b4/Week%206/Day%204/Servizio%201/2.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/2ff9612554db7d599995934eeb3dca9c788ed55a/Week%206/Day%204/Servizio%202/24.JPG) |

Dopodiché, vogliamo osservare quando ci sono stati più Split, per mese. Per entrambi i Servizi, il massimo è avvenuto ad Agosto.
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/2ff9612554db7d599995934eeb3dca9c788ed55a/Week%206/Day%204/Servizio%201/3.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/2ff9612554db7d599995934eeb3dca9c788ed55a/Week%206/Day%204/Servizio%202/2.JPG) |

La Revenue che _Split_ rappresenta, da quali   

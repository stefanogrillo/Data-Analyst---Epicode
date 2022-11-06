# Progetto Tableau

Questi file si basano sull'analisi di due servizi per clienti. L'analisi si focalizza sulla Revenue e sulle Coorti. Qui si seguito i codici.

[File Servizio 1](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/4d4e6a56d7e36363586662737e4c306b330d5130/Week%206/Day%204/Progetto_Service_1.twb)

[File Servizio 2](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/4d4e6a56d7e36363586662737e4c306b330d5130/Week%206/Day%204/Progetto_Service_2.twb)

# Pre-Analisi

Vogliamo creare dei campi calcolati che ci serviranno per migliorare la nostra analisi.

<b>Prima Data</b> <br>
Questo campo calcolato rappresenta il primo accesso al marketplace. 
```
{ FIXED [Click Id]: MIN([Postback Timestamp]) }
```

<b>Ripetizione</b><br>
Questo campo calcolato è una ricerca degli User che non fanno un secondo accesso al nostro marketplace.
```
IF [Postback Timestamp]>[Prima Data] THEN [Postback Timestamp] ELSE NULL END
```

<b>Seconda Data</b><br>
Questo campo calcolato rappresenta l'ultimo accesso al marketplace.
```
{ FIXED [Click Id]:MAX([Ripetizione]) }
```

<b>Giorni di Differenza</b><br>
L'obiettivo è contare la distanza tra la Prima e l'ultima Data.
```
DATEDIFF('day', [Prima Data], [Seconda Data])
```

<b>Prima Data Time-Zone</b><br>
Si creano fasce orarie da studiare.
```
IF DATEPART('hour',[Prima Data]) > 1 AND DATEPART('hour',[Prima Data]) < 8 THEN 'Notte'
ELSEIF DATEPART('hour',[Prima Data]) >= 8 AND DATEPART('hour',[Prima Data]) < 12 THEN 'Mattina'
ELSEIF DATEPART('hour',[Prima Data]) >= 12 AND DATEPART('hour',[Prima Data]) < 18 THEN 'Pomeriggio'
ELSE 'Sera'
END
```

<b>Seconda Data Time-Zone</b><br>
Si creano fasce orarie da studiare.
```
IF DATEPART('hour',[Seconda Data]) > 1 AND DATEPART('hour',[Seconda Data]) < 8 THEN 'Notte'
ELSEIF DATEPART('hour',[Seconda Data]) >= 8 AND DATEPART('hour',[Seconda Data]) < 12 THEN 'Mattina'
ELSEIF DATEPART('hour',[Seconda Data]) >= 12 AND DATEPART('hour',[Seconda Data]) < 18 THEN 'Pomeriggio'
ELSE 'Sera'
END
```

<b>Conversion / Click Id</b><br>
Metrica di paragone tra marketplaces/datasets
```
COUNT([Conversion Type]) / COUNTD([Click Id])
```

<b>Revenue / Click Id (univoco)</b><br>
Metrica di paragone tra marketplaces/datasets
```
SUM([Cast Revenue]) / COUNTD([Click Id])
```

<b>Split / Click Id (univoco)</b><br>
Metrica di paragone tra marketplaces/datasets
```
SUM(IF [Conversion Type]="split" THEN 1 END) / COUNT([Click Id])
```

# Analisi 

Qual è il tipo di Conversion Type che genera Revenue? Come si può vedere, il Servizio 2 ha più Split, che oltretutto rendono di più.
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/a84c1ea7f462f71689bb25d54ee0f147549f81b4/Week%206/Day%204/Servizio%201/1.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/046802529bc467ec73917551d51354b4c5b43e69/Week%206/Day%204/Servizio%202/1.JPG) |

Come si sviluppa la Revenue nel Tempo e per Click Id? Qui si conferma il fatto che il Servizio 2 rende più in termini di Revenue.
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/a84c1ea7f462f71689bb25d54ee0f147549f81b4/Week%206/Day%204/Servizio%201/2.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/2ff9612554db7d599995934eeb3dca9c788ed55a/Week%206/Day%204/Servizio%202/24.JPG) |

Quando ci sono stati più Split?  Per entrambi i Servizi, il massimo è avvenuto ad Agosto.
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/2ff9612554db7d599995934eeb3dca9c788ed55a/Week%206/Day%204/Servizio%201/3.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/2ff9612554db7d599995934eeb3dca9c788ed55a/Week%206/Day%204/Servizio%202/2.JPG) |

Il Conversion Type Split che quantità ha generato per Purchase Type? In entrambi i Servizi, "Credito" ha reso di più.
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/0a1a5fe7fa28a3f2cc5b05b133d648708703a995/Week%206/Day%204/Servizio%201/4.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/2ff9612554db7d599995934eeb3dca9c788ed55a/Week%206/Day%204/Servizio%202/3.JPG) |

Il Conversion Type Split quanto Revenue ha generato per Purchase Type? In entrambi i Servizi, "Credito" ha reso di più.
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/0a1a5fe7fa28a3f2cc5b05b133d648708703a995/Week%206/Day%204/Servizio%201/5.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/14b731202f30d53fb350ecaf328c57c41f1561f7/Week%206/Day%204/Servizio%202/4.JPG) |

Il Conversion Type Split quanto Revenue ha generato per Purchase Type? Il Servizio 2 si riconferma migliore in termini di prestazioni.
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/14b731202f30d53fb350ecaf328c57c41f1561f7/Week%206/Day%204/Servizio%201/6.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/14b731202f30d53fb350ecaf328c57c41f1561f7/Week%206/Day%204/Servizio%202/5.jpg) |

Il Conversion Type Split quanto Revenue potrebbe generare per Purchase Type? Il Servizio 2 in termini di predizione di Revenue ha meno gap del Servizio 1. 
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/14b731202f30d53fb350ecaf328c57c41f1561f7/Week%206/Day%204/Servizio%201/7.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/14b731202f30d53fb350ecaf328c57c41f1561f7/Week%206/Day%204/Servizio%202/6.JPG) |

A quanto ammonta in media una Purchase per Purchase Type? 
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/14b731202f30d53fb350ecaf328c57c41f1561f7/Week%206/Day%204/Servizio%201/8.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/14b731202f30d53fb350ecaf328c57c41f1561f7/Week%206/Day%204/Servizio%202/7.JPG) |

Che cosa vendiamo per Abbonamento?
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/14b731202f30d53fb350ecaf328c57c41f1561f7/Week%206/Day%204/Servizio%201/9.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/14b731202f30d53fb350ecaf328c57c41f1561f7/Week%206/Day%204/Servizio%202/8.JPG) |

Che cosa vendiamo per Crediti?
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/14b731202f30d53fb350ecaf328c57c41f1561f7/Week%206/Day%204/Servizio%201/10.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/14b731202f30d53fb350ecaf328c57c41f1561f7/Week%206/Day%204/Servizio%202/9.JPG) |

Quanta Revenue viene prodotta da un Click Id e a quanti Giorni di Distanza?
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%201/11.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%202/10.JPG) |

Quanta Revenue viene prodotta da un Click Id e a quanti Giorni di Distanza? (Versione B)
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%201/12.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%202/11.JPG) |

Quanta Revenue viene prodotta in base all'ora di utilizzo nel primo giorno di accesso? A quanti Click Id corrisponde?
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%201/13.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%202/12.JPG) |

Quanta Revenue viene prodotta in base all'ora di utilizzo nel primo giorno di accesso? A quanti Click Id corrisponde?
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%201/14.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%202/13.JPG) |

Quanta Revenue viene prodotta in base all'ora di utilizzo nel primo giorno di accesso per "purchase_uomo"? A quanti Click Id corrisponde? 
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%201/15.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%202/14.JPG) |

Quanta Revenue viene prodotta in base all'ora di utilizzo nell'ultimo giorno di accesso? A quanti Click Id corrisponde?
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%201/16.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%202/15.JPG) |

Quanta Revenue viene prodotta in base all'ora di utilizzo nell'ultimo giorno di accesso? A quanti Click Id corrisponde?
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%201/17.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%202/16.JPG) |

Studio delle Conversion Type: chi ha fatto cosa?
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%201/18.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%202/17.JPG) |

Studio delle Conversion Type: Primo e Secondo Giorno
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%201/19.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%202/18.JPG) |

Studio delle Conversion Type: Primo e Secondo Giorno
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%201/20.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%202/19.JPG) |

Studio delle Conversion Type: ordine storico delle operazioni di un Utente
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%201/21.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%202/20.JPG) |

Metriche di Resa (non Revenue)
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%201/22.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%202/21.JPG) |

Tutte queste analisi sono state raccolte in 4 Storie (2 per Servizio)
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%201/23.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%202/22.JPG) |

Pre-Sale + Post-Sale
| Servizio 1 | Servizio 2 |
| - | - | 
| ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%201/24%20pre+post.JPG) | ![alt](https://github.com/stefanogrillo/Data-Analyst---Epicode/blob/49c7cfa9c1ca1cee050c5dbe1ae84662e27b11e3/Week%206/Day%204/Servizio%202/23%20pre+post.JPG) |

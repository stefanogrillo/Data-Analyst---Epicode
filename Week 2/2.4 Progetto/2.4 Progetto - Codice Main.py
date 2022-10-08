import csv
import statistics as s
import datetime
from main import selected_country_variables, inhabitants, new_daily, new_date, first_case



###     PRE-ANALISI

path = ('C:\\Users\\elste\\Desktop\\epicode\\2_Week\\Day_4\\owid_covid_data.csv')
with open(path, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    # print("reader è di tipo ", type(reader))
    # class = '_csv.reader'


    # Per praticità, la voglio trasformare in una lista di liste, con lunghezza e con struttura come segue
    list_of_rows = list(reader)
    print("Il numero di liste è {:,.2f}".format(len(list_of_rows)))
    print(list_of_rows[0:2])


    # Per ridurre il numero di variabili, dal Header recupero gli indici delle variabili che mi interessano:
    print("continent ", list_of_rows[0].index('continent'))
    print("location ", list_of_rows[0].index('location'))
    print("date", list_of_rows[0].index('date'))
    print("new_cases ", list_of_rows[0].index('new_cases'))
    print("new_deaths ", list_of_rows[0].index('new_deaths'))
    print("new_vaccinations_smoothed ", list_of_rows[0].index('new_vaccinations_smoothed'))
    print("population ", list_of_rows[0].index('population'))


    # Lista degli indici di colonna che mi interessano
    lista = [1,2,3,5,8,39,48]
    print("\n")

    """
    Ho scelto queste variabili perché: 
    - Continent mi permette di selezionare i continenti che voglio: North America e Europe
    - Location mi permette di selezionare i paesi che voglio: Italy e Germany
    - Date (non implementato)
    - New cases mi permette di vedere l'andamento giornaliero di Nuovi Casi, e di calcolarne il totale
    - New deaths mi permette di vedere l'andamento giornaliero di Nuove Morti, e di calcolarne il totale
    - New vaccinations smooth mi permette di vedere l'andamento giornaliero mediato su 7 giorni (ha più valori rispetto
      a "new vaccinations)
    - Population mi permette di comprendere le dimensioni dei continenti e degli Stati/Paesi
    """




###     ANALISI

##### NORTH AMERICA
    print("NORTH AMERICA")
    # Voglio estrarre solo i valori corrispondenti al continente "North America"
    america = selected_country_variables(list_of_rows, 1, 'North America', 1, 'North America', lista)
    # america = selected_country(nuova, 0, 'North America')
    # print(america[0])
    print(" ")


    # Zero: Starting Date
    date_list, counter_date = new_date(america, 2)

    print("Starting Date:", min(date_list))

    paese1NA = selected_country_variables(list_of_rows, 1, 'North America', 3, '2020-01-06', [2, 5])
    print("First Count:", paese1NA)

    temporanea1NA = selected_country_variables(list_of_rows, 1, 'North America', 4, ['1.0', '2.0', '3.0'], [2, 3, 4, 8])
    first1_NA = first_case(temporanea1NA)
    paese2NA = selected_country_variables(temporanea1NA, 1, first1_NA, 1, first1_NA, [0, 1, 2])
    print("First Case:", paese2NA)

    temporanea2NA = selected_country_variables(list_of_rows, 1, 'North America', 7, ['1.0', '2.0', '3.0'], [2, 3, 5, 8])
    first2_NA = first_case(temporanea2NA)
    paese3NA = selected_country_variables(temporanea2NA, 1, first2_NA, 1, first2_NA, [0, 1, 3])
    print("First Death:", paese3NA)
    print(" ")
    # Il Messico ha iniziato a raccogliere dati dal 1 Gennaio 2020, ma il primo caso nel continente è avvenuto il
    # 22 Gennaio negli Stati Uniti. La prima morte è avvenuta negli Stati Uniti il 29 Febbraio 2020.


    # First: Total inhabitants in North America
    persone_NA = inhabitants(america)
    print("Numero Abitanti in {}: {:,.2f}".format(america[0][0], persone_NA))
    print(" ")


    # Second: Total New Daily Cases in North America
    new_daily_cases_NA, cases_tot_NA, counter_cases_NA = new_daily(america, 3)
    print("Casi Totali nel Nord America: {:,.2f}".format(cases_tot_NA))

    print("Percentuale di Ammalati sulla Popolazione: {:,.2f} %".format((cases_tot_NA * 100) / persone_NA))

    print("Media Giornaliera di Nuovi Ammalati: {:,.2f}".format(s.mean(new_daily_cases_NA)))

    print("Valori Mancanti: {:,.2f} \nValori Totali: {:,.2f} \nPercentuale Mancanti: {:,.2f} %".format(counter_cases_NA,
            len(america), (counter_cases_NA * 100 / len(america))))
    if (counter_cases_NA * 100 / len(america)) < 5.0:
        print("Meno del 5% di osservazioni è mancante")
    else:
        print("Più del 5% di osservazioni è mancante: perché?")

    print("Mediana: {:,.2f}".format(s.median(new_daily_cases_NA)))

    print("Massimo Nuovi Casi Giornalieri: {:,.2f}".format(max(new_daily_cases_NA)))

    print("Minimo Nuovi Casi Giornalieri: {:,.2f}".format(min(new_daily_cases_NA)))
    print(" ")
    # Le osservazioni sul numero di casi rivelano che più del 5% di osservazioni è mancante. Questo indica o una
    # mancanza di dati ufficiali o che l'arrivo del virus nel Continente è da datare dopo l'inizio della pandemia
    # (inizio osservazioni).


    # Third: Total New Daily Deaths in North America
    new_daily_deaths_NA, deaths_tot_NA, counter_deaths_NA = new_daily(america, 4)
    print("Morti Totali: {:,.2f}".format(sum(new_daily_deaths_NA)))

    print("Percentuale di Morti sugli Ammalati: {:,.2f} %".format(sum(new_daily_deaths_NA) * 100 / cases_tot_NA))

    print("Percentuale di Morti sugli Abitanti: {:,.2f} %".format(sum(new_daily_deaths_NA) * 100 / persone_NA))

    print("Media Giornaliera di Nuovi Morti: {:,.2f}".format(s.mean(new_daily_deaths_NA)))

    print("Valori Mancanti: {:,.2f} \nValori Totali: {:,.2f} \nPercentuale Mancanti: {:,.2f} %".format(counter_deaths_NA,
            len(america), (counter_deaths_NA * 100 / len(america))))
    if (counter_deaths_NA * 100 / len(america)) < 5.0:
        print("Meno del 5% di osservazioni è mancante")
    else:
        print("Più del 5% di osservazioni è mancante: perché?")

    print("Mediana: {:,.2f}".format(s.median(new_daily_deaths_NA)))

    print("Massimo Nuove Morti Giornaliere: {:,.2f}".format(max(new_daily_deaths_NA)))

    print("Minimo Nuove Morti Giornaliere: {:,.2f}".format(min(new_daily_deaths_NA)))
    print(" ")
    # I valori mancanti nella variabile "nuove morti" identifica o una mancanza di dati ufficiali sulle morti da COVID
    # o un minore effetto sul Continente rispetto al numero di ammalati.


    # Fourth: Total New Vaccinations Smoothed in North America
    new_daily_vacc_NA, vacc_tot_NA, counter_vacc_NA = new_daily(america, 5)
    print("Vaccinazioni Totali: {:,.2f} \nPercentuale della Popolazione: {:,.2f} %".format(sum(new_daily_vacc_NA), (
            vacc_tot_NA * 100) / persone_NA))

    print("Percentuale di Vaccinazioni su Ammalati: {:.2f} %".format(sum(new_daily_vacc_NA) * 100 / cases_tot_NA))

    print("Media di Nuove Vaccinazioni Giornaliere: {:,.2f}".format(s.mean(new_daily_vacc_NA)))

    print("Valori Mancanti: {:,.2f} \nValori Totali: {:,.2f} \nPercentuale Mancanti: {:,.2f} %".format(counter_vacc_NA,
            len(america), (counter_vacc_NA * 100 / len(america))))
    if (counter_vacc_NA * 100 / len(america)) < 5.0:
        print("Meno del 5% di osservazioni è mancante")
    else:
        print("Più del 5% di osservazioni è mancante: perché?")

    print("Mediana delle Vaccinazioni: {:,.2f}".format(s.median(new_daily_vacc_NA)))

    print("Massimo Nuove Vaccinazioni Giornaliere: {:,.2f}".format(max(new_daily_vacc_NA)))

    print("Minimo Nuove Vaccinazioni Giornaliere: {:,.2f}".format(min(new_daily_vacc_NA)))
    print("\n")
    # E' da notare che le vaccinazioni sono partite molto in ritardo rispetto all'inizio dell'epidemia. Questo va
    # ricordato nel momento in cui si valuta il significato statistico della media in paragone ai valori mancanti:
    # quei valori non potevano esserci perché non esisteva il vaccino.


##### EUROPA
    print("EUROPA")
    # Voglio estrarre solo i valori corrispondenti al continente "Europa"
    europa = selected_country_variables(list_of_rows, 1, 'Europe', 1, 'Europe', lista)
    #print(europa[0])
    print(" ")

    # Zero: Starting Date
    date_list, counter_date = new_date(europa, 2)

    print("Starting Date:", min(date_list))

    paese1EU = selected_country_variables(list_of_rows, 1, 'Europe', 3, '2020-01-06', [2, 5])
    print("First Count:", paese1EU)

    temporanea1EU = selected_country_variables(list_of_rows, 1, 'Europe', 4, ['1.0', '2.0', '3.0'], [2, 3, 4, 8])
    first1_EU = first_case(temporanea1EU)
    paese2EU = selected_country_variables(temporanea1EU, 1, first1_EU, 1, first1_EU, [0, 1, 2])
    print("First Case:", paese2EU)

    temporanea2EU = selected_country_variables(list_of_rows, 1, 'Europe', 7, ['1.0', '2.0', '3.0'], [2, 3, 5, 8])
    first2_EU = first_case(temporanea2EU)
    paese3EU = selected_country_variables(temporanea2EU, 1, first2_EU, 1, first2_EU, [0, 1, 3])
    print("First Death:", paese3EU)
    print(" ")
    # I dati Europei mostrano l'inizio delle osservazioni il 6 Gennaio 2020 nei Paesi Estonia, Grecia e Latvia. I
    # primi casi sono stati in Francia il 24 Gennaio 2020. La prima morte in Europa è avvenuta in Regno Unito il
    # 30 Gennaio.


    # First: Total inhabitants in Europe
    persone_EU = inhabitants(europa)
    print("Numero Abitanti in {}: {:,.2f}".format(europa[0][0], persone_EU))
    print(" ")
    # La differenza tra i due continenti si riduce a 152 milioni di persone circa. Nonostante le due popolazioni non
    # siano identiche, voglio considerarle comparabili perché hanno almeno lo stesso ordine di grandezza e uno sviluppo
    # culturale simile.


    # Second: Total New Daily Cases in Europe
    new_daily_cases_EU, cases_tot_EU, counter_cases_EU = new_daily(europa, 3)
    print("I casi totali in Europa sono {:,.2f}".format(cases_tot_EU))

    print("Percentuale di Ammalati sulla Popolazione: {:,.2f} %".format((cases_tot_EU * 100) / persone_EU))

    print("Media Giornaliera di Nuovi Ammalati: {:,.2f}".format(s.mean(new_daily_cases_EU)))

    print("Valori Mancanti: {:,.2f} \nValori Totali: {:,.2f} \nPercentuale Mancanti: {:,.2f} %".format(counter_cases_EU,
            len(europa), (counter_cases_EU * 100 / len(europa))))
    if (counter_cases_EU * 100 / len(europa)) < 5.0:
        print("Meno del 5% di osservazioni è mancante")
    else:
        print("Più del 5% di osservazioni è mancante: perché?")

    print("Mediana: {:,.2f}".format(s.median(new_daily_cases_EU)))

    print("Massimo Nuovi Casi Giornalieri: {:,.2f}".format(max(new_daily_cases_EU)))

    print("Minimo Nuovi Casi Giornalieri: {:,.2f}".format(min(new_daily_cases_EU)))
    print(" ")
    # Considerendo che il virus ha avuto la sua comparsa nel continente Europa in Italia, il numero di osservazioni
    # mancanti è più basso rispetto al continente Nord America.


    # Third: Total New Daily Deaths in Europe
    new_daily_deaths_EU, deaths_tot_EU, counter_deaths_EU = new_daily(europa, 4)
    print("Morti Totali: {:,.2f}".format(sum(new_daily_deaths_EU)))

    print("Percentuale di Morti sugli Ammalati: {:,.2f} %".format(sum(new_daily_deaths_EU) * 100 / cases_tot_EU))

    print("Percentuale di Morti sugli Abitanti: {:,.2f} %".format(sum(new_daily_deaths_EU) * 100 / persone_EU))

    print("Media di Nuovi Morti Giornaliera: {:,.2f}".format(s.mean(new_daily_deaths_EU)))

    print("Valori Mancanti: {:,.2f} \nValori Totali: {:,.2f} \nPercentuale Mancanti: {:,.2f} %".format(counter_deaths_EU,
          len(europa), (counter_deaths_EU * 100 / len(europa))))
    if (counter_deaths_EU * 100 / len(europa)) < 5.0:
        print("Meno del 5% di osservazioni è mancante")
    else:
        print("Più del 5% di osservazioni è mancante: perché?")

    print("Mediana: {:,.2f}".format(s.median(new_daily_deaths_EU)))

    print("Massimo Nuove Morti Giornaliere: {:,.2f}".format(max(new_daily_deaths_EU)))

    print("Minimo Nuove Morti Giornaliere: {:,.2f}".format(min(new_daily_deaths_EU)))
    print(" ")
    # I valori mancanti nella variabile "nuove morti" identifica o una mancanza di dati ufficiali sulle morti da COVID
    # o un effetto ritardato sul Continente rispetto al numero di ammalati.

    # Fourth: Total New Vaccinations Smoothed in Europe
    new_daily_vacc_EU, vacc_tot_EU, counter_vacc_EU = new_daily(europa, 5)
    print("Vaccinazioni Totali: {:,.2f} \nPercentuale della Popolazione: {:,.2f} %".format(sum(new_daily_vacc_EU), (
                vacc_tot_EU * 100) / persone_EU))

    print("Percentuale di Vaccinazioni sugli Ammalati: {:,.2f} %".format(sum(new_daily_vacc_EU) * 100 / cases_tot_EU))

    print("Media di Nuove Vaccinazioni Giornaliere: {:,.2f}".format(s.mean(new_daily_vacc_EU)))

    print("Valori Mancanti: {:,.2f} \nValori Totali: {:,.2f} \nPercentuale Mancanti: {:,.2f} %".format(counter_vacc_EU,
                len(europa), (counter_vacc_EU * 100 / len(europa))))
    if (counter_vacc_EU * 100 / len(europa)) < 5.0:
        print("Meno del 5% di osservazioni è mancante")
    else:
        print("Più del 5% di osservazioni è mancante: perché?")

    print("Mediana: {:,.2f}".format(s.median(new_daily_vacc_EU)))

    print("Massimo Nuove Vaccinazioni Giornaliere: {:,.2f}".format(max(new_daily_vacc_EU)))

    print("Minimo Nuove Vaccinazioni Giornaliere: {:,.2f}".format(min(new_daily_vacc_EU)))
    print("\n")
    # E' da notare che le vaccinazioni sono partite molto in ritardo rispetto all'inizio dell'epidemia. Questo va
    # ricordato nel momento in cui si valuta il significato statistico della media in paragone ai valori mancanti:
    # quei valori non potevano esserci perché non esisteva il vaccino.




##### ITALIA
    print("ITALIA")
    # Voglio estrarre solo i valori corrispondenti al Paese "Italia"
    italia = selected_country_variables(list_of_rows, 2, 'Italy', 2, 'Italy', lista)
    # print(italia[0])
    print(" ")


    # Zero: Starting Date
    date_list, counter_date = new_date(italia, 2)

    print("Starting Date:", min(date_list))

    temporanea1IT = selected_country_variables(list_of_rows, 2, 'Italy', 4, ['1.0', '2.0', '3.0'], [2, 3, 4, 8])
    first1_IT = first_case(temporanea1IT)
    print("First Case:", first1_IT)

    temporanea2IT = selected_country_variables(list_of_rows, 2, 'Italy', 7, ['1.0', '2.0', '3.0'], [2, 3, 5, 8])
    first2_IT = first_case(temporanea2IT)
    paese3IT = selected_country_variables(temporanea2IT, 1, first2_IT, 1, first2_IT, [0, 1, 3])
    print("First Death:", paese3IT[0])
    print(" ")


    # First: Total inhabitants in Italy
    persone_IT = float(italia[0][-1])
    print("Numero Abitanti in {}: {:,.2f}".format(italia[0][1] ,float(italia[0][-1])))
    print(" ")


    # Second: Total New Daily Cases in Italy
    new_daily_cases_IT, cases_tot_IT, counter_cases_IT = new_daily(italia, 3)
    print("I casi totali in Italia sono {:,.2f}".format(cases_tot_IT))

    print("Percentuale di Ammalati sulla Popolazione: {:,.2f} %".format((cases_tot_IT * 100) / persone_IT))

    print("Media Giornaliera di Nuovi Ammalati: {:,.2f}".format(s.mean(new_daily_cases_IT)))

    print("Valori Mancanti: {:,.2f} \nValori Totali: {:,.2f} \nPercentuale Mancanti: {:,.2f} %".format(counter_cases_IT,
            len(italia), (counter_cases_IT * 100 / len(italia))))
    if (counter_cases_IT * 100 / len(italia)) < 5.0:
        print("Meno del 5% di osservazioni è mancante")
    else:
        print("Più del 5% di osservazioni è mancante: perché?")

    print("Mediana: {:,.2f}".format(s.median(new_daily_cases_IT)))

    print("Massimo Nuovi Casi Giornalieri: {:,.2f}".format(max(new_daily_cases_IT)))

    print("Minimo Nuovi Casi Giornalieri: {:,.2f}".format(min(new_daily_cases_IT)))
    print(" ")
    # Le date di partenza del dataset cambiano di Paese in Paese; in Italia il dataset parte dal '2020-01-31', ossia
    # 979 giorni (osservazioni) ad oggi 6 Ottobre 2022. La mancanza di 1 valore è da considerarsi quasi irrilevante.


    # Third: Total New Daily Deaths in Italy
    new_daily_deaths_IT, deaths_tot_IT, counter_deaths_IT = new_daily(italia, 4)
    print("Morti Totali: {:,.2f}".format(sum(new_daily_deaths_IT)))

    print("Percentuale di Morti sugli Ammalati: {:,.2f} %".format(sum(new_daily_deaths_IT) * 100 / cases_tot_IT))

    print("Percentuale di Morti sugli Abitanti: {:,.2f} %".format(sum(new_daily_deaths_IT) * 100 / persone_IT))

    print("Media di Nuovi Morti Giornaliera: {:,.2f}".format(s.mean(new_daily_deaths_IT)))

    print("Valori Mancanti: {:,.2f} \nValori Totali: {:,.2f} \nPercentuale Mancanti: {:,.2f} %".format(counter_deaths_IT,
            len(italia), (counter_deaths_IT * 100 / len(italia))))
    if (counter_deaths_IT * 100 / len(italia)) < 5.0:
        print("Meno del 5% di osservazioni è mancante")
    else:
        print("Più del 5% di osservazioni è mancante: perché?")

    print("Mediana: {:,.2f}".format(s.median(new_daily_deaths_IT)))

    print("Massimo Nuove Morti Giornaliere: {:,.2f}".format(max(new_daily_deaths_IT)))

    print("Minimo Nuove Morti Giornaliere: {:,.2f}".format(min(new_daily_deaths_IT)))
    print(" ")
    # I pochi valori mancanti riguardo al valore Nuovi Morti rappresenta la velocità con cui il virus ha avuto effetti
    # negativi sulla popolazione.

    # Fourth: Total New Vaccinations Smoothed in Italy
    new_daily_vacc_IT, vacc_tot_IT, counter_vacc_IT = new_daily(italia, 5)
    print("Vaccinazioni Totali: {:,.2f} \nPercentuale della Popolazione: {:,.2f} %".format(sum(new_daily_vacc_IT), (
                vacc_tot_IT * 100) / persone_IT))

    print("Percentuale di Vaccinazioni sugli Ammalati: {:,.2f} %".format(sum(new_daily_vacc_IT) * 100 / cases_tot_IT))

    print("Media di Nuove Vaccinazioni Giornaliere: {:,.2f}".format(s.mean(new_daily_vacc_IT)))

    print("Valori Mancanti: {:,.2f} \nValori Totali: {:,.2f} \nPercentuale Mancanti: {:,.2f} %".format(counter_vacc_IT,
                len(italia), (counter_vacc_IT * 100 / len(italia))))
    if (counter_vacc_IT * 100 / len(italia)) < 5.0:
        print("Meno del 5% di osservazioni è mancante")
    else:
        print("Più del 5% di osservazioni è mancante: perché?")

    print("Mediana: {:,.2f}".format(s.median(new_daily_vacc_IT)))

    print("Massimo Nuove Vaccinazioni Giornaliere: {:,.2f}".format(max(new_daily_vacc_IT)))

    print("Minimo Nuove Vaccinazioni Giornaliere: {:,.2f}".format(min(new_daily_vacc_IT)))
    print("\n")
    # E' da notare che le vaccinazioni sono partite molto in ritardo rispetto all'inizio dell'epidemia. Questo va
    # ricordato nel momento in cui si valuta il significato statistico della media in paragone ai valori mancanti:
    # quei valori non potevano esserci perché non esisteva il vaccino.




##### GERMANY
    print("GERMANIA")
    # Voglio estrarre solo i valori corrispondenti al Paese "Germania"
    germania = selected_country_variables(list_of_rows, 2, 'Germany', 2, 'Germany', lista)
    # print(germania[0])
    print(" ")

    
    # Zero: Starting Date
    date_list, counter_date = new_date(germania, 2)
    
    print("Starting Date:",min(date_list))
    
    temporanea1GR = selected_country_variables(list_of_rows, 2, 'Germany', 4, ['1.0', '2.0', '3.0'], [2, 3, 4, 8])
    first1_GR = first_case(temporanea1GR)
    print("First Case:", first1_GR)
    
    temporanea2GR = selected_country_variables(list_of_rows, 2, 'Germany', 7, ['1.0', '2.0', '3.0'] , [2, 3, 5, 8])
    first2_GR = first_case(temporanea2GR)
    paese3GR = selected_country_variables(temporanea2GR, 1, first2_GR, 1, first2_GR, [1, 3])    
    print("First Death:", paese3GR[0])

    
    # First: Total inhabitants in Germany
    persone_GR = float(germania[0][-1])
    print("Numero Abitanti in {}: {:,.2f}".format(germania[0][1] ,float(germania[0][-1])))
    print(" ")
    # Come nel caso dei Continenti appena visti, anche qui i valori tra Germania e Italia non corrispondono. La differenza è di 34 milioni
    # di abitanti, però hanno almeno lo stesso ordine di grandezza e uno sviluppo culturale simile.


    # Second: Total New Daily Cases in Germany
    new_daily_cases_GR, cases_tot_GR, counter_cases_GR = new_daily(germania, 3)
    print("I casi totali in Italia sono {:,.2f}".format(cases_tot_GR))

    print("Percentuale di Ammalati sulla Popolazione: {:,.2f} %".format((cases_tot_GR * 100) / persone_GR))

    print("Media Giornaliera di Nuovi Ammalati: {:,.2f}".format(s.mean(new_daily_cases_GR)))

    print("Valori Mancanti: {:,.2f} \nValori Totali: {:,.2f} \nPercentuale Mancanti: {:,.2f} %".format(counter_cases_GR,
                len(germania), (counter_cases_GR * 100 / len(germania))))
    if (counter_cases_GR * 100 / len(germania)) < 5.0:
        print("Meno del 5% di osservazioni è mancante")
    else:
        print("Più del 5% di osservazioni è mancante: perché?")

    print("Mediana: {:,.2f}".format(s.median(new_daily_cases_GR)))

    print("Massimo Nuovi Casi Giornalieri: {:,.2f}".format(max(new_daily_cases_GR)))

    print("Minimo Nuovi Casi Giornalieri: {:,.2f}".format(min(new_daily_cases_GR)))
    print(" ")
    # Le date di partenza del dataset cambiano di Paese in Paese; in Germania il dataset parte dal '2020-01-27', ossia
    # 983 giorni (osservazioni) ad oggi 6 Ottobre 2022. La mancanza di 2 valori è da considerarsi quasi irrilevante.

    # Third: Total New Daily Deaths in Germany
    new_daily_deaths_GR, deaths_tot_GR, counter_deaths_GR = new_daily(germania, 4)
    print("Morti Totali: {:,.2f}".format(sum(new_daily_deaths_GR)))

    print("Percentuale di Morti sugli Ammalati: {:,.2f} %".format(sum(new_daily_deaths_GR) * 100 / cases_tot_GR))

    print("Percentuale di Morti sugli Abitanti: {:,.2f} %".format(sum(new_daily_deaths_GR) * 100 / persone_GR))

    print("Media di Nuovi Morti Giornaliera: {:,.2f}".format(s.mean(new_daily_deaths_GR)))

    print("Valori Mancanti: {:,.2f} \nValori Totali: {:,.2f} \nPercentuale Mancanti: {:,.2f} %".format(counter_deaths_GR,
            len(germania), (counter_deaths_GR * 100 / len(germania))))
    if (counter_deaths_GR * 100 / len(germania)) < 5.0:
        print("Meno del 5% di osservazioni è mancante")
    else:
        print("Più del 5% di osservazioni è mancante: perché?")

    print("Mediana: {:,.2f}".format(s.median(new_daily_deaths_GR)))

    print("Massimo Nuove Morti Giornaliere: {:,.2f}".format(max(new_daily_deaths_GR)))

    print("Minimo Nuove Morti Giornaliere: {:,.2f}".format(min(new_daily_deaths_GR)))
    print(" ")
    # I valori mancanti rappresentano i giorni trascorsi tra i primi casi e le prime morti.

    # Fourth: Total New Vaccinations Smoothed in Germany
    new_daily_vacc_GR, vacc_tot_GR, counter_vacc_GR = new_daily(germania, 5)
    print("Vaccinazioni Totali: {:,.2f} \nPercentuale della Popolazione: {:,.2f} %".format(sum(new_daily_vacc_GR), (
                vacc_tot_GR * 100) / persone_GR))

    print("Percentuale di Vaccinazioni sugli Ammalati: {:,.2f} %".format(sum(new_daily_vacc_GR) * 100 / cases_tot_GR))

    print("Media di Nuove Vaccinazioni Giornaliere: {:,.2f}".format(s.mean(new_daily_vacc_GR)))

    print("Valori Mancanti: {:,.2f} \nValori Totali: {:,.2f} \nPercentuale Mancanti: {:,.2f} %".format(counter_vacc_GR,
                len(germania), (counter_vacc_GR * 100 / len(germania))))
    if (counter_vacc_GR * 100 / len(germania)) < 5.0:
        print("Meno del 5% di osservazioni è mancante")
    else:
        print("Più del 5% di osservazioni è mancante: perché?")

    print("Mediana: {:,.2f}".format(s.median(new_daily_vacc_GR)))

    print("Massimo Nuove Vaccinazioni Giornaliere: {:,.2f}".format(max(new_daily_vacc_GR)))

    print("Minimo Nuove Vaccinazioni Giornaliere: {:,.2f}".format(min(new_daily_vacc_GR)))

    """
    - Il virus è arrivato prima in Nord America che in Europa. E prima in Germania che in Italia.
    - Tuttavia la prima morte è avvenuta in Europa (UK), non nel Nord America. Ed in Italia prima che in Germania.
    - I casi in Nord America sono 114,470,189.00, il 19.20% della popolazione. In Europa sono 230,163,124.00, il 30.74%. 
      Questo forse è dovuto alle diverse densità di popolazione. La Germania ha avuto 33,652,314.00 casi, il 40.30% 
      della popolazione. In Italia ci sono stati 22,648,211.00 casi, cioè il 38.23% della popolazione.
    - In Nord America è morto il 1.32% degli ammalati. In Europa lo 0.84 %. In particolare, in Germania è morto lo 
      0.45 % e in Italia lo 0.78 %.
    - L'Europa ha il record di vaccinazioni: 1,328,554,234.00 contro 1,061,067,059.00 del Nord America. La Germania ha 
      185,905,489.00  vaccinazioni, 40 milioni in più dell'Italia. Cionostante, la percentuale di vaccinazioni su
      popolazione è maggiore in Italia (perché ha meno abitanti). In entrambi questi ultimi Paesi, ogni persona ha 
      ricevuto in media 2.2 vaccini.
    """

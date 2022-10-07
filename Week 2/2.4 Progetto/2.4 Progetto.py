import csv
import statistics as s

def selected_country(original, indice, valore):
    """
    Legge una lista di liste e crea una nuova lista di liste con solo le righe selezionate
    :param original: lista di liste di origine
    :param indice: indice nella lista di liste di origine dove controllare per un valore
    :param valore: valore nella lista di liste di origine in posizione indice
    :return: lista di liste
    """
    country = []
    # Voglio estrarre i dati dagli index prescelti; devo iterare nelle liste di liste
    for i in range(0, (len(original))):
        valori = original[i][int(indice)]
        if valori == str(valore):
            riga = []
            country.append(riga)
            for j in range(0,len(original[0])):
                riga.append(original[i][j])
    return(country)


def inhabitants(original):
    """
    Legge una lista di liste e restituisce il numero di abitanti per regione
    :param original: lista di liste di origine
    :return: stampa del numero di abitanti
    """
    nations_in_region = []
    for i in range(0, len(original)):
        nations_in_region.append((original[i][1], original[i][6]))

    set_nations_in_region = set(nations_in_region)
    sum_set = [float(t[1]) for t in set_nations_in_region]

    return sum(sum_set)


def new_daily(original, indice):
    """
    Legge una lista di liste e restituisce il numero di nuovi casi
    :param original: lista di liste di origine
    :param indice: indice nella lista di liste di cosa vogliamo ottenere (X)
    :return: lista dei valori di X; somma totale di X; somma valori mancanti
    """
    cases = []
    counter = 0
    for i in range(0,len(original)):
        if original[i][int(indice)] != '':
            cases.append(float(original[i][int(indice)]))
        else:
            counter += 1

    total = int(sum(cases))

    return cases, total, int(counter)




path = ('C:\\Users\\elste\\Desktop\\epicode\\2_Week\\Day_4\\owid_covid_data.csv')
with open(path, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    # print("reader è di tipo ", type(reader))
    # class = '_csv.reader'


    # Per praticità, ora sarà una lista di liste
    list_of_rows = list(reader)
    # print(list_of_rows)


    print("Il numero di liste è {:,.2f}".format(len(list_of_rows)))
    # 221,492


    # I nomi delle colonne sono:
    # print(list_of_rows[0])

    # ['iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases', 'new_cases_smoothed', 'total_deaths',
    # 'new_deaths', 'new_deaths_smoothed', 'total_cases_per_million', 'new_cases_per_million', 'new_cases_smoothed_per_million',
    # 'total_deaths_per_million', 'new_deaths_per_million', 'new_deaths_smoothed_per_million', 'reproduction_rate',
    # 'icu_patients', 'icu_patients_per_million', 'hosp_patients', 'hosp_patients_per_million', 'weekly_icu_admissions',
    # 'weekly_icu_admissions_per_million', 'weekly_hosp_admissions', 'weekly_hosp_admissions_per_million', 'total_tests',
    # 'new_tests', 'total_tests_per_thousand', 'new_tests_per_thousand', 'new_tests_smoothed', 'new_tests_smoothed_per_thousand',
    # 'positive_rate', 'tests_per_case', 'tests_units', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated',
    # 'total_boosters', 'new_vaccinations', 'new_vaccinations_smoothed', 'total_vaccinations_per_hundred',
    # 'people_vaccinated_per_hundred', 'people_fully_vaccinated_per_hundred', 'total_boosters_per_hundred',
    # 'new_vaccinations_smoothed_per_million', 'new_people_vaccinated_smoothed', 'new_people_vaccinated_smoothed_per_hundred',
    # 'stringency_index', 'population', 'population_density', 'median_age', 'aged_65_older', 'aged_70_older', 'gdp_per_capita',
    # 'extreme_poverty', 'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers', 'male_smokers', 'handwashing_facilities',
    # 'hospital_beds_per_thousand', 'life_expectancy', 'human_development_index', 'excess_mortality_cumulative_absolute',
    # 'excess_mortality_cumulative', 'excess_mortality', 'excess_mortality_cumulative_per_million']


    # A me interessa ridurre il numero di variabili, creando una nuova lista di liste
    # Per farlo mi servono le posizioni degli Header (le variabili) che mi interessano:
    if False:
        print("continent ", list_of_rows[0].index('continent'))
        # 1
        print("location ", list_of_rows[0].index('location'))
        # 2
        print("date", list_of_rows[0].index('date'))
        # 3
        print("new_cases ", list_of_rows[0].index('new_cases'))
        # 5
        print("new_deaths ", list_of_rows[0].index('new_deaths'))
        # 8
        print("new_vaccinations_smoothed ", list_of_rows[0].index('new_vaccinations_smoothed'))
        # 39
        print("population ", list_of_rows[0].index('population'))
        # 48
    """
    Ho scelto questi valori perché: 
    - Continente mi permette di selezionare i continenti che voglio
    - Location mi permette di selezionare i paesi che voglio
    - Date (non implementato)
    - New cases mi permette di vedere l'andamento giornaliero
    - New deaths mi permette di vedere l'andamento giornaliero
    - New vaccinations smooth mi permette di vedere l'andamento giornaliero mediato su 7 giorni (ha più valori)
    - Population mi permette di comprendere le dimensioni dei continenti e degli Stati/Paesi
    """


    # Creo un nuovo database semplificato
    nuova = []
    # Voglio estrarre i dati dagli index prescelti; devo iterare nelle liste di liste
    for i in range(0, (len(list_of_rows))):
        riga = []
        nuova.append(riga)
        for j in [1,2,3,5,8,39,48]:
            riga.append(list_of_rows[i][j])
    # print(nuova[0])
    # ['continent', 'location', 'date', 'new_cases', 'new_deaths', 'new_vaccinations_smoothed', 'population']




    print(" ")
    # AMERICA
    # Voglio estrarre solo i valori corrispondenti al continente "North America"
    america = selected_country(nuova, 0, 'North America')
    # print(america[0])


    print(" ")
    # First: Total inhabitants in North America
    persone_NA = inhabitants(america)
    print("Gli abitanti in {} sono {:,.2f}".format(america[0][0], persone_NA))
    # 596,315,269


    print(" ")
    # Second: Total New Daily Cases in North America
    new_daily_cases_NA, cases_tot_NA, counter_cases_NA = new_daily(america, 3)
    print("I casi totali nel Nord America sono {:,.2f}".format(cases_tot_NA))
    # 114,470,189.0

    print("La percentuale di ammalati sulla popolazione è {:,.2f} %".format((cases_tot_NA * 100) / persone_NA))
    # 19.19 %

    print("La media giornaliera è di {:,.2f} casi".format(s.mean(new_daily_cases_NA)))
    # 3,600
    print("Mancano {:,.2f} valori su {:,.2f} ossia il {:,.2f} %".format(counter_cases_NA, len(america), (counter_cases_NA * 100/len(america))))
    if (counter_cases_NA * 100/len(america)) < 5.0:
        print("Il parametro è accettabile perchè ha meno del 5% di osservazioni mancanti")
    else:
        print("Il parametro non è accettabile perchè ha più del 5% di osservazioni mancanti")
    # La media ha poco senso perchè dei valori manca il 6.7%, ossia 2'274 valori su 34'068

    print("La mediana è {:,.2f}".format(s.median(new_daily_cases_NA)))
    # 4.00
    # La mediana è molto bassa. Questo implica che ci sia una crescita dei casi giornalieri non costante, ma esponenziale

    print("Il massimo è {:,.2f} nuovi casi al giorno".format(max(new_daily_cases_NA)))
    # 1'355'368.0
    print("Il minimo è {:,.2f} nuovi casi al giorno".format(min(new_daily_cases_NA)))
    # 0


    print(" ")
    # Third: Total New Daily Deaths in North America
    new_daily_deaths_NA, deaths_tot_NA, counter_deaths_NA = new_daily(america, 4)
    print("Le morti totali sono {:,.2f}".format(sum(new_daily_deaths_NA)))
    # 1'509'163

    print("La percentuale di morti sugli ammalati è {:,.2f} %".format(sum(new_daily_deaths_NA) * 100 / cases_tot_NA))
    # 1.32 %
    print("La percentuale di morti sugli abitanti è {:,.2f} %".format(sum(new_daily_deaths_NA) * 100 / persone_NA))
    # 0.25 %

    print("La media giornaliera è di {:,.2f} morti".format(s.mean(new_daily_deaths_NA)))
    # 54.7
    print("Mancano {:,.2f} valori su {:,.2f} ossia il {:,.2f} %".format(counter_deaths_NA, len(america), (counter_deaths_NA * 100/len(america))))
    if (counter_deaths_NA * 100/len(america)) < 5.0:
        print("Il parametro è accettabile perchè ha meno del 5% di osservazioni mancanti")
    else:
        print("Il parametro non è accettabile perchè ha più del 5% di osservazioni mancanti")
    # Il parametro non è accettabile perchè ha più del 5% di osservazioni mancanti

    print("La mediana è {:,.2f}".format(s.median(new_daily_deaths_NA)))
    # 0
    # La mediana è molto bassa. Questo implica che ci sia una crescita delle morti giornaliere non costante, ma esponenziale

    print("Il massimo è {:,.2f} nuove morti al giorno".format(max(new_daily_deaths_NA)))
    # 4,395.0
    print("Il minimo è {:,.2f} nuove morti al giorno".format(min(new_daily_deaths_NA)))
    # 0


    print(" ")
    # Fourth: Total New Vaccinations Smoothed in North America
    new_daily_vacc_NA, vacc_tot_NA, counter_vacc_NA = new_daily(america, 5)
    print("Le vaccinazioni totali sono {:,.2f}, ossia il {:,.2f} % della popolazione".format(sum(new_daily_vacc_NA), (vacc_tot_NA * 100) / persone_NA))
    # 1'509'163

    print("La percentuale di vaccinazioni sugli ammalati è {:.2f} %".format(sum(new_daily_vacc_NA) * 100 / cases_tot_NA))
    # 1.31 %
    print("La percentuale di vaccinazioni sugli abitanti è {:.2f} %".format(sum(new_daily_vacc_NA) * 100 / persone_NA))
    # 0.25 %

    print("La media giornaliera è di {:,.2f} vaccinazioni".format(s.mean(new_daily_vacc_NA)))
    # 54.7
    print("Mancano {:,.2f} valori su {:,.2f}, il {:,.2f} %".format(counter_vacc_NA, len(america), (counter_vacc_NA * 100/len(america))))
    if (counter_vacc_NA * 100/len(america)) < 5.0:
        print("Il parametro è accettabile perchè ha meno del 5% di osservazioni mancanti")
    else:
        print("Il parametro non è accettabile perchè ha più del 5% di osservazioni mancanti")
    # La media ha poco senso perchè dei valori manca il 19.1%, ossia 6'518 valori su 34'068

    print("La mediana delle vaccinazioni è {:,.2f}".format(s.median(new_daily_vacc_NA)))
    # 0
    # La mediana è molto bassa. Questo implica che ci sia una crescita delle morti giornaliere non costante, ma esponenziale

    print("Il massimo è {:,.2f} nuove vaccinazioni al giorno".format(max(new_daily_vacc_NA)))
    # 4,395.0
    print("Il minimo è {:,.2f} nuove vaccinazioni al giorno".format(min(new_daily_vacc_NA)))
    # 0




    print(" ")
    # EUROPA
    print(" ")
    # Creo uno spazio utile per la stampa
    print(" ")
    # Voglio estrarre solo i valori corrispondenti al continente "Europa"
    europa = selected_country(nuova, 0, 'Europe')
    # print("EU: ", europa[0])


    print(" ")
    # First: Total inhabitants in Europe
    persone_EU = inhabitants(europa)
    print("Gli abitanti in {} sono {:,.2f}".format(europa[0][0], persone_EU))
    # 748,655,221.00


    print(" ")
    # Second: Total New Daily Cases in Europe
    new_daily_cases_EU, cases_tot_EU, counter_cases_EU = new_daily(europa, 3)
    print("I casi totali in Europa sono {:,.2f}".format(cases_tot_EU))
    # 230,163,124.00

    print("La percentuale di ammalati sulla popolazione è {:,.2f} %".format((cases_tot_EU * 100) / persone_EU))
    # 30.74 %

    print("La media giornaliera è di {:,.2f} casi".format(s.mean(new_daily_cases_EU)))
    # 4,939.23
    print("Mancano {:,.2f} valori su {:,.2f}, il {:,.2f} %".format(counter_cases_EU, len(europa), (counter_cases_EU * 100/len(europa))))
    # Mancano 1,300.00 valori su 47,899.00, il 2.71 %
    if (counter_cases_EU * 100/len(europa)) < 5.0:
        print("Il parametro è accettabile perchè ha meno del 5% di osservazioni mancanti")
    else:
        print("Il parametro non è accettabile perchè ha più del 5% di osservazioni mancanti")
    # Il parametro è accettabile perchè ha meno del 5% di osservazioni mancanti

    print("La mediana è {:,.2f}".format(s.median(new_daily_cases_EU)))
    # 290.00
    # La mediana è bassa in confronto alla media giornaliera
    # Questo implica che ci sia una crescita dei casi giornalieri non costante, ma esponenziale

    print("Il massimo è {:,.2f} nuovi casi al giorno".format(max(new_daily_cases_EU)))
    # 527,487.00
    print("Il minimo è {:,.2f} nuovi casi al giorno".format(min(new_daily_cases_EU)))
    # 0


    print(" ")
    # Third: Total New Daily Deaths in Europe
    new_daily_deaths_EU, deaths_tot_EU, counter_deaths_EU = new_daily(europa, 4)
    print("Le morti totali sono {:,.2f}".format(sum(new_daily_deaths_EU)))
    # 1,944,478.00

    print("La percentuale di morti sugli ammalati è {:,.2f} %".format(sum(new_daily_deaths_EU) * 100 / cases_tot_EU))
    # 0.84 %
    print("La percentuale di morti sugli abitanti è {:,.2f} %".format(sum(new_daily_deaths_EU) * 100 / persone_EU))
    # 0.26 %

    print("La media giornaliera è di {:,.2f} morti".format(s.mean(new_daily_deaths_EU)))
    # 44.01
    print("Mancano {:,.2f} valori su {:,.2f}, il {:,.2f} %".format(counter_deaths_EU, len(america), (counter_deaths_EU * 100/len(europa))))
    # Mancano 3,716.00 valori su 34,068.00, il 7.76 %
    if (counter_deaths_EU * 100/len(europa)) < 5.0:
        print("Il parametro è accettabile perchè ha meno del 5% di osservazioni mancanti")
    else:
        print("Il parametro non è accettabile perchè ha più del 5% di osservazioni mancanti")
    # Il parametro non è accettabile perchè ha più del 5% di osservazioni mancanti

    print("La mediana è {:,.2f}".format(s.median(new_daily_deaths_EU)))
    # 3.00
    # La mediana è molto bassa. Questo implica che ci sia una crescita delle morti giornaliere non costante, ma esponenziale

    print("Il massimo è {:,.2f} nuove morti al giorno".format(max(new_daily_deaths_EU)))
    # 1,623.00
    print("Il minimo è {:,.2f} nuove morti al giorno".format(min(new_daily_deaths_EU)))
    # 0


    print(" ")
    # Fourth: Total New Vaccinations Smoothed in Europe
    new_daily_vacc_EU, vacc_tot_EU, counter_vacc_EU = new_daily(europa, 5)
    print("Le vaccinazioni totali sono {:,.2f}, ossia il {:,.2f} % della popolazione".format(sum(new_daily_vacc_EU), (vacc_tot_EU * 100) / persone_EU))
    # Le vaccinazioni totali sono 1,328,554,234.00, ossia il 177.46 % della popolazione

    print("La percentuale di vaccinazioni sugli ammalati è {:,.2f} %".format(sum(new_daily_vacc_EU) * 100 / cases_tot_EU))
    # 577.22 %
    print("La percentuale di vaccinazioni sugli abitanti è {:,.2f} %".format(sum(new_daily_vacc_EU) * 100 / persone_EU))
    # 177.46 %

    print("La media giornaliera è di {:,.2f} vaccinazioni".format(s.mean(new_daily_vacc_EU)))
    # 45,639.10
    print("Mancano {:,.2f} valori su {:,.2f}, il {:,.2f} %".format(counter_vacc_EU, len(europa), (counter_vacc_EU * 100/len(europa))))
    # Mancano 18,789.00 valori su 47,899.00, il 39.23 %
    if (counter_vacc_EU * 100/len(europa)) < 5.0:
        print("Il parametro è accettabile perchè ha meno del 5% di osservazioni mancanti")
    else:
        print("Il parametro non è accettabile perchè ha più del 5% di osservazioni mancanti")
    # Il parametro non è accettabile perchè ha più del 5% di osservazioni mancanti

    print("La mediana delle vaccinazioni è {:,.2f}".format(s.median(new_daily_vacc_EU)))
    # 6,178.50
    # La mediana è alta. Questo implica che ci sia una crescita molto importante del numero di vaccinazioni

    print("Il massimo è {:,.2f} nuove vaccinazioni al giorno".format(max(new_daily_vacc_EU)))
    # 1,147,861.00
    print("Il minimo è {:,.2f} nuove vaccinazioni al giorno".format(min(new_daily_vacc_EU)))
    # 0




    print(" ")
    # ITALIA
    print(" ")
    # Voglio estrarre solo i valori corrispondenti al paese "Italia"
    italia = selected_country(nuova, 1, 'Italy')
    # print("ITA: ", italia[0])


    print(" ")
    # First: Total inhabitants in Italy
    persone_IT = float(italia[0][-1])
    print("Gli abitanti in Italia sono {:,}".format(float(italia[0][-1])))
    # 59,240,330


    print(" ")
    # Second: Total New Daily Cases in Italy
    new_daily_cases_IT, cases_tot_IT, counter_cases_IT = new_daily(italia, 3)
    print("I casi totali in Italia sono {:,.2f}".format(cases_tot_IT))
    # 22,648,211.00

    print("La percentuale di ammalati sulla popolazione è {:,.2f} %".format((cases_tot_IT * 100) / persone_IT))
    # 38.23 %

    print("La media giornaliera è di {:,.2f} casi".format(s.mean(new_daily_cases_IT)))
    # 23,157.68
    print("Mancano {:,.2f} valori su {:,.2f}, il {:,.2f} %".format(counter_cases_IT, len(italia), (counter_cases_IT * 100/len(italia))))
    # La media giornaliera è di 23,157.68 casi
    if (counter_cases_IT * 100/len(italia)) < 5.0:
        print("Il parametro è accettabile perchè ha meno del 5% di osservazioni mancanti")
    else:
        print("Il parametro non è accettabile perchè ha più del 5% di osservazioni mancanti")
    # Il parametro è accettabile perchè ha meno del 5% di osservazioni mancanti

    print("La mediana è {:,.2f}".format(s.median(new_daily_cases_IT)))
    # 10,411.00
    # La mediana è alta in confronto alla media giornaliera
    # Questo implica che ci sia una crescita dei casi giornalieri non costante, ma esponenziale

    print("Il massimo è {:,.2f} nuovi casi al giorno".format(max(new_daily_cases_IT)))
    # 228,123.00
    print("Il minimo è {:,.2f} nuovi casi al giorno".format(min(new_daily_cases_IT)))
    # 0


    print(" ")
    # Third: Total New Daily Deaths in Italy
    new_daily_deaths_IT, deaths_tot_IT, counter_deaths_IT = new_daily(italia, 4)
    print("Le morti totali sono {:,.2f}".format(sum(new_daily_deaths_IT)))
    # 177,331.00

    print("La percentuale di morti sugli ammalati è {:,.2f} %".format(sum(new_daily_deaths_IT) * 100 / cases_tot_IT))
    # 0.78 %
    print("La percentuale di morti sugli abitanti è {:,.2f} %".format(sum(new_daily_deaths_IT) * 100 / persone_IT))
    # 0.30 %

    print("La media giornaliera è di {:,.2f} morti".format(s.mean(new_daily_deaths_IT)))
    # 185.30
    print("Mancano {:,.2f} valori su {:,.2f}, il {:,.2f} %".format(counter_deaths_IT, len(italia), (counter_deaths_IT * 100/len(italia))))
    # Mancano 22.00 valori su 979.00, il 2.25 %
    if (counter_deaths_IT * 100/len(italia)) < 5.0:
        print("Il parametro è accettabile perchè ha meno del 5% di osservazioni mancanti")
    else:
        print("Il parametro non è accettabile perchè ha più del 5% di osservazioni mancanti")
    # Il parametro è accettabile perchè ha meno del 5% di osservazioni mancanti

    print("La mediana è {:,.2f}".format(s.median(new_daily_deaths_IT)))
    # 99.00
    # La mediana è molto bassa. Questo implica che ci sia una crescita delle morti giornaliere non costante, ma esponenziale

    print("Il massimo è {:,.2f} nuove morti al giorno".format(max(new_daily_deaths_IT)))
    # 993.00
    print("Il minimo è {:,.2f} nuove morti al giorno".format(min(new_daily_deaths_IT)))
    # 1.00


    print(" ")
    # Fourth: Total New Vaccinations Smoothed in North America
    new_daily_vacc_IT, vacc_tot_IT, counter_vacc_IT = new_daily(italia, 5)
    print("Le vaccinazioni totali sono {:,.2f}, ossia il {:,.2f} % della popolazione".format(sum(new_daily_vacc_IT), (vacc_tot_IT * 100) / persone_IT))
    # Le vaccinazioni totali sono 140,819,912.00, ossia il 237.71 % della popolazione

    print("La percentuale di vaccinazioni sugli ammalati è {:,.2f} %".format(sum(new_daily_vacc_IT) * 100 / cases_tot_IT))
    # 621.77 %
    print("La percentuale di vaccinazioni sugli abitanti è {:,.2f} %".format(sum(new_daily_vacc_IT) * 100 / persone_IT))
    # 237.71 %

    print("La media giornaliera è di {:,.2f} vaccinazioni".format(s.mean(new_daily_vacc_IT)))
    # 217,650.56
    print("Mancano {:,.2f} valori su {:,.2f}, il {:,.2f} %".format(counter_vacc_IT, len(italia), (counter_vacc_IT * 100/len(italia))))
    # Mancano 332.00 valori su 979.00, il 33.91 %
    if (counter_vacc_IT * 100/len(italia)) < 5.0:
        print("Il parametro è accettabile perchè ha meno del 5% di osservazioni mancanti")
    else:
        print("Il parametro non è accettabile perchè ha più del 5% di osservazioni mancanti")
    # Il parametro non è accettabile perchè ha più del 5% di osservazioni mancanti

    print("La mediana delle vaccinazioni è {:,.2f}".format(s.median(new_daily_vacc_IT)))
    # 163,744.00
    # La mediana è alta. Questo implica che ci sia una crescita molto importante del numero di vaccinazioni

    print("Il massimo è {:,.2f} nuove vaccinazioni al giorno".format(max(new_daily_vacc_IT)))
    # 665,079.00
    print("Il minimo è {:,.2f} nuove vaccinazioni al giorno".format(min(new_daily_vacc_IT)))
    # 1,302.00




    print(" ")
    # GERMANIA
    print(" ")
    # Voglio estrarre solo i valori corrispondenti al paese "Germania"
    germania = selected_country(nuova, 1, 'Germany')
    # print("GER: ", germania[0])


    print(" ")
    # First: Total inhabitants in Germany
    persone_GR = float(germania[0][-1])
    print("Gli abitanti in Germania sono {:,.2f}".format(float(germania[0][-1])))
    # 83,408,554


    print(" ")
    # Second: Total New Daily Cases in Germany
    new_daily_cases_GR, cases_tot_GR, counter_cases_GR = new_daily(germania, 3)
    print("I casi totali in Germania sono {:,.2f}".format(cases_tot_GR))
    # 33,652,314.00

    print("La percentuale di ammalati sulla popolazione è {:,.2f} %".format((cases_tot_GR * 100) / persone_GR))
    # 40.35 %

    print("La media giornaliera è di {:,.2f} casi".format(s.mean(new_daily_cases_GR)))
    # 34,304.09
    print("Mancano {:,.2f} valori su {:,.2f}, il {:,.2f} %".format(counter_cases_GR, len(germania), (counter_cases_GR * 100/len(germania))))
    # Mancano 2.00 valori su 983.00, il 0.20 %
    if (counter_cases_GR * 100/len(germania)) < 5.0:
        print("Il parametro è accettabile perchè ha meno del 5% di osservazioni mancanti")
    else:
        print("Il parametro non è accettabile perchè ha più del 5% di osservazioni mancanti")
    # Il parametro è accettabile perchè ha meno del 5% di osservazioni mancanti

    print("La mediana è {:,.2f}".format(s.median(new_daily_cases_GR)))
    # 9,658.00
    # La mediana è alta in confronto alla media giornaliera
    # Questo implica che ci sia una crescita dei casi giornalieri non costante, ma esponenziale

    print("Il massimo è {:,.2f} nuovi casi al giorno".format(max(new_daily_cases_GR)))
    # 527,487.00
    print("Il minimo è {:,.2f} nuovi casi al giorno".format(min(new_daily_cases_GR)))
    # 0


    print(" ")
    # Third: Total New Daily Deaths in Germany
    new_daily_deaths_GR, deaths_tot_GR, counter_deaths_GR = new_daily(germania, 4)
    print("Le morti totali sono {:,.2f}".format(sum(new_daily_deaths_GR)))
    # 150,310.00

    print("La percentuale di morti sugli ammalati è {:,.2f} %".format(sum(new_daily_deaths_GR) * 100 / cases_tot_GR))
    # 0.45 %
    print("La percentuale di morti sugli abitanti è {:,.2f} %".format(sum(new_daily_deaths_GR) * 100 / persone_GR))
    # 0.18 %

    print("La media giornaliera è di {:,.2f} morti".format(s.mean(new_daily_deaths_GR)))
    # 160.25
    print("Mancano {:,.2f} valori su {:,.2f}, il {:,.2f} %".format(counter_deaths_GR, len(germania), (counter_deaths_GR * 100/len(germania))))
    # Mancano 45.00 valori su 983.00, il 4.58 %
    if (counter_deaths_GR * 100/len(germania)) < 5.0:
        print("Il parametro è accettabile perchè ha meno del 5% di osservazioni mancanti")
    else:
        print("Il parametro non è accettabile perchè ha più del 5% di osservazioni mancanti")
    # Il parametro è accettabile perchè ha meno del 5% di osservazioni mancanti

    print("La mediana è {:,.2f}".format(s.median(new_daily_deaths_GR)))
    # 91.50
    # La mediana è molto bassa. Questo implica che ci sia una crescita delle morti giornaliere non costante, ma esponenziale

    print("Il massimo è {:,.2f} nuove morti al giorno".format(max(new_daily_deaths_GR)))
    # 1,244.00
    print("Il minimo è {:,.2f} nuove morti al giorno".format(min(new_daily_deaths_GR)))
    # 0.00


    print(" ")
    # Fourth: Total New Vaccinations Smoothed in Germany
    new_daily_vacc_GR, vacc_tot_GR, counter_vacc_GR = new_daily(germania, 5)
    print("Le vaccinazioni totali sono {:,.2f}, ossia il {:,.2f} % della popolazione".format(sum(new_daily_vacc_GR), (vacc_tot_GR * 100) / persone_GR))
    # Le vaccinazioni totali sono 185,905,489.00, ossia il 222.89 % della popolazione

    print("La percentuale di vaccinazioni sugli ammalati è {:,.2f} %".format(sum(new_daily_vacc_GR) * 100 / cases_tot_GR))
    # 552.43 %
    print("La percentuale di vaccinazioni sugli abitanti è {:,.2f} %".format(sum(new_daily_vacc_GR) * 100 / persone_GR))
    # 222.89 %

    print("La media giornaliera è di {:,.2f} vaccinazioni".format(s.mean(new_daily_vacc_GR)))
    # 287,334.60
    print("Mancano {:,.2f} valori su {:,.2f}, il {:,.2f} %".format(counter_vacc_GR, len(germania), (counter_vacc_GR * 100/len(germania))))
    # Mancano 336.00 valori su 983.00, il 34.18 %
    if (counter_vacc_GR * 100/len(germania)) < 5.0:
        print("Il parametro è accettabile perchè ha meno del 5% di osservazioni mancanti")
    else:
        print("Il parametro non è accettabile perchè ha più del 5% di osservazioni mancanti")
    # Il parametro non è accettabile perchè ha più del 5% di osservazioni mancanti

    print("La mediana delle vaccinazioni è {:,.2f}".format(s.median(new_daily_vacc_GR)))
    # 165,624.00
    # La mediana è alta. Questo implica che ci sia una crescita molto importante del numero di vaccinazioni

    print("Il massimo è {:,.2f} nuove vaccinazioni al giorno".format(max(new_daily_vacc_GR)))
    # 1,147,861.00
    print("Il minimo è {:,.2f} nuove vaccinazioni al giorno".format(min(new_daily_vacc_GR)))
    # 18,007.00

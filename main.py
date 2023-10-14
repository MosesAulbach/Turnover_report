from helper import * 


# TODO: Performancekennzahlen Levi's Buttenheim Store (als Klasse darstellen!!!)

# Target-Variablen pro Tag
target_revenue = 12000          # Umsatzziel 
target_upt = 2                  # Teile pro Rechnung (Bon) 
target_atv = 200                # durchschnittl. Wert pro Rechnung (Bon) 
target_aur = 100                # durchschnittl. Wert pro Artikel
target_sot = 150                # Wert pro Besucher 


# Abrechnung-end-of-the-day-Variables
# revenue = 8900                   # revenue = Umsatz
# visitors = 120                   # visitors = Besucher
# transactions = 63               # transactions = Transaktionen
# articles = 150                  # articles = Artikel (Teilstück)

# Berechnung KPI's = Leistungskennzahlen

# upt = calc_upt(articles, transactions)
# atv = calc_atv(revenue, transactions) # atv = Umsatz (revenue / Anzahl rechung(bons)) = Anzahl der Transaktionen
# aur = calc_aur(revenue, articles)
# sot = calc_sot(revenue, visitors)

# print(f"Heute wurden im Durchschnitt {upt} Kleidungsstücke pro Kunde verkauft.")
# print(f"Der durchschnittliche Wert pro Rechnung beträgt {atv}.")
# print(f"Der durchschnittliche Wert pro Artikel beträgt {aur}.")
# print(f"Der durchschnittliche Wert pro Besucher beträgt {sot}.")

# Beispiel: Absoluter Pfad
# file_object = open("/Users/moses/Desktop/workspace/2023-07-09_Turnover_report/data.txt", "r")

try:
    data_list = []
    file_object = open("data/data.txt", "r")
    # print(file_object.read())
    data_list = file_object.read().splitlines()
    file_object.close()

except FileNotFoundError as e:
    print(e)


counter = 0
while counter < 3:
    raw = data_list[counter]
    # print(raw)
    counter = counter + 1
    daily_list = raw.split('*')
    revenue = daily_list[0]
    visitors = daily_list[1]
    transactions = daily_list[2]
    articles = daily_list[3]


    print(f"{counter}. data raw:")
    print(f"The revenue is: {revenue}.")
    print(f"The total visitors were: {visitors}.")
    print(f"The transactions sum up to: {transactions}.")
    print(f"The articles sold in total are: {articles}.")
    print()

    # TODO: Hausaufgabe: While/ for Schleife so gestalten dass Ändeurngen in data.txt übernommen werden! (Zeile hinzufügen/ Zeile Wegnehmen)
    #--> Ansatz: for-schleife da Durchlauf des vorgegebenen Bereichs nicht durch Benutzer unterbrochen werden soll
    ##Wann soll die schleife enden? Endlosschleife? 
    # Len? --> while counter < len(daily_list):^1

    


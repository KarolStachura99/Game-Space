# Gra Python przy użyciu PygameZero

import time, random, math 

###############
##  ZMIENNE  ##
###############

WIDTH = 800 #rozmiar okna
HEIGHT = 800

#zmienne GRACZA
IMIE_GRACZA = "Karol" 
IMIE_PRZYJACIELA1 = "Zbyszek" 
IMIE_PRZYJACIELA2 = "Kasia"

aktualny_pokoj = 31 # poczatkowy pokoj to 31

gora_lewa_x = 100
gora_lewa_y = 150

#generowanie i przypisanie losowych lokalzacji lądownika
LADOWNIK_SEKTOR = random.randint(1, 24)
LADOWNIK_X = random.randint(2, 11)
LADOWNIK_Y = random.randint(2, 11)

ROZMIAR_KAFELKA = 30

gracz_y, gracz_x = 2, 5
koniec_gry = False

GRACZ = {
    "lewo": [images.skafander_lewy, images.skafander_lewy_1,
             images.skafander_lewy_2, images.skafander_lewy_3,
             images.skafander_lewy_4
             ], 
    "prawo": [images.skafander_prawy, images.skafander_prawy_1,
              images.skafander_prawy_2, images.skafander_prawy_3,
              images.skafander_prawy_4
              ],
    "gora": [images.skafander_tyl, images.skafander_tyl_1,
           images.skafander_tyl_2, images.skafander_tyl_3,
           images.skafander_tyl_4 
           ],
    "dol": [images.skafander_przod, images.skafander_przod_1,
             images.skafander_przod_2, images.skafander_przod_3,
             images.skafander_przod_4
             ]
    }

gracz_kierunek = "dol"
gracz_ramka = 0
gracz_obraz = GRACZ[gracz_kierunek][gracz_ramka]
gracz_przesuniecie_x, gracz_przesuniecie_y = 0, 0

GRACZ_CIEN = {
    "lewo": [images.skafander_lewy_cien, images.skafander_lewy_1_cien,
             images.skafander_lewy_2_cien, images.skafander_lewy_3_cien,
             images.skafander_lewy_4_cien
             ],
    "prawo": [images.skafander_prawy_cien, images.skafander_prawy_1_cien,
              images.skafander_prawy_2_cien,
              images.skafander_prawy_4_cien, images.skafander_prawy_3_cien
              ],
    "gora": [images.skafander_tyl_cien, images.skafander_tyl_1_cien,
           images.skafander_tyl_2_cien, images.skafander_tyl_3_cien,
           images.skafander_tyl_4_cien
           ],
    "dol": [images.skafander_przod_cien, images.skafander_przod_1_cien,
             images.skafander_przod_2_cien, images.skafander_przod_3_cien,
             images.skafander_przod_4_cien
             ]
    }

gracz_obraz_cien = GRACZ_CIEN["dol"][0]

FILARY = [
    images.filar, images.filar_95, images.filar_80,
    images.filar_60, images.filar_50
    ]

ramka_przezroczystosci_sciany = 0

CZARNY = (0, 0, 0)
NIEBIESKI = (0, 155, 255)
ZOLTY = (255, 255, 0)
BIALY = (255, 255, 255)
ZIELONY = (0, 255, 0)
CZERWONY = (128, 0, 0)

powietrze, energia = 100, 100
skafander_zeszyty, butla_naprawiona = False, False
ramka_startu = 0


###############
##   MAPA    ##
###############  

MAPA_SZEROKOSC = 5
MAPA_WYSOKOSC = 10 
MAPA_ROZMIAR = MAPA_SZEROKOSC * MAPA_WYSOKOSC

MAPA_GRY = [ ["Pokoj 0 - magazyn nieuzywanych obiektow", 0, 0, False, False] ]

pokoje_zewnetrzne = range(1, 26)
for sektoryplanety in range(1, 26): #tu generowane sa pokoje 1-25
    MAPA_GRY.append( ["Zapylona powierzchnia planety", 13, 13, True, True] )

MAPA_GRY  += [
        #["Nazwa pokoju", wysokosc, szerokosc, Gorne wyjscie?, Prawe wyjscie?]
        ["Sluza powietrzna", 13, 5, True, False], # pokoj 26
        ["Maszynownia", 13, 13, False, False], # pokoj 27
        ["Centrum sterowania Poodle", 9, 13, False, True], # pokoj 28
        ["Galeria widokowa", 9, 15, False, False], # pokoj 29
        ["Lazienka zalogi", 5, 5, False, False], # pokoj 30
        ["Przedsionek do sluzy powietrznej", 7, 11, True, True], # pokoj 31
        ["Pokoj z lewym wyjsciem", 9, 7, True, False], # pokoj 32
        ["Pokoj z prawym wyjsciem", 7, 13, True, True], # pokoj 33
        ["Laboratorium", 13, 13, False, True], # pokoj 34
        ["Szklarnia", 13, 13, True, False], # pokoj 35
        ["Sypialnia kpt. " + IMIE_GRACZA, 9, 11, False, False], # pokoj 36
        ["Zachodni korytarz", 15, 5, True, True], # pokoj 37
        ["Sala konferencyjna", 7, 13, False, True], # pokoj 38
        ["Swietlica zalogi", 11, 13, True, False], # pokoj 39
        ["Glowne centrum sterowania", 14, 14, False, False], # pokoj 40
        ["Izba chorych", 12, 7, True, False], # pokoj 41
        ["Zachodni korytarz", 9, 7, True, False], # pokoj 42
        ["Centrum infrastruktury technicznej", 9, 9, False, True], # pokoj 43
        ["Centrum zarzadzania systemami", 9, 11, False, False], # pokoj 44
        ["Wejscie do centrum sterowania", 7, 7, True, False], # pokoj 45
        ["Sypialnia plk. " + IMIE_PRZYJACIELA1, 9, 11, True, True], # pokoj 46
        ["Sypialnia plk. " + IMIE_PRZYJACIELA2, 9, 11, True, True], # pokoj 47
        ["Pokoj z systemem rur", 13, 11, True, False], # pokoj 48
        ["Biuro glownego naukowca", 9, 7, True, True], # pokoj 49
        ["Warsztat robotow", 9, 11, True, False] # pokoj 50
        ]

#proste sprawdzenie poprawnosci wpisanych powyzej danych mapy
assert len(MAPA_GRY)-1 == MAPA_ROZMIAR, "Rozmiar mapy nie pasuje do MAPA_GRY"


###############
##  OBIEKTY  ##
###############

obiekty = {
    0: [images.podloga, None, "Podloga jest czysta i blyszczaca"],
    1: [images.filar, images.pelny_cien, "Sciana jest gladka i zimna"],
    2: [images.gleba, None, "Wyglada jak pustynia"],
    3: [images.filar_niski, images.polcien, "Sciana jest gladka i zimna"],
    4: [images.lozko, images.polcien, "Czyste i wygodne lozko"],
    5: [images.stol, images.polcien, "Zrobiony z mocnego plastiku"],
    6: [images.krzeslo_lewe, None, "Krzeslo z miekkim siedziskiem"],
    7: [images.krzeslo_prawe, None, "Krzeslo z miekkim siedziskiem"],
    8: [images.regal_wysoki, images.pelny_cien,
        "Regal wypelniony podrecznikami"],
    9: [images.regal_niski, images.polcien,
        "Regal wypelniony podrecznikami"],
    10: [images.szafka, images.polcien,
         "Mala szafka do przechowywania przedmiotow osobistych"],
    11: [images.komputer_stacjonarny, images.polcien,
         "Komputer. Uzyj do sprawdzania stanu powietrza i energii"],
    12: [images.roslina, images.roslina_cien, "Krzaczek truskawki, wyhodowany na stacji"],
    13: [images.elektryczne1, images.polcien,
         "Systemy elektryczne do zasilania stacji kosmicznej"],
    14: [images.elektryczne2, images.polcien,
         "Systemy elektryczne do zasilania stacji kosmicznej"],
    15: [images.kaktus, images.kaktus_cien, "Au! Uwazaj na kaktusa!"],
    16: [images.krzew, images.krzew_cien,
         "Kosmiczna salata. Nieco zwiedla, ale niesamowite, ze rosnie na stacji!"],
    17: [images.rury1, images.rury1_cien, "Rury instalacji do uzdatniania wody"],
    18: [images.rury2, images.rury2_cien,
         "Rury systemu podtrzymywania zycia"],
    19: [images.rury3, images.rury3_cien,
         "Rury systemu podtrzymywania zycia"],
    20: [images.drzwi, images.drzwi_cien, "Drzwi bezpieczenstwa. Otwierane automatycznie \
przed astronautami w dzialajacych skafandrach."],
    21: [images.drzwi, images.drzwi_cien, "Drzwi sluzy powietrznej. \
Ze wzgledow bezpieczenstwa, do obslugi wymagaja 2 osob."],
    22: [images.drzwi, images.drzwi_cien, "Zamkniete drzwi. Potrzebna karta dostepu \
kpt. "+ IMIE_GRACZA ],
    23: [images.drzwi, images.drzwi_cien, "Zamkniete drzwi. Potrzebna karta dostepu \
plk. "+ IMIE_PRZYJACIELA1 ],
    24: [images.drzwi, images.drzwi_cien, "Zamkniete drzwi. Potrzebna karta dostepu \
plk. "+ IMIE_PRZYJACIELA2 ],
    25: [images.drzwi, images.drzwi_cien,
         "Zamkniete drzwi. Otwierane z glownego centrum sterowania"],
    26: [images.drzwi, images.drzwi_cien,
         "Zamkniete drzwi w maszynowni."],
    27: [images.mapa, images.pelny_cien,
         "Miejsce katastrofy to sektor: " \
         + str(LADOWNIK_SEKTOR) + " // X: " + str(LADOWNIK_X) + \
         " // Y: " + str(LADOWNIK_Y)],
    28: [images.skala_duza, images.skala_duza_cien,
         "Skala. Jej twarda chropowata powierzchnia przypomina piaskowiec", "skala"],
    29: [images.skala_mala, images.skala_mala_cien,
         "Maly, ale ciezki kawalek marsjanskiej skaly"],
    30: [images.krater, None, "Krater na powierzchni planety"],
    31: [images.ogrodzenie, None,
         "Ogrodzenie z gazy. Pomaga chronic stacje przed burza piaskowa"],
    32: [images.mechanizm, images.mechanizm_cien,
         "Jeden z eksperymentow naukowych. Delikatnie wibruje"],
    33: [images.ramie_robota, images.ramie_robota_cien,
         "Ramie robota, sluzy do podnoszenia ciezarow"],
    34: [images.sedes, images.polcien, "Lsniacy czystoscia sedes"],
    35: [images.zlew, None, "Zlew z biezaca woda", "kran"],
    36: [images.globus, images.globus_cien,
         "Wielki globus planety. Delikatnie podswietlony od wewnatrz"],
    37: [images.stol_laboratoryjny, None,
         "Stol laboratoryjny do analizy gleby i pylu planety"],
    38: [images.automat, images.pelny_cien,
         "Automat. Wymaga uzycia monet.", "automat"],
    39: [images.mata_podlogowa, None,
         "Czujnik nacisku blokujacy wychodzenie w pojedynke"],
    40: [images.statek_ratowniczy, images.statek_ratowniczy_cien, "Statek ratowniczy!"],
    41: [images.centrum_sterowania_misja, images.centrum_sterowania_misja_cien, \
         "Stanowiska centrum sterowania"],
    42: [images.przycisk, images.przycisk_cien,
         "Przycisk do otwierania automatycznie zamykanych drzwi w maszynowni"],
    43: [images.tablica, images.pelny_cien,
         "Tablica uzywana podczas spotkan organizacyjnych"],
    44: [images.okno, images.pelny_cien,
         "Okno z widokiem na powierzchnie planety"],
    45: [images.robot, images.robot_cien, "Robot sprzatajacy. Wylaczony."],
    46: [images.robot2, images.robot2_cien,
         "Nieskonfigurowany jeszcze robot do badania powierzchni planety."],
    47: [images.rakieta, images.rakieta_cien, "Jednoosobowy statek jest w naprawie"], 
    48: [images.toksyczna_podloga, None, "Toksyczna podloga - nie stawaj na niej!"],
    49: [images.dron, None, "Dron dostawczy"],
    50: [images.kula_energii, None, "Kula energii - niebezpieczna!"],
    51: [images.kula_energii2, None, "Kula energii - niebezpieczna!"],
    52: [images.komputer, images.komputer_cien,
         "Terminal do zarzadzania systemami stacji kosmicznej."],
    53: [images.notatnik, None,
         "Notatnik. Ktos cos w nim nagryzmolil.", "notatnik"],
    54: [images.guma_do_zucia, None,
         "Kawalek klejacej gumy do zucia. Smak truskawkowy.", "guma do zucia"],
    55: [images.yoyo, None, "Zabawka z cienkiej, mocnej linki i plastiku. \
Sluzy do eksperymentow antygrawitacyjnych", "Jojo kpt. " + IMIE_GRACZA],
    56: [images.nitka, None,
         "Kawalek cienkiej, mocnej linki", "kawalek linki"],
    57: [images.igla, None,
         "Ostra igla kaktusa", "igla kaktusa"],
    58: [images.igla_z_nitka, None,
         "Igla kaktusa z przymocowana linka", "igla z linka"],
    59: [images.butla, None,
         "Butla z tlenem przecieka.", "przeciekajaca butla z tlenem"],
    60: [images.butla, None,
         "Lata chyba sie trzyma!", "zalatana butla z tlenem"],
    61: [images.lustro, None,
         "Lustro rzuca aureole swiatla na sciane.", "lustro"], 
    62: [images.pojemnik_pusty, None,
         "Rzadko uzywany pojemnik z lekkiego plastiku", "pojemnik"],
    63: [images.pojemnik_pelny, None,
         "Ciezki pojemnik wypelniony woda", "pojemnik wypelniony woda"],
    64: [images.szmaty, None,
         "Tlusta szmata! Podnies tylko jesli musisz!", "tlusta szmata"], 
    65: [images.mlotek, None,
         "Mlotek. Byc moze nadaje sie do rozlupywania ...", "mlotek"],
    66: [images.lyzka, None, "Wielka metalowa łyzka", "lyzka"],
    67: [images.torebka_z_jedzeniem, None,
         "Saszetka z suszonym jedzeniem. Wymaga wody.", "suszone jedzenie"], 
    68: [images.jedzenie, None,
         "Saszetka z jedzeniem. Uzyj, aby odzyskac 100% energii.", "jedzenie gotowe do spozycia"], 
    69: [images.ksiazka, None, "Ksiazka ma tytul 'Nie panikuj' \
napisany duza, uspakajajaca czcionka", "ksiazka"], 
    70: [images.odtwarzacz_mp3, None,
         "Odtwarzacz MP3, z najnowszymi hitami", "odtwarzacz MP3"],
    71: [images.ladownik, None, "Poodle, maly statek do eksploracji kosmosu. \
Jego czarne pudelko zawiera radio.", "ladownik Poodle"],
    72: [images.radio, None, "System komunikacji radiowej z ladownika \
Poodle", "radio do komunikacji"],
    73: [images.modul_gps, None, "Modul GPS", "modul GPS"],
    74: [images.system_pozycjonowania, None, "Czesc systemu pozycjonowania. \
Potrzebuje modulu GPS.", "interfejs pozycjonowania"],
    75: [images.system_pozycjonowania, None,
         "Dzialajacy system pozycjonowania", "system pozycjonowania"],
    76: [images.nozyczki, None, "Nozyczki. Zbyt tepe, by cokolwiek przeciac. \
Czy mozesz je naostrzyc?", "tepe nozyczki"],
    77: [images.nozyczki, None,
         "Bardzo ostre nozyczki. Ostroznie!", "naostrzone nozyczki"],
    78: [images.moneta, None, "Mala moneta do uzycia w automatach na stacji", "moneta"],
    79: [images.karta_dostepu, None,
         "Ta karta dostepu nalezy do kpt. " + IMIE_GRACZA, "karta dostepu" ],
    80: [images.karta_dostepu, None,
         "Ta karta dostepu nalezy do plk. " + IMIE_PRZYJACIELA1, "karta dostepu" ],
    81: [images.karta_dostepu, None,
         "Ta karta dostepu nalezy do plk. " + IMIE_PRZYJACIELA2, "karta dostepu" ]
    }

gracz_moze_przenosic = list(range(53, 82))
# Ponizsze numery reprezentuja podloge, mate podlogowa, glebe i toksyczna podloge
gracz_moze_stac_na = gracz_moze_przenosic + [0, 39, 2, 48]


#################
## SCENOGRAFIA ##
#################

# Scenografia opisuje obiekty, ktorych nie mozna przenosic miedzy pokojami
# numer pokoju : [[numer obiektu, polozenie y, polozenie x]...]
scenografia = {
    26: [[39,8,2]],
    27: [[33,5,5], [33,1,1], [33,1,8], [47,5,2],
         [47,3,10], [47,9,8], [42,1,6]],
    28: [[27,0,3], [41,4,3], [41,4,7]],
    29: [[7,2,6], [6,2,8], [12,1,13], [44,0,1],
         [36,4,10], [10,1,1], [19,4,2], [17,4,4]],
    30: [[34,1,1], [35,1,3]],
    31: [[11,1,1], [19,1,8], [46,1,3]],
    32: [[48,2,2], [48,2,3], [48,2,4], [48,3,2], [48,3,3],
         [48,3,4], [48,4,2], [48,4,3], [48,4,4]],
    33: [[13,1,1], [13,1,3], [13,1,8], [13,1,10], [48,2,1],
         [48,2,7], [48,3,6], [48,3,3]],
    34: [[37,2,2], [32,6,7], [37,10,4], [28,5,3]],
    35: [[16,2,9], [16,2,2], [16,3,3], [16,3,8], [16,8,9], [16,8,2], [16,1,8],
         [16,1,3], [12,8,6], [12,9,4], [12,9,8],
         [15,4,6], [12,7,1], [12,7,11]],
    36: [[4,3,1], [9,1,7], [8,1,8], [8,1,9],
         [5,5,4], [6,5,7], [10,1,1], [12,1,2]],
    37: [[48,3,1], [48,3,2], [48,7,1], [48,5,2], [48,5,3],
         [48,7,2], [48,9,2], [48,9,3], [48,11,1], [48,11,2]],
    38: [[43,0,2], [6,2,2], [6,3,5], [6,4,7], [6,2,9], [45,1,10]],
    39: [[38,1,1], [7,3,4], [7,6,4], [5,3,6], [5,6,6],
         [6,3,9], [6,6,9], [45,1,11], [12,1,8], [12,1,4]], 
    40: [[41,5,3], [41,5,7], [41,9,3], [41,9,7],
         [13,1,1], [13,1,3], [42,1,12]],
    41: [[4,3,1], [10,3,5], [4,5,1], [10,5,5], [4,7,1],
         [10,7,5], [12,1,1], [12,1,5]],
    44: [[46,4,3], [46,4,5], [18,1,1], [19,1,3],
         [19,1,5], [52,4,7], [14,1,8]],
    45: [[48,2,1], [48,2,2], [48,3,3], [48,3,4], [48,1,4], [48,1,1]],
    46: [[10,1,1], [4,1,2], [8,1,7], [9,1,8], [8,1,9], [5,4,3], [7,3,2]],
    47: [[9,1,1], [9,1,2], [10,1,3], [12,1,7], [5,4,4], [6,4,7], [4,1,8]],
    48: [[17,4,1], [17,4,2], [17,4,3], [17,4,4], [17,4,5], [17,4,6], [17,4,7],
         [17,8,1], [17,8,2], [17,8,3], [17,8,4],
         [17,8,5], [17,8,6], [17,8,7], [14,1,1]],
    49: [[14,2,2], [14,2,4], [7,5,1], [5,5,3], [48,3,3], [48,3,4]], 
    50: [[45,4,8], [11,1,1], [13,1,8], [33,2,1], [46,4,6]] 
    }

suma_kontrolna = 0
licznik_kontrolny = 0
for klucz, lista_scenografii_pokoju in scenografia.items():
    for lista_elem_scenografii in lista_scenografii_pokoju:
        suma_kontrolna += (lista_elem_scenografii[0] * klucz
                     + lista_elem_scenografii[1] * (klucz + 1) 
                     + lista_elem_scenografii[2] * (klucz + 2))
        licznik_kontrolny += 1
print("Elementy scenografii: ", licznik_kontrolny)
assert licznik_kontrolny == 161, "Oczekiwano 161 elementow scenografii"
assert suma_kontrolna == 200095, "Blad w danych scenografii"
print("Suma kontrolna scenografii: " + str(suma_kontrolna))

for pokoj in range(1, 26):# Dodawanie losowej scenografii na zewnatrz.
    if pokoj != 13: # Pokoj 13 pominiety.
        elem_scenografii = random.choice([16, 28, 29, 30])
        scenografia[pokoj] = [[elem_scenografii, random.randint(2, 10),
                          random.randint(2, 10)]]
        
# Petle do dodania ogrodzen do pokoi na powierzchni planety.
for wspolrzedna_pokoju in range(0, 13):
    for numer_pokoju in [1, 2, 3, 4, 5]: # Dodanie gornego ogrodzenia
        scenografia[numer_pokoju] += [[31, 0, wspolrzedna_pokoju]]
    for numer_pokoju in [1, 6, 11, 16, 21]: # Dodanie lewego ogrodzenia
        scenografia[numer_pokoju] += [[31, wspolrzedna_pokoju, 0]]
    for numer_pokoju in [5, 10, 15, 20, 25]: # Dodanie prawego ogrodzenia
        scenografia[numer_pokoju] += [[31, wspolrzedna_pokoju, 12]]

del scenografia[21][-1] # Usuniecie ostatniego panelu z pokoju 21
del scenografia[25][-1] # Usuniecie ostatniego panelu z pokoju 25
           

####################
## TWORZENIE MAPY ##
####################

def sprawdz_typ_podlogi():
    if aktualny_pokoj in pokoje_zewnetrzne:
        return 2 # gleba
    else:
        return 0 # wykafelkowana podloga       

def generuj_mape():
# Ta funkcja tworzy mape aktualnego pokoju,
# przy uzyciu danych pokoju, scenografii i rekwizytow.
    global mapa_pokoju, szer_pokoju, wys_pokoju, nazwa_pokoju, mapa_zagrozen
    global gora_lewa_x, gora_lewa_y, ramka_przezroczystosci_sciany
    dane_pokoju = MAPA_GRY[aktualny_pokoj]
    nazwa_pokoju = dane_pokoju[0]
    wys_pokoju = dane_pokoju[1]
    szer_pokoju = dane_pokoju[2]

    typ_podlogi = sprawdz_typ_podlogi()
    if aktualny_pokoj in range(1, 21):
        dolny_brzeg = 2 #gleba
        boczny_brzeg = 2 #gleba
    if aktualny_pokoj in range(21, 26):
        dolny_brzeg = 1 #sciana
        boczny_brzeg = 2 #gleba
    if aktualny_pokoj > 25:
        dolny_brzeg = 1 #sciana
        boczny_brzeg = 1 #sciana

    # Tworzenie gornego rzedu mapy pokoju.
    mapa_pokoju=[[boczny_brzeg] * szer_pokoju]
    # Dodanie srodkowych rzedow mapy pokoju (sciana, posrodku podloga, sciana).
    for y in range(wys_pokoju - 2):
        mapa_pokoju.append([boczny_brzeg]
                        + [typ_podlogi]*(szer_pokoju - 2) + [boczny_brzeg])
    # Dodanie dolnego rzedu mapy pokoju .
    mapa_pokoju.append([dolny_brzeg] * szer_pokoju)

    # Dodanie wyjsc.
    srodkowy_rzad = int(wys_pokoju / 2)
    srodkowa_kolumna = int(szer_pokoju / 2)

    if dane_pokoju[4]: # Jesli pokoj ma prawe wyjscie
        mapa_pokoju[srodkowy_rzad][szer_pokoju - 1] = typ_podlogi
        mapa_pokoju[srodkowy_rzad+1][szer_pokoju - 1] = typ_podlogi
        mapa_pokoju[srodkowy_rzad-1][szer_pokoju - 1] = typ_podlogi

    if aktualny_pokoj % MAPA_SZEROKOSC != 1: # Jesli pokoj nie lezy po lewej stronie mapy
        pokoj_po_lewej = MAPA_GRY[aktualny_pokoj - 1]
        # Jesli pokoj po lewej ma prawe wyjscie, dodanie lewego wyjscia w tym pokoju
        if pokoj_po_lewej[4]: 
            mapa_pokoju[srodkowy_rzad][0] = typ_podlogi 
            mapa_pokoju[srodkowy_rzad + 1][0] = typ_podlogi
            mapa_pokoju[srodkowy_rzad - 1][0] = typ_podlogi

    if dane_pokoju[3]: # Jesli pokoj ma gorne wyjscie
        mapa_pokoju[0][srodkowa_kolumna] = typ_podlogi
        mapa_pokoju[0][srodkowa_kolumna + 1] = typ_podlogi
        mapa_pokoju[0][srodkowa_kolumna - 1] = typ_podlogi

    if aktualny_pokoj <= MAPA_ROZMIAR - MAPA_SZEROKOSC: # Jesli pokoj nie lezy w dolnym rzedzie
        pokoj_ponizej = MAPA_GRY[aktualny_pokoj+MAPA_SZEROKOSC]
        # Jesli pokoj ponizej ma gorne wyjscie, dodanie dolnego wyjscia w tym pokoju
        if pokoj_ponizej[3]: 
            mapa_pokoju[wys_pokoju-1][srodkowa_kolumna] = typ_podlogi 
            mapa_pokoju[wys_pokoju-1][srodkowa_kolumna + 1] = typ_podlogi
            mapa_pokoju[wys_pokoju-1][srodkowa_kolumna - 1] = typ_podlogi
    
    if aktualny_pokoj in scenografia:# Sprawdzamy, czy dla aktualnego pokoju istnieje przypisana scenografia.
        for ta_scenografia in scenografia[aktualny_pokoj]:  # Iterujemy przez wszystkie elementy scenografii przypisane do aktualnego pokoju.
            scenografia_numer = ta_scenografia[0]# Pobieramy numer identyfikacyjny danego elementu scenografii
            scenografia_y = ta_scenografia[1]# Pobieramy współrzędną Y elementu scenografii
            scenografia_x = ta_scenografia[2]# Pobieramy współrzędną X elementu scenografii
            # Umieszczamy numer elementu scenografii w odpowiednim miejscu mapy pokoju
            mapa_pokoju[scenografia_y][scenografia_x] = scenografia_numer
            # Pobieramy obraz przypisany do danego elementu scenografii
            obraz_tutaj = obiekty[scenografia_numer][0]
            obraz_szerokosc = obraz_tutaj.get_width()# Pobieramy szerokość obrazu scenografii w pikselach
            obraz_kafel_szerokosc = int(obraz_szerokosc / ROZMIAR_KAFELKA)# Obliczamy szerokość obrazu scenografii w jednostkach kafelków
            # Iterujemy przez dodatkowe kafelki zajmowane przez scenografię, jeśli jest szersza niż jeden kafelek
            for numer_kafelka in range(1, obraz_kafel_szerokosc):
                mapa_pokoju[scenografia_y][scenografia_x + numer_kafelka] = 255

    srodek_y = int(HEIGHT / 2) # Srodek okna gry
    srodek_x = int(WIDTH / 2)
    szer_pokoju_w_piks = szer_pokoju * ROZMIAR_KAFELKA # Rozmiar pokoju w pikselach
    wys_pokoju_w_piks = wys_pokoju * ROZMIAR_KAFELKA
    gora_lewa_x = srodek_x - 0.5 * szer_pokoju_w_piks 
    gora_lewa_y = (srodek_y - 0.5 * wys_pokoju_w_piks) + 110

    for rekwizyt_numer, rekwizyt_info in rekwizyty.items():
        rekwizyt_pokoj = rekwizyt_info[0]
        rekwizyt_y = rekwizyt_info[1]
        rekwizyt_x = rekwizyt_info[2]
         # Sprawdzenie, czy rekwizyt należy do aktualnego pokoju oraz czy kafelek, na którym się znajduje, 
         # jest jednym z dozwolonych (0, 39, 2)
        if (rekwizyt_pokoj == aktualny_pokoj and
            mapa_pokoju[rekwizyt_y][rekwizyt_x] in [0, 39, 2]):
            # Umieszczenie numeru rekwizytu na odpowiednim kafelku mapy pokoju.
                mapa_pokoju[rekwizyt_y][rekwizyt_x] = rekwizyt_numer
                # Pobranie obrazu przypisanego do danego rekwizytu.
                obraz_tutaj = obiekty[rekwizyt_numer][0]
                # Pobranie szerokości obrazu w pikselach.
                obraz_szerokosc = obraz_tutaj.get_width()
                # Obliczenie szerokości obrazu w jednostkach kafelków.
                obraz_kafel_szerokosc = int(obraz_szerokosc / ROZMIAR_KAFELKA)
                 # Oznaczenie dodatkowych kafelków zajmowanych przez rekwizyt na mapie pokoju.
                for numer_kafelka in range(1, obraz_kafel_szerokosc):
                    mapa_pokoju[rekwizyt_y][rekwizyt_x + numer_kafelka] = 255    

    mapa_zagrozen = [] # pusta lista
    for y in range(wys_pokoju):
        mapa_zagrozen.append( [0] * szer_pokoju )
        

###############
## PETLA GRY ##
###############

def przygotuj_pokoj():
    global ramka_drzwi_sluzy
    pokaz_tekst("Jestes tutaj: " + nazwa_pokoju, 0)
    if aktualny_pokoj == 26: # Pokoj z automatycznie zamykanymi drzwiami
        ramka_drzwi_sluzy = 0
        clock.schedule_interval(drzwi_w_pokoju_26, 0.05)
    przygotuj_zagrozenia()

def petla_gry():
    global gracz_x, gracz_y, aktualny_pokoj
    global gracz_z_x, gracz_z_y
    global gracz_obraz, gracz_obraz_cien 
    global wybrany_element, trzymany_element, energia 
    global gracz_przesuniecie_x, gracz_przesuniecie_y
    global gracz_ramka, gracz_kierunek

    if koniec_gry:
        return

    if gracz_ramka > 0:
        gracz_ramka += 1
        time.sleep(0.05)
        if gracz_ramka == 5:
            gracz_ramka = 0
            gracz_przesuniecie_x = 0
            gracz_przesuniecie_y = 0

# Zapisanie aktualnej pozycji gracza
    poprz_gracz_x = gracz_x
    poprz_gracz_y = gracz_y

# Ruch, jesli nacisnieto klawisz
    if gracz_ramka == 0:
        if keyboard.right:
            gracz_z_x = gracz_x
            gracz_z_y = gracz_y
            gracz_x += 1
            gracz_kierunek = "prawo"
            gracz_ramka = 1
        elif keyboard.left: #elif powstrzymuje przed przechodzeniem po skosie
            gracz_z_x = gracz_x
            gracz_z_y = gracz_y
            gracz_x -= 1
            gracz_kierunek = "lewo"
            gracz_ramka = 1
        elif keyboard.up:
            gracz_z_x = gracz_x
            gracz_z_y = gracz_y
            gracz_y -= 1
            gracz_kierunek = "gora"
            gracz_ramka = 1
        elif keyboard.down:
            gracz_z_x = gracz_x
            gracz_z_y = gracz_y
            gracz_y += 1
            gracz_kierunek = "dol"
            gracz_ramka = 1        

# Wykrywanie wyjscia z pokoju
    if gracz_x == szer_pokoju: # przez drzwi po PRAWEJ
        clock.unschedule(ruch_zagrozenia)
        aktualny_pokoj += 1
        generuj_mape()
        gracz_x = 0 # wejscie z lewej
        gracz_y = int(wys_pokoju / 2) # wejscie przez drzwi
        gracz_ramka = 0
        przygotuj_pokoj()
        return

    if gracz_x == -1: # przez drzwi po LEWEJ
        clock.unschedule(ruch_zagrozenia)
        aktualny_pokoj -= 1
        generuj_mape()
        gracz_x = szer_pokoju - 1  # wejscie z prawej
        gracz_y = int(wys_pokoju / 2) # wejscie przez drzwi
        gracz_ramka = 0
        przygotuj_pokoj()
        return

    if gracz_y == wys_pokoju: # przez drzwi na DOLE
        clock.unschedule(ruch_zagrozenia)
        aktualny_pokoj += MAPA_SZEROKOSC
        generuj_mape()
        gracz_y = 0 # wejscie z gory
        gracz_x = int(szer_pokoju / 2) # wejscie przez drzwi
        gracz_ramka = 0
        przygotuj_pokoj()
        return

    if gracz_y == -1: # przez drzwi na GORZE
        clock.unschedule(ruch_zagrozenia)
        aktualny_pokoj -= MAPA_SZEROKOSC
        generuj_mape()
        gracz_y = wys_pokoju - 1 # wejscie z dolu
        gracz_x = int(szer_pokoju / 2) # wejscie przez drzwi
        gracz_ramka = 0
        przygotuj_pokoj()
        return 

    if keyboard.w:
        podnies_obiekt()

    if keyboard.tab and len(w_ekwipunku) > 0:
        wybrany_element += 1
        if wybrany_element > len(w_ekwipunku) - 1:
            wybrany_element = 0
        trzymany_element = w_ekwipunku[wybrany_element]
        wyswietl_ekwipunek()

    if keyboard.r and trzymany_element:
        upusc_obiekt(poprz_gracz_y, poprz_gracz_x)
        
    if keyboard.space:
        zbadaj_obiekt()

    if keyboard.u:
        uzyj_obiektu()


  # Jesli gracz stoi w nieodpowiednim miejscu, przeniesienie go z powrotem.
    if mapa_pokoju[gracz_y][gracz_x] not in gracz_moze_stac_na \
               or mapa_zagrozen[gracz_y][gracz_x] != 0:
        gracz_x = poprz_gracz_x
        gracz_y = poprz_gracz_y
        gracz_ramka = 0

    if mapa_pokoju[gracz_y][gracz_x] == 48: # toksyczna podloga
        wyczerpuj_energie(1)

    if gracz_kierunek == "prawo" and gracz_ramka > 0:
        gracz_przesuniecie_x = -1 + (0.25 * gracz_ramka)
    if gracz_kierunek == "lewo" and gracz_ramka > 0:
        gracz_przesuniecie_x = 1 - (0.25 * gracz_ramka)
    if gracz_kierunek == "gora" and gracz_ramka > 0:
        gracz_przesuniecie_y = 1 - (0.25 * gracz_ramka)
    if gracz_kierunek == "dol" and gracz_ramka > 0:
        gracz_przesuniecie_y = -1 + (0.25 * gracz_ramka)


##################
## WYSWIETLANIE ##
##################
            
def rysuj_obraz(obraz, y, x):
    screen.blit(
        obraz,
        (gora_lewa_x + (x * ROZMIAR_KAFELKA),
         gora_lewa_y + (y * ROZMIAR_KAFELKA) - obraz.get_height())
        )

def rysuj_cien(obraz, y, x):
    screen.blit(
        obraz,
        (gora_lewa_x + (x * ROZMIAR_KAFELKA),
         gora_lewa_y + (y * ROZMIAR_KAFELKA))
        )

def rysuj_gracza():
    gracz_obraz = GRACZ[gracz_kierunek][gracz_ramka]
    rysuj_obraz(gracz_obraz, gracz_y + gracz_przesuniecie_y,
               gracz_x + gracz_przesuniecie_x)
    gracz_obraz_cien = GRACZ_CIEN[gracz_kierunek][gracz_ramka]
    rysuj_cien(gracz_obraz_cien, gracz_y + gracz_przesuniecie_y,
                gracz_x + gracz_przesuniecie_x)

def draw():
    if koniec_gry:
        return

    # Oczyszczenie pola gry.
    prostokat = Rect((0, 150), (800, 600))
    screen.draw.filled_rect(prostokat, CZERWONY)
    prostokat = Rect ((0, 0), (800, gora_lewa_y + (wys_pokoju - 1)*30))
    screen.surface.set_clip(prostokat)
    typ_podlogi = sprawdz_typ_podlogi()

    for y in range(wys_pokoju): # Wylozenie kafelkow podlogowych, a pozniej elementow na podlodze
        for x in range(szer_pokoju):
            rysuj_obraz(obiekty[typ_podlogi][0], y, x)
            # Aby cienie mogly padac na obiekty na podlodze
            if mapa_pokoju[y][x] in gracz_moze_stac_na: 
                rysuj_obraz(obiekty[mapa_pokoju[y][x]][0], y, x)

    # Tutaj dodajemy mate w pokoju 26, aby moc umieszczac na niej rekwizyty.
    if aktualny_pokoj == 26:
        rysuj_obraz(obiekty[39][0], 8, 2)
        obraz_na_macie = mapa_pokoju[8][2]
        if obraz_na_macie > 0:
            rysuj_obraz(obiekty[obraz_na_macie][0], 8, 2)

    for y in range(wys_pokoju):
        for x in range(szer_pokoju):
            element_tutaj = mapa_pokoju[y][x]
            # Nie mozna stac na 255: to miejsce uzywane przez szersze obiekty
            if element_tutaj not in gracz_moze_stac_na + [255]:
                obraz = obiekty[element_tutaj][0]

                if (aktualny_pokoj in pokoje_zewnetrzne 
                    and y == wys_pokoju - 1
                    and mapa_pokoju[y][x] == 1) or \
                    (aktualny_pokoj not in pokoje_zewnetrzne
                    and y == wys_pokoju - 1
                    and mapa_pokoju[y][x] == 1
                    and x > 0
                    and x < szer_pokoju - 1): 
                    # Dodawanie przezroczystego obrazu sciany z przodu
                    obraz = FILARY[ramka_przezroczystosci_sciany]
               
                rysuj_obraz(obraz, y, x)

                if obiekty[element_tutaj][1] is not None: # Jesli obiekt ma cien
                    obraz_cienia = obiekty[element_tutaj][1]
                    # Gdy cien wymaga poziomego podzialu na kafelki
                    if obraz_cienia in [images.polcien,
                                        images.pelny_cien]:
                        cien_szerokosc = int(obraz.get_width() / ROZMIAR_KAFELKA)
                        # Rozszerzanie cienia na caly obiekt.
                        for z in range(0, cien_szerokosc):
                            rysuj_cien(obraz_cienia, y, x+z)
                    else:
                        rysuj_cien(obraz_cienia, y, x)

            zagrozenie_tutaj = mapa_zagrozen[y][x]
            if zagrozenie_tutaj != 0: # Jesli zagrozenie znajduje sie na tej pozycji
                rysuj_obraz(obiekty[zagrozenie_tutaj][0], y, x)
                
        if (gracz_y == y):
                rysuj_gracza()

    screen.surface.set_clip(None)

def dostosuj_przezroczystosc_sciany():
    global ramka_przezroczystosci_sciany

    if (gracz_y == wys_pokoju - 2
        and mapa_pokoju[wys_pokoju - 1][gracz_x] == 1
        and ramka_przezroczystosci_sciany < 4):  
        ramka_przezroczystosci_sciany += 1 # Znikanie sciany.
        
    if ((gracz_y < wys_pokoju - 2
            or mapa_pokoju[wys_pokoju - 1][gracz_x] != 1)
            and ramka_przezroczystosci_sciany > 0):
        ramka_przezroczystosci_sciany -= 1 # Pojawianie sie sciany.
        
def pokaz_tekst(tekst_do_pokazania, numer_rzedu):
    if koniec_gry:
        return
    rzedy_tekstu = [15, 50]
    prostokat = Rect((0, rzedy_tekstu[numer_rzedu]), (800, 35))
    screen.draw.filled_rect(prostokat, CZARNY)
    screen.draw.text(tekst_do_pokazania,
                     (20, rzedy_tekstu[numer_rzedu]), color=ZIELONY)


###############
## REKWIZYTY ##
###############

# Rekwizyty to obiekty, ktore moga byc przenoszone miedzy pokojami, pojawiac sie i znikac.
# Wszystkie rekwizyty musza byc tu dodane. Rekwizyty niedostepne jeszcze w grze umieszczane sa w pokoju 0.
# numer obiektu : [pokoj, y, x]
rekwizyty = {
    20: [31, 0, 4], 21: [26, 0, 1], 22: [41, 0, 2], 23: [39, 0, 5],
    24: [45, 0, 2],
    25: [32, 0, 2], 26: [27, 12, 5], # dwie strony tych samych drzwi
    40: [0, 8, 6], 53: [45, 1, 5], 54: [0, 0, 0], 55: [0, 0, 0],
    56: [0, 0, 0], 57: [35, 4, 6], 58: [0, 0, 0], 59: [31, 1, 7],
    60: [0, 0, 0], 61: [36, 1, 1], 62: [36, 1, 6], 63: [0, 0, 0],
    64: [27, 8, 3], 65: [50, 1, 7], 66: [39, 5, 6], 67: [46, 1, 1],
    68: [0, 0, 0], 69: [30, 3, 3], 70: [47, 1, 3],
    71: [0, LADOWNIK_Y, LADOWNIK_X], 72: [0, 0, 0], 73: [27, 4, 6], 
    74: [28, 1, 11], 75: [0, 0, 0], 76: [41, 3, 5], 77: [0, 0, 0],
    78: [35, 9, 11], 79: [26, 3, 2], 80: [41, 7, 5], 81: [29, 1, 1]
    }

suma_kontrolna = 0
for klucz, rekwizyt in rekwizyty.items():
    if klucz != 71: # rekwizyt 71 pominiety, poniewaz w kazdej grze jest inny.
        suma_kontrolna += (rekwizyt[0] * klucz
                     + rekwizyt[1] * (klucz + 1) 
                     + rekwizyt[2] * (klucz + 2))
print(len(rekwizyty), "rekwizytow")
assert len(rekwizyty) == 37, "Oczekiwano 37 elem. rekwizytow"
print("Suma kontrolna rekwizytow:", suma_kontrolna)
assert suma_kontrolna == 61414, "Blad w danych rekwizytow"


w_ekwipunku = [55]
wybrany_element = 0 # pierwszy element
trzymany_element = w_ekwipunku[wybrany_element]

PRZEPISY = [
    [62, 35, 63], [76, 28, 77], [78, 38, 54], [73, 74, 75],
    [59, 54, 60], [77, 55, 56], [56, 57, 58], [71, 65, 72],
    [88, 58, 89], [89, 60, 90], [67, 35, 68]
    ]

suma_kontrolna = 0
licznik_kontrolny = 1
for przepis in PRZEPISY:
    suma_kontrolna += (przepis[0] * licznik_kontrolny
                 + przepis[1] * (licznik_kontrolny + 1) 
                 + przepis[2] * (licznik_kontrolny + 2))
    licznik_kontrolny += 3
print(len(PRZEPISY), "przepisow")
assert len(PRZEPISY) == 11, "Oczekiwano 11 przepisow"
assert suma_kontrolna == 37296, "Blad w danych przepisow"
print("Suma kontrolna przepisow:", suma_kontrolna)



##############################
## INTERAKCJE Z REKWIZYTAMI ##
##############################

def znajdz_x_poczatku_obiektu():
    sprawdzacz_x = gracz_x
    while mapa_pokoju[gracz_y][sprawdzacz_x] == 255:
        sprawdzacz_x -= 1
    return sprawdzacz_x

def wez_elem_pod_graczem():
    element_x = znajdz_x_poczatku_obiektu()
    gracz_na_elemencie = mapa_pokoju[gracz_y][element_x]
    return gracz_na_elemencie

def podnies_obiekt():
    global mapa_pokoju
    # Pobranie numeru obiektu na pozycji gracza.
    gracz_na_elemencie = wez_elem_pod_graczem()
    if gracz_na_elemencie in gracz_moze_przenosic:
        # Wyczyszczenie miejsca na podlodze.
        mapa_pokoju[gracz_y][gracz_x] = sprawdz_typ_podlogi() 
        dodaj_obiekt(gracz_na_elemencie)
        pokaz_tekst("Obiekt dodany do ekwipunku: " + obiekty[gracz_na_elemencie][3], 0)
        time.sleep(0.5)
    else:
        pokaz_tekst("Nie mozna tego podniesc", 0)

def dodaj_obiekt(element): # Dodanie obiektu do ekwipunku.
    global wybrany_element, trzymany_element
    w_ekwipunku.append(element)
    trzymany_element = element
    # Minus 1 poniewaz indeksy zaczynaja sie od 0.
    wybrany_element = len(w_ekwipunku) - 1 
    wyswietl_ekwipunek()
    rekwizyty[element][0] = 0 # Noszone obiekty laduja w pokoju 0 (poza mapa).

def wyswietl_ekwipunek():# Tworzenie prostokąta tła dla ekwipunku i wypełnienie go kolorem czarnym
    prostokat = Rect((0, 45), (800, 105))
    screen.draw.filled_rect(prostokat, CZARNY)
    # Jeśli ekwipunek jest pusty, kończymy funkcję.
    if len(w_ekwipunku) == 0:
        return

    pocz_wyswietlania = (wybrany_element // 16) * 16
    lista_do_pokazania = w_ekwipunku[pocz_wyswietlania : pocz_wyswietlania + 16]
    znacznik_wyboru = wybrany_element % 16# Obliczenie pozycji znacznika wyboru w bieżącej liście.

    for licznik_elem in range(len(lista_do_pokazania)):# Wyświetlanie każdego elementu z listy na ekranie.
        numer_elem = lista_do_pokazania[licznik_elem]# Numer elementu z ekwipunku
        obraz = obiekty[numer_elem][0]# Pobranie grafiki przypisanej do elementu
        screen.blit(obraz, (25 + (46 * licznik_elem), 90))# Wyświetlenie elementu
    # Obliczenie pozycji ramki wyboru wokół wybranego elementu.
    ramka_lewa = (znacznik_wyboru * 46) - 3
    ramka = Rect((22 + ramka_lewa, 85), (40, 40))#rostokąta ramki
    screen.draw.rect(ramka, BIALY)# Rysowanie białej ramki
    # Pobranie wybranego elementu ekwipunku i jego opisu.
    wyrozniony_elem = w_ekwipunku[wybrany_element]
    opis = obiekty[wyrozniony_elem][2]# Pobranie opisu obiektu.
    screen.draw.text(opis, (20, 130), color="white")# Wyświetlenie opisu wybranego elementu pod ekwipunkiem

def upusc_obiekt(poprz_y, poprz_x):
    global mapa_pokoju, rekwizyty
    if mapa_pokoju[poprz_y][poprz_x] in [0, 2, 39]: # tu mozna upuszczac obiekty
        rekwizyty[trzymany_element][0] = aktualny_pokoj
        rekwizyty[trzymany_element][1] = poprz_y
        rekwizyty[trzymany_element][2] = poprz_x
        mapa_pokoju[poprz_y][poprz_x] = trzymany_element
        pokaz_tekst("Upuszczono obiekt: " + obiekty[trzymany_element][3], 0)

        usun_obiekt(trzymany_element)
        time.sleep(0.5)
    else: # Tylko wtedy, gdy rekwizyt juz sie tu znajduje
        pokaz_tekst("Nie mozesz upuscic tu obiektu.", 0)
        time.sleep(0.5)

def usun_obiekt(element): # Wyjecie elementu z ekwipunku
    global wybrany_element, w_ekwipunku, trzymany_element
    w_ekwipunku.remove(element)
    wybrany_element = wybrany_element - 1
    if wybrany_element < 0:
        wybrany_element = 0
    if len(w_ekwipunku) == 0: # Gdy ekwipunek pusty
        trzymany_element = False # zmiennej trzymany_element przypisujemy False
    else: # W przeciwnym razie przypisujemy nowy wybrany element
        trzymany_element = w_ekwipunku[wybrany_element]
    wyswietl_ekwipunek()

def zbadaj_obiekt():
    gracz_na_elemencie = wez_elem_pod_graczem()
    lewy_kafalek_elementu = znajdz_x_poczatku_obiektu()
    if gracz_na_elemencie in [0, 2]: # nie opisujemy podlogi
        return
    opis = "To jest: " + obiekty[gracz_na_elemencie][2]
    for rekwizyt_numer, szczegoly in rekwizyty.items():
        # rekwizyty = numer obiektu: [numer pokoju, y, x]
        if szczegoly[0] == aktualny_pokoj: # jesli rekwizyt jest w pokoju
            # jesli rekwizyt jest ukryty (na pozycji gracza, ale nie na mapie)
            if (szczegoly[1] == gracz_y
                and szczegoly[2] == lewy_kafalek_elementu 
                and mapa_pokoju[szczegoly[1]][szczegoly[2]] != rekwizyt_numer):
                dodaj_obiekt(rekwizyt_numer)
                opis = "Znaleziono obiekt: " + obiekty[rekwizyt_numer][3]

    pokaz_tekst(opis, 0)
    time.sleep(0.5)


#####################
## UZYCIE OBIEKTOW ##
#####################

def uzyj_obiektu():
    global mapa_pokoju, rekwizyty, trzymany_element, powietrze, wybrany_element, energia
    global w_ekwipunku, skafander_zeszyty, butla_naprawiona, koniec_gry

    komunikat_uzycia = "Cos tam majstrujesz, ale bezskutecznie."
    standardowe_reakcje = {
        4: "Powietrze sie konczy. Teraz nie pora na sen.",
        6: "To nie pora na bezczynne siedzenie.",
        7: "To nie pora na bezczynne siedzenie.",
        32: "Trzesie sie i turkocze, ale nic sie nie dzieje.",
        34: "Ale ulga! Teraz trzeba umyc rece.",
        35: "Myjesz rece i strzepujesz wode.",
        37: "Po wstrzasnieciu, z probowki wydobywa sie nieco dymu.",
        54: "Zujesz gume. Jest klejaca.",
        55: "Jojo zwija sie i rozwija, nieco wolniej niz na Ziemi",
        56: "Za bardzo sie wygina. Moze mozna ja do czegos przymocowac?",
        59: "Musisz naprawic przeciek przed uzyciem butli",
        61: "Probujesz wyslac sygnaly przy uzyciu lustra, ale nikt ich nie widzi.",
        62: "Nie wyrzucaj zasobow. Moga sie do czegos przydac.",
        67: "Aby uzyskac pyszne jedzenie, wystarczy dodac wody!",
        75: "Jestes w sektorze: " + str(aktualny_pokoj) + " // X: " \
            + str(gracz_x) + " // Y: " + str(gracz_y)  
        }

    # Pobranie numeru obiektu na pozycji gracza.
    gracz_na_elemencie = wez_elem_pod_graczem()
    for ten_element in [gracz_na_elemencie, trzymany_element]:
        if ten_element in standardowe_reakcje:
            komunikat_uzycia = standardowe_reakcje[ten_element]

    if trzymany_element == 70 or gracz_na_elemencie == 70:
        komunikat_uzycia = "Super muza!"


    elif gracz_na_elemencie == 11:
        komunikat_uzycia = "POWIETRZE: " + str(powietrze) + \
                      "% / ENERGIA " + str(energia) + "% / "
        if not skafander_zeszyty:
            komunikat_uzycia += "SKAFANDER MA DZIURE / "
        if not butla_naprawiona:
            komunikat_uzycia += "SKAFANDER NIE MA BUTLI"
        if skafander_zeszyty and butla_naprawiona:
            komunikat_uzycia += " SKAFANDER OK"
        pokaz_tekst(komunikat_uzycia, 0)
        time.sleep(0.5)
        # Jesli gracz "na" komputerze chce sprawdzic aktualny stan
        # Powrot, aby uzycie innego obiektu przypadkiem nie nadpisalo komunikatu.
        return

    elif trzymany_element == 60 or gracz_na_elemencie == 60: 
        komunikat_uzycia = obiekty[60][3] + " przymocowana do skafandra" 
        butla_naprawiona = True
        powietrze = 90 
        redukuj_powietrze()
        usun_obiekt(60)

    elif (trzymany_element == 58 or gracz_na_elemencie == 58) \
       and not skafander_zeszyty:
        komunikat_uzycia = "Uzyta " + obiekty[56][3] + \
                      " skutecznie zalatala dziure w skafandrze"
        skafander_zeszyty = True
        usun_obiekt(58)

    elif trzymany_element == 72 or gracz_na_elemencie == 72: 
        komunikat_uzycia = "Wysylasz sygnal o pomoc. Pomoc nadchodzi. \
Miejsce spotkania: sektor 13, na zewnatrz."
        rekwizyty[40][0] = 13 

    elif (trzymany_element == 66 or gracz_na_elemencie == 66) \
            and aktualny_pokoj in pokoje_zewnetrzne:
        komunikat_uzycia = "Kopiesz..."
        if (aktualny_pokoj == LADOWNIK_SEKTOR
            and gracz_x == LADOWNIK_X 
            and gracz_y == LADOWNIK_Y):
            dodaj_obiekt(71)
            komunikat_uzycia = "Znaleziono obiekt: ladownik Poodle!"

    elif gracz_na_elemencie == 40:
        clock.unschedule(redukuj_powietrze)
        pokaz_tekst("Gratulacje kpt. "+ IMIE_GRACZA +"!", 0)
        pokaz_tekst("Ewakuacja powiodla sie i misja zakonczyla sie sukcesem.", 1)
        koniec_gry = True

        sekwencja_konczenia_gry()

    elif gracz_na_elemencie == 16:
        energia += 1
        if energia > 100:
            energia = 100
        komunikat_uzycia = "Po schrupaniu salaty odzyskales troche energii"
        rysuj_energie_powietrze()        

    elif gracz_na_elemencie == 42:
        if aktualny_pokoj == 27:
            otworz_drzwi(26)
        rekwizyty[25][0] = 0 # drzwi z pokoju 32 do maszynowni
        rekwizyty[26][0] = 0 # drzwi wewnatrz maszynowni
        clock.schedule_unique(zamknij_drzwi_maszynowni, 60)
        komunikat_uzycia = "Naciskasz przycisk"
        pokaz_tekst("Drzwi do maszynowni otwarte na 60 sekund", 1)

    elif trzymany_element == 68 or gracz_na_elemencie == 68:
        energia = 100
        komunikat_uzycia = "Jedzenie pozwala odzyskac energie"
        usun_obiekt(68)
        rysuj_energie_powietrze()

    if skafander_zeszyty and butla_naprawiona: # otwarcie dostepu do sluzy 
        if aktualny_pokoj == 31 and rekwizyty[20][0] == 31:
            otworz_drzwi(20) # lacznie z usunieciem drzwi
            pokaz_tekst("Komputer informuje, ze sluza jest otwarta.", 1)
        elif rekwizyty[20][0] == 31:
            rekwizyty[20][0] = 0 # usuniecie drzwi z mapy

            pokaz_tekst("Komputer informuje, ze sluza jest otwarta.", 1)

    for przepis in PRZEPISY:# Iterujemy przez wszystkie przepisy dostępne w grze
        skladnik1 = przepis[0]# Pierwszy składnik przepisu.
        skladnik2 = przepis[1]# Drugi  składnik przepisu.
        kombinacja = przepis[2]# Wynikowa kombinacja, czyli nowy obiekt
        # Sprawdzamy, czy trzymany element i element, na którym stoi gracz, pasują do przepisu
        if (trzymany_element == skladnik1
            and gracz_na_elemencie == skladnik2) \
            or (trzymany_element == skladnik2
                and gracz_na_elemencie == skladnik1):
            # Tworzymy komunikat informujący o udanym połączeniu obiektów
            komunikat_uzycia = "Polaczenie obiektow " + obiekty[skladnik1][3] \
                          + " plus " + obiekty[skladnik2][3] \
                          + " daje obiekt " + obiekty[kombinacja][3]
            #Jeśli element, na którym stoi gracz, istnieje w słowniku rekwizytów:
            if gracz_na_elemencie in rekwizyty.keys(): 
                rekwizyty[gracz_na_elemencie][0] = 0# Usuwamy obiekt z mapy 
                # Aktualizujemy mapę pokoju, przywracając typ podłogi w tym miejscu
                mapa_pokoju[gracz_y][gracz_x] = sprawdz_typ_podlogi()
            w_ekwipunku.remove(trzymany_element)# Usuwamy trzymany element z ekwipunku, ponieważ został użyty w przepisie
            dodaj_obiekt(kombinacja)# Dodajemy nowo utworzony obiekt do ekwipunku gracza


    # {numer obiektu klucza: numer obiektu drzwi}
    SLOWNIK_DOSTEPU = { 79:22, 80:23, 81:24 }
    if trzymany_element in SLOWNIK_DOSTEPU:# Sprawdzamy, czy trzymany element jest kluczem, który może otworzyć drzwi
        numer_drzwi = SLOWNIK_DOSTEPU[trzymany_element]# Pobranie numeru odpowiadających drzwi
        if rekwizyty[numer_drzwi][0] == aktualny_pokoj:# Sprawdzamy, czy drzwi znajdują się w aktualnym pokoju
            komunikat_uzycia = "Otwierasz drzwi!"# Tworzymy komunikat o otwarciu drzwi
            otworz_drzwi(numer_drzwi)# Wywołujemy funkcję odpowiedzialną za otwarcie drzwi

    pokaz_tekst(komunikat_uzycia, 0)# Wyświetlamy komunikat o akcji gracza (np. połączeniu obiektów lub otwarciu drzwi)
    time.sleep(0.5)# Krótkie opóźnienie, aby gracz miał czas na przeczytanie komunikatu

def sekwencja_konczenia_gry():
    global ramka_startu #(poczatkowa wartosc ustawiana w sekcji ZMIENNE to 0)
    prostokat = Rect((0, 150), (800, 600))
    screen.draw.filled_rect(prostokat, (128, 0, 0))
    prostokat = Rect ((0, gora_lewa_y - 30), (800, 390))
    screen.surface.set_clip(prostokat)

    for y in range(0, 13):
        for x in range(0, 13):
            rysuj_obraz(images.gleba, y, x)

    ramka_startu += 1
    if ramka_startu < 9:
        rysuj_obraz(images.statek_ratowniczy, 8 - ramka_startu, 6)
        rysuj_cien(images.statek_ratowniczy_cien, 8 + ramka_startu, 6)
        clock.schedule(sekwencja_konczenia_gry, 0.25)
    else:
        screen.surface.set_clip(None)
        screen.draw.text("MISJA", (200, 380), color = "white",
                     fontsize = 128, shadow = (1, 1), scolor = "black")
        screen.draw.text("ZAKONCZONA", (145, 480), color = "white",
                     fontsize = 128, shadow = (1, 1), scolor = "black")


###############
##   DRZWI   ##
###############

def otworz_drzwi(numer_otwieranych_drzwi):
    global ramki_drzwi, ramki_cienia_drzwi
    global numer_ramki_drzwi, numer_obiektu_drzwi
    ramki_drzwi = [images.drzwi1, images.drzwi2, images.drzwi3,
                   images.drzwi4, images.podloga]
    # (Ostatnia ramka przygotowuje cien do ponownego pojawienia sie drzwi).
    ramki_cienia_drzwi = [images.drzwi1_cien, images.drzwi2_cien,
                          images.drzwi3_cien, images.drzwi4_cien,
                          images.drzwi_cien]
    numer_ramki_drzwi = 0
    numer_obiektu_drzwi = numer_otwieranych_drzwi
    odtworz_animacje_drzwi()

def zamknij_drzwi(numer_zamykanych_drzwi):
    global ramki_drzwi, ramki_cienia_drzwi
    global numer_ramki_drzwi, numer_obiektu_drzwi, gracz_y
    ramki_drzwi = [images.drzwi4, images.drzwi3, images.drzwi2,
                   images.drzwi1, images.drzwi]
    ramki_cienia_drzwi = [images.drzwi4_cien, images.drzwi3_cien,
                          images.drzwi2_cien, images.drzwi1_cien,
                          images.drzwi_cien]
    numer_ramki_drzwi = 0
    numer_obiektu_drzwi = numer_zamykanych_drzwi
    # Jesli gracz jest w tym samym rzedzie co drzwi, musi stanac w wejsciu
    if gracz_y == rekwizyty[numer_obiektu_drzwi][1]:
        if gracz_y == 0: # jesli w gornym wyjsciu
            gracz_y = 1 # przeniesienie w dol
        else:
            gracz_y = wys_pokoju - 2 # przeniesienie w gore
    odtworz_animacje_drzwi()

def odtworz_animacje_drzwi():
    global ramki_drzwi, numer_ramki_drzwi, numer_obiektu_drzwi, obiekty
    obiekty[numer_obiektu_drzwi][0] = ramki_drzwi[numer_ramki_drzwi]
    obiekty[numer_obiektu_drzwi][1] = ramki_cienia_drzwi[numer_ramki_drzwi]
    numer_ramki_drzwi += 1
    if numer_ramki_drzwi == 5: 
        if ramki_drzwi[-1] == images.podloga:
            rekwizyty[numer_obiektu_drzwi][0] = 0 # usun drzwi z listy rekwizytow
        # W razie potrzeby ponownie generujemy mape pokoju,
        # aby umiescic tam drzwi.
        generuj_mape() 
    else:
        clock.schedule(odtworz_animacje_drzwi, 0.15)

def zamknij_drzwi_maszynowni():
    global aktualny_pokoj, numer_pokoju_drzwi, rekwizyty
    rekwizyty[25][0] = 32 # drzwi z pokoju 32 do maszynowni.
    rekwizyty[26][0] = 27 # drzwi wewnatrz maszynowni.
    generuj_mape() # Dodanie drzwi do mapa_pokoju, jesli sa w danym pokoju.
    if aktualny_pokoj == 27:
        zamknij_drzwi(26)
    if aktualny_pokoj == 32:
        zamknij_drzwi(25)
    pokaz_tekst("Komputer informuje, ze drzwi sa zamkniete.", 1)


def drzwi_w_pokoju_26():
    global ramka_drzwi_sluzy, mapa_pokoju
    ramki = [images.drzwi, images.drzwi1, images.drzwi2,
              images.drzwi3,images.drzwi4, images.podloga
              ]

    ramki_cieni = [images.drzwi_cien, images.drzwi1_cien,
                     images.drzwi2_cien, images.drzwi3_cien,
                     images.drzwi4_cien, None]

    if aktualny_pokoj != 26:
        clock.unschedule(drzwi_w_pokoju_26)
        return

    # rekwizyt 21 to drzwi w pokoju 26.
    if ((gracz_y == 8 and gracz_x == 2) or rekwizyty[63] == [26, 8, 2]) \
            and rekwizyty[21][0] == 26:
        ramka_drzwi_sluzy += 1
        if ramka_drzwi_sluzy == 5:
            rekwizyty[21][0] = 0 # Usuwanie drzwi z mapy, gdy calkiem otwarte.
            mapa_pokoju[0][1] = 0
            mapa_pokoju[0][2] = 0
            mapa_pokoju[0][3] = 0

    if ((gracz_y != 8 or gracz_x != 2) and rekwizyty[63] != [26, 8, 2]) \
            and ramka_drzwi_sluzy > 0:
        if ramka_drzwi_sluzy == 5:
            # Dodanie drzwi do rekwizytow i mapy w celu pokazania animacji.
            rekwizyty[21][0] = 26
            mapa_pokoju[0][1] = 21
            mapa_pokoju[0][2] = 255
            mapa_pokoju[0][3] = 255
        ramka_drzwi_sluzy -= 1

    obiekty[21][0] = ramki[ramka_drzwi_sluzy]
    obiekty[21][1] = ramki_cieni[ramka_drzwi_sluzy]


###############
## POWIETRZE ##
###############
                      
def rysuj_energie_powietrze():
    prostokat = Rect((20, 765), (450, 20))
    screen.draw.filled_rect(prostokat, CZARNY)
    screen.draw.text("POWIETRZE", (20, 766), color=NIEBIESKI)
    screen.draw.text("ENERGIA", (260, 766), color=ZOLTY)

    if powietrze > 0:
        prostokat = Rect((130, 765), (powietrze, 20))
        screen.draw.filled_rect(prostokat, NIEBIESKI) # Rysuje nowy pasek powietrza.

    if energia > 0:
        prostokat = Rect((350, 765), (energia, 20))
        screen.draw.filled_rect(prostokat, ZOLTY) # Rysuje nowy pasek energii.

def zakoncz_gre(przyczyna):
    global koniec_gry
    pokaz_tekst(przyczyna, 1)
    koniec_gry = True
    screen.draw.text("KONIEC GRY", (120, 400), color = "white",
                     fontsize = 128, shadow = (1, 1), scolor = "black")
    
def redukuj_powietrze():
    global powietrze, koniec_gry
    if koniec_gry:
        return # Nie wyczerpujemy powietrza po utracie zycia.
    powietrze -= 1
    rysuj_energie_powietrze()
    if powietrze < 1:
        zakoncz_gre("Skonczylo ci sie powietrze!")

def alarm():
    pokaz_tekst("Powietrze sie konczy, kpt. " + IMIE_GRACZA
              + "! Znajdz bezpieczne miejsce i wezwij pomoc przez radio!", 1)
  


################
## ZAGROZENIA ##
################

dane_zagrozen = {
    # numer pokoju: [[y, x, kierunek, liczba dodawana do kierunku]]
    28: [[1, 8, 2, 1], [7, 3, 4, 1]], 32: [[1, 5, 4, -1]],
    34: [[5, 1, 1, 1], [5, 5, 1, 2]], 35: [[4, 4, 1, 2], [2, 5, 2, 2]],
    36: [[2, 1, 2, 2]], 38: [[1, 4, 3, 2], [5, 8, 1, 2]],
    40: [[3, 1, 3, -1], [6, 5, 2, 2], [7, 5, 4, 2]],
    41: [[4, 5, 2, 2], [6, 3, 4, 2], [8, 1, 2, 2]],
    42: [[2, 1, 2, 2], [4, 3, 2, 2], [6, 5, 2, 2]],
    46: [[2, 1, 2, 2]],
    48: [[1, 8, 3, 2], [8, 8, 1, 2], [3, 9, 3, 2]]
    }

def wyczerpuj_energie(kara):
    global energia, koniec_gry
    if koniec_gry:
        return #Nie wyczerpujemy energii po utracie zycia.
    energia = energia - kara
    rysuj_energie_powietrze()
    if energia < 1:
        zakoncz_gre("Skonczyla ci sie energia!")

def przygotuj_zagrozenia():
    global aktualny_pokoj_lista_zagrozen, mapa_zagrozen
    if aktualny_pokoj in dane_zagrozen.keys():
        aktualny_pokoj_lista_zagrozen = dane_zagrozen[aktualny_pokoj]
        for zagrozenie in aktualny_pokoj_lista_zagrozen:
            zagrozenie_y = zagrozenie[0]
            zagrozenie_x = zagrozenie[1]
            mapa_zagrozen[zagrozenie_y][zagrozenie_x] = 49 + (aktualny_pokoj % 3)
        clock.schedule_interval(ruch_zagrozenia, 0.15)

def ruch_zagrozenia():
    global aktualny_pokoj_lista_zagrozen, dane_zagrozen, mapa_zagrozen
    global poprz_gracz_x, poprz_gracz_y

    if koniec_gry: # Jeśli gra została zakończona, przerwij działanie funkcji
        return
    
    for zagrozenie in aktualny_pokoj_lista_zagrozen:# Pętla przechodzi przez każde zagrożenie w aktualnym pokoju.
        # Współrzędne i kierunek poruszania się zagrożenia.
        zagrozenie_y = zagrozenie[0]
        zagrozenie_x = zagrozenie[1]
        zagrozenie_kierunek = zagrozenie[2]
        
        poprz_zagrozenie_x = zagrozenie_x
        poprz_zagrozenie_y = zagrozenie_y
        mapa_zagrozen[poprz_zagrozenie_y][poprz_zagrozenie_x] = 0 
            
        if zagrozenie_kierunek == 1: # gora
            zagrozenie_y -= 1
        if zagrozenie_kierunek == 2: # prawo
            zagrozenie_x += 1
        if zagrozenie_kierunek == 3: # dol
            zagrozenie_y += 1
        if zagrozenie_kierunek == 4: # lewo
            zagrozenie_x -= 1

        zagrozenie_ma_sie_odbic = False

        if (zagrozenie_y == gracz_y and zagrozenie_x == gracz_x) or \
           (zagrozenie_y == gracz_z_y and zagrozenie_x == gracz_z_x
            and gracz_ramka > 0):
            wyczerpuj_energie(10)
            zagrozenie_ma_sie_odbic = True

        # Zatrzymuje zagrozenie przed wyjsciem przez drzwi
        if zagrozenie_x == szer_pokoju: 
            zagrozenie_ma_sie_odbic = True
            zagrozenie_x = szer_pokoju - 1
        if zagrozenie_x == -1: 
            zagrozenie_ma_sie_odbic = True
            zagrozenie_x = 0
        if zagrozenie_y == wys_pokoju:
            zagrozenie_ma_sie_odbic = True
            zagrozenie_y = wys_pokoju - 1
        if zagrozenie_y == -1:
            zagrozenie_ma_sie_odbic = True
            zagrozenie_y = 0

        # Gdy zagrozenie uderzy element scenografii lub inne zagrozenie
        if mapa_pokoju[zagrozenie_y][zagrozenie_x] not in gracz_moze_stac_na \
               or mapa_zagrozen[zagrozenie_y][zagrozenie_x] != 0:
            zagrozenie_ma_sie_odbic = True

        if zagrozenie_ma_sie_odbic:
            zagrozenie_y = poprz_zagrozenie_y # Powrot w poprzednie prawidlowe polozenie.
            zagrozenie_x = poprz_zagrozenie_x
            zagrozenie_kierunek += zagrozenie[3]
            if zagrozenie_kierunek > 4:
                zagrozenie_kierunek -= 4
            if zagrozenie_kierunek < 1:
                zagrozenie_kierunek += 4
            zagrozenie[2] = zagrozenie_kierunek

        mapa_zagrozen[zagrozenie_y][zagrozenie_x] = 49 + (aktualny_pokoj % 3)
        zagrozenie[0] = zagrozenie_y
        zagrozenie[1] = zagrozenie_x

    
###############
##   START   ##
###############

clock.schedule_interval(petla_gry, 0.03)
generuj_mape()
#clock.schedule_interval(dostosuj_przezroczystosc_sciany, 0.05)
clock.schedule_unique(wyswietl_ekwipunek, 1)
clock.schedule_unique(rysuj_energie_powietrze, 0.5)
clock.schedule_unique(alarm, 10)
# Wieksza liczba ponizej zwieksza limit czas
clock.schedule_interval(redukuj_powietrze, 5)


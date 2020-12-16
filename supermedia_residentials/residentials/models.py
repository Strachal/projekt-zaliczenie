from django.db import models


# klasa opisująca osiedle
class Buildings(models.Model):
    STATUS = [
        (1, "realizacja"),
        (2, "eksploatacja"),
        (3, "niezrealizowane"),
        (4, "negocjacje"),
        (5, "chcemy"),
        (6, "inwestycja wstrzymana"),
    ]

    ACCEPT = [
        (1, "yes"),
        (2, "no"),
        (2, "in progress")
    ]

    SERVICES = [
        (1, "GPON/IPTV"),
        (2, "GPON/CATV"),
        (3, "LAN/CATV"),
        (4, "LAN")
    ]

    INTERNAL = [
        (1, "SM"),
        (2, "SM/JMDI"),
        (3, "SM/UPC"),
        (4, "SM/UPC/ Vectra"),
        (5, "SM/Wspólnota"),
        (6, "Wspólnota")
    ]

    INHABIT = [
        (1, "zasiedlone"),
        (2, "w trakcie"),
        (3, "deweloper")
    ]

    # director = models.ForeignKey(Person, related_name="movies_directed", on_delete=models.CASCADE)
    # actors = models.ManyToManyField(Person, related_name="movies_cast")


    KI_number = models.IntegerField() # numer inwestycji z Kompasu Inwestycji, może służyć do wygenerowania linku do KI
    MPK_number = models.CharField(max_length=10, null=True) # unikatowy numer MPK osiedla
    MPK_number_sewerage = models.CharField(max_length=10, null=True) # unikatowy numer MPK przyłącza
    building_name = models.CharField(max_length=255) # nazwa deweoperska osiela, jeśli nie ma to adres główny
    building_adres = models.CharField(max_length=255) # adres osiedla (może być kilka
    # adresów)
    parcel_number = models.CharField(max_length=255, null=True) # numer działki i obrębu
    GPON_node_localisation = models.ForeignKey("GPON_node_list", on_delete=models.CASCADE) # lokalizacja na terenie Warszawy
    quantity_HP = models.IntegerField(null=True) # ilość lokali mieszkalnych
    quantity_LU = models.IntegerField(null=True) # ilość lokali użytkowych
    competitors = models.ManyToManyField("Competitors") # konkurencja na osiedlu
    estimated_budget_accept = models.IntegerField(choices=ACCEPT, null=True) # akceptacja kosztorysu
    flat_price = models.FloatField(null=True) # cena lokalu w plnach
    kind_of_inhabitation = models.IntegerField(choices=INHABIT) # status zasidlenia w trakcie budowy sieci
    status = models.IntegerField(choices=STATUS, default=5) # handlowy status projektu
    services_provided = models.IntegerField(choices=SERVICES, default=1) # sposób świadczenia usług
    range_of_activity = models.ManyToManyField("Activities") # zakres budowy sieci
    internal_net_property = models.IntegerField(choices=INTERNAL, null=True) # własność sieci wewnętrznych
    remarks_of_MS = models.TextField(null=True) # uwagi MS
    remarks_of_AK = models.TextField(null=True) # uwagi AK


# klasa opisująca osoby zaangażowane w projekt osiedlowy, zarówno ze strony dewelopera, generalnego wykonawcy jaki i SM
class Persons(models.Model):
    deweloper_company = models.ForeignKey("Developer", on_delete=models.CASCADE, null=True) # nazwa firmy deweloperskiej
    general_contractor = models.ForeignKey("General", on_delete=models.CASCADE, null=True) # nazwa generalnego wykonawcy
    first_last_name = models.CharField(max_length=40) # imie i nazwisko danej osoby
    job = models.CharField(max_length=20) # stanowisko danej osoby
    phone = models.IntegerField(null=True) # telefon do danej osoby
    email = models.CharField(max_length=64, null=True) # email do danej osoby
    SM_PM_initial = models.CharField(max_length=4, null=True) # inicjały PM projektu po stronie SM

# klasa opisująca daty związane z budową osiedla
class AllDate(models.Model):

    QUARTER = [
        (1, "I kw."),
        (2, "II kw."),
        (3, "III kw."),
        (4, "IV kw.")
    ]

    date_Launch_services = models.DateField(null=True) # dniowa data uruchomienia uslug
    year_Launch_services = models.DateField(null=True) # roku budżetowy danego osiedla
    month_Launch_services = models.DateField(null=True) # miesiąc uruchomienia osiedla
    quarter_Launch_services = models.IntegerField(choices=QUARTER, null=True) # kwartał uruchomienia osiedla
    date_card_project = models.DateField(null=True) # data założęnia projektu w SMP
    date_agreement = models.DateField(null=True) # data podpisania umowy
    date_estimated_budget_order = models.DateField(null=True) # data zlecenia wykonania kosztorysu
    date_estimated_budget_execution = models.DateField(null=True) # data wykonania kosztorysu
    date_estimated_budget_to_fill = models.DateField(null=True) # data uzupełnienia kosztorysu
    date_estimated_budget_accept = models.DateField(null=True) # data akceptacji kosztorysu
    date_internal_net_order = models.DateField(null=True) # data zlecenia wykonania sieci wewnętrznych
    date_internal_net_execution = models.DateField(null=True) # data wykonania sieci wewnętrznych
    date_FO_question_of_price = models.DateField(null=True) # data zapytania o wycenę FO
    date_FO_answer_with_price = models.DateField(null=True) # data wyceny FO
    date_FO_order = models.DateField(null=True) # data zlecenia doprowadzenia FO
    date_FO_execution = models.DateField(null=True) # data doprowadzenia FO
    date_LAN_GPON_launch = models.DateField(null=True) # data uruchomienia usług inet
    date_CATV_IPTV_launch = models.DateField(null=True) # data uruchomienia usług TV
    date_reckoning = models.DateField(null=True) # data rozliczenia - data wysłania maila z prośbą o zamknięcie księgowe osiedla
    date_expenditure_FO = models.DateField(null=True) # data wydania środków na FO
    date_expenditure_avtive_elements = models.DateField(null=True) # data wydania środków na elementy aktywne sieci wewnętrznej
    date_expenditure_inactive_elements = models.DateField(null=True) # data wydania środków na elementu bierne sieci wewn.
    date_expenditure_sewerage = models.DateField(null=True) # data wydania środków na kanalizację teletechniczną
    date_expenditure_OLT = models.DateField(null=True) # data wydania środków na OLT
    date_expenditure_for_deweloper = models.DateField(null=True) # data wydania środków dla dewelopera



# klasa obejmująca finanse osiedla
class Finances(models.Model):
    amount_total = models.FloatField(null=True) # całkowity koszt projektu (suma FO, kanalizacji i sieci wew.)
    amount_FO = models.FloatField(null=True) # koszt doprowadzenia FO
    amount_sewerage = models.FloatField(null=True) # koszt budowy kanalizacji
    amount_internal_network = models.FloatField(null=True) # koszt budowy sieci wewnętrznych (
    amount_to_reckoning_budget = models.FloatField(null=True) # koszt do kosztorysu rozliczonego
    amount_CN_to_reckoning_budget = models.FloatField(null=True) # koszt FO CN do kosztorysy rozliczonego
    amount_sewerage_to_reckoning_budget = models.FloatField(null=True) # koszt kanalizacja do kosztorysy rozliczonego
    amount_per_HP_without_FO = models.FloatField(null=True) # koszt budowy bez kosztów FO na HP
    amount_per_HP_with_FO = models.FloatField(null=True) # koszt budowy z kosztami FO na HP
    amount_inactive_elements = models.FloatField(null=True) # koszt elementów biernych
    amount_active_elements = models.FloatField(null=True) # koszt elementów aktywnych
    amount_activity = models.FloatField(null=True) # "kwota na robociznę, zasilanie, służebność, zakres"
    amount_OLT = models.FloatField(null=True) # koszt ruczaltu OLT
    amount_for_deweloper = models.FloatField(null=True) # koszt "kasy dla dewelopera"


# klasa do przygotowania raportu
class Raport(models.Model):
    pass

# klasa zawierająca linki związane z osiedlami
class Links(models.Model):
    link_RT = models.URLField(null=True) # link do RT budowa sieci wewnętrznych  - przed pojawieniem się SMP
    link_RT_FO = models.URLField(null=True) # link do RT budowa FO - przed pojawieniem się SMP
    link_KI = models.URLField(null=True) # link do Kompasu Inwestycji
    link_SMP_osiedle = models.URLField(null=True) # link do projektu w SMP
    link_SMP_FO = models.URLField(null=True) # link do projektu FO w SMP
    link_kosztorys_ryczałtowy = models.URLField(null=True) # link do katalogu, w którym znajduje się kosztorys
    link_kosztorys_rozliczony = models.URLField(null=True) # link do katalogu, w którym znajduje się kosztorys
    link_skan_umowy = models.URLField(null=True) # link do katalogu, w którym znajduje się skan umowy

#klasa opisująca konkurencję osiedlową
class Competitors(models.Model):
    name = models.CharField(max_length=15)
    # competitor2 = models.CharField(max_length=15)
    # competitor3 = models.CharField(max_length=15)
    # competitor4 = models.CharField(max_length=15)
    # competitor5 = models.CharField(max_length=15)
    # competitor6 = models.CharField(max_length=15)
    # competitor7 = models.CharField(max_length=15)


#klasa opisująca generalnego wykonawcę
class General(models.Model):
    pass

# klasa opisująca dewelopera
class Developer(models.Model):
    pass

# klasa opisująca węzeł Gpon
class GPON_node_list(models.Model):
    pass

class Activities(models.Model):
    rg6_100_percent = models.CharField(max_length=15)
    rg6_50_percent = models.CharField(max_length=15)
    rg6_30_percent = models.CharField(max_length=15)
    rg6_33_percent = models.CharField(max_length=15)
    backbone_ftth = models.CharField(max_length=15)
    backbone_lan = models.CharField(max_length=15)
    backbone_catv = models.CharField(max_length=15)
    connection = models.CharField(max_length=15)
    ftth_100_percent = models.CharField(max_length=15)
    utp_100_percent = models.CharField(max_length=15)
    rg6_100_percent = models.CharField(max_length=15)
    sewerage = models.CharField(max_length=15)
    money_to_deweloper = models.CharField(max_length=15)
    ftth_reserves = models.CharField(max_length=15)
    mast_radio = models.CharField(max_length=15)
    utp_reserves_50_percent = models.CharField(max_length=15)
    rg6_zit_100_percent = models.CharField(max_length=15)
    zit = models.CharField(max_length=15)

def mijn_functie_2(a, b):
    eerste_getal = a + b
    tweede_getal = a - b
    derde_getal = a * b
    vierde_getal = a / b
    return [eerste_getal, tweede_getal, derde_getal, vierde_getal]
def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1-korting)
    uitvoer = f"Vandaag in de aanbieding: Emmertje ijs(1 liter) in de smaak {smaak},van {prijs} euro voor {prijs_na_korting:.2f} euro."
    return uitvoer
def inkomsten_totaal(inkomsten, btw):
    inkomsten_week = sum(inkomsten)
    uitvoering = f"Het totaal van alle inkomsten van deze week is {inkomsten_week} euro, waarover {inkomsten_week * btw} euro btw betaald dient te worden."
    return uitvoering
dagelijkse_inkomsten = [220, 430, 125, 160, 205, 90, 345]
def laag_en_hoog(mijn_lijst):
   return  [max(mijn_lijst), min(mijn_lijst)]
def gemiddelde(mijn_lijst):
    return f"De gemiddelde inkomsten van deze week zijn {sum(mijn_lijst) / len(mijn_lijst)} euro."
def meervoudig(invoer_lijst):
    return [max(invoer_lijst), min(invoer_lijst)]
def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2)
    a, b = korte_lijst
    resultaat = mijn_functie_2(a, b)
    return resultaat

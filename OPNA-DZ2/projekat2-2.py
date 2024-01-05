import math as mat

# svodi koeficijente na oblik a0.a1a2a3... * 10^stepen
def urediKoeficijenteStepene(polinom):
    koeficijenti = []
    stepeni = []
    for i in range(len(polinom)):
        stepen = 0
        if polinom[i] == 0:
            koeficijenti.append(polinom[i])
            stepeni.append(0)
        else:
            koef = abs(polinom[i])
            while koef < 1:
                stepen -= 1
                koef *= 10
            if polinom[i] < 0:
                koeficijenti.append(-koef)
            else:
                koeficijenti.append(koef)
            stepeni.append(stepen)
    return koeficijenti, stepeni

# svodi koeficijente na oblik a0.a1a2 * 10^stepen
# vrseci skracivanje na k decimala prema pravilima
def skratiKoeficijente(koeficijenti):
    skraceni_koeficijenti = []
    for koeficijent in koeficijenti:
        koef_str = str(koeficijent)
        if koeficijent < 0:
            koef_str_skracen = koef_str[:5]
            koef_abs = abs(float(koef_str_skracen))
            koef_abs += 0.01
            skraceni_koeficijenti.append(round(float(koef_abs * -1), k))
        else:
            koef_str_skracen = koef_str[:4]
            skraceni_koeficijenti.append(float(koef_str_skracen))
    return skraceni_koeficijenti

# ispisuje polinom u obliku koef*10^stepen[i]*x^stepen + ...
def ispisiPolinom(koeficijenti, skraceni_koeficijenti, stepeni):
    ispis = ""
    brojStepeni = len(koeficijenti) - 1
    for i in range(len(koeficijenti)):
        if skraceni_koeficijenti[i] == 0:
            continue  # preskače ispisivanje ako je koeficijent 0
        stepen = brojStepeni - i
        if ispis != "" and skraceni_koeficijenti[i] > 0:
            ispis += "+ "  # dodaje plus znak pre pozitivnih koeficijenata
        # ispisuje koeficijent
        ispis += str(skraceni_koeficijenti[i])
        # dodaje faktor 10^stepen ako stepen nije 0
        if stepeni[i] != 0:
            ispis += "*10^" + str(stepeni[i]) + " "
        # dodaje faktor x^stepen ako stepen nije 0
        if stepen > 0:
            ispis += "*x^" + str(stepen) + " "
    ispis = ispis.strip()
    ispis = ispis.replace('+-', '-')
    return ispis

k = 2
#Polinom = [mat.pi/1260 - 1/420, -mat.pi*mat.pi/1680 + mat.pi/840, -mat.pi/30 + 1/10,
           #-mat.pi*mat.pi/60+mat.pi/30, mat.pi*2/3-2, 0, 0, 0, 0]
polinom = [mat.pi*(2**0.5), 0, mat.pi - 2**0.5, 2*mat.pi, -(mat.pi**0.5)/mat.pi, 2*(mat.pi-(mat.pi**0.5)), 0, mat.pi/(mat.pi**0.5) - 1.7]
print(polinom)

koeficijenti = []
stepeni = []

koeficijenti, stepeni = urediKoeficijenteStepene(polinom)
koeficijenti_skraceni = skratiKoeficijente(koeficijenti)
print("Koeficijenti nakon skracivanja su: " + str(koeficijenti_skraceni))
print("Stepeni nakon skracivanja su: " + str(stepeni))
print(ispisiPolinom(koeficijenti, koeficijenti_skraceni, stepeni))

#koeficijenti = [1,0,-3,-1,3,3,-1,-3,0,1]
#skraceni_koeficijenti = [1,0,-3,-1,3,3,-1,-3,0,1] # Ovo bi bili koeficijenti nakon skracivanja
#stepeni = [0,0,0,0,0,0,0,0,0,0]  # Ovo bi bili stepeni za svaki koeficijent
#print("Polinom P(x) nakon skracivanja: " + ispisiPolinom(koeficijenti, skraceni_koeficijenti, stepeni))


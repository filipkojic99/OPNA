import math as mat

def formirajKoeficijenteIstepenePreSkracivanja():
    for i in range(len(Polinom)):
        stepen_curr = 0
        if (Polinom[i] == 0):
            koeficijenti.append((Polinom[i]))
            stepeni.append(0)
        else:
            koef = Polinom[i]
            if (Polinom[i] < 0):
                koef *= -1
                while koef < 1:
                    stepen_curr = stepen_curr - 1
                    koef *= 10
                koeficijenti.append(koef * (-1))
                stepeni.append(stepen_curr)
            else:
                while koef < 1:
                    stepen_curr = stepen_curr - 1
                    koef *= 10
                koeficijenti.append(koef)
                stepeni.append(stepen_curr)

def skrati():
    for i in range(len(koeficijenti_skraceni)):
        koef_str = str(koeficijenti[i])
        if (koeficijenti_skraceni[i] < 0):
            koef_str_skracen = koef_str[0:5]
            koef_abs = abs(float(koef_str_skracen))
            koef_abs += 0.01
            koeficijenti_skraceni[i] = round(float(koef_abs * -1), 2)
        else:
            koef_str_skracen = koef_str[0:4]
            koeficijenti_skraceni[i] = float(koef_str_skracen)

def ispisiPolinomNakonSkracivanja():
    konacanIspis = ""
    brojStepena = len(koeficijenti) - 1
    for i in range(len(koeficijenti)):
        stepen = brojStepena - i
        konacanIspis += str(koeficijenti_skraceni[i]) + "*10^" + str(stepeni[i]) + "*x^" + str(stepen) + " "
        if(i >= 0 and i < brojStepena):
            konacanIspis += "+"
    konacanIspis = konacanIspis.replace('+-', '-')
    konacanIspis = konacanIspis.replace('0.0*10^0', '0')
    print("Polinom P(x) nakon skracivanja: " + konacanIspis)


#Polinom = [mat.pi/1260 - 1/420, -mat.pi*mat.pi/1680 + mat.pi/840, -mat.pi/30 + 1/10,
           #-mat.pi*mat.pi/60+mat.pi/30, mat.pi*2/3-2, 0, 0, 0, 0]
Polinom = [mat.pi*(2**0.5), 0, mat.pi - 2**0.5, 2*mat.pi, -(mat.pi**0.5)/mat.pi, 2*(mat.pi-(mat.pi**0.5)), 0, mat.pi/(mat.pi**0.5) - 1.7]
k = 2
print(Polinom)

koeficijenti = []
stepeni = []

formirajKoeficijenteIstepenePreSkracivanja()
koeficijenti_skraceni = koeficijenti
skrati()
print("Koeficijenti nakon skracivanja su: " + str(koeficijenti_skraceni))
print("Stepeni nakon skracivanja su: " + str(stepeni))
ispisiPolinomNakonSkracivanja()
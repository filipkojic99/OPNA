import sympy as s

def sracunaj_gcd(Pol1, Pol2):
    return s.gcd(Pol1, Pol2)

def sturmova_teorema(Pol1, Pol2):
    rezultat = []
    P_0, R_0 = s.div(Pol1, Pol2)
    P_1 = s.diff(P_0, x, 1)
    rezultat.append(P_0)
    rezultat.append(P_1)
    while s.degree(P_0) >= 2: #Provera da li je polinom stepena veceg od 2
        P_curr, R_curr = s.div(P_0, P_1)
        rezultat.append(-R_curr)
        P_0 = P_1
        P_1 = -R_curr
    return rezultat

def sracunajVrednostiPolinoma(vrednost):
    rezultat = []
    for i in range(len(sturmovi_polinomi)):
        polinom_curr = sturmovi_polinomi[i]
        vrednost_curr = polinom_curr.subs(x, vrednost)
        rezultat.append(vrednost_curr)
    return rezultat

def ispisiVrednostiSturmovihPolinoma(donja_granica, gornja_granica):
    for i in range(len(donja_granica)):
        val1 = float(donja_granica[i])
        val2 = float(gornja_granica[i])
        print("P" + str(i) + "(" + a + ") = " + str(val1) + ", P" + str(i) + "(" + b + ") = " + str(val2))

def proveriPromenuZnaka(niz_vrednosti):
    vel = len(niz_vrednosti)
    promenaZnaka = 0
    for i in range(0, vel-1):
        if((niz_vrednosti[i] < 0 and niz_vrednosti[i+1] >= 0) or (niz_vrednosti[i] >= 0 and niz_vrednosti[i+1] < 0)):
            promenaZnaka = promenaZnaka + 1
    return promenaZnaka


print('Unesite vrednosti za [a,b] tako da je a < b odvojene spejsom: ')
a, b = input().split(' ')
print("------")
print("[a,b]=[{},{}]".format(a, b))
print("------")
x = s.symbols('x')
Polinom = 3.14 * x**10 + 0 * x**9 + 0 * x**8 + 0 * x**7 + 0 * x**6 + 3.46 * x**5 + 3.0 * x**4 - 4.51 * 10**-1 * x**3 + 2.0 * x**2 + 0 * x + 1.23
#Polinom = 1.12 * 10**-4 * x**8 - 2.14 * 10**-3 * x**7 - 4.72 * 10**-3 * x**6 - 5.98 * 10**-2 * x**5 + 9.43 * 10**-2 * x**4
#Polinom = x**4 - 3*x**2 - 4*x + 8
#Polinom = x**9 - 3*x**7 - x**6 + 3*x**5 + 3*x**4 - x**3 - 3*x**2 + 1
#Polinom = x**10 + 3*x**8 - 2*x**7 + 5*x**5 - 4*x**3 - 1
#Polinom = 5.1*x**6 + 4.2*x**4 - 2.3*x**3 + 2.4*x**2 - 3.5*x**1 - 1.6
#Polinom = 7/62500*x**8 - 107/50000*x**7 - 59/12500*x**6 - 299/5000*x**5 + 943/10000*x**4
#Polinom = 111/25*x**7+43/25*x**5+157/25*x**4-113/200*x**3+273/100*x**2+181/2500
PolinomIspis = str(Polinom)
PolinomIspis = PolinomIspis.replace('x**', 'x^')
Polinom_prviIzvod = s.diff(Polinom, x, 1)
PrviIzvodIspis= str(Polinom_prviIzvod)
PrviIzvodIspis = PrviIzvodIspis.replace('x**', 'x^')
print("P(x) := " + PolinomIspis)
print("P'(x) := " + PrviIzvodIspis)
GCD = sracunaj_gcd(Polinom, Polinom_prviIzvod)
GCDIspis = str(GCD)
print("GCD(P(x), P'(x)) := " + GCDIspis.replace('x**', 'x^'))
sturmovi_polinomi = []
sturmovi_polinomi = sturmova_teorema(Polinom, GCD)
print("------")
print("Sturmovi polinomi:")
print("------")
for i in range(len(sturmovi_polinomi)):
    print("P" + str(i) + "(x) = " + str(sturmovi_polinomi[i]).replace('x**', 'x^'))
vrednosti_polinoma_a = sracunajVrednostiPolinoma(a)
vrednosti_polinoma_b = sracunajVrednostiPolinoma(b)
ispisiVrednostiSturmovihPolinoma(vrednosti_polinoma_a, vrednosti_polinoma_b)

promenaZnaka1 = proveriPromenuZnaka(vrednosti_polinoma_a)
promenaZnaka2 = proveriPromenuZnaka(vrednosti_polinoma_b)
print("------")
print("V(" + a + ") = " + str(promenaZnaka1))
print("V(" + b + ") = " + str(promenaZnaka2))
print("------")
brojNula = abs(promenaZnaka1 - promenaZnaka2)
tekst = ""
if(brojNula == 0):
    tekst = " NULA "
elif(brojNula == 1):
    tekst = " NULU "
elif(brojNula > 1 and brojNula < 7):
    tekst = " NULE "
else:
    tekst = " NULA "
print("------")
print("P(x) = " + PolinomIspis + ", IMA " + str(brojNula) + tekst + "na intervalu" + " [a,b]=[{},{}]".format(a, b))
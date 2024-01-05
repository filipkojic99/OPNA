import sympy as s

# ispis polinoma
def ispisiPolinom(polinom):
    return str(polinom).replace('x**', 'x^')

# trazenje prvog izvoda polinoma
def nadjiPrviIzvod(polinom):
    return s.diff(polinom, x, 1)

# trazenje najveceg zajednickog delioca polinoma
def izracunaj_GCD(polinom1, polinom2):
    return s.gcd(polinom1, polinom2)

# implementacija sturmovog algoritma
def sturmova_teorema(polinom1, polinom2):
    sturm_niz = []
    pol0, rem0 = s.div(polinom1, polinom2)
    pol1 = s.diff(pol0, x, 1)
    sturm_niz.append(pol0)
    sturm_niz.append(pol1)
    while s.degree(pol0) > 1:
        pol, rem = s.div(pol0, pol1)
        sturm_niz.append(-rem)
        pol0 = pol1
        pol1 = -rem
    return sturm_niz

# uvrstavanje granica intervala [a, b] u sturmove polinome
def izracunajVrednostiPolinoma(a, b):
    rezultatiA = []
    rezultatiB = []
    for polinom in sturm_niz:
        vrednost1 = polinom.subs(x, a)
        vrednost2 = polinom.subs(x, b)
        rezultatiA.append(vrednost1)
        rezultatiB.append(vrednost2)
    return rezultatiA, rezultatiB

# ispis vrednosti sturmovih polinoma sa a i b granicama intervala
def ispisVrednostiSturmovihPolinoma(rezultatiA, rezultatiB):
    for i in range(len(rezultatiA)):
        val1 = rezultatiA[i]
        val2 = rezultatiB[i]
        print("P" + str(i) + "(" + str(a) + ") = " + str(val1) + "  P" + str(i) + "(" + str(b) + ") = " + str(val2))

# prebrojavanje promena znaka za nizove vrednosti sa a i b granicama intervala
def prebrojPromeneZnaka(rezultatiA, rezultatiB):
    promenaZnakaA = 0
    promenaZnakaB = 0
    duzina = len(rezultatiA)
    for i in range(0, duzina - 1):
        if (rezultatiA[i] < 0 and rezultatiA[i + 1] >= 0) or (rezultatiA[i] >= 0 and rezultatiA[i + 1] < 0):
            promenaZnakaA += 1
        if (rezultatiB[i] < 0 and rezultatiB[i + 1] >= 0) or (rezultatiB[i] >= 0 and rezultatiB[i + 1] < 0):
            promenaZnakaB += 1
    return promenaZnakaA, promenaZnakaB

x = s.symbols('x')
polinom = x**9 - 3*x**7 - x**6 + 3*x**5 + 3*x**4 - x**3 - 3*x**2 + 1
# polinom = 111/25*x**7+43/25*x**5+157/25*x**4-113/200*x**3+273/100*x**2+181/2500
prviIzvod = nadjiPrviIzvod(polinom)

print("P0(x) = " + ispisiPolinom(polinom))
print("P1(x) = " + ispisiPolinom(prviIzvod))

gcd = izracunaj_GCD(polinom, prviIzvod)
print("GCD(P0(x), P1(x)) = " + ispisiPolinom(gcd))

sturm_niz = []
sturm_niz = sturmova_teorema(polinom, gcd)
print("********************************************************************")
print("Šturmov niz polinoma:")
print("********************************************************************")
for i in range(len(sturm_niz)):
    print("P" + str(i) + "(x) = " + ispisiPolinom(sturm_niz[i]))

# granice intervala [a, b]
a = 0
b = 3
rezultatiA, rezultatiB = izracunajVrednostiPolinoma(a, b)
print("********************************************************************")
print("Vrednosti Šturmovih polinoma:")
print("********************************************************************")
ispisVrednostiSturmovihPolinoma(rezultatiA, rezultatiB)

promenaZnakaA, promenaZnakaB = prebrojPromeneZnaka(rezultatiA, rezultatiB)
print("********************************************************************")
print("Broj promena znaka za granicu a: V(" + str(a) + ") = " + str(promenaZnakaA))
print("Broj promena znaka za granicu b: V(" + str(b) + ") = " + str(promenaZnakaB))
print("********************************************************************")
brojNula = abs(promenaZnakaA - promenaZnakaB)
print("Broj nula polinoma P(x) = {}, na intervalu [a, b] = [{}, {}] je: {}".format(ispisiPolinom(polinom), a, b, brojNula))

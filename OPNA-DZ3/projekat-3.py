import sympy as sym
import math as m

# KOD IZ DRUGOG PROJEKTNOG ZADATKA

# ispis polinoma
def ispisiPolinom(polinom):
    return str(polinom).replace('x**', 'x^')

# trazenje prvog izvoda polinoma
def nadjiPrviIzvod(polinom):
    return sym.diff(polinom, x, 1)

# trazenje najveceg zajednickog delioca polinoma
def izracunaj_GCD(polinom1, polinom2):
    return sym.gcd(polinom1, polinom2)

# implementacija sturmovog algoritma
def sturmova_teorema(polinom1, polinom2):
    sturm_niz = []
    pol0, rem0 = sym.div(polinom1, polinom2)
    pol1 = sym.diff(pol0, x, 1)
    sturm_niz.append(pol0)
    sturm_niz.append(pol1)
    while sym.degree(pol0) > 1:
        pol, rem = sym.div(pol0, pol1)
        sturm_niz.append(-rem)
        pol0 = pol1
        pol1 = -rem
    return sturm_niz

# uvrstavanje granica intervala [a, b] u sturmove polinome
def izracunajVrednostiPolinoma(a, b, sturm_niz):
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

# KOD ZA TRECI PROJEKTNI ZADATAK

# ispis funkcije
def ispisiFunkciju(funkcija):
    return str(funkcija).replace('**', '^')

# maklorenov razvoj za funkciju kosinusa do zadatog stepena
def kosinus_maklorenov_razvoj(stepen):
    broj_clanova = stepen / 2 + 1
    maklorenov_razvoj = sym.Poly(1, x)
    for k in range(1, broj_clanova):
        znak = (-1) ** k
        brojilac = znak * x ** (2 * k)
        imenilac = m.factorial(2 * k)
        clan = sym.Poly(brojilac / imenilac)
        maklorenov_razvoj = maklorenov_razvoj.add(clan)
    return maklorenov_razvoj

# maklorenov razvoj za funkciju sinusa do zadatog stepena
def sinus_maklorenov_razvoj(stepen):
    broj_clanova = (stepen - 1) / 2 + 1
    maklorenov_razvoj = sym.Poly(x, x)
    for k in range(1, broj_clanova):
        znak = (-1) ** k
        brojilac = znak * x ** (2 * k + 1)
        imenilac = m.factorial(2 * k + 1)
        clan = sym.Poly(brojilac / imenilac)
        maklorenov_razvoj = maklorenov_razvoj.add(clan)
    return maklorenov_razvoj

# menja sin i cos sa njihovim odgovarajucim polinomima
def zamena_trig_funkcija_maklorenovim_polinomima(MTP_fja, s_vrednost, r_vrednost):
    stepen_kosinus = alfa.subs(s, s_vrednost)
    stepen_sinus = beta.subs(r, r_vrednost)
    makloren_cos_value = kosinus_maklorenov_razvoj(stepen_kosinus)
    makloren_sin_value = sinus_maklorenov_razvoj(stepen_sinus)
    MTP_fja = MTP_fja.subs(sym.cos(x), makloren_cos_value.as_expr()).subs(sym.sin(x), makloren_sin_value.as_expr())
    return MTP_fja

# primena sturmove metode da bi se odredile nule
# polinoma na zadatom intervali i utvrdila pozitivnost
def primena_sturmove_metode(polinom, k1, k2):
    prviIzvod = nadjiPrviIzvod(polinom)
    gcd = izracunaj_GCD(polinom, prviIzvod)
    sturm_niz = sturmova_teorema(polinom, gcd)
    print("********************************************************************")
    print("Šturmov niz polinoma:")
    print("********************************************************************")

    for i in range(len(sturm_niz)):
        print("P" + str(i) + "(x) = " + ispisiPolinom(sturm_niz[i]))
    rezultatiA, rezultatiB = izracunajVrednostiPolinoma(a, b, sturm_niz)
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
    print("Broj nula polinoma P[{}, {}](x) na intervalu [a, b] = [{}, {}] je: {}".format(k1, k2, a, b, brojNula))


    if brojNula == 0:
        vrednost_funkcije = polinom.subs(x, m.pi/2-0.00001)
        if vrednost_funkcije < 0:
            print("P[" + str(k1) + "," + str(
                k2) + "](x) nema nule na intervalu [0, pi/2], ali je negativna, te stoga NE DOKAZUJE pozitivnost MTP funkcije nad zadatim intervalom!")
        else:
            print("P[" + str(k1) + "," + str(
                k2) + "](x) name nule na intervalu [0, pi/2], ali je pozitivna, te stoga DOKAZUJE pozitivnost MTP funkcije nad zadatim intervalom!")
    else:
        print("P[" + str(k1) + "," + str(
            k2) + "](x) ima nule na intervalu [0, pi/2], te stoga NE DOKAZUJE pozitivnost MTP funkcije nad zadatim intervalom!")

x = sym.symbols('x')

# za odredjivanje stepena maklorenovog razvoja
s = sym.symbols('s')
r = sym.symbols('r')

# za kosinus, alfa < 0 i alfa > 0
alfa_0 = 4 * s; alfa_1 = 4 * s + 2;
# za sinus, beta < 0 i beta > 0
beta_0 = 4 * r + 1; beta_1 = 4 * r+ 3;

# PRIMER:
MTP_funkcija = x**3 * sym.cos(x)**2 + x**2 - x * sym.sin(x) + 0.5
# koriscena poredjenja
alfa = alfa_1
beta = beta_0
# granice intervala [0-PI/2]
a = 0.0001; b = m.pi / 2

print("MTP funkcija za koju utvrdjujemo pozitivnost: " + ispisiFunkciju(MTP_funkcija))

# odredjivanje koeficijenata k1 i k2 za koje je polinom
# i funkcija pozitivna na zadatom intervalu
P0 = zamena_trig_funkcija_maklorenovim_polinomima(MTP_funkcija, 0, 0)
P1 = zamena_trig_funkcija_maklorenovim_polinomima(MTP_funkcija, 0, 1)
P2 = zamena_trig_funkcija_maklorenovim_polinomima(MTP_funkcija, 1, 0)
P3 = zamena_trig_funkcija_maklorenovim_polinomima(MTP_funkcija, 1, 1)

print("")
print("P0(x) = P[0,0](x) = " + ispisiPolinom(P0))
primena_sturmove_metode(P0, 0, 0)
print("********************************************************************\n")
print("P1(x) = P[0,1](x) = " + ispisiPolinom(P1))
primena_sturmove_metode(P1, 0, 1)
print("********************************************************************\n")
print("P2(x) = P[1,0](x) = " + ispisiPolinom(P2))
primena_sturmove_metode(P2, 1, 0)
print("********************************************************************\n")
print("P3(x) = P[1,1](x) = " + ispisiPolinom(P3))
primena_sturmove_metode(P3, 1, 1)
print("********************************************************************")

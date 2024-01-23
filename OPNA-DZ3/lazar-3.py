# Treci projektni zadatak iz OPNE
import sympy as sym
import math as m

x = sym.symbols('x')
s = sym.symbols('s')
r = sym.symbols('r')

# alfa = [alfa < 0, alfa > 0], za cosinus
# beta = [beta < 0, beta > 0], za sinus
alfa_niz = [4 * s, 4 * s + 2]
beta_niz = [4 * r + 1, 4 * r + 3]


def sracunaj_gcd(Pol1, Pol2):
    return sym.gcd(Pol1, Pol2)


def sturmova_teorema(Pol1, Pol2):
    rezultat = []
    P_0, R_0 = sym.div(Pol1, Pol2)
    P_1 = sym.diff(P_0, x, 1)
    rezultat.append(P_0)
    rezultat.append(P_1)
    while sym.degree(P_0) >= 2:  # Provera da li je polinom stepena veceg od 2
        P_curr, R_curr = sym.div(P_0, P_1)
        rezultat.append(-R_curr)
        P_0 = P_1
        P_1 = -R_curr
    return rezultat


def sracunajVrednostiPolinoma(vrednost, polinomi):
    rezultat = []
    for i in range(len(polinomi)):
        polinom_curr = polinomi[i]
        vrednost_curr = polinom_curr.subs(x, vrednost)
        rezultat.append(vrednost_curr)
    return rezultat


def ispisiVrednostiSturmovihPolinoma(donja_granica, gornja_granica):
    print("")
    print("Vrednosti Sturmovih polinoma: ")
    for i in range(len(donja_granica)):
        val1 = float(donja_granica[i])
        val2 = float(gornja_granica[i])
        print("P" + str(i) + "(" + str(aa) + ") = " + str(val1) + ", P" + str(i) + "(" + str(bb) + ") = " + str(val2))


def proveriPromenuZnaka(niz_vrednosti):
    vel = len(niz_vrednosti)
    promenaZnaka = 0
    for i in range(0, vel - 1):
        if ((niz_vrednosti[i] * niz_vrednosti[i + 1]) < 0):
            promenaZnaka = promenaZnaka + 1
    return promenaZnaka


def ispis_funkcije(MTP):
    MTP_ulepsan_ispis = MTP.replace('**', '^')
    return MTP_ulepsan_ispis


# Za primer1
#def koriscena_poredjenja():
#    alfa = alfa_niz[0]
 #   beta = beta_niz[1]
  #  return [alfa, beta]

# Za primer2 i primer3
#def koriscena_poredjenja():
#    alfa = alfa_niz[1]
 #   beta = beta_niz[1]
  #  return [alfa, beta]

# Za primer fikus
def koriscena_poredjenja():
    alfa = alfa_niz[1]
    beta = beta_niz[0] # bilo beta 1 za test 2
    return [alfa, beta]


def maklorenov_razvoj_kosinus(n1):
    n = n1 / 2
    brClanova = n + 1
    maklorenov_razvoj = sym.Poly(1, x)
    for k in range(1, brClanova):
        znak = (-1) ** k
        brojilac = znak * x ** (2 * k)
        imenilac = m.factorial(2 * k)
        clan_razvoja = sym.Poly(brojilac / imenilac)
        maklorenov_razvoj = maklorenov_razvoj.add(clan_razvoja)
    #print(str(maklorenov_razvoj.as_expr()))
    return maklorenov_razvoj


def maklorenov_razvoj_sinus(n1):
    n = (n1 - 1) / 2
    brClanova = n + 1
    maklorenov_razvoj = sym.Poly(x, x)
    for k in range(1, brClanova):
        znak = (-1) ** k
        brojilac = znak * x ** (2 * k + 1)
        imenilac = m.factorial(2 * k + 1)
        clan_razvoja = sym.Poly(brojilac / imenilac)
        maklorenov_razvoj = maklorenov_razvoj.add(clan_razvoja)
    return maklorenov_razvoj


def pozitivnost_mtp_funkcije(F, s1, r1):
    alfa_iter = a
    beta_iter = b
    alfa_iter = alfa_iter.subs(s, s1)
    beta_iter = beta_iter.subs(r, r1)
    makloren_cos_value = maklorenov_razvoj_kosinus(alfa_iter)
    makloren_sin_value = maklorenov_razvoj_sinus(beta_iter)
    F = F.subs(sym.cos(x), makloren_cos_value.as_expr()).subs(sym.sin(x), makloren_sin_value.as_expr())
    print(F)
    return F


def drugi_projektni_zadatak_metoda(polinom, izvod, i1, i2):
    GCD = sracunaj_gcd(polinom, izvod)
    sturmovi_polinomi = sturmova_teorema(polinom, GCD)
    print("")
    print("Sturmovi polinomi:")
    for i in range(len(sturmovi_polinomi)):
        print("P" + str(i) + "(x) = " + str(sturmovi_polinomi[i]).replace('x**', 'x^'))
    vrednosti_polinoma_a = sracunajVrednostiPolinoma(aa, sturmovi_polinomi)
    vrednosti_polinoma_b = sracunajVrednostiPolinoma(bb, sturmovi_polinomi)
    ispisiVrednostiSturmovihPolinoma(vrednosti_polinoma_a, vrednosti_polinoma_b)

    promenaZnaka1 = proveriPromenuZnaka(vrednosti_polinoma_a)
    promenaZnaka2 = proveriPromenuZnaka(vrednosti_polinoma_b)
    print("")
    print("V(" + str(aa) + ") = " + str(promenaZnaka1))
    print("V(" + str(bb) + ") = " + str(promenaZnaka2))
    print("")
    brojNula = abs(promenaZnaka1 - promenaZnaka2)
    print("Broj nula je: " + str(brojNula))
    print(" ")

    if brojNula == 0:
        vrednost_funkcije = polinom.subs(x, m.pi/2-0.00001)
        if vrednost_funkcije < 0:
            print("P[" + str(i1) + "," + str(
                i2) + "](x) NEMA NULE na intervalu [0, pi/2] ali je NEGATIVNA, pa NE DOKAZUJE pozitivnost MTP funkcije na tom intervalu!")
        else:
            print("P[" + str(i1) + "," + str(
                i2) + "](x) NEMA NULE na intervalu [0, pi/2] ali je POZITIVNA, pa DOKAZUJE pozitivnost MTP funkcije na tom intervalu!")
    else:
        print("P[" + str(i1) + "," + str(
            i2) + "](x) IMA NULA na intervalu [0, pi/2], pa NE DOKAZUJE pozitivnost MTP funkcije na tom intervalu!")

def metoda_za_iscrtavanje():
    graph = sym.plot(MTP, p[0], p[1], p[2], p[3], show=False)
    graph.title = "MTP Funkcije"
    graph[0].label = "MTP f(x)"
    graph[1].label = "P[0,0](x)"
    graph[2].label = "P[0,1](x)"
    graph[3].label = "P[1,0](x)"
    graph[4].label = "P[1,1](x)"
    graph[0].line_color = colors[0]
    graph[1].line_color = colors[1]
    graph[2].line_color = colors[2]
    graph[3].line_color = colors[3]
    graph[4].line_color = colors[4]
    #Primer 1 graph.xlim = [-0.25, 2]
    #Primer 1 graph.ylim = [-3, 1]
    #Primer 2, Primer 3
    graph.ylim = [-3, 3]
    #Primer 2, Primer 3
    graph.xlim = [-0.25, 2]
    graph.xlabel = "Ox"
    graph.ylabel = "Oy"
    graph.legend = True
    graph.show()

# MTP Funkcija f(x) = x^3*sin(x) - x*cos^3(x) + x - 3/2*x^3 + 3/32*x^4, na intervalu [0, pi/2]
#Primer1
#MTP = x ** 3 * sym.sin(x) - x * sym.cos(x) ** 3 + x - 3 / 2 * x ** 3 + 3 / 32 * x ** 4
#Primer2
#MTP = -x**4*sym.sin(x)**5 + x*sym.cos(x)**5 + x**4 - 1/2*x**3 + x**2
#Primer3
#MTP = -x ** 4 * sym.sin(x) + x * sym.cos(x) ** 2 - x**2 + 6 / 2 * x ** 3 - 3 / 7 * x ** 5 + 1

#MTP = x**4 * sym.cos(x)**4 + x**3 - 0.5 * x**2 + 2 * x * sym.sin(x) + 1
MTP = x**3 * sym.cos(x)**2 + x**2 - x * sym.sin(x) + 0.5;
print("MTP funkcija za koju dokazujemo pozitivnost: " + ispis_funkcije(str(MTP)))
[a, b] = koriscena_poredjenja();
aa, bb = [0.0001, m.pi / 2]
sturmovi_polinomi = []
print(a)
print(b)
p0 = pozitivnost_mtp_funkcije(MTP, 0, 0)
p0_izvod = sym.diff(p0, x, 1)
p1 = pozitivnost_mtp_funkcije(MTP, 0, 1)
p1_izvod = sym.diff(p1, x, 1)
p2 = pozitivnost_mtp_funkcije(MTP, 1, 0)
p2_izvod = sym.diff(p2, x, 1)
p3 = pozitivnost_mtp_funkcije(MTP, 1, 1)
p3_izvod = sym.diff(p3, x, 1)
p = [p0, p1, p2, p3]

print("----------")
print("P0(x) = P[0,0](x) = " + ispis_funkcije(str(p0)))
drugi_projektni_zadatak_metoda(p0, p0_izvod, 0, 0)
print("----------")
print("P1(x) = P[0,1](x) = " + ispis_funkcije(str(p1)))
drugi_projektni_zadatak_metoda(p1, p1_izvod, 0, 1)
print("----------")
print("P2(x) = P[1,0](x) = " + ispis_funkcije(str(p2)))
drugi_projektni_zadatak_metoda(p2, p2_izvod, 1, 0)
print("----------")
print("P3(x) = P[1,1](x) = " + ispis_funkcije(str(p3)))
drugi_projektni_zadatak_metoda(p3, p3_izvod, 1, 1)

colors = ['r', 'b', 'g', 'y', 'c']
#metoda_za_iscrtavanje()

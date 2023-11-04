package prvi;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.Scanner;

public class Main {
	
	// realni broj
	static double a;
	
	// granicne vrednosti imenioca q
	static int n;
	static int m;
	
	// razlomci p/q
	public static ArrayList<Razlomak> razlomci = new ArrayList<>();
	
	// lista sa clanovima veriznog razvoja broja a
	public static ArrayList<Integer> verizniRazvoj = new ArrayList<>();
		
	// liste za algoritam sa pdf-a
	public static ArrayList<Double> nizX = new ArrayList<>();;
	public static ArrayList<Double> nizA = new ArrayList<>();;
	public static ArrayList<Double> nizD = new ArrayList<>();;
	
	// konvergente broja a
	public static ArrayList<Razlomak> konvergente = new ArrayList<>();
	// set sa konvergentama u vidu stringa
	public static HashSet<String> setKonvergenti = new HashSet<>();
	// set sa razlomcima prve vrste u vidu stringa
	public static HashSet<String> setPrvaVrsta = new HashSet<>();
	
	// aproksimacije I i II i N vrste
	public static ArrayList<Razlomak> aprokcimacije1 = new ArrayList<>();
	public static ArrayList<Razlomak> aprokcimacije2 = new ArrayList<>();
	public static ArrayList<Razlomak> aprokcimacijeN = new ArrayList<>();
	
	// formiranje svih p/q razlomaka
	public static void formirajRazlomke() {
		System.out.println("*****************************************************************");
		System.out.println("Svi razlomci: ");
		System.out.printf("%-10s %-25s", "RAZLOMAK", "VERIZNI RAZVOJ");
		System.out.println();
		for(int i = n; i <= m; i++) {
			int q = i;
			int p = (int) Math.round((double) a * q);
			Razlomak razlomak = new Razlomak(p, q);
			razlomak.odrediVerizniRazvoj();
			razlomak.izracunajGreske(a);
			razlomci.add(razlomak);
			System.out.printf("%-10s %-25s", razlomak, razlomak.ispisiVerizniRazvoj());
			System.out.println();
		}
	}
	
	// odredjivanje veriznih decimala broja a
	private static void odrediVerizniRazvoj() {
		// postavljanje pocetnih vrednosti u listama
		double x0 = a;
		double a0 = Math.floor(x0);
		double d0 = x0 - a0;
		nizX.add(x0); nizA.add(a0); nizD.add(d0);
		verizniRazvoj.add((int) Math.round(a0));
		
		// racunanje veriznih decimala
		for(int i = 0; i <= m - n; i++) {
			if (nizD.get(i) <= Razlomak.PRAG) {
				break;
			}
	        double x = 1.0 / nizD.get(i); nizX.add(x);
	        double a = Math.floor(x); nizA.add(a);
	        double d = x - a; nizD.add(d);
	        verizniRazvoj.add((int) a);
		}
		
		// azuriranje pretposlednje verizne decimale ukoliko je
	    // poslednja decimala jednaka 1
	    int brojClanova = verizniRazvoj.size();
	    if (brojClanova >= 2) {
	        int poslednjaDecimala = verizniRazvoj.get(brojClanova - 1);
	        if (poslednjaDecimala == 1) {
	            int pretposlednjaDecimala = verizniRazvoj.get(brojClanova - 2) + 1;
	            verizniRazvoj.set(brojClanova - 2, pretposlednjaDecimala);
	            verizniRazvoj.remove(brojClanova - 1);
	        }
	    }
		
	    // ispis clanova veriznog razvoja
	    System.out.println("*****************************************************************");
	    StringBuilder ispisBuilder = new StringBuilder();
	    ispisBuilder.append("[");

	    for(int i = 0; i < verizniRazvoj.size(); i++) {
	        if (i == 0) {
	            ispisBuilder.append(verizniRazvoj.get(i));
	            if (verizniRazvoj.size() > 1) {
	                ispisBuilder.append("; ");
	            }
	        } else {
	            ispisBuilder.append(verizniRazvoj.get(i));
	            if (i < (verizniRazvoj.size() - 1)) {
	                ispisBuilder.append(", ");
	            }
	        }
	    }
	    ispisBuilder.append("]");
		System.out.println("Verizni razvoj broja a: " + ispisBuilder.toString());
	}
	
	// racunanje konvergenti broja a
	public static void odrediKonvergente() {
        // racunanje prve dve konvergente
		long p0 = verizniRazvoj.get(0); 
		long q0 = 1;
		konvergente.add(new Razlomak(p0, q0));
		setKonvergenti.add(p0 + "/" + q0);
		if(verizniRazvoj.size() < 2) {
			// ispis konvergenti
			System.out.println("*****************************************************************");
			System.out.print("Konvergente: ");
			System.out.println(konvergente);
			return;
		}
		long p1 = p0 * verizniRazvoj.get(1) + 1;
		long q1 = verizniRazvoj.get(1);
		konvergente.add(new Razlomak(p1, q1));
		setKonvergenti.add(p1 + "/" + q1);
		
		// racunanje ostalih konvergenti rekurentnom formulom
		for (int j = 2; j < verizniRazvoj.size(); j++) {
			long p = konvergente.get(j - 1).p * verizniRazvoj.get(j) + konvergente.get(j - 2).p;
			long q = konvergente.get(j - 1).q * verizniRazvoj.get(j) + konvergente.get(j - 2).q;
			konvergente.add(new Razlomak(p, q));
			setKonvergenti.add(p + "/" + q);
		}
		
		// ispis konvergenti
		System.out.println("*****************************************************************");
		System.out.print("Konvergente: ");
		System.out.println(konvergente);
	}
	
	// podela razlomaka na aprokscimacije I, II i N vrste
	public static void odrediAproksimacije() {
		for(int i = 0; i < razlomci.size(); i++) {
			Razlomak razlomak = razlomci.get(i);
			// provera da li je razlomak nakon skracivanja u konvergentama
			long nzd = razlomak.nzd();
			long p = razlomak.p / nzd;
			long q = razlomak.q / nzd;
			String s = p + "/" + q;
			// konvergente su aproksimacije II vrste
			if(setKonvergenti.contains(s)) {
				aprokcimacije2.add(razlomak);
				razlomak.tip = "II";
				continue;
			}
			
			if(setPrvaVrsta.contains(s)) {
				aprokcimacije1.add(razlomak);
				razlomak.tip = "I";
				continue;
			}
			
			// provera da li je manja greska nego u prethodnicima
			double apsGreska = Math.abs(razlomak.greska_prve_vrste);
			boolean najboljaAproksimacija = true;
			for (int j = i - 1; j >= 0; j--) {
		        Razlomak prethodni = razlomci.get(j);
		        double apsGreskaPrethodni = Math.abs(prethodni.greska_prve_vrste);
		        if(apsGreskaPrethodni <= apsGreska) {
		          najboljaAproksimacija = false;
		          break;
		       }
		    }
		    if(najboljaAproksimacija) {
		        aprokcimacije1.add(razlomak);
		        setPrvaVrsta.add(s);
		        razlomak.tip = "I";
		        continue;
		    }
		    aprokcimacijeN.add(razlomak);
		    razlomak.tip = "N";
		}
	}
	
	private static void sortirajIspisiAproksimacije() {
		// sortiranje aproksimacija po rastucoj vrednosti odstupanja od a
		Collections.sort(aprokcimacije1, (r1, r2) -> 
	    Double.compare(Math.abs(r1.greska_prve_vrste), Math.abs(r2.greska_prve_vrste))
	    );
		Collections.sort(aprokcimacije2, (r1, r2) -> 
	    Double.compare(Math.abs(r1.greska_prve_vrste), Math.abs(r2.greska_prve_vrste))
	    );
		Collections.sort(aprokcimacijeN, (r1, r2) -> 
	    Double.compare(Math.abs(r1.greska_prve_vrste), Math.abs(r2.greska_prve_vrste))
	    );
		// ispisivanje aproksimacija
		System.out.println("*****************************************************************");
		System.out.println("Aproksimacije I vrste sortirane rastuce po odstupanju: ");
		System.out.printf("%-10s %-25s %-35s", "RAZLOMAK", "VERIZNI RAZVOJ",  "ODSTUPANJE");
		System.out.println();
		for(int i = 0; i < aprokcimacije1.size(); i++) {
			Razlomak razlomak = aprokcimacije1.get(i);
			System.out.printf("%-10s %-25s %-35s", razlomak, razlomak.ispisiVerizniRazvoj(), razlomak.greska_prve_vrste);
			System.out.println();
		}
        
		System.out.println("*****************************************************************");
		System.out.println("Aproksimacije II vrste sortirane rastuce po odstupanju: ");
		System.out.printf("%-10s %-25s %-35s", "RAZLOMAK", "VERIZNI RAZVOJ", "ODSTUPANJE");
		System.out.println();
		for(int i = 0; i < aprokcimacije2.size(); i++) {
			Razlomak razlomak = aprokcimacije2.get(i);
			System.out.printf("%-10s %-25s %-35s", razlomak, razlomak.ispisiVerizniRazvoj(), razlomak.greska_prve_vrste);
			System.out.println();
		}
        
		System.out.println("*****************************************************************");
		System.out.println("Aproksimacije N vrste sortirane rastuce po odstupanju: ");
		System.out.printf("%-10s %-25s %-35s", "RAZLOMAK", "VERIZNI RAZVOJ", "ODSTUPANJE");
		System.out.println();
		for(int i = 0; i < aprokcimacijeN.size(); i++) {
			Razlomak razlomak = aprokcimacijeN.get(i);
			System.out.printf("%-10s %-25s %-35s", razlomak, razlomak.ispisiVerizniRazvoj(), razlomak.greska_prve_vrste);
			System.out.println();
		}
		
	}
	
	public static void sortirajIspisiRazlomke() {
		// sortiranje razlomaka po rastucoj vrednosti odstupanja
		Collections.sort(razlomci, (r1, r2) -> 
	    Double.compare(Math.abs(r1.greska_prve_vrste), Math.abs(r2.greska_prve_vrste))
	  );
		// ispisivanje razlomaka
		System.out.println("*****************************************************************");
		System.out.println("Svi razlomci sortirani rastuce po odstupanju: ");
		System.out.printf("%-10s %-25s %-35s %-5s", "RAZLOMAK", "VERIZNI RAZVOJ", "ODSTUPANJE", "TIP");
		System.out.println();
        for(int i = 0; i < razlomci.size(); i++) {
        	Razlomak razlomak = razlomci.get(i);
        	System.out.printf("%-10s %-25s %-35s %-5s", razlomak, 
					razlomak.ispisiVerizniRazvoj(), razlomak.greska_prve_vrste, razlomak.tip);
			System.out.println();
        }
	}
	
	 public static void main(String[] args) {
	        Scanner scanner = new Scanner(System.in);
	        System.out.println("*****************************************************************");

	        // unos a
	        while (true) {
	            System.out.print("Unesite realan broj: ");
	            if (scanner.hasNextDouble()) {
	                a = scanner.nextDouble();
	                break;
	            } else {
	                System.out.println("Unesite validan realan broj.");
	                scanner.next();
	            }
	        }

	        // unos n
	        while (true) {
	            System.out.print("Unesite pozitivan ceo broj n: ");
	            if (scanner.hasNextInt()) {
	                n = scanner.nextInt();
	                if (n > 0) {
	                    break;
	                } else {
	                    System.out.println("Broj n mora biti veci od 0.");
	                }
	            } else {
	                System.out.println("Unesite validan pozitivan ceo broj.");
	                scanner.next(); // ocisti nevazeci unos
	            }
	        }

	        // unos m
	        while (true) {
	            System.out.print("Unesite pozitivan ceo broj m veci od n: ");
	            if (scanner.hasNextInt()) {
	                m = scanner.nextInt();
	                if (m > n) {
	                    break;
	                } else {
	                    System.out.println("Broj m mora biti veci od broja n.");
	                }
	            } else {
	                System.out.println("Unesite validan pozitivan ceo broj.");
	                scanner.next(); // ocisti nevazeci unos
	            }
	        }

	        formirajRazlomke();
	        odrediVerizniRazvoj();
	        odrediKonvergente();
	        odrediAproksimacije();
	        sortirajIspisiAproksimacije();
	        sortirajIspisiRazlomke();

	        scanner.close();
	    }
}

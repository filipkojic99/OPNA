package prvi;

import java.util.ArrayList;

public class Razlomak {
	
	// brojilac i imenilac
	public long p;
	public long q;
	
	// tolerancija na gresku 
	public static final double PRAG = 1e-8;
	
	// lista sa clanovima veriznog razvoja
	public ArrayList<Integer> verizniRazvoj;
	
	// liste za algoritam sa pdf-a
    public ArrayList<Double> nizX;
    public ArrayList<Double> nizA;
    public ArrayList<Double> nizD;
    
    // greske I i II vrste
	public double greska_prve_vrste;
	public double greska_druge_vrste;
	
	// tip razlomka - I, II ili N vrsta
	public String tip;
	
	// konstruktor za kreiranje objekta razlomka
	public Razlomak(long p, long q) {
		this.p = p;
		this.q = q;
		// kreiranje listi
		verizniRazvoj = new ArrayList<>();
		nizX = new ArrayList<>();
		nizA = new ArrayList<>();
		nizD = new ArrayList<>();
	}
	
	// odredjivanje veriznih decimala
	public void odrediVerizniRazvoj() {
	    // postavljanje pocetnih vrednosti u listama
	    double x0 =  this.p * 1.0 / this.q;
	    double a0 = Math.floor(x0);
	    double d0 = x0 - a0;
	    nizX.add(x0); nizA.add(a0); nizD.add(d0);
	    verizniRazvoj.add((int)a0);

	    // racunanje veriznih decimala
	    int i = 0;
	    while (nizD.get(i) > PRAG) {
	        i++;
	        double x = 1.0 / nizD.get(i - 1);
	        double a = Math.floor(x);
	        double d = x - a;
	        nizX.add(x); nizA.add(a); nizD.add(d);
	        verizniRazvoj.add((int) a);
	    }
	    
	    // azuriranje pretposlednje verizne decimale ukoliko je
	    // poslednja decimala jednaka 1
	    int brojClanova = verizniRazvoj.size();
	    if(brojClanova >= 2) {
	        int poslednjaDecimala = verizniRazvoj.get(brojClanova - 1);
	        if(poslednjaDecimala == 1) {
	            int pretposlednjaDecimala = verizniRazvoj.get(brojClanova - 2) + 1;
	            verizniRazvoj.set(brojClanova - 2, pretposlednjaDecimala);
	            verizniRazvoj.remove(brojClanova - 1);
	        }
	    }
	}

	// racunanje gresaka I i II vrste
	public void izracunajGreske(double a) {
		this.greska_prve_vrste = a - (this.p * 1.0 / this.q);
		this.greska_druge_vrste = this.q * a - this.p;
	}

	// ispis clanova veriznog razvoja
	public String ispisiVerizniRazvoj() {
	    StringBuilder ispisBuilder = new StringBuilder();
	    ispisBuilder.append("[");

	    for(int i = 0; i < verizniRazvoj.size(); i++) {
	        if(i == 0) {
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
	    return ispisBuilder.toString();
	}
	
	// metoda za trazenje najveceg zajednickog delioca
	// za skracivanje razlomka ukoliko je to potrebno
	public long nzd() {
		long qq = q;
		long pp = p;
        while (qq != 0) {
            long t = qq;
            qq = pp % qq;
            pp = t;
        }
        return pp;
    }

	// ispis razlomka kao p/q
	public String toString() {
		return this.p + "/" + this.q;
	}
	
}

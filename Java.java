// Darmowy program NetBeans
// https://www.programiz.com/java-programming/keywords-identifiers
// 1
class Nazwa_pliku {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        // Twój kod
    }
}

// Zmienne
boolean flag1 = false;
boolean flag2 = true;

byte a = 10;
short b = 100;
int c = 1000;
long d = 10000;
float e = 1.5F; // Domyślny zmiennoprzecinkowy double
double f = 1.555;
char g = 'F';
String h = "Java Programming";

System.out.println(a + " " + b + " " + c + " " + d + " " + e + " " + f + " " + g + " " + h);

// Operatory
DZIAŁANIA i OPERATORY:
Operatory arytmetyczne:
    +	Dodanie	        2 + 2 = 4
    -	Odejmowanie	    5 - 2 = 3
    *	Mnożenie	    3 * 3 = 9
    /	Dzielenie	    22 / 8 = 2.75 // int 2, float 2.75
    %	Moduł / Reszta z dzielenie  22 % 8 = 6

Operatory przypisania wartości:
    =   Przypisanie wartości z lewej do prawej; znaczenie:  i=1;
    +=  Dodawanie; znaczenie:   x = x + y;
    -=  Odejmowanie; znaczenie: x = x - y;
    *=  Mnożenie; znaczenie:    x = x * y;
    /=  Dzielenie; znaczenie:   x = x / y;
    %=  Moduł / Reszta z dzielenie  x = x % y;

Operatory inkrementacji i dekrementacji:
    ++  Inkrementacja; znaczenie: i=i+1; // i++ lub ++i
    --  Dekrementacja; znaczenie: i=i+1; // i-- lub --i

Operatory porównania / relacji:
    !   Zaprzeczenie; znaczenie:    x ! y;
    ==  Równy; znaczenie:           x == y;
    !=  Różny; znaczenie:           x != y;
    <   Mniejszy; znaczenie:        x < y;
    >   Większy; znaczenie:         x > y;
    <=  Mniejszy równy; znaczenie:  x <= y;
    >=  Większy równy; znaczenie:   x >= y;

Operatory logiczne - działają po kolei do lewej - zwracają bool -> T/F:
    !   Zaprzeczenie / Negacja  NOT ("nie"); znaczenie: x ! y;
    &&  Koniunkcja  AND ("i"); znaczenie:       x && y;
    ||  Alternatywa OR  ("lub"); znaczenie:     x || y;
    
	bool result;
	result = (3 != 5) && (3 < 5);     // true


































// Szkolne programy
package projekt1;
import java.util.Scanner;
public class Projekt1 {

    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);
        System.out.println("Jak masz na imie?");
        //scan.nextLine(); //Pobiera Enter i zapodziane znaki białe
        //scan.nextInt();
        //scan.nextDouble();
        String imie = scan.nextLine();
        System.out.println("Witaj " + imie);
    }
    
}



package projekt1;

public class Projekt1 {

    public static void main(String[] args) {

        int x = 5;
        double y = 5.5;
        boolean z = true;

        if (x < y) {
            System.out.println("To jest " + x);
            System.out.println("To jest " + x);
        } else {
            System.out.println("To jest " + y);
        }

    }
}



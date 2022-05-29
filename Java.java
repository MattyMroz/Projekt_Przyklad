// Darmowy program NetBeans
// https://www.programiz.com/java-programming/keywords-identifiers
// 1
public class Nazwa_pliku  {
    public static void main(String[] args) {
        System.out.println("Hello World!");
        // Twój kod
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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









////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Gruby chudy
import java.util.Scanner;
import static java.lang.Math.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Podaj wage w kg:");
        double waga = scanner.nextDouble();
        System.out.println("Podaj wzrost w cm:");
        double wzrost = scanner.nextDouble();
        wzrost /= 100;
        double BMI = waga/Math.pow(wzrost,2);
        System.out.println(BMI);

        if(BMI < 18.5)
        {
            System.out.println("Jesteś za chudy!");
        }
        else if(BMI > 25)
        {
            System.out.println("Jesteś za gruby!");
        }
        else 
        {
            System.out.println("Jesteś za w normie!");
        }
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
 
        double a, b, c;
        Scanner sc = new Scanner(System.in);
 
        System.out.print("a=");
        a = sc.nextFloat();
 
        System.out.print("b=");
        b = sc.nextFloat();
 
        System.out.print("c=");
        c = sc.nextFloat();
 
        if (a != 0) {
            double delta = b * b - 4 * a * c;
 
            if (delta < 0) {
                System.out.println("Brak rozwiązań (delta < 0)");
            } else if (delta == 0) {
                double x;
                x = -b / (2 * a);
                System.out.printf("Jedno podwójne rozwiązanie x = %f", x);
            } else {
                double x1 = (-b + Math.sqrt(delta)) / (2 * a);
                double x2 = (-b - Math.sqrt(delta)) / (2 * a);
                System.out.printf("Istnieją dwa rozwiązania x1 = %f oraz x2 = %f", x1, x2);
            }
        } else {
            System.out.println("Parametr a == 0");
        }
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Kalkulator
package main;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        int jeden = 0;
        int dwaw = 0;
        int co = 0;
        Scanner scan = new Scanner(System.in);
        System.out.println("Co dzisiaj robimy? Wpisz odpowiedni numer");
        System.out.println("1. Dodawanie, 2. Odejmowanie, 3. Mnożenie, 4. Dzielenie");
        co = Integer.parseInt(scan.nextLine());
        System.out.println("Podaj 1 liczbę");
        jeden = Integer.parseInt(scan.nextLine());
        System.out.println("Podaj 2 liczbę");
        dwaw = Integer.parseInt(scan.nextLine());
        if (co == 1) {
            int Wynik = jeden + dwaw;
            System.out.println(Wynik); }
        if (co == 2) {
            int Wynik = jeden - dwaw;
            System.out.println(Wynik); }
        if (co == 3) {
            int Wynik = jeden * dwaw;
            System.out.println(Wynik); }
        if (co == 4) {
            int Wynik = jeden / dwaw;
            System.out.println(Wynik); }
    }
}



////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Trójka pitagorejska
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a, b, c;
        System.out.printf("Podaj liczbę a: ");
        a = scan.nextInt();
        System.out.printf("Podaj liczbę b: ");
        b = scan.nextInt();
        System.out.printf("Podaj liczbę c: ");
        c = scan.nextInt();
        if ((Math.pow(a,2) + Math.pow(b,2) == Math.pow(c,2)) ||
            (Math.pow(a,2) + Math.pow(c,2) == Math.pow(b,2)) ||
            (Math.pow(b,2) + Math.pow(c,2) == Math.pow(a,2))) {
            System.out.printf("Liczby stanowią trojkę pitagorejska!");
        } else {
            System.out.printf("To nie jest trojka pitagorejska!");
        }
    }
}


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Prosty kalkulator
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int choice = 0;
        double a, b;
        boolean test = true;

        while (test){
            System.out.println("Wybierz co chcesz zrobić:");
            System.out.println("1. Dodawane");
            System.out.println("2. Odejmowanie");
            System.out.println("3. Mnoźenie");
            System.out.println("4. Dzielenie");
            System.out.printf("Twój wybór to: ");
            choice = scan.nextInt();

            if (choice < 1 || choice > 4) {
                System.out.println("Podaj poprawną wartość!");
                System.out.println("");
                continue;
            }

            System.out.println("Podaj dwie liczby:");
            System.out.printf("a = ");
            a = scan.nextDouble();
            System.out.printf("b = ");
            b = scan.nextDouble();

            if (choice == 1) {
                System.out.println(a + b);
                break;
            } else if (choice == 2) {
                System.out.println(a - b);
                break;
            } else if (choice == 3) {
                System.out.println(a * b);
                break;
            } else {
                System.out.println(a / b);
                break;
            }
        }
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Sprawdzanie czy rok jest przestępny
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.printf("Podaj rok: ");
        int rok = scan.nextInt();

        if (((rok % 4 == 0) && (rok % 100 != 0)) || (rok % 400 == 0)) {
            System.out.println("Rok jest przestępny!");
        } else {
            System.out.println("Rok nie jest przestępny!");
        }
    }
}






////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Odczyt i zapis do pliku projekt
// 1
// Szablon
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main  {
    public static void main(String[] args) {
        try{
            //zapis
            PrintWriter zapis = new PrintWriter("dane.txt");
            zapis.println("admin;login;haslo");
            zapis.println("user;aaa;aaa");
            zapis.close();

            //odczyt
            File plik = new File("dane.txt");
            Scanner in = new Scanner(plik);
            String zdanie;
            while(in.hasNext()){
                zdanie = in.nextLine();

                List<String> tokens = new ArrayList<>();
                StringTokenizer tokenizer = new StringTokenizer(zdanie, ";");
                while (tokenizer.hasMoreElements()) {
                    tokens.add(tokenizer.nextToken());
                }

                System.out.print("Uprawnienia: ");
                System.out.println(tokens.get(0));
                System.out.print("Login: ");
                System.out.println(tokens.get(1));
                System.out.print("Haslo: ");
                System.out.println(tokens.get(2));
                System.out.println();
            }

        }catch(FileNotFoundException e){

        }
    }
}



////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 22222222222222222222222
// Zadanie 1
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main2 {
    public static void main(String[] args) {
        try {
            // zapis
            PrintWriter zapis = new PrintWriter("dane1.txt");
            zapis.println("admin;admin;haslo_poprawne");
            zapis.println("admin;admin_niepoprawny;haslo_poprawne");
            zapis.println("admin;admin;haslo_niepoprawne");

            zapis.println("user;admin;haslo_poprawne");
            zapis.println("user;user_niepoprawny;haslo_poprawne");
            zapis.println("user;admin;haslo_niepoprawne");
            zapis.close();

            // odczyt
            File plik = new File("dane1.txt");
            Scanner in = new Scanner(plik);
            String zdanie;
            while (in.hasNext()) {
                zdanie = in.nextLine();

                List<String> tokens = new ArrayList<>();
                StringTokenizer tokenizer = new StringTokenizer(zdanie, ";");
                while (tokenizer.hasMoreElements()) {
                    tokens.add(tokenizer.nextToken());
                }
                System.out.println();
                System.out.print("Uprawnienia: ");
                System.out.println(tokens.get(0));
                // Zad1 Po uruchomieniu program ten przyzna dostęp wyłącznie użytkownikowi o
                // nazwie admin, który dysponuje właściwym hasłem
                // uznałem że nazwa (admin) = login, a nie uprawnienia
                System.out.print("Login: ");
                if (tokens.get(1).equals("admin")) {
                    System.out.println(tokens.get(1));
                } else {
                    System.out.println("Niepoprawny login");
                    continue;
                }

                System.out.print("Haslo: ");
                if (tokens.get(2).equals("haslo_poprawne")) {
                    System.out.println(tokens.get(2));
                } else {
                    System.out.println("Niepoprawne haslo");
                    continue;
                }
                System.out.println("Poprawnie zalogowano!");
                System.out.println();

            }

        } catch (FileNotFoundException e) {

        }
    }
}



////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 333333333333333333
// Połączenie zadań 2 i 3
// Razem tworzą lepszą funkcjonalność i spełniają wszystkie warunki owych zadań
// Funkcje zrobione są amatorsko można by je bardziej porozdzielać, by zapobiegać redundancji kodu
// Taki kod zroniony w pare godzin, wynik twórczego działania ;)
import java.io.File;
// import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.StringTokenizer;
import java.io.BufferedWriter;
import java.io.FileWriter;
// import java.io.Writer;
import java.io.IOException;
import java.io.FileNotFoundException;

public class Main3 {

    public static boolean sign_in_admin(String login_admin, String haslo_admin) {
        int n = 0;
        try {
            // Ddczyt pliku
            File plik = new File("dane2.txt");
            Scanner in = new Scanner(plik);
            String zdanie;
            while (in.hasNext()) {
                zdanie = in.nextLine();

                List<String> tokens = new ArrayList<>();
                StringTokenizer tokenizer = new StringTokenizer(zdanie, ";");
                while (tokenizer.hasMoreElements()) {
                    tokens.add(tokenizer.nextToken());
                }
                System.out.println();

                if (tokens.get(0).equals("admin") && tokens.get(1).equals(login_admin)
                        && tokens.get(2).equals(haslo_admin)) {
                    n = 1;
                    break;
                } else {
                    n = 0;
                }
            }

        } catch (FileNotFoundException e) {
            System.out.println(e.getMessage());
        }
        if (n == 1) {
            return true;
        } else {
            return false;
        }
    }

    public static int sign_in_all_users(String login, String haslo) {
        int n = 0;
        try {
            // Doczyt pliku
            File plik = new File("dane2.txt");
            Scanner in = new Scanner(plik);
            String zdanie;
            while (in.hasNext()) {
                zdanie = in.nextLine();

                List<String> tokens = new ArrayList<>();
                StringTokenizer tokenizer = new StringTokenizer(zdanie, ";");
                while (tokenizer.hasMoreElements()) {
                    tokens.add(tokenizer.nextToken());
                }
                System.out.println();

                if (tokens.get(0).equals("admin") && tokens.get(1).equals(login) && tokens.get(2).equals(haslo)) {
                    n = 1;
                    break;
                } else if (tokens.get(0).equals("user") && tokens.get(1).equals(login) && tokens.get(2).equals(haslo)) {
                    n = 2;
                } else {
                    n = 3;
                }

            }

        } catch (FileNotFoundException e) {
            System.out.println(e.getMessage());
        }
        if (n == 1) {
            return 1;
        } else if (n == 2) {
            return 2;
        } else {
            return 3;
        }
    }

    public static void main(String[] args) {
        char x;
        String y, user_admin, login, haslo;
        Scanner scan = new Scanner(System.in);

        while (true) {

            System.out.println("    MENU GLOWNE");
            System.out.println("-------------------");
            System.out.println("1. REJESTRACJA UZYTKOWNIKOW - TYLKO ADMIN");
            System.out.println("2. LOGOWANIE");
            System.out.println("3. Koniec progromu");
            System.out.println("------------------");
            System.out.println("Podpowiedz: Nacisnij klawisz odpowiadajacy cyfrom: 1, 2 lub 3");
            System.out.println();
            x = scan.next().charAt(0);

            switch (x) {
            case '1':
                scan.nextLine();
                System.out.println("Tylko Administrator moze dodawac uzytkownikow!");
                System.out.println("Wpisz haslo do uprawnien administratora!");
                System.out.println("(JESLI jestes administratoram wpisz: admin)");
                user_admin = scan.nextLine();

                if (user_admin.equals("admin")) {
                    System.out.println("Zaloguj sie by dodac uzytkownikow! - Login: admin, Haslo: haslo");

                    System.out.print("Podaj login: ");
                    login = scan.nextLine();
                    System.out.print("Podaj haslo: ");
                    haslo = scan.nextLine();

                    // Gdy plik jest pusty dodaje użytkownika admin;admin;haslo
                    try {
                        File plik = new File("dane2.txt");
                        BufferedWriter zapis = new BufferedWriter(new FileWriter(plik, true));
                        if (plik.length() == 0) {
                            zapis.append("admin;admin;haslo");
                        }
                        zapis.close();
                    } catch (Exception e) {
                        System.out.println(e.getMessage());
                    }

                    // Rejestracja użytkowników przez administratora
                    if (sign_in_admin(login, haslo) == true) {
                        try {
                            // Rejestracja
                            System.out.println("Chcesz stworzyc:");
                            System.out.println("1 - Administratora");
                            System.out.println("2 - Urzytkownika");
                            int x1 = scan.nextInt();
                            scan.nextLine();

                            int n = 0;
                            boolean user_is = true;
                            while (n < 2) {
                                user_is = true;

                                File plik = new File("dane2.txt");
                                Scanner in = new Scanner(plik);

                                System.out.print("Podaj login nowego uzytkownika: ");
                                login = scan.nextLine();
                                System.out.print("Podaj haslo nowego uzytkownika: ");
                                haslo = scan.nextLine();

                                // Odczyt pliku
                                String zdanie;
                                while (in.hasNext()) {
                                    zdanie = in.nextLine();

                                    List<String> tokens = new ArrayList<>();
                                    StringTokenizer tokenizer = new StringTokenizer(zdanie, ";");
                                    while (tokenizer.hasMoreElements()) {
                                        tokens.add(tokenizer.nextToken());
                                    }
                                    System.out.println();

                                    if (tokens.get(0).equals("admin") && tokens.get(1).equals(login)
                                            || tokens.get(0).equals("user") && tokens.get(1).equals(login)) {
                                        System.out.println("Istnieje juz uzytkownik o podanym loginie!");
                                        user_is = false;
                                        break;
                                    }

                                }

                                BufferedWriter zapis = new BufferedWriter(new FileWriter(plik, true));
                                if (x1 == 1 && user_is == true) {
                                    n++;
                                    zapis.append("\nadmin;" + login + ";" + haslo);
                                } else if (x1 == 2 && user_is == true) {
                                    n++;
                                    zapis.append("\nuser;" + login + ";" + haslo);
                                } else {
                                    System.out.println("Powodzenia za nastepnym razem!");
                                }
                                zapis.close();
                                n++;
                            }

                        } catch (Exception e) {
                            System.out.println(e.getMessage());
                        }
                    } else {
                        System.out.println("Logowanie sie nie powiodlo!");
                        System.out.println("Sproboj jeszcze raz!");
                    }
                } else {
                    System.out.println("Zegnam!");
                }

                break;
            case '2':
                int m = 0;
                while (m < 2) {
                    scan.nextLine();
                    System.out.print("Podaj login: ");
                    login = scan.nextLine();
                    System.out.print("Podaj haslo: ");
                    haslo = scan.nextLine();
                    if (sign_in_all_users(login, haslo) == 1) {
                        System.out.println("Zalogowano poprawnie!");
                        System.out.println("Uprawnienia: Administrator");
                        System.out.println("Login: " + login);
                        System.out.println("Haslo: " + haslo);
                        m = 2;
                    } else if (sign_in_all_users(login, haslo) == 2) {
                        System.out.println("Zalogowano poprawnie!");
                        System.out.println("Uprawnienia: Uzytkownik");
                        System.out.println("Login: " + login);
                        System.out.println("Haslo: " + haslo);
                        m = 2;
                    } else {
                        System.out.println("Nie zalogowano poprawnie!");
                        m++;
                    }
                }

                break;
            case '3':
                System.exit(0);
                break;

            default:
                System.out.println("Podaj wartosc 1, 2 lub 3!");
                System.out.println("Wcisnij Enter");
                System.out.println();
                scan.nextLine();
                break;
            }
            y = scan.nextLine();
            System.out.print("\033[H\033[2J");
        }
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Zad 1 Rysowanie przyklejonych trójkątów
import java.util.Scanner;

public class Main1 {

    public static void main(String[] args) {
        System.out.println("Podaj wielkosc boku trojkata:");
        int x;
        Scanner scaner = new Scanner(System.in);
        x = scaner.nextInt();

        for(int i=x;i>=0;i--){
            for(int j=i;j>=0;j--)
                System.out.print(" ");
            for(int j=i;j<x;j++)
                System.out.print("##");
            System.out.println("");
        }
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Zad 2
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        System.out.print("n = ");
        int x;
        Scanner scaner = new Scanner(System.in);
        x = scaner.nextInt();

        if (x == 0) {
            System.out.println("Silnia 0 = 1!");
        } else if (x > 0) {
            int suma = 1;
            for (int i = 1; i <= x; i++) {
                suma *= i;
            }
            System.out.println(x + "!" + " = " + suma);
        } else {
            System.out.println("Blad! Liczba jest ujemna!");
        }
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Zad 2 silnia rekurencyjnie
import java.util.Scanner;

public class Main1 {
    
    public static void main(String[] args) {
        int n;
        Scanner klaw=new Scanner(System.in);
        System.out.print("n = ");
        n=klaw.nextInt();
        int wynik = 0;
        if (n > 0){
            wynik=silnia(n);
            System.out.print(n);
            System.out.print("! = ");
            System.out.println(wynik);
        } else {
            System.out.println("Blad! Liczba jest ujemna!");
        }

    }

    static int silnia(int n){
        if(n>1)
            return n*silnia(n-1);
        else
            return 1;
    }

}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Zad 3
import java.util.Scanner;
import static java.lang.Math.*;
public class Main1 {

    public static void main(String[] args) {
        int x;
        double precyzja = 0, suma = 0, w1 = 0, w2 = 0;
        Scanner scaner = new Scanner(System.in);

        System.out.print("x = ");
        x = scaner.nextInt();
        System.out.print("Precyzja = ");
        precyzja = scaner.nextDouble();


        while (abs(w1 - w2)<precyzja)
        {
            
        }
        // cos(x) = 1 − x2/2! + x4/4! − x6/6! + . . .

        abs(x);


        // dzielnik = 0,0001
        // |wynik1 - wynik2| < dzielnik

        // System.exit(0);






        if (x > 0){
            int wynik=silnia(x);
            System.out.println(wynik);
        }

        System.out.println("cos(x) = ");
    }

    static int silnia(int n){
        if(n>1)
            return n*silnia(n-1);
        else
            return 1;
    }

}



////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////// COŚ
import java.util.Scanner;
import static java.lang.Math.*;

public class Main2 {

    static int silnia(int n) {
        if (n > 1)
            return n * silnia(n - 1);
        else
            return 1;
    }
    static double potega(double x, int n) {
        double wynik = 1;
        for (int i = 0; i < n; i++)
            wynik *= x;
        return wynik;
    }

    public static void main(String[] args) {
        int n, licznik = 0;
        double x0, wyraz, wynik = 0;
        Scanner scanner = new Scanner(System.in);
        System.out.print("x = ");
        x0 = scanner.nextDouble();
        System.out.print("Precyzja / Ilosc wyrazow w szeregu = ");
        n = scanner.nextInt();

        while (licznik <= n){
            if (licznik % 2 == 0)
                wyraz = -1;
            else
                wyraz = 1;
            wyraz = wyraz * potega(x0, 2*licznik+1) / silnia(2*licznik+1);
            wynik += wyraz;
            licznik++;

        }
        System.out.printf("cos(x) = " + wynik);


    }

}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Kalkulator systemów liczbowych
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        char x;
        String bin, dec, hex;

        Scanner s = new Scanner(System.in);

        while (true) {
            System.out.println("");
            System.out.println("    MENU GLOWNE");
            System.out.println("-------------------");
            System.out.println("1. Z systemu binarnego");
            System.out.println("2. Z systemu dziesietnego");
            System.out.println("3. Z systemu heksodecymalnego");
            System.out.println("4. Koniec progromu");
            System.out.println("------------------");
            System.out.println("Podpowiedz: Nacisnij klawisz odpowiadajacy cyfrom: 1, 2, 3 lub 4");
            System.out.println();
            x = s.next().charAt(0);

            switch (x) {
            case '1':
                System.out.println("1. Z systemu binarnego, podaj liczbe:");
                // pobranie bin zamiana bin na dec i hex i wyswietlenie bin dec i hex
                try {
                    bin = s.next();
                    dec = Integer.toString(Integer.parseInt(bin, 2));
                    hex = Integer.toHexString(Integer.parseInt(bin, 2));
                    System.out.println("Liczba binarna: " + bin);
                    System.out.println("Liczba dziesietna: " + dec);
                    System.out.println("Liczba heksodecymalna: " + hex);
                } catch (Exception e) {
                    System.out.println("Niepoprawna liczba");
                }
                break;
            case '2':
                System.out.println("2. Z systemu dziesietnego, podaj liczbe:");
                // pobranie dec zamiana dec na bin i hex i wyswietlenie bin dec i hex
                try {
                    dec = s.next();
                    bin = Integer.toBinaryString(Integer.parseInt(dec));
                    hex = Integer.toHexString(Integer.parseInt(dec));
                    System.out.println("Liczba binarna: " + bin);
                    System.out.println("Liczba dziesietna: " + dec);
                    System.out.println("Liczba heksodecymalna: " + hex);
                } catch (Exception e) {
                    System.out.println("Niepoprawna liczba");
                }
                break;
            case '3':
                System.out.println("3. Z systemu heksodecymalnego, podaj liczbe:");
                // pobranie hex zamiana hex na bin i dec i wyswietlenie bin dec i hex
                try {
                    hex = s.next();
                    bin = Integer.toBinaryString(Integer.parseInt(hex, 16));
                    dec = Integer.toString(Integer.parseInt(hex, 16));
                    System.out.println("Liczba binarna: " + bin);
                    System.out.println("Liczba dziesietna: " + dec);
                    System.out.println("Liczba heksodecymalna: " + hex);
                } catch (Exception e) {
                    System.out.println("Niepoprawna liczba");
                }
                break;
            case '4':
                System.exit(0);
                break;

            default:
                System.out.println("Podaj wartosc 1, 2, 3 lub 4!");
                System.out.println();
                s.nextLine();
                break;
            }
        }
    }
}


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////
package main;

import java.util.Scanner;

public class main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("Podaj liczbe całkowita: ");
        int liczba = scanner.nextInt();
        // obliczanie sum
        int suma = 0, parzyste = 0, p_dzielnik = 0, nieparzyste = 0, np_dzielnik = 0;
        while (liczba > 0) {
            suma += liczba % 10;
            if (liczba % 2 == 0) {
                parzyste += liczba % 10;
                p_dzielnik++;
            } else {
                nieparzyste += liczba % 10;
                np_dzielnik++;
            }
            liczba /= 10;
        }
        // stosunek średniej arytmetycznej cyfr parzystych do średniej arytmetycznej
        // cyfr nieparzystych
        System.out.println("Suma cyfr: " + suma);
        System.out.println("Suma cyfr parzystych: " + parzyste);
        System.out.println("Suma cyfr nieparzystych: " + nieparzyste);
        System.out.println("Srednia arytmetyczna cyfr parzystych: " + (double) parzyste / p_dzielnik);
        System.out.println("Srednia arytmetyczna cyfr nieparzystych: " + (double) nieparzyste / np_dzielnik);
        System.out.println(
                "Stosunek średniej arytmetycznej cyfr parzystych do średniej arytmetycznej cyfr nieparzystych: "
                        + (double) parzyste / nieparzyste);
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////
package main;

import java.util.Scanner;

public class main2 {
    public static void main(String[] args) {
        // Napisać program, dla podanej liczby całkowitej wyświetla jej dzielniki.
        Scanner scanner = new Scanner(System.in);
        System.out.println("Podaj liczbę całkowitą: ");
        int number = scanner.nextInt();
        for (int i = 1; i <= number; i++) {
            if (number % i == 0) {
                System.out.print(i + " ");
            }
        }
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////// Silnia

package main;

import java.security.Principal;
import java.util.Scanner;

public class main3 {
    public static void main(String[] args) {
        // Napisać program, który sprawdza, czy podana liczba całkowita n, n > 1, jest
        // liczbą pierwszą
        Scanner scanner = new Scanner(System.in);
        System.out.println("Podaj liczbę: ");
        int number = scanner.nextInt();
        int i = 2;
        if (number > 1) {
            while (i < number) {
                if (number % i == 0) {
                    System.out.println("Liczba nie jest liczbą pierwszą");
                    break;
                }
                i++;
            }
            if (i == number) {
                System.out.println("Liczba jest liczbą pierwszą");
            }
        } else {
            System.out.println("Liczba nie jest liczbą pierwszą");
        }
    }

}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////// NWD
package main;

import java.util.Scanner;

public class main2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Podaj liczbę");
        int a = scanner.nextInt();
        System.out.println("Podaj liczbę");
        int b = scanner.nextInt();

        while (a != b) {
            if (a > b) {
                a = a - b;
            } else {
                b = b - a;
            }
        }
        System.out.println("NWD = " + a);
        scanner.close();
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////// Fibonaci
package main;

import java.util.Scanner;

public class main3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Podaj n");
        int n = scanner.nextInt();
        if (n < 0) {
            System.out.println("Nieprawidłowe dane");
        } else {
            System.out.println("Wynik iteracyjny: " + fibonacciIter(n));
            System.out.println("Wynik rekurencyjny: " + fibonacciRec(n));
        }
        scanner.close();
    }

    public static int fibonacciIter(int n) {
        int a = 0;
        int b = 1;
        int c = 0;
        if (n == 0) {
            return a;
        } else if (n == 1) {
            return b;
        } else {
            for (int i = 2; i <= n; i++) {
                c = a + b;
                a = b;
                b = c;
            }
            return c;
        }
    }

    public static int fibonacciRec(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else {
            return fibonacciRec(n - 1) + fibonacciRec(n - 2);
        }
    }

}



////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Podaj a:");
        int a = scanner.nextInt();
        System.out.println("Podaj b:");
        int b = scanner.nextInt();
        System.out.println("Podaj h:");
        int c = scanner.nextInt();
        double d = 3.14;
        pole(a);
        pole(a, b);
        pole(a, d);
        pole(a, b, c);
        scanner.close();
    }

    public static void pole(int a) {
        System.out.println("Pole kwadratu wynosi: " + a * a);
    }

    public static void pole(int a, int b) {
        System.out.println("Pole prostokata wynosi: " + a * b);
    }

    public static void pole(int a, double d) {
        System.out.println("Pole kola wynosi: " + d * a * a);
    }

    public static void pole(int a, int b, int c) {
        System.out.println("Pole trojkata wynosi: " + (a + b + c) / 2);
    }

}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import java.util.Scanner;

public class main2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Podaj wyraz:");
        String wyraz = scanner.nextLine();
        System.out.println("Podaj prefiks:");
        String prefiks = scanner.nextLine();
        startsWith(wyraz, prefiks);
        System.out.println(startsWith(wyraz, prefiks));
        System.out.println(startsWith("Alibaba", "Ali"));
        System.out.println(startsWith("Alibaba", "Alibaba"));
        System.out.println(startsWith("Kot", "Pies"));
        scanner.close();
    }

    public static boolean startsWith(String str1, String str2) {
        if (str1.length() < str2.length()) {
            return false;
        }
        for (int i = 0; i < str2.length(); i++) {
            if (str1.charAt(i) != str2.charAt(i)) {
                return false;
            }
        }
        return true;
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import java.util.Scanner;

public class Main3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // System.out.println("Podaj liczbe:");
        // String liczba = scanner.nextLine();
        // System.out.println(strToInt(liczba));
        System.out.println(strToInt("-12"));
        System.out.println(strToInt("+12"));
        System.out.println(strToInt("0001"));
        System.out.println(strToInt("991-234-23"));
        System.out.println(strToInt("+zonk"));
        System.out.println(strToInt(""));
        System.out.println(strToInt("-12e5"));
        System.out.println(strToInt("-12e-5"));
        // strToInt("-12") -> -12
        // strToInt("+12") -> 12
        // strToInt("0001") -> 1
        // strToInt("991-234-23") -> 991
        // strToInt("+zonk") -> 0
        // strToInt("") -> 0
        // strToInt("-12e5") -> -1200000
        // strToInt("-12e-5") -> -12, bo int nie double
        // jeśli po ciągu oznaczającum liczbe występuje e to znaczy że trzeba pomnożyć
        // przez 10 do potędi liczby po znaku e i zamienić na inta
        // jeśli napotka na inne znaki niż 1,2,3,4,5,6,7,8,9,0 to zwraca wynik resulut
        scanner.close();
    }

    public static int strToInt(String str) {
        int result = 0, power = 0;
        int sign = 1;
        int i = 0;

        if (str.length() == 0) {
            return 0;
        }

        if (str.charAt(0) == '-') {
            sign = -1;
            i = 1;
        } else if (str.charAt(0) == '+') {
            i = 1;
        }

        for (; i < str.length(); i++) {
            if (str.charAt(i) >= '0' && str.charAt(i) <= '9') {
                result = result * 10 + (str.charAt(i) - '0');
            } else if (str.charAt(i) == 'e') {
                i++;
                for (; i < str.length(); i++) {
                    if (str.charAt(i) >= '0' && str.charAt(i) <= '9') {
                        power = power * 10 + (str.charAt(i) - '0');
                    } else {
                        break;
                    }
                }
                return result * sign * (int) Math.pow(10, power);
            } else {
                return result * sign;
            }
        }
        return result * sign;
    }
}


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////// Tablice i random
import java.util.Scanner;
import java.util.Arrays;
import java.util.Random;

public class main1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] tablica = new int[10];
        // losowe liczby
        Random random = new Random();
        for (int i = 0; i < tablica.length; i++) {
            tablica[i] = random.nextInt(20) - 10;
        }
        System.out.println(Arrays.toString(tablica));
        // wyznaczy najmniejszy oraz największy element w tablicy
        int min = tablica[0];
        int max = tablica[0];
        for (int i = 0; i < tablica.length; i++) {
            if (tablica[i] < min) {
                min = tablica[i];
            }
            if (tablica[i] > max) {
                max = tablica[i];
            }
        }
        System.out.println("Najmniejszy element tablicy to: " + min);
        System.out.println("Najwiekszy element tablicy to: " + max);

        // wyznaczy średnią arytmetyczną elementów tablicy
        int suma = 0;
        for (int i = 0; i < tablica.length; i++) {
            suma += tablica[i];
        }
        System.out.println("Srednia arytmetyczna tablicy to: " + suma / tablica.length);

        // wyznaczy ile elementów jest mniejszych, ile większych od średniej
        int licznikmin = 0;
        int licznikmax = 0;
        for (int i = 0; i < tablica.length; i++) {
            if (tablica[i] < suma / tablica.length) {
                licznikmin++;
            }
            if (tablica[i] > suma / tablica.length) {
                licznikmax++;
            }
        }

        System.out.println("Liczba elementow mniejszych od sredniej arytmetycznej to: " + licznikmin);
        System.out.println("Liczba elementow wiekszych od sredniej arytmetycznej to: " + licznikmax);

        // wypisze na ekranie zawartość tablicy w odwrotnej kolejności, tj. od
        // ostatniego do pierwszego
        System.out.print("Tablica odwrotnie: ");
        for (int i = 0; i < tablica.length; i++) {
            System.out.print(tablica[tablica.length - 1 - i] + " ");
        }

        scanner.close();
    }

}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////// Tablice i random za pomocą math
import java.util.Scanner;
import java.util.Arrays;
import java.util.Random;

public class main2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] tablica = new int[20];
        // random math
        for (int i = 0; i < tablica.length; i++) {
            tablica[i] = (int) (Math.random() * 10);
        }
        System.out.println(Arrays.toString(tablica));
        // random random
        Random random = new Random();
        for (int i = 0; i < tablica.length; i++) {
            tablica[i] = random.nextInt(10);
        }
        System.out.println(Arrays.toString(tablica));

        int licznik = 0;
        for (int i = 1; i <= 10; i++) {
            for (int j = 0; j < tablica.length; j++) {
                if (i == tablica[j]) {
                    licznik++;
                }
            }
            System.out.println(i + " razy " + licznik);
            licznik = 0;

        }

        scanner.close();
    }

}


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import java.util.Scanner;
import java.util.Arrays;
import java.util.Random;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int[] array = new int[1000];

        Random random = new Random();
        for (int i = 0; i < array.length; i++) {
            array[i] = random.nextInt(1000);
        }

        int[] array2 = array.clone();
        System.out.println("\nTablica nieposortowana:");
        System.out.println(Arrays.toString(array2));
        System.out.println("Bubble sort - Sortowanie babelkowe: ");
        long startTime = System.currentTimeMillis();
        bubbleSort(array2);
        long endTime = System.currentTimeMillis();
        long duration = (endTime - startTime);
        System.out.println(Arrays.toString(array2));
        System.out.println("Czas wykonania: " + duration + " ms");

        array2 = array.clone();
        System.out.println("\nTablica nieposortowana:");
        System.out.println(Arrays.toString(array2));
        System.out.println("Selection sort - Sortowanie przez wybor: ");
        startTime = System.currentTimeMillis();
        selectionSort(array2);
        endTime = System.currentTimeMillis();
        duration = (endTime - startTime);
        System.out.println(Arrays.toString(array2));
        System.out.println("Czas wykonania: " + duration + " ms");

        array2 = array.clone();
        System.out.println("\nTablica nieposortowana:");
        System.out.println(Arrays.toString(array2));
        System.out.println("Insertion sort - Sortowanie przez wstawianie: ");
        startTime = System.currentTimeMillis();
        insertionSort(array2);
        endTime = System.currentTimeMillis();
        duration = (endTime - startTime);
        System.out.println(Arrays.toString(array2));
        System.out.println("Czas wykonania: " + duration + " ms");

        array2 = array.clone();
        System.out.println("\nTablica nieposortowana:");
        System.out.println(Arrays.toString(array2));
        System.out.println("Merge sort - Sortowanie przez scalanie: ");
        startTime = System.currentTimeMillis();
        mergeSort(array2, array2.length);
        endTime = System.currentTimeMillis();
        duration = (endTime - startTime);
        System.out.println(Arrays.toString(array2));
        System.out.println("Czas wykonania: " + duration + " ms");

        array2 = array.clone();
        System.out.println("\nTablica nieposortowana:");
        System.out.println(Arrays.toString(array2));
        System.out.println("Quick sort - Sortowanie szybkie: ");
        startTime = System.currentTimeMillis();
        quickSort(array2, 0, array2.length - 1);
        endTime = System.currentTimeMillis();
        duration = (endTime - startTime);
        System.out.println(Arrays.toString(array2));
        System.out.println("Czas wykonania: " + duration + " ms");

        scanner.close();
    }

    public static void bubbleSort(int[] array) {
        int temp;
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array.length - i - 1; j++) {
                if (array[j] > array[j + 1]) {
                    temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }

    }

    public static void selectionSort(int[] array) {
        for (int i = 0; i < array.length; i++) {
            int min = i;
            for (int j = i + 1; j < array.length; j++) {
                if (array[j] < array[min]) {
                    min = j;
                }
            }
            int temp = array[i];
            array[i] = array[min];
            array[min] = temp;
        }
    }

    public static void insertionSort(int[] array) {
        int temp, j;
        for (int i = 1; i < array.length; i++) {
            temp = array[i];
            for (j = i - 1; j >= 0 && array[j] > temp; j--) {
                array[j + 1] = array[j];
            }
            array[j + 1] = temp;

            // j = i - 1;
            // while (j >= 0 && array[j] > temp) {
            // array[j + 1] = array[j];
            // j--;
            // }
            // array[j + 1] = temp;
        }
    }

    public static void mergeSort(int[] array, int n) {
        if (n < 2) {
            return;
        }
        int mid = n / 2;
        int[] left = new int[mid];
        int[] right = new int[n - mid];

        for (int i = 0; i < mid; i++) {
            left[i] = array[i];
        }

        for (int i = mid; i < n; i++) {
            right[i - mid] = array[i];
        }
        mergeSort(left, mid);
        mergeSort(right, n - mid);
        merge(array, left, right, mid, n - mid);

    }

    public static void merge(
            int[] a, int[] l, int[] r, int left, int right) {

        int i = 0, j = 0, k = 0;
        while (i < left && j < right) {
            if (l[i] <= r[j]) {
                a[k++] = l[i++];
            } else {
                a[k++] = r[j++];
            }
        }
        while (i < left) {
            a[k++] = l[i++];
        }
        while (j < right) {
            a[k++] = r[j++];
        }
    }

    public static void quickSort(int[] array, int left, int right) {
        int v = array[(left + right) / 2];
        int i, j, x;
        i = left;
        j = right;
        while (array[i] < v) {
            i++;
        }
        while (array[j] > v) {
            j--;
        }
        do {
            if (i <= j) {
                x = array[i];
                array[i] = array[j];
                array[j] = x;
                i++;
                j--;
            }
        } while (i <= j);
        if (j > left) {
            quickSort(array, left, j);
        }
        if (i < right) {
            quickSort(array, i, right);
        }
    }

}

// Liczby if (tab = względnie pierwsze (NWD)): + else . dla tablicy [n][n]
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int n = 0;
        while (n <= 0) {
            System.out.println("Enter the number of elements in the array:");
            n = scanner.nextInt();
        }

        boolean[][] array = new boolean[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // System.out.print(i + " " + j);
                if (NWD(i + 1, j + 1) == 1) {
                    array[i][j] = true;
                } else {
                    array[i][j] = false;
                }
                // System.out.print(array[i][j] + " ");
                if (array[i][j]) {
                    System.out.print("+ ");
                } else {
                    System.out.print(". ");
                }
            }
            System.out.println();
        }

        scanner.close();
    }

    // NWD
    public static int NWD(int a, int b) {
        if (b == 0)
            return a;
        return NWD(b, a % b);
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////// Emerytura
import java.util.Scanner;
import java.io.*;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        emerytura("emerytura.txt");

        scanner.close();
    }

    public static void emerytura(String nazwaPliku) {
        File file = new File(nazwaPliku);
        boolean exists = file.exists();
        if (exists) {
            System.out.println("Plik istnieje");
        } else {
            System.out.println("Plik nie istnieje");
        }
        try {
            FileReader fileReader = new FileReader(file);
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            String line = bufferedReader.readLine();
            while (line != null) {
                String[] split = line.split(" ");
                String imie = split[0];
                String nazwisko = split[1];
                String plec = split[2];
                int wiek = Integer.parseInt(split[3]);
                int latDoEmerytury = 0;
                if (plec.equals("M")) {
                    latDoEmerytury = 65 - wiek;
                    System.out.println(nazwisko + " " + imie + " " + latDoEmerytury);
                    // zapisz dane do pliku menzczyzni.txt
                    FileWriter fileWriter = new FileWriter("mezczyzni.txt", true);
                    BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
                    bufferedWriter.write(nazwisko + " " + imie + " " + latDoEmerytury + "\n");
                    bufferedWriter.close();
                } else {
                    latDoEmerytury = 60 - wiek;
                    System.out.println(nazwisko + " " + imie + " " + latDoEmerytury);
                    // zapisz dane do pliku kobiety.txt
                    FileWriter fileWriter = new FileWriter("kobiety.txt", true);
                    BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
                    bufferedWriter.write(nazwisko + " " + imie + " " + latDoEmerytury + "\n");
                    bufferedWriter.close();
                }
                line = bufferedReader.readLine();
            }
            bufferedReader.close();
        } catch (FileNotFoundException ex) {
            System.out.println("Plik nie istnieje");
        } catch (IOException ex) {
            System.out.println("Błąd odczytu");
        }
    }
}


/////////////////////////////////////// Klasy 
// W main1.java
import java.util.Scanner;

public class main1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Podaj pierwsza liczbe: ");
        MyNumber a = new MyNumber(scanner.nextInt());
        System.out.print("Podaj druga liczbe: ");
        MyNumber b = new MyNumber(scanner.nextInt());

        System.out.println("Suma: " + a.add(a.myNymber, b.myNymber));
        System.out.println("Roznica: " + a.subtract(a.myNymber, b.myNymber));
        System.out.println("Pierwiastek: " + a.sqrt());
        System.out.println("Potega: " + a.pow(a.myNymber, b.myNymber));
        System.out.println("Czy liczba jest parzysta: " + a.isEven());
        System.out.println("Czy liczba jest nieparzysta: " + a.isOdd());

        System.out.println("");

        System.out.println("Pole prostokata: " + new Prostokat(a.myNymber, b.myNymber).pole());
        System.out.println("Obwod prostokata: " + new Prostokat(a.myNymber, b.myNymber).obwod());
        System.out.println("Przekatna prostokata: " + new Prostokat(a.myNymber, b.myNymber).przekatna());

        scanner.close();
    }
}

	
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// W MyNumber.java
public class MyNumber {
    int myNymber;

    public MyNumber(int myNymber) {
        this.myNymber = myNymber;
    }

    public boolean isOdd() {
        if (myNymber % 2 == 0) {
            return false;
        } else {
            return true;
        }
    }

    public boolean isEven() {
        if (myNymber % 2 == 0) {
            return true;
        } else {
            return false;
        }
    }

    public double sqrt() {
        return Math.sqrt(myNymber);
    }

    public double pow(int n, int m) {
        int result = 1;
        for (int i = 0; i < m; i++) {
            result *= n;
        }
        return result;
    }

    public double add(double a, double b) {
        return a + b;
    }

    public double subtract(double a, double b) {
        return a - b;
    }
}


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// W Prostakat.java
public class Prostokat {
    public int a, b;

    public Prostokat(int a, int b) {
        this.a = a;
        this.b = b;
    }

    public int pole() {
        return a * b;
    }

    public int obwod() {
        return 2 * (a + b);
    }

    public double przekatna() {
        return Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2));
    }
}


//////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////
// Zamówienia projekt

Pozycja.java
import java.io.*;

public class Pozycja implements Serializable {
    public String nazwaTowaru;
    public int ileSztuk;
    public double cena;

    public Pozycja(String nazwaTowaru, int ileSztuk, double cena) {
        this.nazwaTowaru = nazwaTowaru;
        this.ileSztuk = ileSztuk;
        this.cena = cena;
    }

    public double obliczWartosc() {
        return ileSztuk * cena;
    }

    public String toString() {
        return String.format(nazwaTowaru + " " + cena + " zl " + ileSztuk + " szt. " + obliczWartosc() + " zl");
    }

    public double obliczWartoscZRabatem() {
        double wartosc = obliczWartosc();
        if (ileSztuk >= 20) {
            wartosc = wartosc * 0.85;
        } else if (ileSztuk >= 10) {
            wartosc = wartosc * 0.9;
        } else if (ileSztuk >= 5) {
            wartosc = wartosc * 0.95;
        }
        return wartosc;
    }
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Zamowienie.java
import java.util.ArrayList;
import java.io.*;

public class Zamowienie implements Serializable {
    ArrayList<Pozycja> pozycje = new ArrayList<Pozycja>();
    // Tabliza zmówień
    ArrayList<Zamowienie> zamowienia = new ArrayList<Zamowienie>();

    public void dodajPozycje(Pozycja p) {
        boolean dodano = false;
        for (Pozycja pozycja : pozycje) {
            if (pozycja.nazwaTowaru.equals(p.nazwaTowaru)) {
                pozycja.ileSztuk += p.ileSztuk;
                dodano = true;
            }
        }
        if (!dodano) {
            pozycje.add(p);
        }
    }

    public int ileSztuk() {
        int ileSztuk = 0;
        for (Pozycja pozycja : pozycje) {
            ileSztuk += pozycja.ileSztuk;
        }
        return ileSztuk;
    }

    public double obliczWartosc() {
        double wartosc = 0;
        for (Pozycja pozycja : pozycje) {
            wartosc += pozycja.obliczWartosc();
        }
        if (ileSztuk() >= 20) {
            wartosc = wartosc * 0.85;
        } else if (ileSztuk() >= 10) {
            wartosc = wartosc * 0.9;
        } else if (ileSztuk() >= 5) {
            wartosc = wartosc * 0.95;
        }
        return wartosc;
    }

    public double rabat() {
        double wartosc = 0;
        for (Pozycja pozycja : pozycje) {
            wartosc += pozycja.obliczWartosc();
        }
        if (ileSztuk() >= 20) {
            wartosc = wartosc * 0.15;
        } else if (ileSztuk() >= 10) {
            wartosc = wartosc * 0.1;
        } else if (ileSztuk() >= 5) {
            wartosc = wartosc * 0.05;
        }
        return wartosc;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (Pozycja p : pozycje) {
            sb.append(p.toString() + "\n");
        }
        sb.append("Wartosc zamowienia: " +

                String.format("%.2f", obliczWartosc())
                + " zl" + ", rabat: " + rabat() + " zl");
        return sb.toString();
    }

    public void usunPozycje(int indeks) {
        pozycje.remove(indeks);
    }

    public Pozycja pobierzPozycje(int indeks) {
        return pozycje.get(indeks);
    }

    public void edytujPozycje(int indeks, Pozycja p) {
        pozycje.set(indeks, p);
    }
}

Main.java
import java.util.Scanner;
import java.util.ArrayList;
import java.io.*;

public class Main {
    public static void zapiszZamowienia(ArrayList<Zamowienie> zamowienia) {
        try {
            FileOutputStream fos = new FileOutputStream("zamowienia.txt");
            ObjectOutputStream oos = new ObjectOutputStream(fos);
            oos.writeObject(zamowienia);
            oos.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void odczytajZPliku() {
        try {
            ObjectInputStream ois = new ObjectInputStream(new FileInputStream("zamowienia.txt"));

            ArrayList<Zamowienie> zamowienia = (ArrayList<Zamowienie>) ois.readObject();

            for (Zamowienie z : zamowienia) {
                System.out.println(z);
            }

        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Pozycje
        System.out.println("==============================");
        Pozycja p1 = new Pozycja("Chleb", 5, 3.5);
        System.out.println(p1);
        System.out.println("Wartosc pozycji z rabatem: " + p1.obliczWartoscZRabatem() + " zl");
        System.out.println("==============================");
        Pozycja p2 = new Pozycja("Cukier", 3, 4);
        System.out.println(p2);
        System.out.println("Wartosc pozycji z rabatem: " + p2.obliczWartoscZRabatem() + " zl");
        System.out.println("==============================");
        Pozycja p = new Pozycja("Mleko", 20, 2.5);
        System.out.println(p);
        System.out.println("Wartosc pozycji z rabatem: " + p.obliczWartoscZRabatem() + " zl");

        // Zamowienie
        System.out.println("==============================");
        System.out.println("==============================");
        Zamowienie z = new Zamowienie();
        z.dodajPozycje(p1);
        z.dodajPozycje(p2);
        z.dodajPozycje(p1);
        System.out.println(z);
        System.out.println("==============================");
        Zamowienie z2 = new Zamowienie();
        z2.dodajPozycje(p);
        z2.dodajPozycje(p);
        System.out.println(z2);
        // z.usunPozycje(0);
        // System.out.println(z);
        // System.out.println("==============================");
        // Pozycja p3 = z.pobierzPozycje(0);
        // System.out.println(p3);
        // System.out.println("==============================");
        // z.edytujPozycje(0, p2);
        // System.out.println(z);
        // System.out.println("==============================");
        // System.out.println("Wartosc zamowienia: " + z.obliczWartosc() + " zl");
        // System.out.println("==============================");

        // Tablica zamówień
        ArrayList<Zamowienie> zamowienia = new ArrayList<Zamowienie>();
        zamowienia.add(z);
        zamowienia.add(z2);

        zapiszZamowienia(zamowienia);
        odczytajZPliku();
        scanner.close();
    }

}





//////////////////////////////// Zapisywanie do pliku 

Main.java
import java.util.Scanner;
import java.util.ArrayList;
import java.io.*;

public class Main {
    public static void zapiszZamowienia(ArrayList<Zamowienie> zamowienia) {
        try {
            FileOutputStream fos = new FileOutputStream("zamowienia.txt");
            ObjectOutputStream oos = new ObjectOutputStream(fos);
            oos.writeObject(zamowienia);
            oos.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void odczytajZPliku() {
        try {
            ObjectInputStream ois = new ObjectInputStream(new FileInputStream("zamowienia.txt"));

            ArrayList<Zamowienie> zamowienia = (ArrayList<Zamowienie>) ois.readObject();

            for (Zamowienie z : zamowienia) {
                System.out.println(z);
            }

        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Pozycje
        System.out.println("==============================");
        Pozycja p1 = new Pozycja("Chleb", 5, 3.5);
        System.out.println(p1);
        System.out.println("Wartosc pozycji z rabatem: " + p1.obliczWartoscZRabatem() + " zl");
        System.out.println("==============================");
        Pozycja p2 = new Pozycja("Cukier", 3, 4);
        System.out.println(p2);
        System.out.println("Wartosc pozycji z rabatem: " + p2.obliczWartoscZRabatem() + " zl");
        System.out.println("==============================");
        Pozycja p = new Pozycja("Mleko", 20, 2.5);
        System.out.println(p);
        System.out.println("Wartosc pozycji z rabatem: " + p.obliczWartoscZRabatem() + " zl");

        // Zamowienie
        System.out.println("==============================");
        System.out.println("==============================");
        Zamowienie z = new Zamowienie();
        z.dodajPozycje(p1);
        z.dodajPozycje(p2);
        z.dodajPozycje(p1);
        System.out.println(z);
        System.out.println("==============================");
        Zamowienie z2 = new Zamowienie();
        z2.dodajPozycje(p);
        z2.dodajPozycje(p);
        System.out.println(z2);
        // z.usunPozycje(0);
        // System.out.println(z);
        // System.out.println("==============================");
        // Pozycja p3 = z.pobierzPozycje(0);
        // System.out.println(p3);
        // System.out.println("==============================");
        // z.edytujPozycje(0, p2);
        // System.out.println(z);
        // System.out.println("==============================");
        // System.out.println("Wartosc zamowienia: " + z.obliczWartosc() + " zl");
        // System.out.println("==============================");

        // Tablica zamówień
        ArrayList<Zamowienie> zamowienia = new ArrayList<Zamowienie>();
        zamowienia.add(z);
        zamowienia.add(z2);

        zapiszZamowienia(zamowienia);
        odczytajZPliku();
        scanner.close();
    }

}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Pozycje.java

import java.io.*;

public class Pozycja implements Serializable {
    public String nazwaTowaru;
    public int ileSztuk;
    public double cena;

    public Pozycja(String nazwaTowaru, int ileSztuk, double cena) {
        this.nazwaTowaru = nazwaTowaru;
        this.ileSztuk = ileSztuk;
        this.cena = cena;
    }

    public double obliczWartosc() {
        return ileSztuk * cena;
    }

    public String toString() {
        return String.format(nazwaTowaru + " " + cena + " zl " + ileSztuk + " szt. " + obliczWartosc() + " zl");
    }

    public double obliczWartoscZRabatem() {
        double wartosc = obliczWartosc();
        if (ileSztuk >= 20) {
            wartosc = wartosc * 0.85;
        } else if (ileSztuk >= 10) {
            wartosc = wartosc * 0.9;
        } else if (ileSztuk >= 5) {
            wartosc = wartosc * 0.95;
        }
        return wartosc;
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Zamówienia.java
import java.util.ArrayList;
import java.io.*;

public class Zamowienie implements Serializable {
    ArrayList<Pozycja> pozycje = new ArrayList<Pozycja>();
    // Tabliza zmówień
    ArrayList<Zamowienie> zamowienia = new ArrayList<Zamowienie>();

    public void dodajPozycje(Pozycja p) {
        boolean dodano = false;
        for (Pozycja pozycja : pozycje) {
            if (pozycja.nazwaTowaru.equals(p.nazwaTowaru)) {
                pozycja.ileSztuk += p.ileSztuk;
                dodano = true;
            }
        }
        if (!dodano) {
            pozycje.add(p);
        }
    }

    public int ileSztuk() {
        int ileSztuk = 0;
        for (Pozycja pozycja : pozycje) {
            ileSztuk += pozycja.ileSztuk;
        }
        return ileSztuk;
    }

    public double obliczWartosc() {
        double wartosc = 0;
        for (Pozycja pozycja : pozycje) {
            wartosc += pozycja.obliczWartosc();
        }
        if (ileSztuk() >= 20) {
            wartosc = wartosc * 0.85;
        } else if (ileSztuk() >= 10) {
            wartosc = wartosc * 0.9;
        } else if (ileSztuk() >= 5) {
            wartosc = wartosc * 0.95;
        }
        return wartosc;
    }

    public double rabat() {
        double wartosc = 0;
        for (Pozycja pozycja : pozycje) {
            wartosc += pozycja.obliczWartosc();
        }
        if (ileSztuk() >= 20) {
            wartosc = wartosc * 0.15;
        } else if (ileSztuk() >= 10) {
            wartosc = wartosc * 0.1;
        } else if (ileSztuk() >= 5) {
            wartosc = wartosc * 0.05;
        }
        return wartosc;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (Pozycja p : pozycje) {
            sb.append(p.toString() + "\n");
        }
        sb.append("Wartosc zamowienia: " +

                String.format("%.2f", obliczWartosc())
                + " zl" + ", rabat: " + rabat() + " zl");
        return sb.toString();
    }

    public void usunPozycje(int indeks) {
        pozycje.remove(indeks);
    }

    public Pozycja pobierzPozycje(int indeks) {
        return pozycje.get(indeks);
    }

    public void edytujPozycje(int indeks, Pozycja p) {
        pozycje.set(indeks, p);
    }
}




////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Samochody i podklasy (nazwy plików ja klasy)
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 1 osobowy 1 dostawczy 1 motocykl i 1 maszyna robocza

        Osobowe o1 = new Osobowe("ABC123", "ABC123", "Czerwony", 10000, 10, 10, 10, 4, 5, "diesla");
        Dostawcze d1 = new Dostawcze("ABC123", "ABC123", "Czerwony", 10000, 10, 10, 10, 4, 5, "diesla", "Dostawcze",
                "Ford", "Focus");

        MaszynyRobocze mr1 = new MaszynyRobocze("ABC123", "ABC123", "Czerwony", 10000, 10, 10, 10, 4, 5,
                "benzyna", "Dostawcze",
                "Ford", "Focus", 6, "2.0", 1000);

        Motocykle m1 = new Motocykle("ABC123", "ABC123", "Czerwony", 10000, 10, 10, 10, "Motocykl", "Yamaha",
                "YZF-R6", "elektryczny");

        System.out.println("Wypisz wszystkie dane osobowego: ");
        System.out.println("Nr rejerstracyjny: " + o1.getNumerRejestracyjny());
        System.out.println("Nr VIN: " + o1.getNumerVin());
        System.out.println("Kolor: " + o1.getKolor());
        // 2 miejsca po przecinku cena
        System.out.println("Cena: " + String.format("%.2f", o1.getCena()) + " zl");
        System.out.println("Spalanie: " + o1.getSpalanie() + " l/100km");
        System.out.println("Stan zbiornika paliwa: " + o1.getStanZbiornikaPaliwa() + " l");
        System.out.println("Licznik przejechanych kilometrow: " + o1.getLicznikPrzejechanychKilometrow() + " km");
        System.out.println("Liczba drzwi: " + o1.getLiczbaDrzwi());
        System.out.println("Liczba miejsc: " + o1.getLiczbaMiejsc());
        System.out.println("Silnik: " + o1.getSilnik());
        System.out.println("");

        System.out.println("Stan zbiornika paliwa: " + o1.getStanZbiornikaPaliwa() + " l");
        System.out.println("Licznik przejechanych kilometrow: " + o1.getLicznikPrzejechanychKilometrow() + " km");

        // TANKOWANIE
        System.out.println("");
        System.out.println("Tankujemy osobowego 40 l");
        o1.tankuj(40);
        System.out.println("Stan zbiornika paliwa po zatankowaniu: " + o1.getStanZbiornikaPaliwa() + " l");

        // JEZDZENIE
        System.out.println("");
        System.out.println("Jedzemy osobowego 55 km");
        o1.jedz(55);
        System.out.println("Stan zbiornika paliwa po podrozy: " + o1.getStanZbiornikaPaliwa() + " l");
        System.out.println("Licznik przejechanych kilometrow: " + o1.getLicznikPrzejechanychKilometrow() + " km");

        scanner.close();
    }
}

/////////////////////////////////////////////////////
public class Pojazdy {
    private String numerRejestracyjny;
    private String numerVin;
    private String kolor;
    private double cena;
    private double spalanie;
    private double stanZbiornikaPaliwa;
    private double licznikPrzejechanychKilometrów;

    public Pojazdy(String numerRejestracyjny, String numerVin, String kolor, double cena, double spalanie,
            double stanZbiornikaPaliwa, double licznikPrzejechanychKilometrów) {
        this.numerRejestracyjny = numerRejestracyjny;
        this.numerVin = numerVin;
        this.kolor = kolor;
        this.cena = cena;
        this.spalanie = spalanie;
        this.stanZbiornikaPaliwa = stanZbiornikaPaliwa;
        this.licznikPrzejechanychKilometrów = licznikPrzejechanychKilometrów;
    }

    public String getNumerRejestracyjny() {
        return numerRejestracyjny;
    }

    public void setNumerRejestracyjny(String numerRejestracyjny) {
        this.numerRejestracyjny = numerRejestracyjny;
    }

    public String getNumerVin() {
        return numerVin;
    }

    public void setNumerVin(String numerVin) {
        this.numerVin = numerVin;
    }

    public String getKolor() {
        return kolor;
    }

    public void setKolor(String kolor) {
        this.kolor = kolor;
    }

    public double getCena() {
        return cena;
    }

    public void setCena(double cena) {
        this.cena = cena;
    }

    public double getSpalanie() {
        return spalanie;
    }

    public void setSpalanie(double spalanie) {
        this.spalanie = spalanie;
    }

    public double getStanZbiornikaPaliwa() {
        return stanZbiornikaPaliwa;
    }

    public void setStanZbiornikaPaliwa(double stanZbiornikaPaliwa) {
        this.stanZbiornikaPaliwa = stanZbiornikaPaliwa;
    }

    public double getLicznikPrzejechanychKilometrow() {
        return licznikPrzejechanychKilometrów;
    }

    public void setLicznikPrzejechanychKilometrow(double licznikPrzejechanychKilometrów) {
        this.licznikPrzejechanychKilometrów = licznikPrzejechanychKilometrów;
    }

    public void jedz(double km) {
        this.licznikPrzejechanychKilometrów += km;
        this.stanZbiornikaPaliwa -= km * (this.spalanie) / 100;
        if (this.stanZbiornikaPaliwa < 0) {
            this.stanZbiornikaPaliwa = 0;
        }
    }

    public void tankuj(double litry) {
        this.stanZbiornikaPaliwa += litry;
    }

    public void zmienStanZbiornikaPaliwa(double litry) {
        this.stanZbiornikaPaliwa += litry;
    }

    public void zmienLicznikPrzejechanychKilometrów(double km) {
        this.licznikPrzejechanychKilometrów += km;
    }

    public void zmienCene(double cena) {
        this.cena += cena;
    }

    public void zmienSpalanie(double spalanie) {
        this.spalanie += spalanie;
    }

    public void zmienKolor(String kolor) {
        this.kolor = kolor;
    }

    public void zmienNumerVin(String numerVin) {
        this.numerVin = numerVin;
    }

    public void zmienNumerRejestracyjny(String numerRejestracyjny) {
        this.numerRejestracyjny = numerRejestracyjny;
    }

}

/////////////////////////////////////////////////////////////////


public class Osobowe extends Pojazdy {
    private int liczbaDrzwi;
    private int liczbaMiejsc;
    private String silnik;

    public Osobowe(String numerRejestracyjny, String numerVin, String kolor, double cena, double spalanie,
            double stanZbiornikaPaliwa, double licznikPrzejechanychKilometrów, int liczbaDrzwi, int liczbaMiejsc,
            String silnik) {
        super(numerRejestracyjny, numerVin, kolor, cena, spalanie, stanZbiornikaPaliwa, licznikPrzejechanychKilometrów);
        this.liczbaDrzwi = liczbaDrzwi;
        this.liczbaMiejsc = liczbaMiejsc;
        this.silnik = silnik;
    }

    public int getLiczbaDrzwi() {
        return liczbaDrzwi;
    }

    public void setLiczbaDrzwi(int liczbaDrzwi) {
        this.liczbaDrzwi = liczbaDrzwi;
    }

    public int getLiczbaMiejsc() {
        return liczbaMiejsc;
    }

    public void setLiczbaMiejsc(int liczbaMiejsc) {
        this.liczbaMiejsc = liczbaMiejsc;
    }

    public String getSilnik() {
        return silnik;
    }

    public void setSilnik(String silnik) {
        this.silnik = silnik;
    }

    public void zmienLiczbaDrzwi(int liczbaDrzwi) {
        this.liczbaDrzwi = liczbaDrzwi;
    }

    public void zmienLiczbaMiejsc(int liczbaMiejsc) {
        this.liczbaMiejsc = liczbaMiejsc;
    }

    public void zmienSilnik(String silnik) {
        this.silnik = silnik;
    }
}

///////////////////////////////////////////////////////////////////////

public class Dostawcze extends Osobowe {
    private String typ;
    private String marka;
    private String model;

    public Dostawcze(String numerRejestracyjny, String numerVin, String kolor, double cena, double spalanie,
            double stanZbiornikaPaliwa, double licznikPrzejechanychKilometrów, int liczbaDrzwi, int liczbaMiejsc,
            String silnik, String typ, String marka, String model) {
        super(numerRejestracyjny, numerVin, kolor, cena, spalanie, stanZbiornikaPaliwa, licznikPrzejechanychKilometrów,
                liczbaDrzwi, liczbaMiejsc, silnik);
        this.typ = typ;
        this.marka = marka;
        this.model = model;
    }

    public String getTyp() {
        return typ;
    }

    public void setTyp(String typ) {
        this.typ = typ;
    }

    public String getMarka() {
        return marka;
    }

    public void setMarka(String marka) {
        this.marka = marka;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public void zmienTyp(String typ) {
        this.typ = typ;
    }

    public void zmienMarka(String marka) {
        this.marka = marka;
    }

    public void zmienModel(String model) {
        this.model = model;
    }
}

////////////////////////////////////////////

public class MaszynyRobocze extends Dostawcze {
    private int liczbaKol;
    private String kolatyp;
    private double mocSilnika;

    public MaszynyRobocze(String numerRejestracyjny, String numerVin, String kolor, double cena, double spalanie,
            double stanZbiornikaPaliwa, double licznikPrzejechanychKilometrów, int liczbaDrzwi, int liczbaMiejsc,
            String silnik, String typ, String marka, String model, int liczbaKol, String kolatyp, double mocSilnika) {
        super(numerRejestracyjny, numerVin, kolor, cena, spalanie, stanZbiornikaPaliwa, licznikPrzejechanychKilometrów,
                liczbaDrzwi, liczbaMiejsc, silnik, typ, marka, model);
        this.liczbaKol = liczbaKol;
        this.kolatyp = kolatyp;
        this.mocSilnika = mocSilnika;
    }

    public int getLiczbaKol() {
        return liczbaKol;
    }

    public void setLiczbaKol(int liczbaKol) {
        this.liczbaKol = liczbaKol;
    }

    public String getKolatyp() {
        return kolatyp;
    }

    public void setKolatyp(String kolatyp) {
        this.kolatyp = kolatyp;
    }

    public double getMocSilnika() {
        return mocSilnika;
    }

    public void setMocSilnika(double mocSilnika) {
        this.mocSilnika = mocSilnika;
    }

    public void zmienLiczbaKol(int liczbaKol) {
        this.liczbaKol = liczbaKol;
    }

    public void zmienKolatyp(String kolatyp) {
        this.kolatyp = kolatyp;
    }

    public void zmienMocSilnika(double mocSilnika) {
        this.mocSilnika = mocSilnika;
    }

}

// 

public class Motocykle extends Pojazdy {
    private String typ;
    private String marka;
    private String model;
    private String silnik;

    public Motocykle(String numerRejestracyjny, String numerVin, String kolor, double cena, double spalanie,
            double stanZbiornikaPaliwa, double licznikPrzejechanychKilometrów, String typ, String marka, String model,
            String silnik) {
        super(numerRejestracyjny, numerVin, kolor, cena, spalanie, stanZbiornikaPaliwa, licznikPrzejechanychKilometrów);
        this.typ = typ;
        this.marka = marka;
        this.model = model;
        this.silnik = silnik;
    }

    public String getTyp() {
        return typ;
    }

    public void setTyp(String typ) {
        this.typ = typ;
    }

    public String getMarka() {
        return marka;
    }

    public void setMarka(String marka) {
        this.marka = marka;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public String getSilnik() {
        return silnik;
    }

    public void setSilnik(String silnik) {
        this.silnik = silnik;
    }

    public void zmienTyp(String typ) {
        this.typ = typ;
    }

    public void zmienMarka(String marka) {
        this.marka = marka;
    }

    public void zmienModel(String model) {
        this.model = model;
    }

    public void zmienSilnik(String silnik) {
        this.silnik = silnik;
    }

}
















////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Main.java

// Program do zarządzania finansami - nie wiem są 2 klasy, nie wpadłem na inny pomysł, jest to jakaś hierarchia XD

import java.io.*;
import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    // zapisywanie listy do pliku
    public static void Zapisywanie(ArrayList<Finanse> finanses, String nazwaPliku) throws IOException {
        FileOutputStream fos = new FileOutputStream(nazwaPliku);
        ObjectOutputStream oos = new ObjectOutputStream(fos);
        oos.writeObject(finanses);
        oos.close();
    }

    // wczytywanie listy z pliku
    public static void Odczytywanie(ArrayList<Finanse> finanses, String nazwaPliku) {
        if (new File(nazwaPliku).exists()) {
            try {
                FileInputStream fis = new FileInputStream(nazwaPliku);
                ObjectInputStream ois = new ObjectInputStream(fis);
                ArrayList<Finanse> przychody = (ArrayList<Finanse>) ois.readObject();
                finanses.addAll(przychody);
                ois.close();
            } catch (IOException e) {
                e.printStackTrace();
            } catch (ClassNotFoundException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // Deklaracja finansów - listy przychodów i wydatków
        Zapisz zapisz = new Zapisz();
        ArrayList<Finanse> przychody = new ArrayList<Finanse>();
        ArrayList<Finanse> wydatki = new ArrayList<Finanse>();

        // ================================================================
        // Ile przychodów i wydatków
        Odczytywanie(przychody, "przychody.txt");
        int i = 0;
        for (Finanse przychod : przychody) {
            i++;
        }
        System.out.println("Ilość przychodów: " + i);

        Odczytywanie(wydatki, "wydatki.txt");
        int j = 0;
        for (Finanse wydatek : wydatki) {
            j++;
        }
        System.out.println("Ilość wydatków: " + j);
        // ================================================================

        // Pomocnicze zmienne
        String[] kategoriePrzychody = { "Etat", "Stypendia", "Bierne", "Emerytura / Renta", "Spadek", "Inne" };
        String[] kategorieWydatki = { "Dom", "Jedzenie", "Transport", "Rozrywka", "Ubranie", "Inne" };
        String[] miesiac = { "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12" };
        String[] miesiaceNazwy = { "Stczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień",
                "Wrzesień", "Październik", "Listopad", "Grudzień" };

        System.out.println("-------------------");
        System.out.println("    MENU GLOWNE");
        System.out.println("-------------------");
        System.out.println("1. Dodaj przychod");
        System.out.println("2. Dodaj wydatek");
        System.out.println("3. Generuj raport na koniec miesiaca");
        System.out.println("4. Wyjdz");
        System.out.println("-------------------");
        System.out.println("Wybierz opcje: ");
        try {
            char x = scanner.next().charAt(0);

            switch (x) {
                case '1':
                    System.out.println("Dodaj przychod");
                    System.out.println("-------------------");
                    System.out.println("1. Etat");
                    System.out.println("2. Stypendium");
                    System.out.println("3. Bierne");
                    System.out.println("4. Emerytura / Renta");
                    System.out.println("5. Spadek");
                    System.out.println("6. Inne");
                    System.out.println("-------------------");

                    System.out.println("Wybierz kategorie: ");
                    int kategoriaPrzychodu = scanner.nextInt();

                    System.out.println("Podaj nazwe przychodu: ");
                    String nazwaPrzychodu = scanner.next();

                    System.out.println("Podaj kwote przychodu (np.: 24,99) : ");
                    double kwotaPrzychodu = scanner.nextDouble();

                    System.out.println("Podaj date przychodu (np.: 01.01.2024) : ");
                    String dataPrzychodu = scanner.next();

                    Finanse p1 = new Finanse(kategoriePrzychody[kategoriaPrzychodu - 1], nazwaPrzychodu, kwotaPrzychodu,
                            dataPrzychodu);

                    // objekt agregujacy przychody
                    zapisz.dodajFinanse(p1);
                    // zapis do listy przychodów
                    przychody.add(p1);
                    // zapis do pliku
                    try {
                        Zapisywanie(przychody, "przychody.txt");
                    } catch (IOException e) {
                        e.printStackTrace();
                    }

                    break;
                case '2':
                    System.out.println("Dodaj wydatek");
                    System.out.println("-------------------");
                    System.out.println("1. Dom");
                    System.out.println("2. Jedzenie");
                    System.out.println("3. Transport");
                    System.out.println("4. Rozrywka");
                    System.out.println("5. Ubranie");
                    System.out.println("6. Inne");
                    System.out.println("-------------------");

                    System.out.println("Wybierz kategorie: ");
                    int kategoriaWydatku = scanner.nextInt();

                    System.out.println("Podaj nazwe wydatku: ");
                    String nazwaWydatku = scanner.next();

                    System.out.println("Podaj kwote wydatku (np.: 24,99) : ");
                    double kwotaWydatku = scanner.nextDouble();

                    System.out.println("Podaj date wydatku (np.: 01.01.2024) : ");
                    String dataWydatku = scanner.next();

                    Finanse w1 = new Finanse(kategorieWydatki[kategoriaWydatku - 1], nazwaWydatku, kwotaWydatku,
                            dataWydatku);

                    // objekt agregujacy wydatki
                    zapisz.dodajFinanse(w1);
                    // zapis do listy wydatków
                    wydatki.add(w1);
                    // zapis do pliku
                    try {
                        Zapisywanie(wydatki, "wydatki.txt");
                    } catch (IOException e) {
                        e.printStackTrace();
                    }

                    break;
                case '3':
                    System.out.println("-------------------");
                    System.out.println("Generowanie raportu na koniec miesiaca");
                    System.out.println("Wpisz 1, dla Stycznia, 2 dla Lutego itd.: ");

                    System.out.println("Wybierz miesiac: ");
                    int miesiacWybrany = scanner.nextInt();

                    System.out.println("Wpisz rok (np.: 2020): ");
                    String rokWybrany = scanner.next();

                    System.out.println("-------------------");
                    System.out.println("       RAPORT");
                    System.out.println("-------------------");

                    // Przychody zalerzne od miesiaca i roku
                    System.out.println("Przychody:");
                    double sumaPrzychodow = 0;
                    for (Finanse przychod : przychody) {
                        przychod.wyswietl(miesiac[miesiacWybrany - 1], rokWybrany);
                        sumaPrzychodow += przychod.getKwota(miesiac[miesiacWybrany - 1], rokWybrany);
                    }
                    System.out.println("Suma przychodow: " + String.format("%.2f", sumaPrzychodow) + " zł");
                    System.out.println("-------------------");

                    // Wydatki zalerzne od miesiaca i roku
                    System.out.println("Wydatki:");
                    double sumaWydatkow = 0;
                    for (Finanse wydatek : wydatki) {
                        wydatek.wyswietl(miesiac[miesiacWybrany - 1], rokWybrany);
                        sumaWydatkow += wydatek.getKwota(miesiac[miesiacWybrany - 1], rokWybrany);
                    }
                    System.out.println("Suma wydatkow: " + String.format("%.2f", sumaWydatkow) + " zł");
                    System.out.println("-------------------");

                    // Przychody - Wydatki = Bilans
                    System.out.println("Bilanse na " + miesiaceNazwy[miesiacWybrany - 1] + " wynosi: "
                            + String.format("%.2f", (sumaPrzychodow - sumaWydatkow)) + " zł");
                    System.out.println("-------------------");

                    break;
                case '4':
                    System.out.println("Bay Bay");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Nie ma takiej opcji");
                    break;
            }
        } catch (Exception e) {
            System.out.println("Źle wpisano dane!!!");
        }

        scanner.close();
    }
}

/////////////////////////////////////////////
Finanse.java
import java.io.*;

public class Finanse implements Serializable {
    private String kategoria;
    private String nazwa;
    private double kwota;
    private String data;

    public Finanse(String kategoria, String nazwa, double kwota, String data) {
        this.kategoria = kategoria;
        this.nazwa = nazwa;
        this.kwota = kwota;
        this.data = data;
    }

    public String getKategoria() {
        return kategoria;
    }

    public String setKategoria(String kategoria) {
        return this.kategoria = kategoria;
    }

    public String getNazwa() {
        return nazwa;
    }

    public String setNazwa(String nazwa) {
        return this.nazwa = nazwa;
    }

    public double getKwota() {
        return kwota;
    }

    public double setKwota(double kwota) {
        return this.kwota = kwota;
    }

    public String getData() {
        return data;
    }

    public String setData(String data) {
        return this.data = data;
    }

    public void wyswietl() {
        System.out.println("-------------------");
        System.out.println("Kategoria: " + kategoria);
        System.out.println("Nazwa: " + nazwa);
        System.out.println("Kwota: " + kwota + " zł");
        System.out.println("Data: " + data);
        System.out.println("-------------------");
    }

    public void wyswietl(String miesiac, String rok) {
        if (data.substring(3, 5).equals(miesiac) && data.substring(6, 10).equals(rok)) {
            System.out.println(kategoria + " " + nazwa + " " + data + "  " + String.format("%.2f", kwota) + " zł");

        }
    }

    public double getKwota(String miesiac, String rok) {
        if (data.substring(3, 5).equals(miesiac) && data.substring(6, 10).equals(rok)) {
            return kwota;
        } else {
            return 0;
        }
    }

}

//////////////////////////////////////////////////
Zapisz.java
import java.util.ArrayList;
import java.io.*;

public class Zapisz implements Serializable {
    ArrayList<Finanse> finanse = new ArrayList<Finanse>();

    public void dodajFinanse(Finanse finance) {
        finanse.add(finance);
    }

    public void wyswietlFinanse() {
        for (Finanse finance : finanse) {
            finance.wyswietl();
        }
    }

    public double sumaFinanse() {
        double suma = 0;
        for (Finanse finance : finanse) {
            suma += finance.getKwota();
        }
        return suma;
    }

}





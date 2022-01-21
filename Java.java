// Darmowy program NetBeans
// https://www.programiz.com/java-programming/keywords-identifiers
// 1
public class Nazwa_pliku  {
    public static void main(String[] args) {
        System.out.println("Hello World!");
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



/////////////////////////
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
//////////////////////////
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

//////////
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



import java.util.Scanner;
import java.util.Arrays;
import java.util.Random;

public class main1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] array = new int[1000];
        // losowe liczby
        Random random = new Random();
        for (int i = 0; i < array.length; i++) {
            array[i] = random.nextInt(1000);
        }

        // sortowanie bąbelkowe
        System.out.println(Arrays.toString(array));
        long startTime = System.currentTimeMillis();
        System.out.println(Arrays.toString(bubbleSort(array)));
        long endTime = System.currentTimeMillis();
        long duration = (endTime - startTime);
        System.out.println("Czas wykonania: " + duration + " ms");

        // sortowanie przez wybór
        System.out.println(Arrays.toString(array));
        startTime = System.currentTimeMillis();
        System.out.println(Arrays.toString(selectionSort(array)));
        endTime = System.currentTimeMillis();
        duration = (endTime - startTime);
        System.out.println("Czas wykonania: " + duration + " ms");

        // sortowanie przez wstawianie
        System.out.println(Arrays.toString(array));
        startTime = System.currentTimeMillis();
        System.out.println(Arrays.toString(insertionSort(array)));
        endTime = System.currentTimeMillis();
        duration = (endTime - startTime);
        System.out.println("Czas wykonania: " + duration + " ms");

        // sortowanie przez scalanie
        System.out.println(Arrays.toString(array));
        startTime = System.currentTimeMillis();
        // System.out.println(Arrays.toString(mergeSort(array)));
        endTime = System.currentTimeMillis();
        duration = (endTime - startTime);
        System.out.println("Czas wykonania: " + duration + " ms");

        // sortowanie szybkie
        System.out.println(Arrays.toString(array));
        startTime = System.currentTimeMillis();
        System.out.println(Arrays.toString(quickSort(array)));
        endTime = System.currentTimeMillis();
        duration = (endTime - startTime);
        System.out.println("Czas wykonania: " + duration + " ms");

        scanner.close();
    }

    public static int[] bubbleSort(int[] array) { // sortowanie bąbelkowe
        System.out.println("\n Bubble sort");
        System.out.println("Sortowanie babelkowe");
        int[] array2 = array.clone();
        int temp;
        for (int i = 0; i < array2.length; i++) {
            for (int j = 0; j < array2.length - i - 1; j++) {
                if (array2[j] > array2[j + 1]) {
                    temp = array2[j];
                    array2[j] = array2[j + 1];
                    array2[j + 1] = temp;
                }
            }
        }

        return array2;
    }

    public static int[] selectionSort(int[] array) { // sortowanie przez wybór
        System.out.println("\n Selection sort");
        System.out.println("Sortowanie przez wybor");
        int[] array2 = array.clone();

        int minIndex, temp;
        for (int i = 0; i < array2.length - 1; i++) {
            minIndex = i;
            for (int j = i + 1; j < array2.length; j++) {
                if (array2[j] < array2[minIndex]) {
                    minIndex = j;
                }
            }
            temp = array2[i];
            array2[i] = array2[minIndex];
            array2[minIndex] = temp;
        }
        return array2;
    }

    public static int[] insertionSort(int[] array) { // sortowanie przez wstawianie
        System.out.println("\n Insertion sort");
        System.out.println("Sortowanie przez wstawianie");
        int[] array2 = array.clone();

        int temp, j;
        for (int i = 1; i < array2.length; i++) {
            temp = array2[i];
            for (j = i - 1; j >= 0 && array2[j] > temp; j--) {
                array2[j + 1] = array2[j];
            }
            array2[j + 1] = temp;
        }
        return array2;
    }

// SORT-SCAL(T, p, r):
// JEŚLI p < r:
// q → (p+r)/2
// SORT-SCAL(T, p, q)
// SORT-SCAL(T, q+1, r)
// SCALANIE(T, p, q, r)

    // public static int[] mergeSort(int[] array) { // sortowanie przez scalanie
    //     System.out.println("\n Merge sort");
    //     System.out.println("Sortowanie przez scalanie");
    //     int[] array2 = array.clone();
    //     int[] array3 = new int[array2.length];
    //     mergeSort(array2, array3, 0, array2.length - 1);
    //     return array3;
    // }

    // public static void mergeSort(int[] array) {
    //     if (array.length > 1) {
    //         int middle = array.length / 2;
    //         int[] left = Arrays.copyOfRange(array, 0, middle);
    //         int[] right = Arrays.copyOfRange(array, middle, array.length);
    //         mergeSort(left);
    //         mergeSort(right);
    //         merge(array, left, right);
    //     }
    // }

    public static int[] quickSort(int[] array) { // sortowanie szybkie
        System.out.println("Quick sort");
        System.out.println("Sortowanie szybkie");
        int[] array2 = array.clone();

        for (int i = 0; i < array2.length; i++) {
            int pivot = array2[i];
            int j = i - 1;
            for (int k = i + 1; k < array2.length; k++) {
                if (array2[k] < pivot) {
                    j++;
                    int temp = array2[j];
                    array2[j] = array2[k];
                    array2[k] = temp;
                }
            }
            int temp = array2[j + 1];
            array2[j + 1] = array2[i];
            array2[i] = temp;

        }
        return array2;
    }

}



/////////////////////////////////////////////////////////////////////////////////// sort merge
import java.util.Scanner;
import java.util.Arrays;
import java.util.Random;

public class main2 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int[] array = new int[1000];
        int left = 0;
        int right = array.length - 1;
        // losowe liczby
        Random random = new Random();
        for (int i = 0; i < array.length; i++) {
            array[i] = random.nextInt(1000);
        }

        // merge sort
        System.out.println("\n Merge sort");
        System.out.println("Sortowanie przez scalanie");
        System.out.println(Arrays.toString(array));
        long startTime = System.currentTimeMillis();

        mergeSort(array, left, right);
        System.out.println(Arrays.toString(array));
        long endTime = System.currentTimeMillis();
        long duration = (endTime - startTime);
        System.out.println("Czas wykonania: " + duration + " ms");


        scanner.close();
    }

    public static void mergeSort(int[] array, int left, int right) {

        if (left < right) {
            int middle = (left + right) / 2;
            mergeSort(array, left, middle);
            mergeSort(array, middle + 1, right);
            merge(array, left, middle, right);
        }

    }

    public static int[] merge(int[] array, int left, int middle, int right) {
        int[] array2 = array.clone();
        int[] array3 = new int[array2.length];
        int i = left, j = middle + 1, k = left;
        while (i <= middle && j <= right) {
            if (array2[i] < array2[j]) {
                array3[k] = array2[i];
                i++;
            } else {
                array3[k] = array2[j];
                j++;
            }
            k++;
        }

        while (i <= middle) {
            array3[k] = array2[i];
            i++;
            k++;
        }
        while (j <= right) {
            array3[k] = array2[j];
            j++;
            k++;
        }
        for (int l = left; l <= right; l++) {
            array[l] = array3[l];
        }
        return array;
    }

}

//////////////////////// lol
import java.util.Scanner;
import java.util.Arrays;
import java.util.Random;

public class main1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] array = new int[10];
        // losowe liczby
        Random random = new Random();
        for (int i = 0; i < array.length; i++) {
            array[i] = random.nextInt(1000);
        }


        // sortowanie bąbelkowe
        System.out.println("\nBubble sort");
        System.out.println("Sortowanie babelkowe");
        System.out.println(Arrays.toString(array));
        long startTime = System.currentTimeMillis();
        System.out.println(Arrays.toString(bubbleSort(array)));
        long endTime = System.currentTimeMillis();
        long duration = (endTime - startTime);
        System.out.println("Czas wykonania: " + duration + " ms");

        // sortowanie przez wybór
        System.out.println("\nSelection sort");
        System.out.println("Sortowanie przez wybor");
        System.out.println(Arrays.toString(array));
        startTime = System.currentTimeMillis();
        System.out.println(Arrays.toString(selectionSort(array)));
        endTime = System.currentTimeMillis();
        duration = (endTime - startTime);
        System.out.println("Czas wykonania: " + duration + " ms");

        // sortowanie przez wstawianie
        System.out.println("\nInsertion sort");
        System.out.println("Sortowanie przez wstawianie");
        System.out.println(Arrays.toString(array));
        startTime = System.currentTimeMillis();
        System.out.println(Arrays.toString(insertionSort(array)));
        endTime = System.currentTimeMillis();
        duration = (endTime - startTime);
        System.out.println("Czas wykonania: " + duration + " ms");
        

        // sortowanie przez scalanie
        int left = 0;
        int right = array.length - 1;
        System.out.println("\nMerge sort");
        System.out.println("Sortowanie przez scalanie");
        System.out.println(Arrays.toString(array));
        startTime = System.currentTimeMillis();
        mergeSort(array, left, right);
        System.out.println(Arrays.toString(array));
        endTime = System.currentTimeMillis();
        duration = (endTime - startTime);
        System.out.println("Czas wykonania: " + duration + " ms");

        // sortowanie szybkie
        System.out.println("\nQuick sort");
        System.out.println("Sortowanie szybkie");
        System.out.println(Arrays.toString(array));
        startTime = System.currentTimeMillis();
        System.out.println(Arrays.toString(quickSort(array, array.length - 1)));
        endTime = System.currentTimeMillis();
        duration = (endTime - startTime);
        System.out.println("Czas wykonania: " + duration + " ms");

        scanner.close();
    }

    public static int[] bubbleSort(int[] array) { // sortowanie bąbelkowe
        int[] array2 = array.clone();
        int temp;
        for (int i = 0; i < array2.length; i++) {
            for (int j = 0; j < array2.length - i - 1; j++) {
                if (array2[j] > array2[j + 1]) {
                    temp = array2[j];
                    array2[j] = array2[j + 1];
                    array2[j + 1] = temp;
                }
            }
        }

        return array2;
    }

    public static int[] selectionSort(int[] array) { // sortowanie przez wybór
        int[] array2 = array.clone();

        for(int i = 0; i < array2.length; i++) {
            int min = i;
            for(int j = i + 1; j < array2.length; j++) {
                if(array2[j] < array2[min]) {
                    min = j;
                }
            }
            int temp = array2[i];
            array2[i] = array2[min];
            array2[min] = temp;
        }
        return array2;
    }

    public static int[] insertionSort(int[] array) { // sortowanie przez wstawianie
        int[] array2 = array.clone();

        int temp, j;
        for (int i = 1; i < array2.length; i++) {
            temp = array2[i];
            for (j = i - 1; j >= 0 && array2[j] > temp; j--) {
                array2[j + 1] = array2[j];
            }
            array2[j + 1] = temp;
        }
        return array2;
    }

    public static void mergeSort(int[] array, int left, int right) { // sortowanie przez scalanie

        if (left < right) {
            int middle = (left + right) / 2;
            mergeSort(array, left, middle);
            mergeSort(array, middle + 1, right);
            merge(array, left, middle, right);
        }

    }

    public static int[] merge(int[] array, int left, int middle, int right) {
        int[] array2 = array.clone();
        int[] array3 = new int[array2.length];
        int i = left, j = middle + 1, k = left;
        while (i <= middle && j <= right) {
            if (array2[i] < array2[j]) {
                array3[k] = array2[i];
                i++;
            } else {
                array3[k] = array2[j];
                j++;
            }
            k++;
        }

        while (i <= middle) {
            array3[k] = array2[i];
            i++;
            k++;
        }
        while (j <= right) {
            array3[k] = array2[j];
            j++;
            k++;
        }
        for (int l = left; l <= right; l++) {
            array[l] = array3[l];
        }
        return array;
    }

    public static int[] quickSort(int[] array) { // sortowanie szybkie
        int[] array2 = array.clone();

        for (int i = 0; i < array2.length; i++) {
            int pivot = array2[i];
            int j = i - 1;
            for (int k = i + 1; k < array2.length; k++) {
                if (array2[k] < pivot) {
                    j++;
                    int temp = array2[j];
                    array2[j] = array2[k];
                    array2[k] = temp;
                }
            }
            int temp = array2[j + 1];
            array2[j + 1] = array2[i];
            array2[i] = temp;

        }
        return array2;
    }

}

///
import java.util.Scanner;
import java.util.Arrays;
import java.util.Random;

public class main1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] array = new int[10];
        // losowe liczby
        Random random = new Random();
        for (int i = 0; i < array.length; i++) {
            array[i] = random.nextInt(1000);
        }


        // sortowanie bąbelkowe
        System.out.println("\nBubble sort");
        System.out.println("Sortowanie babelkowe");
        System.out.println(Arrays.toString(array));
        long startTime = System.currentTimeMillis();
        System.out.println(Arrays.toString(bubbleSort(array)));
        long endTime = System.currentTimeMillis();
        long duration = (endTime - startTime);
        System.out.println("Czas wykonania: " + duration + " ms");

        // sortowanie przez wybór
        System.out.println("\nSelection sort");
        System.out.println("Sortowanie przez wybor");
        System.out.println(Arrays.toString(array));
        startTime = System.currentTimeMillis();
        System.out.println(Arrays.toString(selectionSort(array)));
        endTime = System.currentTimeMillis();
        duration = (endTime - startTime);
        System.out.println("Czas wykonania: " + duration + " ms");

        // sortowanie przez wstawianie
        System.out.println("\nInsertion sort");
        System.out.println("Sortowanie przez wstawianie");
        System.out.println(Arrays.toString(array));
        startTime = System.currentTimeMillis();
        System.out.println(Arrays.toString(insertionSort(array)));
        endTime = System.currentTimeMillis();
        duration = (endTime - startTime);
        System.out.println("Czas wykonania: " + duration + " ms");
        

        // sortowanie przez scalanie
        int left = 0;
        int right = array.length - 1;
        System.out.println("\nMerge sort");
        System.out.println("Sortowanie przez scalanie");
        System.out.println(Arrays.toString(array));
        startTime = System.currentTimeMillis();
        mergeSort(array, left, right);
        System.out.println(Arrays.toString(array));
        endTime = System.currentTimeMillis();
        duration = (endTime - startTime);
        System.out.println("Czas wykonania: " + duration + " ms");

        // sortowanie szybkie
        System.out.println("\nQuick sort");
        System.out.println("Sortowanie szybkie");
        System.out.println(Arrays.toString(array));
        startTime = System.currentTimeMillis();
        System.out.println(Arrays.toString(quickSort(array)));
        endTime = System.currentTimeMillis();
        duration = (endTime - startTime);
        System.out.println("Czas wykonania: " + duration + " ms");

        scanner.close();
    }

    public static int[] bubbleSort(int[] array) { // sortowanie bąbelkowe
        int[] array2 = array.clone();
        int temp;
        for (int i = 0; i < array2.length; i++) {
            for (int j = 0; j < array2.length - i - 1; j++) {
                if (array2[j] > array2[j + 1]) {
                    temp = array2[j];
                    array2[j] = array2[j + 1];
                    array2[j + 1] = temp;
                }
            }
        }

        return array2;
    }

    public static int[] selectionSort(int[] array) { // sortowanie przez wybór
        int[] array2 = array.clone();


        for(int i = 0; i < array2.length; i++) {
            int min = i;
            for(int j = i + 1; j < array2.length; j++) {
                if(array2[j] < array2[min]) {
                    min = j;
                }
            }
            int temp = array2[i];
            array2[i] = array2[min];
            array2[min] = temp;
        }
        return array2;
    }

    public static int[] insertionSort(int[] array) { // sortowanie przez wstawianie
        int[] array2 = array.clone();

        int temp, j;
        for (int i = 1; i < array2.length; i++) {
            temp = array2[i];
            for (j = i - 1; j >= 0 && array2[j] > temp; j--) {
                array2[j + 1] = array2[j];
            }
            array2[j + 1] = temp;
        }
        return array2;
    }

    public static void mergeSort(int[] array, int left, int right) { // sortowanie przez scalanie

        if (left < right) {
            int middle = (left + right) / 2;
            mergeSort(array, left, middle);
            mergeSort(array, middle + 1, right);
            merge(array, left, middle, right);
        }

    }

    public static int[] merge(int[] array, int left, int middle, int right) {
        int[] array2 = array.clone();
        int[] array3 = new int[array2.length];
        int i = left, j = middle + 1, k = left;
        while (i <= middle && j <= right) {
            if (array2[i] < array2[j]) {
                array3[k] = array2[i];
                i++;
            } else {
                array3[k] = array2[j];
                j++;
            }
            k++;
        }

        while (i <= middle) {
            array3[k] = array2[i];
            i++;
            k++;
        }
        while (j <= right) {
            array3[k] = array2[j];
            j++;
            k++;
        }
        for (int l = left; l <= right; l++) {
            array[l] = array3[l];
        }
        return array;
    }

    public static int[] quickSort(int[] array) { // sortowanie szybkie
        int[] array2 = array.clone();

        for (int i = 0; i < array2.length; i++) {
            int pivot = array2[i];
            int j = i - 1;
            for (int k = i + 1; k < array2.length; k++) {
                if (array2[k] < pivot) {
                    j++;
                    int temp = array2[j];
                    array2[j] = array2[k];
                    array2[k] = temp;
                }
            }
            int temp = array2[j + 1];
            array2[j + 1] = array2[i];
            array2[i] = temp;

        }
        return array2;
    }

}


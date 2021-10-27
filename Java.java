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






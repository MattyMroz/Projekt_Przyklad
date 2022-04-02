#include <iostream>
using namespace std;

int main()
{
    cout << "Hello world!" << endl;
    return 0;
}

// Zamiana liczby dziesiętnej na binarną
#include <iostream>
using namespace std;

void dec_to_bin(int liczba)
{
	int i=0,tab[31];

	while(liczba) //dopóki liczba będzie różna od zera
	{
		tab[i++]=liczba%2;
		liczba/=2;
	}

	for(int j=i-1;j>=0;j--)
		cout<<tab[j];
}

int main()
{
	int liczba;

	cout<<"Podaj liczbę: ";
	cin>>liczba;

	cout<<liczba<<" po zamianie na postać binarną: ";
	dec_to_bin(liczba);
	cout<<endl;

	return 0;
}


#include <iostream>
using namespace std;

void dec_to_bin(int liczba)
{
	int i=31;
	bool ok=false;
	while(i--)
	{
		//warunek, który pozwoli ominąć początkowe zera
		if(liczba>>i&1&!ok) 
			ok=true;

		if(ok)
			cout<<((liczba>>i)&1);

	}
}

int main()
{
	int liczba;
	cout<<"Podaj liczbę: ";
	cin>>liczba;

	cout<<liczba<<" po zamianie na postać binarną: ";
	dec_to_bin(liczba);
	cout<<endl;

	return 0;
}



// Binarna na dziesiętną
#include <iostream>
#include <cmath>
using namespace std;

void bin_to_dec(string bin){

    int dec, dlugosc, i;
    cin >> bin;
    dec = 0;
    dlugosc = bin.length();
    i = 0;
    do
    {
        cout << bin[ dlugosc - 1 ];
        dec +=( bin[ dlugosc - 1 ] - 48 ) * pow( 2, i );
        i++;
        dlugosc--;
    }
    while( dlugosc > 0 );

    cout << '\n' << dec;
}

int main()
{

    string bin;
    bin_to_dec(bin);

	return 0;
}


// Dziesiętny na szesnastkowy

#include <iostream>
#include <string>
 
using namespace std;
int a, r;
 
int main()
{
 
    cout << "Podaj liczbe w systemie dziesietnym:" << endl;
    cin >> a;
    string hex = ""; //do tej zmiennej będziemy zapisywać kolejne znaki
 
    while (a>0)
    {
        r = a % 16;
        a /= 16;
 
        if (r == 10)
            hex += 'A';
        else if (r == 11)
            hex += 'B';
        else if (r == 12)
            hex += 'C';
        else if (r == 13)
            hex += 'D';
        else if (r == 14)
            hex += 'E';
        else if (r == 15)
            hex += 'F';
        else
            hex += to_string(r); //konwersja zmiennej r z typu int na string
    }
 
    for (int i = hex.length()-1; i >= 0; i--) //wypisanie kolejno od tyłu zawartości zmiennej hex
    {
        cout << hex[i];
    }
 
    return 0;
}


// System rzymski
#include <iostream>
#include <string.h>
 
using namespace std;
const int N = 13;
 
int main()
{
        string rom[N] = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        int dec[N] = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
        int x;
        string lr = "";
 
        cout << "Podaj dowolna liczbe: " << endl;
        cin >> x;
 
        for (int i = 0; i < N; i++)
                while (dec[i] <= x)
                {
                        lr += rom[i];
                        x -= dec[i];
                }
 
        cout << "W notacji rzymskiej to: " << lr << endl;
 return 0;
}



#include <iostream>
#include <string.h>
#include <conio.h>
using namespace std;
string ROM;
int DEC;
char s[81];
unsigned int n;

const char *Symbol[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
const unsigned int Value[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

void welcome();
void clearBuffer();
void testCinDecToRom();
void testCinRomToDec();
bool IntToRom(unsigned int n, char *s, int maxLen);
bool RomToInt(char *s, unsigned int &n);

int main()
{

    char choice;
    for (;;)
    {
        welcome();
        clearBuffer();
        choice = getch();
        switch (choice)
        {
        case '1':
        {
            cout << "1. Z SYSTEMU DZIESIETNEGO NA RZYMSKI" << endl;

            do
            {
                testCinDecToRom();

                if (IntToRom(n, s, 81) == true)
                {
                    cout << ROM << endl;
                }
            } while (IntToRom(n, s, 81) == false);

            break;
        }

        case '2':
        {
            cout << "2. Z SYSTEMU RZYMSKIEGO NA DZIESIETNY" << endl;

            do
            {
                testCinRomToDec();
                if (RomToInt(s, n) == true)
                {
                    cout << DEC << endl;
                }
            } while (RomToInt(s, n) == false);

            break;
        }

        case '3':
            exit(0);
            break;

        default:
            cout << "Nie ma takiej opcji w menu!";
        }
        clearBuffer();
        getchar();
        system("cls");
    }
    return 0;
}

void welcome()
{
    cout << endl;
    cout << "    MENU GLOWNE" << endl;
    cout << "-------------------" << endl;
    cout << "1. Z SYSTEMU DZIESIETNEGO NA RZYMSKI" << endl;
    cout << "2. Z SYSTEMU RZYMSKIEGO NA DZIESIETNY" << endl;
    cout << "3. Koniec progromu" << endl;
    cout << "-------------------" << endl;
    cout << "Podpowiedz: Nacisnij klawisz odpowiadajacy cyfrom: 1, 2 lub 3." << endl;
    cout << endl;
}

void clearBuffer()
{
    cin.clear();
    cin.sync();
}

void testCinDecToRom()
{
    do
    {
        cout << "Podaj poprawna liczbe z przedzialu 1 - 3999:" << endl;
        cin >> n;
        clearBuffer();
    } while (n <= 0 || n > 3999);
}

void testCinRomToDec()
{
    bool ver1, ver2;
    do
    {
        ver1 = false;
        ver2 = false;
        cout << "Podaj poprawna liczbe rzymska:" << endl;
        cin >> s;
        clearBuffer();

        ROM = s;
        size_t position = ROM.find("MMMM");
        if (position != string::npos)
        {
            ver1 = true;
        }
        for (int i = 0; i < ROM.length(); i++)
        {

            if (ROM[i] != 'I' &&
                ROM[i] != 'V' &&
                ROM[i] != 'X' &&
                ROM[i] != 'L' &&
                ROM[i] != 'C' &&
                ROM[i] != 'D' &&
                ROM[i] != 'M')
            {
                ver2 = true;
            }
        }
    } while (ver1 || ver2);
}

bool IntToRom(unsigned int n, char *s, int maxLen)
{
    *s = '\0';
    for (int r = 0; n > 0;)
        if (Value[r] <= n)
        {
            if ((maxLen -= (int)strlen(Symbol[r])) < 0)
                return false;
            strcat(s, Symbol[r]);
            n -= Value[r];
        }
        else
            r++;
    ROM = s;
    return (n == 0) && (*s != '\0');
}

bool RomToInt(char *s, unsigned int &n)
{
    const int Nast[] = {1, 5, 4, 5, 5, 9, 8, 9, 9, 13, 12, 13, 13};
    int k = 256;
    for (int r = n = 0; (r < 13) && (*s != 0); k = (r % 4) ? 1 : 3)
    {
        bool b = false;
        while ((k > 0) && (strncmp(s, Symbol[r], strlen(Symbol[r])) == 0))
        {
            n += Value[r];
            s += strlen(Symbol[r]);
            b = true;
            k--;
        }
        if (b)
            r = Nast[r];
        else
            r++;
    }
    DEC = n;
    return (n > 0) && (*s == 0);
}



//ŹLE	
#include <iostream>
#include <string.h>
#include <conio.h>
using namespace std;

struct Roman_numerals
{
    char rom;
    int dec;
};

Roman_numerals Rome[7] =
    {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}};

void welcome();
void clearBuffer();

int testCinDecToRom();
string decToRom(int x);

string testCinRomToDec();
int rome_to_dec(char x);
void RomToDec(string x);

int main()
{
    char choice;
    for (;;)
    {
        welcome();
        clearBuffer();
        choice = getch();
        switch (choice)
        {
        case '1':
        {
            cout << "1. Z SYSTEMU DZIESIETNEGO NA RZYMSKI" << endl;
            cout << decToRom(testCinDecToRom());
            break;
        }

        case '2':
        {
            cout << "2. Z SYSTEMU RZYMSKIEGO NA DZIESIETNY" << endl;
            RomToDec(testCinRomToDec());
            break;
        }

        case '3':
            exit(0);
            break;

        default:
            cout << "Nie ma takiej opcji w menu!";
        }
        clearBuffer();
        getchar();
        system("cls");
    }
    return 0;
}

void welcome()
{
    cout << endl;
    cout << "    MENU GLOWNE" << endl;
    cout << "-------------------" << endl;
    cout << "1. Z SYSTEMU DZIESIETNEGO NA RZYMSKI" << endl;
    cout << "2. Z SYSTEMU RZYMSKIEGO NA DZIESIETNY" << endl;
    cout << "3. Koniec progromu" << endl;
    cout << "-------------------" << endl;
    cout << "Podpowiedz: Nacisnij klawisz odpowiadajacy cyfrom: 1, 2 lub 3." << endl;
    cout << endl;
}

void clearBuffer()
{
    cin.clear();
    cin.sync();
}

int testCinDecToRom()
{
    int x;
    do
    {
        cout << "Podaj poprawna liczbe z przedzialu 1 - 3999:" << endl;
        cin >> x;
        clearBuffer();
    } while (x <= 0 || x > 3999);

    return x;
}

string decToRom(int x)
{
    const int N = 13;
    string rom[N] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    int dec[N] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    string display_rom = "";

    for (int i = 0; i < N; i++)
        while (dec[i] <= x)
        {
            display_rom += rom[i];
            x -= dec[i];
        }

    return display_rom;
}

string testCinRomToDec()
{
    struct Roman_wrong_num
    {
        string rom_wrong;
    };

    Roman_wrong_num Rome_wrong[40] = {"IIII", "XXXX", "CCCC", "MMMM",
                                      "IIV", "IIX", "IL", "IC", "ID", "IM",
                                      "VX", "VL", "VC", "VD", "VM",
                                      "XXL", "XD", "XXC", "XM",
                                      "LC", "LD", "LM",
                                      "CCD", "CCM",
                                      "DM",
                                      "VV", "LL", "DD",
                                      "IVIV", "IXIX", "XLXL", "XCXC", "CDCD", "CMCM",
                                      "IVI", "IXI", "XLX", "XCX", "CDC", "CMC"};
    string x;
    char var;
    bool verification1, verification2;
    do
    {
        cout << "Podaj poprawna liczbe rzymska:" << endl;
        cin >> x;

        verification1 = false;
        verification2 = false;
        for (int i = 0; i < 40; i++)
        {
            size_t position = x.find(Rome_wrong[i].rom_wrong);
            if (position != string::npos)
            {
                verification1 = true;
            }
        }
        for (int i = 0; i < x.length(); i++)
        {

            if (x[i] != 'I' &&
                x[i] != 'V' &&
                x[i] != 'X' &&
                x[i] != 'L' &&
                x[i] != 'C' &&
                x[i] != 'D' &&
                x[i] != 'M')
            {
                verification2 = true;
            }
        }
    } while (verification1 || verification2);

    return x;
}

int rome_to_dec(char x)
{
    int rom;

    for (int i = 0; i < 7; i++)
    {
        if (x == Rome[i].rom)
        {
            rom = Rome[i].dec;
        }
    }
    return rom;
}

void RomToDec(string x)
{
    int display_dec = 0;
    int L = x.length();

    if (L > 1)
    {
        int First = rome_to_dec(x[0]), i = 0;
        while (i < L)
        {
            i++;
            int Second = rome_to_dec(x[i]);
            if (First < Second)
            {
                display_dec -= First;
            }
            else
            {
                display_dec += First;
            }
            First = Second;
        }
    }
    else
    {
        display_dec = rome_to_dec(x[0]);
    }
    cout << display_dec;
}

// Sortwanie bąbelkowe 1-4
#include <iostream>
using namespace std;
int a[20] = {2,4,5,1,-9,8,238,1,2,9,6,86,43,5,-79,23,43,5,6,65};
int main()
{
    for(int i=0; i<19;i++)
    {
        for(int j=0; j<19;j++)
        {
            if(a[j]<a[j+1])
            {
                swap(a[j],a[j+1]);
            }
        }

    }

    for(int i=0;i<20;i++)
    {
        cout << a[i] << " ";
    }
    return 0;
}



#include <iostream>
using namespace std;
int a[10];
int main()
{

    for(int i=0; i<10; i++)
    {
        cin >> a[i];
    }

    for(int i=0; i<9;i++)
    {
        for(int j=0; j<9;j++)
        {
            if(a[j]<a[j+1])
            {
                swap(a[j],a[j+1]);
            }
        }

    }

    for(int i=0;i<10;i++)
    {
        cout << a[i] << " ";
    }
    return 0;
}


#include <iostream>
using namespace std;
string a[15] = {"a","ab","abc","abce","abcf","abcg","abch","abci","abcj","abcdasdk","abcdasdk","abcdasdk","abcdsdfasdk","abcdsdffsdfsdfsdfsdfsfdasdk","abcdfsfsdfsdasdk"};
int main()
{


    for(int i=0; i<15; i++)
    {
        for(int j=0; j<15; j++)
        {
            if(a[j].size() > a[j+1].size())
            {
                swap(a[j],a[j+1]);
            }
        }
    }

    for(int i=0;i<15;i++)
    {
        cout << a[i] << " ";
    }

    return 0;
}

#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
    string wyrazy[15];

    cout << "Podaj dziesięć wyrazów:\n";

    //BASIA KASIA DARIA ANNA KAMILA
    for (int i = 0; i < 15; i++)
        cin >> wyrazy[i];

    sort(wyrazy, wyrazy + 15);

    cout << "Elementy posortowane:\n";
    for (int i = 0; i < 15; i++)
        cout << wyrazy[i] << endl;

    return 0;
}

// Sortowanie przez wstawianie
#include<iostream>
using namespace std;

void sortowanie_przez_wstawianie(int n, int *tab)
{
     int pom, j;
     for(int i=1; i<n; i++)
     {
             //wstawienie elementu w odpowiednie miejsce
             pom = tab[i]; //ten element będzie wstawiony w odpowiednie miejsce
             j = i-1;
             
             //przesuwanie elementów większych od pom
             while(j>=0 && tab[j]>pom) 
             {
                        tab[j+1] = tab[j]; //przesuwanie elementów
                        --j;
             }
             tab[j+1] = pom; //wstawienie pom w odpowiednie miejsce
     }     
}

int main()
{
    int n, *tab;
    cout<<"Podaj wielkość zbioru: ";
    cin>>n;
    
    tab = new int [n];
    
    for(int i=0; i<n; i++)
    {
            cout<<"Podaj "<<i+1<<" element: ";
            cin>>tab[i];
    }
    
    cout<<"Elementy przed sortowaniem:\n";
    for(int i=0; i<n; i++)
            cout<<tab[i]<<" ";
    
    sortowanie_przez_wstawianie(n, tab);
    
    cout<<"\nElementy posortowaniem:\n";
    for(int i=0; i<n; i++)
            cout<<tab[i]<<" ";
    
    cin.ignore();
    cin.get();
    return 0;    
} 

// Sortowanie przez wstawianie według długości string
#include <iostream>
using namespace std;

void sortowanie_przez_wstawianie(int n, string *tab)
{
    int j;
    string pom;
    for (int i = 1; i < n; i++)
    {
        pom = tab[i];
        j = i - 1;

        while (j >= 0 && tab[j].size() > pom.size())
        {
            tab[j + 1] = tab[j];
            --j;
        }
        tab[j + 1] = pom;
    }
}

int main()
{
    int n;
    string *tab;
    cout << "Podaj wielkość zbioru: ";
    cin >> n;

    tab = new string[n];

    for (int i = 0; i < n; i++)
    {
        cout << "Podaj " << i + 1 << " element: ";
        cin >> tab[i];
    }

    cout << "Elementy przed sortowaniem:\n";
    for (int i = 0; i < n; i++)
        cout << tab[i] << " ";

    sortowanie_przez_wstawianie(n, tab);

    cout << "\nElementy posortowaniem:\n";
    for (int i = 0; i < n; i++)
        cout << tab[i] << " ";

    cin.ignore();
    cin.get();
    return 0;
}



// Sortowanie przez selekcję
#include <iostream>
using namespace std;

void selection_sort(int tab[], int n) //n - ilość elementów do posortowania
{
    int mn_index; //zmienna pomocnicza przechowująca indeks komórki
                  //z minimalną wartością
    for (int i = 0; i < n - 1; i++)
    {
        mn_index = i;
        for (int j = i + 1; j < n; j++) //pętla wyszukuje najmniejszy element w podzbiorze nieposortowanym
            if (tab[j] < tab[mn_index])
                mn_index = j;

        //zamiana elementu najmniejszego w podzbiorze z pierwszą pozycją nieposortowaną
        swap(tab[i], tab[mn_index]);
    }
}

int main()
{
    int *tab, n;

    cout << "Podaj wielkość zbioru: ";
    cin >> n;

    tab = new int[n];

    for (int i = 0; i < n; i++)
    {
        cout << "Podaj " << i + 1 << " element: ";
        cin >> tab[i];
    }

    cout << "Elementy przed sortowaniem:\n";
    for (int i = 0; i < n; i++)
        cout << tab[i] << " ";

    selection_sort(tab, n); //sortowanie przez selekcję

    cout << "\nElementy posortowaniem:\n";
    for (int i = 0; i < n; i++)
        cout << tab[i] << " ";

    cout << endl;
    system("pause");
    return 0;
}


// Sortowanie przez selekcję według długości string
#include <iostream>
using namespace std;

void selection_sort(string tab[], int n)
{
    int mn_index;

    for (int i = 0; i < n - 1; i++)
    {
        mn_index = i;
        for (int j = i + 1; j < n; j++)
            if (tab[j].size() < tab[mn_index].size())
                mn_index = j;

        swap(tab[i], tab[mn_index]);
    }
}

int main()
{
    int n;
    string *tab;

    cout << "Podaj wielkość zbioru: ";
    cin >> n;

    tab = new string[n];

    for (int i = 0; i < n; i++)
    {
        cout << "Podaj " << i + 1 << " element: ";
        cin >> tab[i];
    }

    cout << "Elementy przed sortowaniem:\n";
    for (int i = 0; i < n; i++)
        cout << tab[i] << " ";

    selection_sort(tab, n);

    cout << "\nElementy posortowaniem:\n";
    for (int i = 0; i < n; i++)
        cout << tab[i] << " ";

    cout << endl;
    system("pause");
    return 0;
}

#include <iostream>
using namespace std;

void sortowanie_babelkowe(int tab[], int n)
{
    for (int i = 0; i < n; i++)
        for (int j = 1; j < n - i; j++) //pętla wewnętrzna
            if (tab[j - 1] > tab[j])
                //zamiana miejscami
                swap(tab[j - 1], tab[j]);
}

int main()
{
    int *tab, n;

    cout << "Ile liczb będziesz chciał posortować? ";
    cin >> n;

    tab = new int[n]; //przydzielenie pamięci na elementy tablicy
    //wczytanie liczb
    for (int i = 0; i < n; i++)
        cin >> tab[i];

    sortowanie_babelkowe(tab, n);

    //wypisanie posortowanych elementów
    for (int i = 0; i < n; i++)
        cout << tab[i] << " ";

    return 0;
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Sortuje liczby z pliku liczby.txt i wpisuje je do wyniki1.txt
// Unikalne liczby wpisze do wyniki2.txt
// Zduplikowane liczby wpisze do wyniki2.txt
#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int creation_count(int count);			 // Zczytuje z pliku liczbę wierszy
int reading(int *array);				 // Wczytuje wiersze, zamienia na int, sortuje, i przekazuje tablice dalej
void typing(int count, int *array);		 // Posortowane wyniki do w1.txt
void unique_num(int count, int *array);	 // Liczy unikalne liczby i wpisuje do w2.txt
void doubled_num(int count, int *array); // Liczy zdublowane liczby i wpisuje do w2.txt

int main()
{
	int count = 0;
	count = creation_count(count);
	// cout << count << endl;
	int *array = new int[count];
	*array = reading(array);

	typing(count, array);	  // Zad1
	unique_num(count, array); // Zad2

	*array = reading(array);
	doubled_num(count, array); // Zad3

	// for(int i = 0; i<count; i++)
	// {
	//     cout<<array[i] << endl;
	// }

	delete[] array;
	return 0;
}

int creation_count(int count)
{
	string line;
	fstream file;

	file.open("liczby.txt", ios::in);
	if (file.good() == true)
	{
		while (getline(file, line))
			count++;
		file.close();
	}
	else
	{
		exit(0);
	}
	return count;
}

int reading(int *array)
{
	string line;
	fstream file;
	int count = 0;

	file.open("liczby.txt", ios::in);
	if (file.good() == true)
	{
		while (!file.eof())
		{
			getline(file, line);
			if (line != "")
			{
				array[count] = stoi(line);
				count++;
			}
		}
		sort(array, array + count);

		file.close();
	}
	else
	{
		exit(0);
	}
	return *array;
}

void typing(int count, int *array)
{
	fstream file;
	file.open("wyniki1.txt", ios::out | ios::app);
	if (file.good() == true)
	{
		for (int i = 0; i < count; i++)
		{
			file << array[i] << endl;
		}
		file.close();
	}
	else
	{
		cout << "Plik nie istnieje!" << endl;
	}
}

void unique_num(int count, int *array)
{
	fstream file;
	file.open("wyniki2.txt", ios::out | ios::app);
	if (file.good() == true)
	{
		// Wpisuje do pliku tylko unikalne liczby
		for (int i = 0; i < count; i++)
		{
			for (int j = i + 1; j < count; j++)
			{
				if (array[i] == array[j])
					array[j] = 0;
			}
		}

		for (int i = 0; i < count; i++)
		{
			if (array[i] != 0)
				file << array[i] << endl;
		}

		file.close();
	}
	else
	{
		cout << "Plik nie istnieje!" << endl;
	}
}

void doubled_num(int count, int *array)
{
	int *array2 = new int[count];
	int x = 0;
	fstream file;
	file.open("wyniki3.txt", ios::out | ios::app);
	if (file.good() == true)
	{
		// Powtarzejące się liczby wpisuje do nowej tablicy
		for (int i = 0; i < count; i++)
		{
			for (int j = i + 1; j < count; j++)
			{
				if (array[i] == array[j])
				{
					array2[x] = array[i];
					x++;
				}
			}
		}

		// Wpisuje do pliku tylko unikalne liczby (z powtarzających się)
		for (int i = 0; i < x; i++)
		{
			for (int j = i + 1; j < x; j++)
			{
				if (array2[i] == array2[j])
					array2[j] = 0;
			}
		}

		for (int i = 0; i < x; i++)
		{
			if (array2[i] != 0)
				file << array2[i] << endl;
		}
		file.close();
		delete[] array2;
	}
	else
	{
		cout << "Plik nie istnieje!" << endl;
	}
}

///////////////////////////////////////////////////////////////////////
// To co powyżej ale z wykorzystaniem vector
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;
// funkcja pobiera liczby z pliku liczby.txt, wpisuje je do vektora i wypisuje do wyniki1.txt
void zad1();
// funkcja pobiera liczby z pliku liczby.txt, wpisuje je do vektora, znajduje unikalne liczby i wypisuje do wyniki2.txt
void zad2();
// funkcja pobiera liczby z pliku liczby.txt, wpisuje je do vektora, znajduje występujące więcej niż jeden raz i wypisuje do wyniki3.txt
void zad3();

int main()
{
    zad1();
    zad2();
    zad3();
    return 0;
}

void zad1()
{
    ifstream plik;
    plik.open("liczby.txt");
    vector<int> liczby;
    int liczba;
    while (plik >> liczba)
    {
        liczby.push_back(liczba);
    }
    plik.close();
    sort(liczby.begin(), liczby.end());
    ofstream wynik;
    wynik.open("wyniki1.txt");
    for (int i = 0; i < liczby.size(); i++)
    {
        wynik << liczby[i] << endl;
    }
    wynik.close();
    cout << "Zadanie 1 zrobione" << endl;
}

void zad2()
{
    ifstream plik;
    plik.open("liczby.txt");
    vector<int> liczby;
    int liczba;
    while (plik >> liczba)
    {
        liczby.push_back(liczba);
    }
    plik.close();
    sort(liczby.begin(), liczby.end());
    vector<int> unikalne;
    for (int i = 0; i < liczby.size(); i++)
    {
        if (i == 0 || liczby[i] != liczby[i - 1])
        {
            unikalne.push_back(liczby[i]);
        }
    }
    ofstream wynik;
    wynik.open("wyniki2.txt");
    for (int i = 0; i < unikalne.size(); i++)
    {
        wynik << unikalne[i] << endl;
    }
    wynik.close();
    cout << "Zadanie 2 zrobione" << endl;
}

void zad3()
{
    ifstream plik;
    plik.open("liczby.txt");
    vector<int> liczby;
    int liczba;
    while (plik >> liczba)
    {
        liczby.push_back(liczba);
    }
    plik.close();
    sort(liczby.begin(), liczby.end());
    vector<int> wystapienia;
    for (int i = 0; i < liczby.size(); i++)
    {
        if (i == 0 || liczby[i] != liczby[i - 1])
        {
            wystapienia.push_back(1);
        }
        else
        {
            wystapienia[wystapienia.size() - 1]++;
        }
    }
    ofstream wynik;
    wynik.open("wyniki3.txt");
    for (int i = 0; i < wystapienia.size(); i++)
    {
        if (wystapienia[i] > 1)
        {
            wynik << liczby[i] << endl;
        }
    }
    wynik.close();
    cout << "Zadanie 3 zrobione" << endl;
}






// Zadanie maturalne  informatyka-2021-maj-matura-rozszerzona-zad-4
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

// zadanie 4.1
void zadanie4_1(vector<string> &lines)
{
    int number = 0;
    for (int i = 0; i < lines.size(); i++)
    {
        if (lines[i][0] == 'D')
        {
            number++;
        }
        else if (lines[i][0] == 'U')
        {
            number--;
        }
    }
    cout << "1) " << number << endl;
}

// zadanie 4.2
void zadanie4_2(vector<string> &lines)
{
    string aktualny_rodzaj = "";
    int aktualna_dlugosc = 0;
    string najdluzszy_rodzaj = "";
    int najdluzsza_dlugosc = 0;
    for (int i = 0; i < lines.size(); i++)
    {
        string rodzaj = lines[i].substr(0, lines[i].find(" "));
        if (aktualny_rodzaj == "")
        {
            aktualny_rodzaj = rodzaj;
            aktualna_dlugosc = 1;
            continue;
        }
        if (aktualny_rodzaj == rodzaj)
        {
            aktualna_dlugosc++;
            if (aktualna_dlugosc > najdluzsza_dlugosc)
            {
                // ten ciąg jest w tym momencie najdłuższy
                najdluzsza_dlugosc = aktualna_dlugosc;
                najdluzszy_rodzaj = rodzaj;
            }
        }
        else
        {
            aktualny_rodzaj = rodzaj;
            aktualna_dlugosc = 1;
        }
    }
    cout << "2) " << najdluzszy_rodzaj << " " << najdluzsza_dlugosc << endl;
}

// zadanie 4.3
void zadanie4_3(vector<string> &lines)
{
    vector<string> rodzaje;

    for (int i = 0; i < lines.size(); i++)
    {
        if (lines[i][0] == 'D')
        {
            rodzaje.push_back(lines[i].substr(lines[i].size() - 1, lines[i].size()));
        }
    }

    // znajduje najczęściej występujący element w wektorze wypisuje go i ilość wystąpień
    int max_count = 0;
    string max_element = "";
    for (int i = 0; i < rodzaje.size(); i++)
    {
        int count = 0;
        for (int j = 0; j < rodzaje.size(); j++)
        {
            if (rodzaje[i] == rodzaje[j])
            {
                count++;
            }
        }
        if (count > max_count)
        {
            max_count = count;
            max_element = rodzaje[i];
        }
    }
    cout << "3) " << max_element << " " << max_count << endl;
}

// zadanie 4.4
string dopisz(vector<string> &lines, string &s, int i)
{
    s += lines[i][lines[i].size() - 1];
    return s;
}

void zamien(vector<string> &lines, string &s, int i)
{
    s[s.size() - 1] = lines[i][lines[i].size() - 1];
}

void usun(vector<string> &lines, string &s)
{
    s.erase(s.size() - 1);
}

void przesun(vector<string> &lines, string &s, int i)
{
    for (int j = 0; j < s.size(); j++)
    {
        if (s[j] == lines[i][lines[i].size() - 1])
        {
            if (lines[i][lines[i].size() - 1] == 'Z')
            {
                s[j] = 'A';
                break;
            }

            s[j] = (lines[i][lines[i].size() - 1]) + 1;
            break;
        }
    }
}

void zadanie4_4(vector<string> &lines)
{
    string s = "";
    for (int i = 0; i < lines.size(); i++)
    {
        if (lines[i][0] == 'D')
        {
            dopisz(lines, s, i);
        }
        else if (lines[i][0] == 'Z')
        {
            zamien(lines, s, i);
        }
        else if (lines[i][0] == 'U')
        {
            usun(lines, s);
        }
        else if (lines[i][0] == 'P')
        {
            przesun(lines, s, i);
        }
    }

    cout << "4) " << s << endl;
}

int main()
{

    ifstream file;
    // file.open("./DANE_2105/przyklad.txt");
    file.open("./DANE_2105/instrukcje.txt");
    vector<string> lines;
    string line;
    while (getline(file, line))
    {
        lines.push_back(line);
    }
    file.close();

    // for (int i = 0; i < lines.size(); i++)
    // {
    //     cout << lines[i] << endl;
    // }

    // Zadanie 4.1
    zadanie4_1(lines);
    zadanie4_2(lines);
    zadanie4_3(lines);
    zadanie4_4(lines);

    return 0;
}

// DOPISZ Z
// DOPISZ U
// USUN 1
// DOPISZ L
// DOPISZ A
// PRZESUN Z
// DOPISZ U
// PRZESUN U
// ZMIEN M
// PRZESUN M
// DOPISZ N
// USUN 1
// DOPISZ T
// DOPISZ U
// DOPISZ R
// DOPISZ N
// PRZESUN H
// DOPISZ V
// ZMIEN G

///////////////////////////////////////////////////////////
// Rekurencja https://www-users.mat.umk.pl//~sendlew/w12/mata2-rekurencja-slajdy.pdf

#include <iostream>
using namespace std;

int kwadrat(int n)
{
    if (n == 1)
        return 1;
    else
        return kwadrat(n - 1) + 2 * n - 1;
}

int trojkata(int n)
{
    if (n == 1)
        return 1;
    else
    {
        return n * n - trojkata(n - 1);
    }
}

int tetraedralne(int n)
{
    if (n == 1)
        return 1;
    else
    {
        return tetraedralne(n - 1) + (n * (n + 1) / 2);
    }
}

main()
{
    int n;
    cout << "Podaj liczbe: ";
    cin >> n;
    cout << "Wynik kwadrat: " << kwadrat(n) << endl;
    cout << "Wynik trojkat: " << trojkata(n) << endl;
    cout << "Wynik tetraedralne: " << tetraedralne(n);
}


////////////////////////////// NWD n liczb dodarnich
#include <iostream>
using namespace std;

int NWD(int a, int b)
{
    if (b == 0)
        return a;
    return NWD(b, a % b);
}

int main()
{
    int n;
    cout << "Podaj ilosc liczb: n = ";
    cin >> n;
    int a, b;
    cout << "Podaj pierwsza liczbe: ";
    cin >> a;
    for (int i = 0; i < n - 1; i++)
    {
        cout << "Podaj kolejna liczbe: ";
        cin >> b;
        a = NWD(a, b);
        // cout << a << " " << endl;
    }
    cout << "NWD tych liczb = " << a << endl;
    return 0;
}


////////////////////////////////////////////////// Skracanie ułamków
#include <iostream>
using namespace std;

struct wymierna
{
    int liczba;
    int mianownik;
};

int NWD(int a, int b)
{
    if (b == 0)
        return a;
    return NWD(b, a % b);
}

void skroc(wymierna &a)
{
    int n;
    cout << "Podaj licznik: ";
    cin >> a.liczba;
    cout << "Podaj mianownik: ";
    cin >> a.mianownik;
    n = NWD(a.liczba, a.mianownik);
    a.liczba /= n;
    a.mianownik /= n;
    cout << "Skrocone wymierne: " << a.liczba << "/" << a.mianownik << endl;
}

int main()
{
    wymierna a;
    skroc(a);

    return 0;
}


//////////////////////// NWD i NWW dla 2 liczb
#include <iostream>
using namespace std;

int NWD(int a, int b)
{
    if (b == 0)
        return a;
    return NWD(b, a % b);
}

int NWW(int a, int b)
{
    return (a * b) / NWD(a, b);
}

int main()
{
    int a, b;
    cout << "Podaj pierwsza liczbe: ";
    cin >> a;
    cout << "Podaj druga liczbe: ";
    cin >> b;
    cout << "NWD(" << a << ", " << b << ") = " << NWD(a, b) << endl;
    cout << "NWW(" << a << ", " << b << ") = " << NWW(a, b) << endl;
    return 0;
}

///////////////////////////////////////////////
// Liczy sume 2 ułamkownych liczb i ją skraca
// Liczy iloczyn 2 ułamkownych liczb i ją skraca
#include <iostream>
using namespace std;

int NWD(int a, int b)
{
    if (b == 0)
        return a;
    return NWD(b, a % b);
}

int NWW(int a, int b)
{
    return (a * b) / NWD(a, b);
}

struct wymierna
{
    int liczba;
    int mianownik;
};

void skroc(wymierna &a)
{
    int n;
    cout << "Podaj licznik: ";
    cin >> a.liczba;
    cout << "Podaj mianownik: ";
    cin >> a.mianownik;
    n = NWD(a.liczba, a.mianownik);
    a.liczba /= n;
    a.mianownik /= n;
    cout << "Skrocone wymierne: " << a.liczba << "/" << a.mianownik << endl;
}

void skroc_ulamek(wymierna &a)
{
    int n;
    n = NWD(a.liczba, a.mianownik);
    a.liczba /= n;
    a.mianownik /= n;
    cout << "Skrocone wymierne: " << a.liczba << "/" << a.mianownik << endl;
}

void suma(wymierna &a, wymierna &b, wymierna &c)
{
    int nww = NWW(a.mianownik, b.mianownik);
    int licznik = (nww / a.mianownik) * a.liczba + (nww / b.mianownik) * b.liczba;
    c.liczba = licznik;
    c.mianownik = nww;
    cout << "Suma: " << c.liczba << "/" << c.mianownik << endl;
}

void mnozenie(wymierna &a, wymierna &b, wymierna &c)
{
    c.liczba = a.liczba * b.liczba;
    c.mianownik = a.mianownik * b.mianownik;
    cout << "Iloczyn: " << c.liczba << "/" << c.mianownik << endl;
}
int main()
{
    wymierna a, b, c;
    skroc(a);
    skroc(b);
    suma(a, b, c);
    skroc_ulamek(c);
    mnozenie(a, b, c);
    skroc_ulamek(c);

    return 0;
}
////////////////////////////// Na ocone liczy ułamek odwrotny wymierny i sprawdza czy jest on poprawny
#include <iostream>
using namespace std;

struct wymierna
{
    int licznik;
    int mianownik;
};

void clearBuffer();
int NWD(int a, int b);
void wczytaj(wymierna &a);
void przypisz(wymierna &a, wymierna &b);
void skroc(wymierna &a);
void odwroc(wymierna &a);
void wypisz(wymierna &a, wymierna &b);
void sprawdz(wymierna &a, wymierna &b);

int main()
{
    wymierna a, b;
    wczytaj(a);
    przypisz(a, b);
    skroc(a);
    skroc(b);
    odwroc(a);
    wypisz(a, b);
    sprawdz(a, b);

    return 0;
}

void clearBuffer()
{
    cin.clear();
    cin.sync();
}

int NWD(int a, int b)
{
    if (b == 0)
        return a;
    return NWD(b, a % b);
}

void wczytaj(wymierna &a)
{
    cout << "\nPodpowiedz: nie mozesz wprowadzic 0, bo nie mozna dzielic przez 0 i odwrotnosc do 0 nie istnieje!" << endl;
    cout << "Podpowiedz: inne znaki niz liczby calkowite sa ignorowane!" << endl;

    string str_licznik, str_mianownik;
    do
    {
        cout << "Podaj poprawny licznik: ";
        cin >> str_licznik;
        clearBuffer();
        a.licznik = atoi(str_licznik.c_str());
    } while (a.licznik == 0);

    do
    {
        cout << "Podaj poprawny mianownik: ";
        cin >> str_mianownik;
        clearBuffer();
        a.mianownik = atoi(str_mianownik.c_str());
    } while (a.mianownik == 0);
}

void przypisz(wymierna &a, wymierna &b)
{
    b.licznik = a.licznik;
    b.mianownik = a.mianownik;
}

void skroc(wymierna &a)
{
    int n;
    n = NWD(a.licznik, a.mianownik);
    a.licznik /= n;
    a.mianownik /= n;
}

void odwroc(wymierna &a)
{
    int b = a.licznik;
    a.licznik = a.mianownik;
    a.mianownik = b;
}

void wypisz(wymierna &a, wymierna &b)
{
    cout << "Ulamek wymierny = " << b.licznik << "/" << b.mianownik << endl;
    cout << "Ulamek odwrotny wymierny = " << a.licznik << "/" << a.mianownik << endl;
}

void sprawdz(wymierna &a, wymierna &b)
{
    if ((a.licznik * b.licznik) / (a.mianownik * b.mianownik) == 1)
        cout << "Iloczyn = 1" << endl;
    else
        cout << "Iloczyn != 1" << endl;
}

/////////////////////////////////
#include <iostream>
#include <cmath>
using namespace std;

bool isPrimary(int n) // liczby pierwsze
{
    if (n < 2) // (n == 1)
        return false;
    for (int i = 2; i <= sqrt(n); i++)
        if (n % i == 0)
            return false;
    return true;
}

void divisors(int n) // dzielniki
{
    for (int i = 1; i <= n; i++)
    {
        if (n % i == 0)
            cout << i << " ";
    }
}

void divisorsPrim(int n) // dzielniki pierwsze
{
    for (int i = 1; i <= n; i++)
    {
        if (isPrimary(i) && n % i == 0)
            cout << i << " ";
    }
}

int main()
{
    int n;
    cout << "Podaj liczbe: ";
    cin >> n;
    if (isPrimary(n))
        cout << "Liczba jest pierwsza" << endl;
    else
        cout << "Liczba nie jest pierwsza" << endl;

    cout << "Dzielniki liczby " << n << ": ";
    divisors(n);

    cout << "\nDzielniki liczby " << n << ", ktore sa liczbami pierwszymi: ";
    divisorsPrim(n);
    return 0;
}

/////////////////////////////////////////////// Zadania z liczbami pierwszymi
#include <iostream>
#include <cmath>
using namespace std;

bool isPrimary(int n) // liczby pierwsze
{
    if (n < 2) // (n == 1)
        return false;
    for (int i = 2; i <= sqrt(n); i++)
        if (n % i == 0)
            return false;
    return true;
}

void zda1() // liczby pierwsze <100
{
    for (int i = 0; i < 100; i++)
    {
        if (isPrimary(i))
            cout << i << " ";
    }
}

void zda2() // 30 pierwszych liczby pierwszych
{
    int n = 0;
    for (int i = 0; i < 1000; i++)
    {
        if (isPrimary(i))
        {
            cout << i << " ";
            n++;
        }
        if (n < 30)
            continue;
        else
            break;
    }
}

void zad3(int n) // dzielniki pierwsze podanej liczby całkowitej dodatniej
{
    for (int i = 1; i <= n; i++)
    {
        if (isPrimary(i) && n % i == 0)
            cout << i << " ";
    }
}

// Dla każdej liczby pierwszej p w zakresie 0..sqrt(liczba):
// Jeśli liczba % p == 0 i jednocześnie liczba/p jest liczbą pierwszą to liczba jest półpierwsza.
bool zad4(int n)
{
    for (int i = 2; i <= sqrt(n); i++)
    {
        if (isPrimary(i) && n % i == 0 && isPrimary(n / i))
            return true;
    }
    return false;
}

void zad5(int n) // liczby czynników pierwszych podanej liczby całkowitej dodatniej
{
    int j = 0;
    for (int i = 1; i <= n; i++)
    {
        if (isPrimary(i) && n % i == 0)
            j++;
    }
    cout << j;
}

int main()
{
    cout << "\n1. Liczby pierwsze < 100: ";
    zda1();
    cout << "\n2. 30 pierwszych liczb pierwszych: ";
    zda2();
    cout << "\nPodaj liczbe calkowita dodatnia: ";
    int n;
    cin >> n;
    cout << "3. Dzielniki liczby " << n << ", ktore sa liczbami pierwszymi: ";
    zad3(n);

    if (zad4(n))
        cout << "\n4. Liczba " << n << " jest polpierwsza";
    else
        cout << "\n4. Liczba " << n << " nie jest polpierwsza";

    cout << "\n5. Liczba czynnikow pierwszych liczby " << n << ": ";
    zad5(n);

    return 0;
}



///////////////// ZADANIE NA 6
// Liczby zaprzyjaźnione w przedziale <1,n>
// Dla n = 100000 wynik:
// 220 i 284
// 1184 i 1210
// 2620 i 2924
// 5020 i 5564
// 6232 i 6368
// 10744 i 10856
// 12285 i 14595
// 17296 i 18416
// 63020 i 76084
// 66928 i 66992
// 67095 i 71145
// 69615 i 87633
// 79750 i 88730
#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

void clearBuffer();
void welcome();
int download();
int sumDivisors(int n);
void answer(int n);

int main(int argc, char const *argv[])
{
    welcome();
    int n = download();
    answer(n);
    system("pause");
    return 0;
}

void clearBuffer()
{
    cin.clear();
    cin.sync();
}

void welcome()
{
    cout << "Witaj w programie liczby zaprzyjaznione!" << endl;
    cout << "Program wyswietla wszystkie liczby zaprzyjaznione zawierajace sie w przedziale <1,n>" << endl;
}

int download() // liczba naturalna
{
    string str;
    int n;
    do
    {
        cout << "Podaj poprawna liczbe naturalna: ";
        cin >> str;
        clearBuffer();
        n = atoi(str.c_str());
    } while (n <= 0);
    // int n = 100000;
    return n;
}

int sumDivisors(int n)
{
    int sum = 1;
    for (int i = 2; i < n; i++)
        if (n % i == 0)
            sum += i;
    return sum;
}

void answer(int n)
{
    int sum, sum2;
    bool isExist = false;
    vector<int> repeating;

    cout << "Szukam liczb zaprzyjaznionych w przedziale <1, " << n << ">:" << endl;
    for (int i = 1; i <= n; i++)
    {
        sum = sumDivisors(i);
        sum2 = sumDivisors(sum);
        if (sum2 == i && i != sum <= n)
            repeating.push_back(sum);
        if (sum2 == i && i != sum && sum <= n && find(repeating.begin(), repeating.end(), i) == repeating.end())
        {
            cout << i << " i " << sum << endl;
            isExist = true;
        }
    }
    if (!isExist)
        cout << "Nie znaleziono liczb zaprzyjaznionych w przedziale <1, " << n << ">!" << endl;
}


//////////////////////// ZADANIE NA 5
// Program wyswietla czy liczba jest pierwsza, polpierwsza, zlozona, czy doskonala.
#include <iostream>
#include <cmath>
using namespace std;

void clearBuffer();
void welcome();
int download();
bool isPrimary(int n);
bool isHalfPrimary(int n);
bool isComposite(int n);
void divisors(int n);
bool isPerfect(int n);
void answer(int n);

int main(int argc, char const *argv[])
{

    welcome();
    int n = download();
    answer(n);

    return 0;
}

void clearBuffer()
{
    cin.clear();
    cin.sync();
}

void welcome()
{
    cout << "Witaj w programie jaka to liczba?" << endl;
    cout << "Program wyswietla czy liczba jest pierwsza, polpierwsza, zlozona, czy doskonala." << endl;
}

int download() // liczba całkowita
{
    string str;
    int n;
    do
    {
        cout << "Podaj poprawna liczbe naturalna: ";
        cin >> str;
        clearBuffer();
        n = atoi(str.c_str());
        if (n == 0 && str[0] == '0')
            break;
    } while (n == 0);
    return n;
}

bool isPrimary(int n)
{
    if (n < 2)
        return false;
    for (int i = 2; i <= sqrt(n); i++)
        if (n % i == 0)
            return false;
    return true;
}

bool isHalfPrimary(int n)
{
    for (int i = 2; i <= sqrt(n); i++)
    {
        if (isPrimary(i) && n % i == 0 && isPrimary(n / i))
            return true;
    }
    return false;
}

bool isComposite(int n)
{
    if (n < 2)
        return false;
    for (int i = 2; i <= sqrt(n); i++)
        if (n % i == 0)
            return true;
    return false;
}

void divisors(int n)
{
    cout << "Dzielniki liczby " << n << " to: ";
    for (int i = 1; i < n; i++) // <= n - wszystkie dzielniki || < n - dzielniki właściwe
        if (n % i == 0)
            cout << i << " ";
    cout << endl;
}

bool isPerfect(int n)
{
    if (n < 2)
        return false;
    int sum = 0;
    for (int i = 1; i < n; i++)
        if (n % i == 0)
            sum += i;
    if (sum == n)
        return true;
    return false;
}

void answer(int n)
{
    cout << "Liczba " << n << endl;
    if (isPrimary(n))
        cout << "Jest liczba pierwsza!" << endl;
    if (isHalfPrimary(n))
        cout << "Jest liczba polpierwsza!" << endl;
    if (isComposite(n))
    {
        cout << "Jest liczba zlozona!" << endl;
        divisors(n);
    }
    if (isPerfect(n))
        cout << "Jest liczba doskonala!" << endl;
    if (isPrimary(n) == false && isHalfPrimary(n) == false && isComposite(n) == false && isPerfect(n) == false)
        cout << "Nie jest liczba pierwsza, polpierwsza, zlozona i doskonala!" << endl;
}



///////////////////////////////////// Palindromy
#include <iostream>
#include <string>
#include <cctype>
#include <vector>
using namespace std;

void clearBuffer();
bool Palindrom(string wyraz);  // Takie same litery
bool Palindrom2(string wyraz); // Niezależnie od wielkości litery
void YesNo(string wyraz);      // Wywołąnie 2 powyższych funkcji
void Zdanie(string zdanie);    // Palindrom z zdania - ignoruje spacje
void WyrazyWZdanieu();         // Czy wszystkie wyrazy w tym zdaniu składają się z tej samej liczby liter oraz czy wszystkie są palindromami. Jeśli tak to wypisz "Tak", jeśli nie to "Nie".
void LiczbyPalindromiczne();   // Czy wszystkie liczby palindromiczne w zakresie 100..999.

main()
{
    string wyraz;
    cout << "Podaj wyraz: ";
    cin >> wyraz;
    YesNo(wyraz);

    clearBuffer();

    string zdanie;
    cout << "\nPodaj zdanie: ";
    getline(cin, zdanie);
    Zdanie(zdanie);

    WyrazyWZdanieu();
    LiczbyPalindromiczne();

    // wyraz.find("a");
    // cout << wyraz.find("a") << endl;

    // wyraz.substr(0, 2);
    // cout << wyraz.substr(0, 2) << endl;

    // wyraz.erase(0, 2);
    // cout << wyraz << endl;

    return 0;
}

void clearBuffer()
{
    cin.clear();
    cin.sync();
}

bool Palindrom(string wyraz) // Takie same litery
{
    for (int i = 0; i < wyraz.length() / 2; i++)
    {
        if (wyraz[i] != wyraz[wyraz.length() - 1 - i])
            return false;
    }
    return true;
}

bool Palindrom2(string wyraz) // Niezależnie od wielkości litery
{

    for (int i = 0; i < wyraz.length() / 2; i++)
    {
        if (tolower(wyraz[i]) != tolower(wyraz[wyraz.length() - 1 - i]))
            return false;
    }
    return true;
}

void YesNo(string wyraz)
{
    if (Palindrom(wyraz))
        cout << "TAK" << endl;
    else
        cout << "NIE" << endl;

    if (Palindrom2(wyraz))
        cout << "TAK" << endl;
    else
        cout << "NIE" << endl;
}

void Zdanie(string zdanie)
{
    string wyraz;
    for (int i = 0; i < zdanie.size(); i++)
    {
        if (zdanie[i] == ' ')
            continue;
        wyraz += zdanie[i];
        if (i == zdanie.size() - 1)
            YesNo(wyraz);
    }
}

void WyrazyWZdanieu()
{
    int licznik = 0;
    string zdanie;
    vector<string> wyrazy;
    bool ok1 = true, ok2 = true;
    cout << "\nPodaj zdanie: ";
    getline(cin, zdanie);

    // Przypisywanie wyrazów do wektora
    for (int i = 0; i < zdanie.length(); i++)
    {
        if (zdanie[i] == ' ')
        {
            wyrazy.push_back(zdanie.substr(licznik, i - licznik));
            licznik = i + 1;
        }
    }
    wyrazy.push_back(zdanie.substr(licznik, zdanie.length() - licznik));

    // Sprawdzanie czy wszystkie wyrazy są palindromami i czy wszystkie wyrazy składają się z tej samej liczby liter
    for (int i = 0; i < wyrazy.size(); i++)
    {
        if (Palindrom2(wyrazy[i]) == false)
        {
            ok1 = false;
            break;
        }
        if (wyrazy[0].length() != wyrazy[i].length())
        {
            ok2 = false;
            break;
        }
    }

    if (ok1 == true && ok2 == true)
        cout << "TAK - zdanie sklada sie z palindromow i wszystkie wyrazy maja taka sama dlugosc" << endl;
    else
        cout << "NIE - zdanie nie sklada sie z palindromow lub nie wszystkie wyrazy maja taka sama dlugosc" << endl;
}

void LiczbyPalindromiczne()
{
    cout << "\nTrzycyfrowe liczby palindromiczne" << endl;
    for (int i = 100; i <= 999; i++)
    {
        if (Palindrom2(to_string(i)))
            cout << i << " ";
    }
}

//////////////// Szyfr cezara
#include <iostream>
#include <string>
using namespace std;

void caesarEncrypt(string text, int kay);
void caesarDecrypt(string text, int kay);

int main(int argc, char const *argv[])
{
    string text;
    int kay, choice;

    cout << "Podaj tekst: ";
    getline(cin, text);

    cout << "Podaj klucz: ";
    cin >> kay;
    while (kay < 0 || kay > 25)
    {
        cout << "Klucz musi byc w przedziale 0-25.\nPodaj ponownie: ";
        cin >> kay;
    }

    cout << "1. Szyfrowanie\n2. Deszyfrowanie\n";
    cin >> choice;
    switch (choice)
    {
    case 1:
        caesarEncrypt(text, kay);
        break;
    case 2:
        caesarDecrypt(text, kay);
        break;
    default:
        cout << "Nie ma takiej opcji";
        break;
    }

    return 0;
}

void caesarEncrypt(string text, int kay)
{
    for (int i = 0; i < text.length(); i++)
    {
        text[i] = toupper(text[i]);
        if (text[i] >= 'A' && text[i] <= 'Z')
        {
            text[i] = ((text[i] - 'A' + kay) % 26) + 'A';
        }
    }
    cout << text << endl;
}

void caesarDecrypt(string text, int kay)
{
    for (int i = 0; i < text.length(); i++)
    {
        text[i] = toupper(text[i]);
        if (text[i] >= 'A' && text[i] <= 'Z')
        {
            text[i] = ((text[i] - 'A' - kay) % 26) + 'A';
            if (text[i] < 'A')
            {
                text[i] = 'Z' - 'A' + text[i] + 1;
            }
        }
    }
    cout << text << endl;
}

// Psełdo kod
// Krok 1: text <- tekst do zaszyfrowania
// Krok 2: kay <- klucz
// Krok 3: Jeśli kay < 0 lub > 25 powrót do kroku 2
// Krok 4: choice <- 1 lub 2 (wybór opcji szyfrowanie lub deszyfrowanie)
// Krok 5: Jeśli choice != 1 i choice != 2, koniec
// Krok 6: Jeśli choice = 1, to:
// Krok 6.1: Wywołanie caesarEncrypt(text, kay)
// Krok 6.2: i <- 0
// Krok 6.3: Jeśli i < długość tekstu, koniec
// Krok 6.4: text[i] <- text[i].toupper() - zamiana na duże litery
// Krok 6.5: Jeśli text[i] < 'A' i text[i] > 'Z', to idz do kroku 6.7
// Krok 6.6: text[i] <- (text[i] - 'A' + kay) % 26 + 'A'
// Krok 6.7: i <- i + 1
// Krok 6.8: Idź do kroku 6.3
// Krok 7: Jeśli choice = 2, to:
// Krok 7.1: Wywołanie caesarDecrypt(text, kay)
// Krok 7.2: i <- 0
// Krok 7.3: Jeśli i < długość tekstu, koniec
// Krok 7.4: text[i] <- text[i].toupper() - zamiana na duże litery
// Krok 7.5: Jeśli text[i] < 'A' i text[i] > 'Z', to idz do kroku 7.8
// Krok 7.6: text[i] <- (text[i] - 'A' - kay) % 26 + 'A'
// Krok 7.7: Jeśli text[i] < 'A', to text[i] <- 'Z' - 'A' + text[i] + 1
// Krok 7.8: i <- i + 1
// Krok 7.9: Idź do kroku 7.3




//////////////////////// Szyfr cezara txt


#include <iostream>
#include <string>
#include <fstream>
using namespace std;

string caesarEncryptTxt(string text, int kay);
string caesarDecryptTxt(string text, int kay);

int main()
{
    ifstream file;
    ofstream file2;
    string text, text2;
    int choice, kay;

    file.open("zadanie53.txt");
    file2.open("zadanie53_out.txt");

    cout << "Podaj  klucz: ";
    cin >> kay;

    cout << "1. Szyfrowanie\n2. Deszyfrowanie\n";
    cin >> choice;
    switch (choice)
    {
    case 1:
        while (!file.eof())
        {
            getline(file, text);
            text2 = caesarEncryptTxt(text, kay);
            file2 << text2 << endl;
        }
        break;
    case 2:
        while (!file.eof())
        {
            getline(file, text);
            text2 = caesarDecryptTxt(text, kay);
            file2 << text2 << endl;
        }
        break;
    default:
        cout << "Nie ma takiej opcji";
        break;
    }
    file2.close();
    file.close();

    return 0;
}

string caesarEncryptTxt(string text, int kay)
{
    for (int i = 0; i < text.length(); i++)
    {
        text[i] = toupper(text[i]);
        if (text[i] >= 'A' && text[i] <= 'Z')
        {
            text[i] = ((text[i] - 'A' + kay) % 26) + 'A';
        }
    }
    return text;
}
string caesarDecryptTxt(string text, int kay)
{
    for (int i = 0; i < text.length(); i++)
    {
        text[i] = toupper(text[i]);
        if (text[i] >= 'A' && text[i] <= 'Z')
        {
            text[i] = ((text[i] - 'A' - kay) % 26) + 'A';
            if (text[i] < 'A')
            {
                text[i] = 'Z' - 'A' + text[i] + 1;
            }
        }
    }
    return text;
}

//////////// Python lepszy
# Python lepszy niż C++ w zakresie złożoności obliczeniowej w takich programach w języku polskim
# Nie chciało mi się tego w C++ robić za dużo zmiennych, kodu i kombinowania, choć to wynik z lekcji tyle, że w pythonie działa :(
# W C++ przy takich zadaniach to aż się odechciewa, jak program wymięka przy 'ą' z powodu kodowań znaków
def Decrypt(letter, kay):
    lowercaseAlphabetPL = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
    uppercaseAlphabetPL = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"

    index = lowercaseAlphabetPL.find(letter)
    if index >= 0 and index <= 34:
        if ((index - kay) % 35 < 0):
            return lowercaseAlphabetPL[35 + (index - kay) % 35]
        else:
            return lowercaseAlphabetPL[(index - kay) % 35]
    else:
        index = uppercaseAlphabetPL.find(letter)
        if index >= 0 and index <= 34:
            if ((index - kay) % 35 < 0):
                return uppercaseAlphabetPL[35 + (index - kay) % 35]
            else:
                return uppercaseAlphabetPL[(index - kay) % 35]
        else:
            return letter


def main():
    file = open("text.txt", "r", encoding="utf-8")
    file2 = open("text2.txt", "w", encoding="utf-8")
    kay = int(input("Podaj klucz dla miejsc parzystych: "))
    kay2 = int(input("Podaj klucz dla miejsc nieparzystych: "))

    for line in file:
        text = line
        text2 = ""
        for i in range(len(text)):
            if i % 2 == 0:
                text2 += Decrypt(text[i], kay)
            else:
                text2 += Decrypt(text[i], kay2)
        print("Po rozszyfrowaniu: " + text2.strip())
        file2.write(text2.strip() + "\n")
        text2 = ""
    file.close()
    file2.close()

main()

//////////////////////////////
			#include <iostream>
#include <fstream>
#include <string>

using namespace std;
string caesarDecryptTxt(string text, int key);

int main(int argc, char const *argv[])
{
    ifstream file("text.txt");
    ofstream file2("text2.txt");

    // 1. Napisz program, który wczyta dane z pliku tekstowego, a następnie zliczy wystąpienie liter i zapisze wyniki do pliku tekstowego.
    int index = 0, letters[26] = {0};
    string text;
    char ch;
    for (index = 0; index < 26; index++)
        letters[index] = 0;

    while (!file.eof())
    {
        getline(file, text);
        for (int i = 0; i < text.length(); i++)
        {
            ch = text[i];
            if (ch >= 'a' && ch <= 'z')
                letters[ch - 'a']++;
            else if (ch >= 'A' && ch <= 'Z')
                letters[ch - 'A']++;
        }
    }
    for (index = 0; index < 26; index++)
        file2 << (char)(index + 'A') << ": " << letters[index] << endl;

    // 2. Napisz program, który wypiszę  literę najczęściej występującą w tekście złożonym z liter łacińskiego alfabetu. Jeśli takich liter jest więcej niż jedna, program powinien wypisać wszystkie.

    int max = 0;
    for (index = 0; index < 26; index++)
    {
        if (letters[index] > max)
            max = letters[index];
    }

    for (index = 0; index < 26; index++)
    {
        if (letters[index] == max)
            file2 << "Najczęściej występujące litery: " << (char)(index + 'A') << endl;
    }

    // 3. Napisz program umożliwiający łamanie szyfru Cezara. Program powinien pobierać szyfrogram z pliku i zapisać tekst będący próbą odszyfrowania kryptogramu również w pliku.

    for (index = 0; index < 26; index++)
        if (letters[index] == max)
            file2 << "Klucz: " << max << " próba: " << caesarDecryptTxt(text, index) << endl;

    for (index = 0; index < 26; index++)
        if (letters[index] == max - 1)
            file2 << "Klucz: " << max - 1 << " próba: " << caesarDecryptTxt(text, index) << endl; // itd...

    file2.close();
    file.close();

    return 0;
}

string caesarDecryptTxt(string text, int kay)
{
    for (int i = 0; i < text.length(); i++)
    {
        text[i] = toupper(text[i]);
        if (text[i] >= 'A' && text[i] <= 'Z')
        {
            text[i] = ((text[i] - 'A' - kay) % 26) + 'A';
            if (text[i] < 'A')
            {
                text[i] = 'Z' - 'A' + text[i] + 1;
            }
        }
    }
    return text;
}


///////////////// PROJEKT PYTHON
# Szyfr Vigenère’a
# Tworzenie polskiej tablicy Vigenere'a
uppercaseAlphabetPL = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"


def arrayVigenere():
    Vigenere = []
    for i in range(len(uppercaseAlphabetPL)):
        Vigenere.append(uppercaseAlphabetPL[i:i+35:] + uppercaseAlphabetPL[:i])
    return Vigenere

# Ładnie wyświetla tablice Vigenere'a


def printVigenere(Vigenere):
    for i in range(len(Vigenere)):
        print(Vigenere[i])


printVigenere(arrayVigenere())

# Szyfrrowanie Vigenère’a


def vigenereEncrypt(text, key):
    encryptedText = ""
    for i in range(len(text)):
        indexLetter = uppercaseAlphabetPL.find(text[i])
        indexKey = uppercaseAlphabetPL.find(key[i])

        if indexLetter >= 0 and indexLetter <= 34:
            encryptedText += arrayVigenere()[indexLetter][indexKey]
        else:
            encryptedText += text[i]
    return encryptedText

# print(vigenereEncrypt(".AĄBŻ", ".AĄBŻ"))

# Odkodowanie Vigenère'a


def vigenereDecrypt(text, key):
    encryptedText = ""
    for i in range(len(text)):
        indexLetter = uppercaseAlphabetPL.find(text[i])
        indexKey = uppercaseAlphabetPL.find(key[i])

        if indexLetter >= 0 and indexLetter <= 34:
            for j in range(len(arrayVigenere()[indexKey])):
                if arrayVigenere()[indexKey][j] == text[i]:
                    encryptedText += uppercaseAlphabetPL[j]
        else:
            encryptedText += text[i]
    return encryptedText

# print(vigenereDecrypt(".ABĆŹ", ".AĄBŻ"))


def main():
    while True:
        print("\n===============")
        print("Szyfr Vigenère'a")
        print("Witaj w programie szyfrowania i deszyfrowania tekstu za pomocą szyfru Vigenère'a")
        print("===============")
        print("Wybierz opcję:")
        print("1. Szyfrowanie")
        print("2. Deszyfrowanie")
        print("3. Dokumentacja")
        print("4. Wyjście")
        print("===============")
        # Wybór opcji
        option = input("Wybierz opcję: ")
        # Opcje
        if option == "1":
            text = input("Podaj tekst do zaszyfrowania: ")
            key = input("Podaj klucz: ")
            print("Tekst zaszyfrowany: " + vigenereEncrypt(text, key))
            input("\nNaciśnij ENTER, aby kontynuować...")
        elif option == "2":
            text = input("Podaj tekst do odszyfrowania: ")
            key = input("Podaj klucz: ")
            print("Tekst odszyfrowany: " + vigenereDecrypt(text, key))
            input("\nNaciśnij ENTER, aby kontynuować...")
        elif option == "3":
            print("""
            Szyfr Vigenère'a
            Witaj w programie szyfrowania i deszyfrowania tekstu za pomocą szyfru Vigenère'a
            W tekście zaszyfrowanym wstawiamy litery z klucza, a następnie wybieramy litery z tekstu zaszyfrowanego.
            W tekście odszyfrowanym wstawiamy litery z klucza, a następnie wybieramy litery z tekstu odszyfrowanego.
            """)
            input("\nNaciśnij ENTER, aby kontynuować...")
        elif option == "4":
            exit()
        else:
            print("Nie ma takiej opcji")
            input("\nNaciśnij ENTER, aby kontynuować...")


main()

/////////////////////// PROJEKT C++
// # Szyfr Vigenère’a

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int array_size;
string uppercaseAlphabetPL;

void createGlobalVariables();                                            // Tworzenie zmiennych globalnych
string vigenereEncrypt(string arrayVigenere[], string text, string key); // Szyfrowanie
string vigenereDecrypt(string arrayVigenere[], string text, string key); // Deszyfrowanie

int main(int argc, char const *argv[])
{
    // Tworzenie polskiej tablicy Vigenere'a
    createGlobalVariables();
    string arrayVigenere[array_size];

    // Zrobienie tablicy Vigenere’a
    for (int i = 0; i < array_size; i++)
        arrayVigenere[i] = uppercaseAlphabetPL.substr(i, 35) + uppercaseAlphabetPL.substr(0, i);

    // Wyświetlanie tablicy Vigenere’a
    // for (int i = 0; i < array_size; i++)
    //     cout << arrayVigenere[i] << endl;
    ifstream file("text.txt");
    ofstream file2("text2.txt");
    string text, key;

    cout << "\n================" << endl;
    cout << "Szyfr Vigenere'a" << endl;
    cout << "Witaj w programie szyfrowania i deszyfrowywania tekstu za pomoca szyfru Vigenere'a" << endl;
    cout << "UWAGA! Zanim rozpoczniesz kozystanie z programu zapoznaj sie z dokumentacja :')" << endl;
    cout << "======MENU======" << endl;
    cout << "1. Szyfrowanie" << endl;
    cout << "2. Deszyfrowanie" << endl;
    cout << "3. Dokumentacja" << endl;
    cout << "4. Wyjscie" << endl;
    cout << "================" << endl;
    cout << "Wybierz opcje:" << endl;

    int choice;
    cin >> choice;
    switch (choice)
    {
    case 1:
        cout << "1. Szyfrowanie" << endl;
        while (!file.eof())
        {
            getline(file, text);
            getline(file, key);
            file2 << vigenereEncrypt(arrayVigenere, text, key) << endl;
            file2 << key << endl;
        }
        break;
    case 2:
        cout << "2. Deszyfrowanie" << endl;
        while (!file.eof())
        {
            getline(file, text);
            getline(file, key);
            file2 << vigenereDecrypt(arrayVigenere, text, key) << endl;
            file2 << key << endl;
        }
        break;
    case 3:
        cout << "================" << endl;
        cout << "==DOKUMENTACJA==" << endl;
        cout << "================" << endl;
        cout << "1. Program korzysta z 3 plikow tekstowych: alphabet.txt, text.txt i text2.txt " << endl;
        cout << "2. alphabet.txt - wprowadzony tam jest alfabet na podstawie ktorego powstaje tabela sluzaca do szyfrowania lub deszyfrowania" << endl;
        cout << "3. text.txt - w nieparzystych liniach piszemy tekst do szyfrowania lub deszyfrowania, a w parzystych klucz szyfryjacy lub deszyfryjacy, UWAGA za ostatnia linia (linia z kluczam) nie powinna znajdowac sie zadna nowa linia (np. ENTER)" << endl;
        cout << "4. text2.txt - po urychomieniu programu w nieparzystych liniach znajdzie sie zaszyfrowana lub odszyfrowana wiadomosc, a w parzystych klucz szyfryjacy lub deszyfryjacy na podstawie ktorego wygenerowana byla wiadomosc" << endl;
        cout << "5. Aby sprawdzic poprawnosc programu przekopiuj uzyskana zawartosc pliku text2.txt do pliku text.txt - powinienesc uzyskac pierwotna wiadomosc" << endl;
        cout << "6. UWAGA szyfrowane i deszyfrowane sa tylko znaki umieszczone w pliku alphabet.txt, co za tym idzie, tam gdzie one nie wystepuja, znaki musza buc takie same na odpowiadajacych sobie miejscach w tekscie i kluczu - przydatna wiedza, gdy klucz jest krotszy do tekstu" << endl;
        cout << "7. UWAGA program nie sprawdza, czy wprowadzony klucz jest poprawny" << endl;
        cout << "8. UWAGA program nie sprawdza, czy wprowadzony tekst jest poprawny" << endl;
        cout << "9. Przyklad poprawnego tekstu i klucza, ktory nalezy umiescic w pliku text.txt" << endl;
        cout << "================" << endl;
        cout << "Tekst do szyfrowania: .MATEUSZ I .KAMIL" << endl;
        cout << "Klucz: .MATEUSZ I .KAMIL" << endl;
        cout << "Tekst po szyfrowaniu: .ZANJOKW Q .TAZQV" << endl;
        cout << "================" << endl;
        cout << "Tekst do odszyfrowania: .ZANJOKW Q .TAZQV" << endl;
        cout << "Klucz: .MATEUSZ I .KAMIL" << endl;
        cout << "Tekst po deszyfrowaniu: .MATEUSZ I .KAMIL" << endl;
        cout << "================" << endl;
        cout << "KRYPTOANALIZA" << endl;
        cout << "Metoda zlamania opierala sie na obserwacji, ze powtorzenia w szyfrogramie moga odpowiadac powtorzeniom w tekscie jawnym i kluczu. To z kolei ulatwialo odgadniecie dlugosci klucza, nastepnie samego klucza i odszyfrowania szyfrogramu." << endl;
        cout << "Bezwarunkowe bezpieczenstwo" << endl;
        cout << "Szyfr Vigenere’a moze byc szyfrem nie do zlamania (zostalo to udowodnione w 1949 przez Claude’a Elwooda Shannona) przy zachowaniu trzech regul:\nklucz uzyty do szyfrowania wiadomosci musi byc dluzszy lub rowny szyfrowanej wiadomosci;\nklucz musi byc wygenerowany w sposob calkowicie losowy(nie moze istniec sposob na odtworzenie klucza na podstawie znajomosci dzialania generatorow liczb pseudolosowych);\nklucz nie moze byc uzyty do zaszyfrowania wiecej niz jednej wiadomosci. Dodatkowo jest wymagane, aby osoba znajaca klucz nikomu go nie zdradzila." << endl;
        cout << "================" << endl;
        break;
    default:
        cout << "Nie ma takiej opcji";
        break;
    }

    file2.close();
    file.close();
    return 0;
}

void createGlobalVariables()
{
    ifstream file;
    file.open("alphabet.txt"); // Zawartość AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ
    if (!file.is_open())
        cout << "Nie udalo sie otworzyc pliku alphabet.txt" << endl;
    getline(file, uppercaseAlphabetPL);
    file.close();

    array_size = uppercaseAlphabetPL.length();
}

string vigenereEncrypt(string arrayVigenere[], string text, string key)
{
    // Wyświetlanie tablicy Vigenere’a
    // for (int i = 0; i < array_size; i++)
    //     cout << arrayVigenere[i] << endl;

    // cout << text << endl;
    // cout << key << endl;
    // cout << endl;

    string vigenereEncrypt = "";
    for (int i = 0; i < text.length(); i++)
    {
        int indexLetter = uppercaseAlphabetPL.find(text[i]);
        int indexKey = uppercaseAlphabetPL.find(key[i]);

        if (indexLetter >= 0 && indexLetter <= 34)
            vigenereEncrypt += arrayVigenere[indexLetter][indexKey];
        else
            vigenereEncrypt += text[i];
    }
    cout << "Poprawny wynik zapisano w pliku text2.txt: " << vigenereEncrypt << endl;
    return vigenereEncrypt;
}

string vigenereDecrypt(string arrayVigenere[], string text, string key)
{
    // Wyświetlanie tablicy Vigenere’a
    // for (int i = 0; i < array_size; i++)
    //     cout << arrayVigenere[i] << endl;

    // cout << text << endl;
    // cout << key << endl;
    // cout << endl;

    string vigenereDecrypt = "";
    for (int i = 0; i < text.length(); i++)
    {
        int indexLetter = uppercaseAlphabetPL.find(text[i]);
        int indexKey = uppercaseAlphabetPL.find(key[i]);

        if (indexLetter >= 0 && indexLetter <= 34)
        {
            for (int j = 0; j < array_size; j++)
                if (arrayVigenere[indexKey][j] == text[i])
                    vigenereDecrypt += uppercaseAlphabetPL[j];
        }
        else
            vigenereDecrypt += text[i];
    }
    cout << "Poprawny wynik zapisano w pliku text2.txt: " << vigenereDecrypt << endl;
    return vigenereDecrypt;
}

void clearBuffer()
{
    cin.clear();
    cin.sync();
}

// PS. PYTHON LEPSZY

			

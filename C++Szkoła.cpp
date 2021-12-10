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


/////////////////// Liczy sume 2 ułamkownych liczb i ją skraca
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

int main()
{
    wymierna a, b, c;
    skroc(a);
    skroc(b);
    suma(a, b, c);
    skroc_ulamek(c);

    return 0;
}



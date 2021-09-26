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

    Roman_wrong_num Rome_wrong[30] = {"IIII", "XXXX", "CCCC", "MMMM",
                                      "IIV", "IIX", "IL", "IC", "ID", "IM",
                                      "VX", "VL", "VC", "VD", "VM",
                                      "XD", "XM",
                                      "LC", "LD", "LM",
                                      "DM",
                                      "VV", "LL", "DD",
                                      "IVIV", "IXIX", "XLXL", "XCXC", "CDCD", "CMCM"};
    string x;
    char var;
    bool verification1, verification2;
    do
    {
        cout << "Podaj poprawna liczbe rzymska:" << endl;
        cin >> x;

        verification1 = false;
        verification2 = false;
        for (int i = 0; i < 30; i++)
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

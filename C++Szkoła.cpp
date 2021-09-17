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




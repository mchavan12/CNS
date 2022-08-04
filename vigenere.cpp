#include<iostream>
using namespace std;

string encrypt(string pt, string key) {
	string ct=pt;
	int i=0,l=key.size();
	for(i=0;i<pt.size();i++)
		ct[i]=((pt[i])+(key[i%l]))%26+'A';
	return ct;
}
string decrypt(string ct, string key) {
	string pt=ct;
	int i=0,l=key.size();
	for(i=0;i<pt.size();i++)
		pt[i]=((ct[i])-(key[i%l]))%26+'A';
	return pt;
}
int main() {
	cout<<"Enter the key (A-Z) : ";
	string key;
	cin>>key;
	cout<<"Enter the plaintext (A-Z) : ";
	string plaintext;
	cin>>plaintext;
	string ciphertext;
	ciphertext=encrypt(plaintext,key);
	cout<<"Vigenere Encrypted Text : "<<ciphertext<<endl;
	string decryptedtext;
	decryptedtext=decrypt(ciphertext,key);
	cout<<"Vigenere Decrypted Text : "<<decryptedtext<<endl;
	return 0;
}

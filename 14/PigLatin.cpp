#include <iostream>
#include <string>
#include <locale>

bool is_vowel(char c){
	if (c =='a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
		return true;
	}
	else{
		return false;
	}
}

std::string PigLatin(std::string w){
	std::string translated = "";
	for (int i = 0; i < w.length(); i++){
		w[i] = tolower(w[i]);
	}
	if (is_vowel(w[0])){
		translated = w + "ay";
	}
	else{
		translated = w.substr(1,w.length()) + w + "ay";
	}
	return translated;
}

int main(){
	std::string piglatin1 = PigLatin("HELLO");
	std::string piglatin2 = PigLatin("Motorcycle");
	std::cout << "PigLatin(Hello) = " << piglatin1 << std::endl;
	std::cout << "PigLatin(Motorctcle) = " << piglatin2 << std::endl;
}
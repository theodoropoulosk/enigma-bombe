#include <iostream>
#include <string>
#include <array>

using namespace std;



char function_change(char setting_cange[], char letter_passed) {

	if (letter_passed == setting_cange[0]) {
		letter_passed = setting_cange[1];
	}
	else if (letter_passed == setting_cange[1]) {
		letter_passed = setting_cange[0];
	}
	return letter_passed;
}



int main() {


	// Settings Changed

	char conect_1[2];
	char conect_2[2];
	char conect_3[2];
	char conect_4[2];
	char conect_5[2];
	char conect_6[2];

	//string answer;
	//int connections = 0;
	//while (connections < 7 && answer != "no") {
	//	cout << "How many conections do you want to make? (1-6)" << endl;
	//	cin >> answer;
	//	 if (answer == "yes") {
	//		 connections = connections + 1;
	//		 for (int i = 0; i < 2; i++) {
	//			 cout << "Enter Capital letter: " << endl;
	//			 cin >> conect_1[i];
	//		 }
	//	}
	//}
	
	char* enter_settings (); {
		char conect[2];
		for (int i = 0; i < 2; i++) {
			cout << "Enter Capital letter: " << endl; 
			cin >> conect[i];
		}
		return conect;
	}
	
	//char test = enter_settings(); 
	//cout << test;

		/*for (int i = 0; i < 2; i++) {
			cout << test[i]; 
		}*/
	//char letter = function_change(setting_cange, letter_passed); 
	//cout << letter; 


	return 0;
}
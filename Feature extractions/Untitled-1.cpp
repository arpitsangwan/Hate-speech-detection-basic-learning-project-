#include <iostream>
#include <string>
#include <vector>
using namespace std;
bool flag = true;
void semiCoErr(string inputString)
{
	cout << "\nScanning for Syntactical Errors:\n";
	if (inputString[inputString.size() - 1] != ';')
	{
		flag = false;
	}
}
void dataTypeErr(string inputString)
{
	string str = "";
	for (int i = 0; i < inputString.size() && inputString[i] != ' ';
		i++)
		str += inputString[i];
	vector<string> v;
	v = { "int", "string", "float", "double", "bool" };
	for (int i = 0; i < v.size(); i++)
	{
		if (v[i] == str)
		{
			flag = true;
			return;
		}
	}
	flag = false;
}
int main()
{
	string inputString;
	cout << "\nEnter the string to be evaluated :\n";
	getline(cin, inputString);
	semiCoErr(inputString);
	dataTypeErr(inputString);
	if (flag)
	{
		cout << "No Compilation Error Detected\n"
			<< endl;
	}
	else
	{
		cout << "CompileTimeError Detected\n"
			<< endl;
	}
	return 0;
}

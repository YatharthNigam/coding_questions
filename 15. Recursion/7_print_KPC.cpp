// PRINT KPC

// 1. You are given a string str. The string str will contains numbers only, where each number stands for a key pressed on a mobile phone.
// 2. The following list is the key to characters map
//     0 -> .;
//    1 -> abc
//    2 -> def
//    3 -> ghi
//    4 -> jkl
//    5 -> mno
//    6 -> pqrs
//    7 -> tu
//    8 -> vwx
//    9 -> yz

// Sample Input
// 78
// Sample Output
// tv
// tw
// tx
// uv
// uw
// ux

#include <iostream>
using namespace std;

string codes[] = {".;", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tu", "vwx", "yz"};

void printKPC(string ques, string asf)
{
    // Print in ques length becomes zero i.e. all digits have been covered.
    if (ques.size() == 0)
    {
        cout << asf << endl;
        return;
    }
    char ch = ques[0];
    string rem = ques.substr(1, ques.size());
    // first code's letters
    string code = codes[ch - '0'];
    // Calling for each char in first code.
    for (auto i : code)
    {
        printKPC(rem, asf + i);
    }
}

int main()
{
    string str;
    cin >> str;
    printKPC(str, "");
}
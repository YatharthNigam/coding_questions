// 1. You are given a number n representing number of stairs in a staircase.
// 2. You are standing at the bottom of staircase. You are allowed to climb 1 step, 2 steps or 3 steps in one move.
// 3. Complete the body of printStairPaths function - without changing signature - to print the list of all paths that can be used to climb the staircase up.
// Use sample input and output to take idea about output.

// Sample Input
// 3
// Sample Output
// 111
// 12
// 21
// 3

// Explanation: Just make tree and you'll understand.

#include <iostream>
using namespace std;

void printStairPaths(int n, string psf)
{
    // write your code here
    if (n == 0)
    {
        cout << psf << endl;
        return;
    }
    if (n > 0)
    {
        psf += "1";
        printStairPaths(n - 1, psf);
        psf.pop_back();
    }
    if (n > 1)
    {
        psf += "2";
        printStairPaths(n - 2, psf);
        psf.pop_back();
    }
    if (n > 2)
    {
        psf += "3";
        printStairPaths(n - 3, psf);
        psf.pop_back();
    }
}

int main()
{

    int n;
    cin >> n;
    printStairPaths(n, "");
}
/*
I-B-H Technique

Step 1: Hypothesis - Idea ki question me kya hoga e.g. in this ques print kar ke ek kam.
Step 2: Induction - Code ki kaise karna hai. Hypothesis execute kaise karoge.
Step 3: Base Condition - Smallest possible output pe khatam karna hai recursion.
*/

#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    void series(int n, int i)
    {
        if (i == n)
        {
            cout << n << " ";
            return;
        }
        cout << i << " ";
        series(n, i + 1);
    }
};

int main()
{
    Solution obj;
    int n = 10;
    obj.series(n, 1);
    return 0;
}
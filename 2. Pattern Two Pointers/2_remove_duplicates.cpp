// REMOVE DUPLICATES

// Problem Statement
// Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space;
// after removing the duplicates in-place return the new length of the array.

// Example 1:

// Input: [2, 3, 3, 3, 6, 9, 9]
// Output: 4
// Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
// Example 2:

// Input: [2, 2, 2, 11]
// Output: 2
// Explanation: The first two elements after removing the duplicates will be [2, 11].

// Solution: Take two pointers. One always pointing at the non repeating element and one which moves forward
// and whenever sees a new element, replaces the next of non repeating element and increases non repeating
// pointer by one.

#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> v = {2, 3, 3, 3, 6, 9, 9};
    int len = v.size();
    int next_non_duplicate = 0;
    for (int i = 1; i < len; i++)
    {
        if (v[i] != v[next_non_duplicate])
        {
            v[next_non_duplicate++] = v[i];
            // next_non_duplicate++;
        }
    }
    cout << next_non_duplicate;
    // int prev = v[0], curr;
    // int j = 1;
    // for (int i = 1; i < v.size(); i++)
    // {
    //     curr = v[i];
    //     if (prev != curr)
    //     {
    //         v[j++] = curr;
    //         prev = curr;
    //     }
    // }
    // cout << j;
}

// Similar Questions #
// Problem 1: Given an unsorted array of numbers and a target ‘key’,
// remove all instances of ‘key’ in-place and return the new length of the array.

// Example 1:

// Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
// Output: 4
// Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].
// Example 2:

// Input: [2, 11, 2, 2, 1], Key=2
// Output: 2
// Explanation: The first two elements after removing every 'Key' will be [11, 1].
// Solution: This problem is quite similar to our parent problem.
// We can follow a two-pointer approach and shift numbers left upon encountering the ‘key’.

// Code:

// int nextElement = 0;
// for (int i = 0; i <v.size(); i++) {
//     if (v[i] != v[nextElement]) {
//         v[nextElement] = v[i];
//         nextElement++;
//     }
// }
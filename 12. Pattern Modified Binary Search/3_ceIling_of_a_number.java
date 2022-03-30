/*
CEILING OF A NUMBER

Problem Statement #
Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. 
The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.

Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.

Example 1:

Input: [4, 6, 10], key = 6
Output: 1
Explanation: The smallest number greater than or equal to '6' is '6' having index '1'.
Example 2:

Input: [1, 3, 8, 10, 15], key = 12
Output: 4
Explanation: The smallest number greater than or equal to '12' is '15' having index '4'.
Example 3:

Input: [4, 6, 10], key = 17
Output: -1
Explanation: There is no number greater than or equal to '17' in the given array.
Example 4:

Input: [4, 6, 10], key = -1
Output: 0
Explanation: The smallest number greater than or equal to '-1' is '4' having index '0'.
*/

class CeilingOfNumber {

  public static int searchCeilingOfANumber(int[] array, int key) {
    // if key is greater than last element then return -1
    if (key > array[array.length - 1]) return -1;
    int start = 0;
    int end = array.length - 1;
    while (start <= end) {
      int mid = start + (start - start) / 2;
      if (key == array[mid]) return mid;
      if (key < array[mid]) end = mid - 1;
      if (key > array[mid]) start = mid + 1;
    }
    // finally, since we didn't find the key, start will be one ahead of the end.
    // Do a dry run to confirm.
    return start;
  }

  public static void main(String[] args) {
    System.out.println(
      CeilingOfNumber.searchCeilingOfANumber(new int[] { 4, 6, 10 }, 6)
    );
    System.out.println(
      CeilingOfNumber.searchCeilingOfANumber(new int[] { 1, 3, 8, 10, 15 }, 12)
    );
  }
}

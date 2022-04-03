#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    void generateAllSubsets(vector<int> &nums, int currentIndex, vector<int> &res, vector<vector<int>> &powerSet)
    {
        // base condition
        if (currentIndex >= nums.size())
        {
            powerSet.push_back(res);
            return;
        }
        int currentVal = nums[currentIndex];
        res.push_back(currentVal);
        generateAllSubsets(nums, currentIndex + 1, res, powerSet);
        // remove the currentVal (not considering)
        res.pop_back();
        generateAllSubsets(nums, currentIndex + 1, res, powerSet);
    }
    vector<vector<int>> subsets(vector<int> &nums)
    {
        vector<vector<int>> powerSet;
        vector<int> res;
        generateAllSubsets(nums, 0, res, powerSet);
        return powerSet;
    }
};

int main() {
    Solution obj;
    vector<int> v = {1, 2, 3, 4, 5, 6};
    vector<vector<int> >ans =obj.subsets(v);
    sort(ans.begin(), ans.end());
    for(int i = 0; i < ans.size(); i++)
    {
        for(int j = 0; j < ans[i].size(); j++)
            cout<<ans[i][j]<<' ';
        cout<<endl;
    }
    return 0;
}

// A similar question is COMBINATIONS where range 1 to n numbers are given and int k is given. 
// Find all the combinations(subsets) whose length is <= k.
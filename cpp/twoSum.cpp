// Two Sum

#include <vector>
#include <unordered_map>
using namespace std;
// Remove these 2 lines when submitting onto leetcode

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap;
        // creates a hash map
        int n = nums.size();


        for (int i = 0; i < n; i ++){
            int complement = target - nums[i];
            if (numMap.count(complement)){
                return {numMap[complement], i};
            }
            numMap[nums[i]] = i;
        }
        return {};
    }
};

// Working solution
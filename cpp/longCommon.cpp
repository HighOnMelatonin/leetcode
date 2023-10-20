//Longest common prefix

#include <iostream>
#include <vector>
#include <string.h>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix;
        prefix = strs[0];

        int prefixLength = size(prefix);

        for (int i = 0; i < prefixLength; i++)
        {
            if (size(prefix) == 0)
            {
                return "";
            }

            else
            {
                for (int j = 0; j < size(strs); j ++)
                {
                    if (strs[j][i] != prefix[i])
                    {
                        return prefix.substr(0,i);
                    }
                }
            }
        }

        return prefix;
    }
};

//Working solution
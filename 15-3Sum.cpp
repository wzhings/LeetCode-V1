// No. 15 - 3Sum.cpp

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
    	sort(nums.begin(), nums.end()); // sort the nums array
    	vector<vector<int>> res; // initial an array as list of list

    	for(int i = 0; i < nums.size(); i++) 
    	{
    		if ((i > 0) && (nums[i] == nums[i-1])) // from i = 1, skip the duplicate
    			continue;
    		int l = i + 1, r = nums.size() - 1; // set th left = i+1, right = final one

    		while (l < r) 
    		{
    			int s = nums[i] + nums[l] + nums[r]; // check the results
    			if (s < 0) // because already sorted
    				l += 1;
    			else if (s > 0)
    				r -= 1;
    			else 
    			{   // equal to zero
    				res.push_back(vector<int> {nums[i], nums[l], nums[r]}); // record this list
    				while( l < r && nums[l] == nums[l+1]) // if repeat, move forward it
    					l++;
    				while( l < r && nums[r] == nums[r-1]) // if repeat, move backward it
    					r--;
    				l++; // move to the next one
    				r--;
    			}
    		}
    	}
        
        return res;      
    }
};
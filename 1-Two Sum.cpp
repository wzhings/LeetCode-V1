class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash;
	    vector<int> result;
	    for (int i = 0; i < nums.size(); i++) {
		    int numberToFind = target - nums[i]; //get the number needed

            //If I can find the number in hash
		    if (hash.find(numberToFind) != hash.end()) {
                //Then, save the index of original index and current index
			    result.push_back(hash[numberToFind]);
			    result.push_back(i);
			    //return the list			
			    return result;
		    }

            //if the number is in the hash, then save the index
		    hash[nums[i]] = i;
	    }
	    return result;
        
    }
};

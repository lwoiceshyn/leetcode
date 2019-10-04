/*
https://leetcode.com/problems/counting-bits/
*/


class Solution {
public:
	/*
	If the number is even, the last bit is 0, otherwise if odd, the last bit is 1. We can determine
	this by &ing the number by 1. In the even case, the number of 1-bits is the exact same as this integer
	right shifted by 1, since all this new value added was a zero bit. We're guaranteed to have already
	encountered that integer, so simply copy this value to the current index. Otherwise, if it's odd,
	it's simply 1 + the previous integer.

	Time Complexity: O(n)
	Space Complexity: O(n)
	*/
    vector<int> countBits(int num) {
        vector<int> res(num+1,0);
        for (int i = 1; i <= num; i++){
        	if((i&1) == 0){
        		res[i] = res[i >> 1];
        	}else{
        		res[i] = 1 + res[i-1];
        	}
        }
        return res;
    }	
};
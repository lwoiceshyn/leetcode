/*
https://leetcode.com/problems/number-of-1-bits/
*/

class Solution {
public:
	/*
	If the rightmost bit in the unsigned int is a 1-bit, if we & it with the unsigned int 1, we will get
	1 back. Thus, we simply need to check if the rightmost bit is a 1, then right shift it by 1, and & it
	with 1 every time, increasing our count by 1 when this & yields 1. Repeat this until n == 0, when we've 
	right shifted all of the non-zero bits, leaving just a 0 int.
	*/
    int hammingWeight(uint32_t n) {
        int count = 0;
        while (n > 0){
        	if (n & 1){
                count += 1;
            }
        	n = n >> 1;
        }
        return count;
    }
};
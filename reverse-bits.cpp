/*
https://leetcode.com/problems/reverse-bits/
*/
class Solution {
public:
	/*
	Start at the end of our input, and iterate 32 times to cover all bits. Initialize our result value as 0. First, left shift
	our result value, so that we move to the next bit. Check if the last bit of the input is 1, and if so, set the first bit of 
	our result int as 1, and if not, leave it as zero. Then, right shift our input. By doing this, we're essentially looking at
	each bit in our input, one at at time, and throwing it on our reversed int, and doing opposite shift operations to ensure that
	our final result is a reversed version.
	
	*/
    uint32_t reverseBits(uint32_t n) {
        uint32_t res = 0;
        for (int i=0; i<32; i++) {
        	res = res << 1;
        	if ((n&1) == 1) {
        		res +=1;
        	}
        	n = n >> 1;
        }
        return res;
    }
};
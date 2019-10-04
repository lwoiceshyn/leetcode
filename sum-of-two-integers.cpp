/*
https://leetcode.com/problems/sum-of-two-integers/
*/

class Solution {
public:
	/*
	Addition of the binary representation of two integers is the same as adding decimal numbers, but carries happen there
	are two 1 bits being added in a column. The addition process can be broken down into finding the carry columns, finding
	the sum of the columns that don't result in a carry, and then left shifting the carries by 1. These three steps need to
	be repeated until there are no carries left in the addition. Thus, first use the & operator to find the carry columns,
	where both bits are 1s. Then, use the XOR operator(^) to find the sum of the non-carry columns (results in a 1 if either
	bit is 1, and 0 if both are 1 or 0). Lastly, left shift the carries, and repeat the process.

	We use one of the input integers to store the non-carry sum, and one to store the carries, and simply use a while loop to
	repeat the process until the carries become 0.
	*/
    int getSum(int a, int b) {
        if(a == 0) return b;
        if(b == 0) return a;

        while(b != 0){
            unsigned int carry = a & b;
            a = a ^ b;
            b = carry << 1;
        }
        
        return a;

    }
};
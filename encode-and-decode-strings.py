'''
https://www.lintcode.com/problem/encode-and-decode-strings/

'''

class Solution:
	'''
	Simple solution that utilizes pythons ord() and chr() mapping functions to
	map each string to a space separated string of the ordinal values for each character,
	and then adds a double-space separation for each string in the list.
	'''
    def encode(self, strs):
        ords = []
        for string in strs:
            ords.append(' '.join([str(ord(c)) for c in string]))
        return '  '.join(ords)
    def decode(self, str):
        strs = []
        ords = str.split('  ')
        for ordinal in ords:
            strs.append(''.join([chr(int(integer)) for integer in ordinal.split(' ')]))
        return strs

class Solution:
	'''
	Solution that doesn't use any built-in help from Python. Define our encoding as 
	the length of the string + a start character + the string. Then, we know that
	once we reach a start character, we can fetch the length, and then fetch
	the corresponding string. The tricky part is the fact that the length can
	be different numbers of digits, so we have to keep track of this as well
	when we are decoding.

	If we start on the first character of the length, then we can count how
	many times until we see the start character, and then we know how many 
	digits there are in the length. We can simply read this info from the
	string, grab the substring based on the length, and then advance our
	while loop pointer to the first character of the length of the 
	proceeding string (i += length+1), and reset our digits counter to 0.
	'''
    def encode(self, strs):
        ret_string = ''
        for string in strs:
            ret_string += str(len(string)) + '#' + string
        return ret_string
    def decode(self, str):
        strs = []
        i = 0
        digits = 0
        while i < len(str):
            if str[i] == '#':
                length = int(str[i-digits:i])
                strs.append(str[i+1:i+1+length])
                i += length+1
                digits = 0
            else:
                i +=1
                digits +=1
        return strs
package leetcode_practice.ex02_len_longest_substr;

import java.util.*;

class Solution{
	public int lengthOfLongestSubstring(String s) {
	Map<Character, Integer> left = new HashMap<Character, Integer>();
	Map<Character, Integer> right = null;
	int i = 0;
	int len_l = 0;
	int len_r = 0;
	while(i < s.length()){
		if (left == null || !left.containsKey(s.charAt(i))){
			left.put(s.charAt(i), i);
			len_l++;
		}
		else {
			if (len_l > len_r)
			{
				right = left;
				len_r = len_l;
				len_l = 0;
				left = new HashMap<Character, Integer>();
			}
		}
		i++;
	}
	if (len_l > len_r)
	{
		right = left;
		len_r = len_l;
	}
	return len_r;
	}
}

public class len_longest{
	public static void main(String[] args){
	Solution s = new Solution();
	int ans = s.lengthOfLongestSubstring("pwwkewabcdwabc");
	System.out.println(ans);
	}
}

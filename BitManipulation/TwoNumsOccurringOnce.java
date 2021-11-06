/*

LC 260

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

*/


class TwoNumsOccurringOnce {
    public int[] singleNumber(int[] nums) {
        
        /* solution 1 - use a set
        read element, if element already present in set then remove it -- it appeared 2 times
        by end of reading all elements, set will contain only those that appeared only once.
        Time complexity: O(N)
        Space complexity: O(N)
        */
        
        //Can we reduce space used ?
        /*
        using XOR, by end of iteration --> result is num1 ^ num2
         result will contain '1' bits set at the location where the 2 numbers are different
         find rightmost bit and do XOR with that bit again,
         this will give us 1 number
         use the first XOR product and this number to get second number
        
        
        */
        
        int n = nums.length;
        
        int xorProduct = 0;
        
        
        
        for(int i=0; i<n; ++i){
            xorProduct ^= nums[i];
        }
        
        int rightMostBit = xorProduct & -xorProduct;
        int a = 0;
        
        for(int i=0; i<n; ++i){
            if ((nums[i] & rightMostBit) != 0) { //Do XOR with only those which contain the rightmost bit
                a ^= nums[i];
            }
        }
        
        return new int[]{a,xorProduct^a};
        
    }
}
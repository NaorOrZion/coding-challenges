public class Solution {
    // Solution 1 - Time: O(n), Space: O(n)    
    public void Rotate(int[] nums, int k) {       
        int[] output = new int[nums.Length];
        for(int i = 0; i < nums.Length; i++) {
            output[(i + k) % nums.Length] = nums[i];
        }
        for(int i = 0; i < nums.Length; i++) {
            nums[i] = output[i];
        }
    }
    //Bubble sort
    public void Rotate(int[] nums, int k) {
        int temp;
        for(int j = 0; j < k; j++){
            for(int i = nums.Length-1 ; i > 0 ; i--){
                temp = nums[i-1];
                nums[i-1] = nums[i];
                nums[i] = temp;
            }            
        }        
    }
}
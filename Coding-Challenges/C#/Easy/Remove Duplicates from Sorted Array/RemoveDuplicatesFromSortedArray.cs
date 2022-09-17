public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int flag = nums[0];
        int count_dash = 1;
        int temp;
        for(int i = 1; i < nums.Length; i++){
            if(flag != nums[i]){
                flag = nums[i];
                count_dash++;
            }
            else{
                nums[i] = 999;
            }
        }
        for(int i = 0; i < nums.Length; i++){
            for(int j = 0; j < nums.Length-1; j++){
                if(nums[j] == 999){
                    temp = nums[j+1];
                    nums[j+1] = nums[j];
                    nums[j] = temp;
                }
            }
        }
        return count_dash;
    }
}
public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        for(int i = 0; i < nums.Length; i++){
            for(int j = 0; j < nums.Length; j++){
                if(j != i)
                    if(nums[j] == nums[i])
                        return true;     
            }
        }
        return false;
    }
}
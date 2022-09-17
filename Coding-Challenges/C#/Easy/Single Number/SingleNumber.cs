using System.Collections.Generic;

public class Solution {
    public int SingleNumber(int[] nums) {
        IDictionary<int, int> number_occurrence = new Dictionary<int, int>();
        for(int i = 0; i < nums.Length; i++){
            if(!number_occurrence.ContainsKey(nums[i])){
                number_occurrence.Add(nums[i], 1);
            }else{
                number_occurrence[nums[i]] += 1;
            }
        }
        
        for(int i = 0; i < nums.Length; i++){
            if(number_occurrence[nums[i]] == 1){
                return(nums[i]);
            }
        }
        return 0;
    }
}
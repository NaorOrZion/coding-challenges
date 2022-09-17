public class Solution {
    //Time: O(n^2) Complexity, Space: O(N) Complexity
    public int[] TwoSum(int[] nums, int target) {
        int[] indices = new int[2];
        for(int i = 0; i < nums.Length; i++){
            for(int j = 0; j < nums.Length; j++){
                if(i != j){
                    if(nums[i] + nums[j] == target){
                        indices[0] = i;
                        indices[1] = j;
                    }
                }
            }
        }
        return indices;
    }

    ////Time: O(n) Complexity, Space: O(N) Complexity
    public int[] TwoSum(int[] nums, int target) {
        //A key: nums[i] and value: i
        Hashtable indexMap = new Hashtable();
        int requiredNum;
        
        for(int i = 0; i < nums.Length; i++){
            requiredNum = target - nums[i];
            if(indexMap.ContainsKey(requiredNum)){
                int[] indices = {(int)indexMap[requiredNum], i};
                return indices;
            }else if(!indexMap.ContainsKey(nums[i]))
                indexMap.Add(nums[i], i);
        }
        return null;
    }
}
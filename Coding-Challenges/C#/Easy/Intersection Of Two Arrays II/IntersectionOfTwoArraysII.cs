using System.Collections.Generic;

public class Solution {
    public int[] Intersect(int[] nums1, int[] nums2) {             
        int count = 0;
        int x = 0;
        LinkedList<int> intersected = new LinkedList<int>();
        
        for(int i = 0; i < nums1.Length; i++){
            for(int j = 0; j < nums2.Length; j++){
                if(nums1[i] == nums2[j]){
                    intersected.AddLast(nums1[i]);
                    nums1[i] = 9999;
                    nums2[j] = 9999;
                    count++;
                    break;
                }
            }
        }
        int[] answer = new int[count];
        
        foreach(int num in intersected){
            answer[x] = num;
            x++;
        }

        return answer;
    }
}
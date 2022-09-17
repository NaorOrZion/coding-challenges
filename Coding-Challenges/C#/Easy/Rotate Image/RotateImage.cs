public class Solution {
    public void Rotate(int[][] matrix) {
        int temp;
        //Reverse the elements in the array
        for(int i = 0; i < matrix.Length; i++){
            Array.Reverse(matrix[i]);
        }

        for(int i = 0; i < matrix.Length; i++){
            for(int j = 0; j < matrix.Length; j++){
                if(i < j){
                    temp = matrix[i][matrix.Length-1-j];
                    matrix[i][matrix.Length-1-j] = matrix[j][matrix.Length-1-i];
                    matrix[j][matrix.Length-1-i] = temp;
                }
            }     
        }
    }
}
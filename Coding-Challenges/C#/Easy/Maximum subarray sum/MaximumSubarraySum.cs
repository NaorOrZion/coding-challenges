using System;

public static class Kata
{
  public static int MaxSequence(int[] arr) 
  {
    if (arr.Length == 0)
      return 0;
    
    int maxsum = arr[0]+arr[1];
    int tempsum = 0;
    int j = 1, mekademj = 1;

    for(int i = 0; i < arr.Length; i++)
    {
      tempsum += arr[i];
      
      while(j < arr.Length)
      {      
        tempsum += arr[j];
        if (tempsum > maxsum)
          maxsum = tempsum;
        j++;
      }
      
      mekademj++;
      j = mekademj;
      tempsum = 0;
    }
    
    return maxsum;
  }
}
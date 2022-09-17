using System;
public static class Kata
{
   public static int CountCombinations(int money, int[] coins)
   {
     int j = 0;
     return solve(money, coins, j);
   }
  
   public static int solve(int money, int[] coins, int j)
   {
    if(money == 0)
    {
     return 1;   
    }
    if(money < 0)
    {
      return 0;
    }
    
    int count = 0;
    for(int i = j; i < coins.Length; i++)
    {
      count += solve(money - coins[i], coins, i);
    }
    return count;
   }
}
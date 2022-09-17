using System;
public class Scramblies 
{
    
    public static bool Scramble(string str1, string str2) 
    {
      string word = "";
      Console.WriteLine("str1: " + str1 + " \nstr2: " + str2);
      for(int i = 0; i < str2.Length; i++)
      {
        for(int j = 0; j < str1.Length; j++)
        {
          if(str1[j] == str2[i])
          {
            word += str1[j];
            str1 = str1.Remove(j, 1);
            break;
          }
        }
      }
      Console.WriteLine("word: " + word);
      if(word == str2)
      {
        Console.WriteLine("True!");
        return true;
      }
      else
      {
        Console.WriteLine("False!");
        return false;
      }
        
    }

}
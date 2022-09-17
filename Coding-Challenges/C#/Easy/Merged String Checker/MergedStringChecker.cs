using System;
public class StringMerger
{
    public static bool isMerge(string s, string part1, string part2)
    {
        if (s.Length != part1.Length + part2.Length)
        {
            return false;
        }
        if (s == "")
        {
            return true;
        }

        if (part1.Length > 0 && s[0] == part1[0])
        {
            if (isMerge(s.Substring(1), part1.Substring(1), part2.Substring(0)))
            {
                return true;
            }
        }
        if (part2.Length > 0 && s[0] == part2[0])
        {
            if (isMerge(s.Substring(1), part1.Substring(0), part2.Substring(1)))
            {
                return true;
            }
        }

        return false;
    }
}
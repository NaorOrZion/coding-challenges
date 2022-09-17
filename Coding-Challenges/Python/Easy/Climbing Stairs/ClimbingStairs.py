class Solution(object):
    def climbStairs(self, n):
        '''
        
        if n == 0:
            return 1
        return climbStairs(self, n-1) + climbStairs(self, n-2)
        '''
        if n==1 or n==2:
            return n 
        
        counter = 2
        list1 = [1, 2]
        i = 0
        j = 1
        while(n != counter):
            list1.append(list1[i]+list1[j])
            counter += 1
            i += 1
            j += 1
            
        return list1[-1]
            
        
        
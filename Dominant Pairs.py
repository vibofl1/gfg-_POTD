 from typing import List


class Solution:
    def dominantPairs(self, n : int, arr : List[int]) -> int:
        
        
        arr[:n//2]=sorted(arr[:n//2])
        arr[n//2:]=sorted(arr[n//2:])
        i=n//2 -1
        j=n-1
        c=0
        # print(arr) 
        while i>=0 and j>=n//2 :
            # print(arr[i],arr[j])
            if arr[i]>=5*arr[j]:
                  c+= j - n//2  +1 
                  i-=1 
            else:
                j-=1
        
            
            
        return c
        
        
        
        # code here
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.dominantPairs(n, arr)
        
        print(res)
        

# } Driver Code Ends
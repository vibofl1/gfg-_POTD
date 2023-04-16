from typing import List
class Solution:
    def solve(self, N : int,a : List[int], b : List[int]) -> int:
        # code here
        oa=[]
        ea=[]
        ob=[]
        eb=[]
        # print(oa,ob,ea,eb)
        for i in range(N):
            if a[i]%2==0:
                ea.append(a[i])
            else:
                oa.append(a[i])
                 
            if b[i]%2==0:
                    eb.append(b[i])
            else :
                    ob.append(b[i])
                
                
        # print(oa,ob,ea,eb)
            
            
            
        if sum(a)!=sum(b) or len(oa)!=len(ob) or len(ea)!=len(eb):
            return -1 
            
        oa.sort()
        ea.sort()
        ob.sort()
        eb.sort()
        ans=0
        for i in range(len(oa)):
            x=abs(oa[i]-ob[i])
            ans+=(x//2)
        for i in range(len(eb)):
            x=abs(eb[i]-ea[i])
            ans+=(x//2)
        
        return ans//2    
         
        
            
         
        
        
        



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
        
        N = int(input())
        
        
        A=IntArray().Input(N)
        
        
        B=IntArray().Input(N)
        
        obj = Solution()
        res = obj.solve(N, A, B)
        
        print(res)
        

# } Driver Code Ends
#User function Template for python3
# two methods :
#sorting of map can be done by importing SortedDict
from sortedcontainers import SortedDict
class Solution: 
    def maxIntersections(self, arr, N):
        mp={}
        for x in arr:
            s = x[0]
            e = x[1]+1
            mp[s] = mp.get(s, 0) + 1
            mp[e] = mp.get(e, 0) - 1
        mmax=0
        presum=0
        # mp=SortedDict(mp)
         
        for x in sorted(mp):
            presum+=mp[x]
            mmax=max(mmax,presum)
        return mmax
        
            
            
        
             
            
        # Code here
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N = int(input())
        lines=[[] for j in range(N)]
        for j in range(2):
            prr = [int(i) for i in input().split()] 
            for i in range(N): 
                lines[i].append(prr[i])
            
    
        ob = Solution()
        print(ob.maxIntersections(lines, N))
        
        T -= 1

# } Driver Code Ends
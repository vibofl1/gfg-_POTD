#User function Template for python3

class Solution():
    def solve(self, a, b, c):
        arr=[a,b,c]
        arr.sort(reverse=True)
        if  arr[0] /2 >arr[1]+arr[2]+1:
            return -1
        else:
            return sum(arr)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import Counter
for _ in range(int(input())):
    a, b, c=map(int,input().split())
    obj = Solution()
    res = obj.solve(a, b, c)
    
    print(res)
# } Driver Code Ends
#User function Template for python3

class Solution():
    def maxSweetness(self, arr, n, k):
        l=0
        h=sum(arr)
        while l<=h:
            mid= (l+h)//2
            piece,sweet=0,0
            for x in arr:
                sweet+=x
                if (sweet>=mid):
                    piece+=1
                    sweet=0
            if piece<k+1:
                h=mid-1
            else :
                l=mid+1  
        return h 
                
            
                
    
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n,k = map(int, input().split())
    sweetness = [int(i) for i in input().split()]
    print(Solution().maxSweetness(sweetness, n,k))
# } Driver Code Ends
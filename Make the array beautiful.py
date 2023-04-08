#User function Template for python3

 

class Solution:
    #approach 2 comparing with   front  element of stack
    def makeBeautiful(self, arr):
         
        l=[arr[0]]
        for i in range(1,len(arr)):
            if  len(l)==0:
                l.append(arr[i])
            elif (arr[i]>=0 and l[-1]>=0 )or (arr[i]<0 and l[-1]<0):
                l.append(arr[i])
            else:
                l.pop()
                
        return l 
    def makeBeautiful(self, arr):
        n=len(arr)-1
        if n==0:    
            return arr
        arr1=arr
        l=[]
        i=0 
        while 1:
            if i> len(arr)-2 or len(arr)==0  or len(arr)==1 :
                    break
             
            if((arr[i] > 0 and arr[i + 1] < 0) or (arr[i] < 0 and arr[i + 1] > 0) or (arr[i] < 0 and arr[i + 1] == 0) or (arr[i] == 0 and arr[i + 1] < 0)) :        
                    
                arr.pop(i)
                arr.pop(i)
                if i!=0:
                    i-=1
            
                # print(arr) 
            
            else:
                i+=1
         
                
        return arr
                
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        arr = list(map(int,input().split()))
        
        obj = Solution()
        res = obj.makeBeautiful(arr)
        print(*res)
# } Driver Code Ends
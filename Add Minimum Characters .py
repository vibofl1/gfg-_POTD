#User function Template for python3

class Solution:
    def addMinChar (self, str):
        # if str[::-1]==str:
        #     return 0
        # mp={}    
        # for x in str:
        #     if x in mp:
        #         mp[x]+=1
        #     else:
        #         mp[x]=1 
        
        # i=0
        # for x in mp:
        #     if mp[x]%2!=0:
        #         i+=1
             
                
        # return i 
        n=len(str)
        i=0
        j=n-1 
        ans=0
        
        while i<=j:
            
            # print(str[i],str[j])
            if str[i]==str[j]:
            
                i+=1
                j-=1
                # print(str[i],str[j])
            else:
                
                i=0
                ans+=1
                j=n-1 - ans
                
                # print(j,ans,str[i],str[j])
                
        return ans
                
        
            
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str1 = input()

        ob = Solution()
        print(ob.addMinChar(str1))

# } Driver Code Ends
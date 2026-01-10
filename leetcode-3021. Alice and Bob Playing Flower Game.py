class Solution:
    def flower(self,n:int,m:int)->int:
        # number of odd values from 1 to n
        odd_n=(n+1)//2
        # number of odd values from 1 to m
        odd_m=(m+1)//2
        # number of even values from 1 to n
        even_n=m//2
        # number of even values from 1 to m
        even_m=n//2
        
        #total number of ways the alice wins
        return int(odd_n*even_m+even_n*odd_m)

    
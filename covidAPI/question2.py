def subArray(A, n, B, sum):
    count=0
    for i in range (n - B + 1): 
        Nowsum = 0
        
        for j in range(B):
            Nowsum = (Nowsum + 
                            A[i + j])
  
        if (Nowsum <= sum):
            count+=1
    print(count)

A=list(map(int ,input().split()))
B=int(input())
sum = 1000
n = len(A)
subArray(A, n, B, sum)

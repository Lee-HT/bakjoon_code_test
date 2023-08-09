num = int(input())
N = [int(input()) for n in range(num)]

def fibonacci(nums):
  max_num = max(nums)
  dp = [[0,0] for i in range(max(2,max_num+1))]
  dp[0],dp[1] = [1,0],[0,1]
  for i in range(2,max_num+1):
    for j in range(2):
      dp[i][j] = dp[i-1][j] + dp[i-2][j]
  answer = [dp[n] for n in nums]
  for ans in answer:
    print(f"{ans[0]} {ans[1]}")

fibonacci(N)

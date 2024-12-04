N = int(input())
score = list(map(int,input().split()))
score.sort()
M = score[-1]
print(sum(score) / M *100 / N )
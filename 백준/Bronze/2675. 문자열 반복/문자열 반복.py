for T in range(int(input())):
    R , S = input().split()
    for N in range(len(S)):
        print(S[N]*int(R), end="")
    print("")
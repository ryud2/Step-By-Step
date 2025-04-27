def solution(polynomial):
    X = 0
    C = 0
    for i in polynomial.split(" "):
        if i[-1] == "x":
            if i == "x":
                X += 1
            else:
                X += int(i[:-1])
        elif i != "+":
            C += int(i)
    if X == 1 :
        X = ""
    if X == 0 :
        return f"{C}"
    elif C == 0:
        return f"{X}x"
    else:
        return f"{X}x + {C}"
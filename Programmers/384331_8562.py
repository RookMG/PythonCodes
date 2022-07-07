def solution(a, b, g, s, w, t):
    left = 0
    right = int(4e14)
    mid = int(1e7)
    l = len(g)
    while left<right:
        gmax,smax,wmax = 0,0,0
        for _ in range(l):
            w_ = ((mid+t[_])//(2*t[_]))*w[_]
            wmax += min(w_,g[_]+s[_])
            gmax += min(w_,g[_])
            smax += min(w_,s[_])
        if a<=gmax and b<=smax and (a+b)<=wmax:
            if mid-left == 1 :
                return mid
            right = mid
        else:
            if right-mid == 1:
                return right
            left = mid
        mid = (right+left)//2
    return mid

print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))
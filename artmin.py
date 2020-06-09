def flip(n):

    if n==0:
        return 0

    elif n==1:
        return 1

    else:
        return flip(n-1)+flip(n-2)
        
                
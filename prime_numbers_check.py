def get_prime(integer):    
    if integer <= 1:
        return False
    elif integer > 100:
        exit()
    else:        
        prime = True
        for num in range(2, integer):
            if integer % num == 0:
                prime == False
            else:
                prime == True
    if prime == True:
        print("Prime")
    else:
        print("Not prime")
n = int(input())
get_prime(n)
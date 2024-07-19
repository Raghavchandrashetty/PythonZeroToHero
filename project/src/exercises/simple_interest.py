def simple_interest_calculator(p, r, t):
    simple_interest = (principal * rate_oif_interest * tenure) / 100
    return simple_interest




principal = float(input("enter principal amount"))
rate_oif_interest = float(input("enter rate of interest"))
tenure = int(input("enter tenure"))

res = principal + simple_interest_calculator(principal, rate_oif_interest, tenure)
print("Res : ", res)

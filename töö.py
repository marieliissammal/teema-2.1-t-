
import math

# 9. ülesanne

try:
    print("Nelinurga kontroll")
    k1=float(input("1. külje pikkus:"))
    k2=float(input("2. külje pikkus:"))
    k3=float(input("3. külje pikkus:"))
    k4=float(input("4. külje pikkus:"))
    if k1>0 and k2>0 and k3>0 and k4>0:
        if k1==k2==k3==k4:
            print("See on ruut.")
        else:
            print("Need on nelinurga küljed.")
    else:
        print("Viga küljed > 0")
    except ValueError:
        print("Viga: täisarv.")


# 10. ülesanne

tehed=["+", "-", "*", "/"]

try:
    arv1=float(input("Sisesta 1. arv: "))
    arv2=float(input("Sisesta 2. arv: "))
    tehe=input("Sisesta tehe: ")
    if tehe in tehed: 
        if tehe=="+":
            print(f"{arv1}{tehe}{arv2}={arv1+arv2}")
        elif tehe=="-":
            print(f"{arv1}{tehe}{arv2}={arv1-arv2}")
        elif tehe=="*":
            print(f"{arv1}{tehe}{arv2}={arv1*arv2}")
        elif tehe=="/":
            if arv2==0:
             print("DIV/0")
         else:
             print(f"{arv1}{tehe}{arv2}={arv1/arv2}")
    else:
        print("Tundmatu tehtemärk")

except ValueError:
    print("Viga: sisesta arvud")

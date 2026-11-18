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

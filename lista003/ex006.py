qtd = int(input())
for c in range(1, qtd + 1):
    if c == 1:
        print(f"{c} elefante incomoda muita gente...")
    else:
        print(f"{c} elefantes incomodam muita gente...")
        
    if c + 1 == 2:
        print(f"{c + 1} elefantes incomodam, incomodam muito mais...")
    else:
        incomodam_str = ", ".join(["incomodam"] * (c + 1))
        print(f"{c + 1} elefantes {incomodam_str} muito mais...")
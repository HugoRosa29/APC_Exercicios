def banner(n):
    if n % 2 == 0 and n >= 0:
        print("| | | | | | | | | |")
    elif n % 2 != 0 and n >= 0:
        print("- - - - - - - - - -")
    elif n % 2 == 0 and n < 0:
        print(". . . . . . . . . .")
    elif n % 2 != 0 and n < 0:
        print("= = = = = = = = = =")
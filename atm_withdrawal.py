def main():
    balance=float(input("enter the balance:-"))
    amount=float(input("enter the amount:-"))
    print("\n"+"-"*34)
    print(f"Balance :Rs{balance:.2f}")
    print(f"Requested Amount :Rs{amount:.2f}")
    print("-"*34)

    if amount <=0:
        print("invalid amount")
    elif amount>balance:
        print("insufficient balance")
    elif amount%100!=0:
        print("amount should be in multiples of 100")
    else:
        balance-=amount
        print(f"withdrawn amount :Rs{amount:.2f}")
        print(f"remaining balance :Rs{balance:.2f}")

    print("-"*34)
    print(f"Balance :Rs{balance:.2f}")

if __name__=="__main__":
    main()

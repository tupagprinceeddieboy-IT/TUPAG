while True:
    
    print("~~Choose operator~~\n1[+]\n2[-]\n3[x]\n4[÷]\n5[Exit]")
    choice = int(input("\nchoose operator: "))
    print("________________")

    if choice == 5:
        print("Bye bye!!")
        break

    if choice < 1 or choice > 5:
       print("Invalid operator, choose again")
       continue
      
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))

    if choice == 1:
        result = num1 + num2
    elif choice == 2:
        result = num1 - num2
    elif choice == 3:
        result = num1 * num2
    elif choice == 4:
        if num2 == 0:
            print("Error")
            continue
        result = num1 / num2  

    
    print("≈≈≈≈≈≈≈≈≈≈🐔RESULT🐔≈≈≈≈≈≈≈≈≈≈")
    print(f"answer: {result}")
    print("≈≈≈≈≈≈≈≈≈≈🐔RESULT🐔≈≈≈≈≈≈≈≈≈≈")
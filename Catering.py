#OPENING BANNER
print ("WELCOME")
message = ("\t"+"How can we excite you today!!")
print(message.title())

#PIZZA SIZE SELECTION
print("\n\t1. SMALL"+"\n\t2. MEDIUM"+"\n\t3. LARGE")
while True :
    pizza_size = input("\n PLEASE SELECT THE BASE SIZE : ")
    size = ['SMALL','MEDIUM','LARGE']
    pizza_size_dump = [ ]
    if pizza_size == '1':
        print("\n\tOK " + size[0] + " BASE SELECTED.")
        pizza_size_dump.append(size[0])
    elif pizza_size == '2':
        print("\n\tOK " + size[1] + " BASE SELECTED.")
        pizza_size_dump.append(size[1])
    elif pizza_size == '3':
        print("\n\tOK " + size[2] + " BASE SELECTED.")
        pizza_size_dump.append(size[2])
    else:
        print("\nPLEASE SELECT A VALID OPTION FROM THE LIST")
        continue
    break

#BASE SELECTION USING IF-ELIF-ELSE LOOP
print("\nSELECT THE TYPE OF CRUST"+"\n\t1. Normal-Crust"+"\n\t2. Pan-Fried"+"\n\t3. Cheese-Crust"+"\n\t4. Thin-Crust")
while True :
    base_selection = input("\nPLEASE ENTER YOUR CHOICE: ")
    pizza_base = ['Normal-Crust', 'Pan-Fried', 'Cheese-Crust', 'Thin-Crust']
    pizza_base_dump = []
    if base_selection == '1':
        print("\nOK!! " + pizza_base[0] + " base selected")
        pizza_base_dump.append(pizza_base[0])
    elif base_selection == '2':
        print("\nOK!! " + pizza_base[1] + " base selected")
        pizza_base_dump.append(pizza_base[1])
    elif base_selection == '3':
        print("\nOK!! " + pizza_base[2] + " base selected")
        pizza_base_dump.append(pizza_base[2])
    elif base_selection == '4':
        print("\nOK!! " + pizza_base[3] + " base selected")
        pizza_base_dump.append(pizza_base[3])
    else:
        print("\n" + "Please select a base from the above list")
        print("\ntry again.")
        continue
    break

#TOPPING SELECTION USING WHILE LOOP
print("\nSELECT THE TYPE OF TOPPINGS"+"\n\t1. olives"+"\n\t2. avocado"+"\n\t3. mushrooms")
pizza_toppings = ['olive', 'avocado', 'mushroom']
list = []
while True :
    pizza_topping_1 = input("\nPlease select a topping: ")
    if pizza_topping_1 == '1':
        print("ok " + pizza_toppings[0] + " selected")
        list.append(pizza_toppings[0])
    elif pizza_topping_1 == '2':
        print("ok " + pizza_toppings[1] + " selected")
        list.append(pizza_toppings[1])
    elif pizza_topping_1 == '3':
        print("ok " + pizza_toppings[2] + " selected")
        list.append(pizza_toppings[2])
    else:
        print("please select a valid topping option")
        continue
    break
choice = input("\nSelect an additional pizza topping ?(Y/N) : ")
choice_1 = 'Y'
choice_2 = 'y'
choice_3 = 'N'
choice_4 = 'n'
while choice not in (choice_1,choice_2,choice_3,choice_4):
    print("PLEASE SELECT Y or N"+"\n Try again")
    choice = input("\nSelect an additional pizza topping ?(Y/N) : ")
    continue
    break
else:
    while choice in (choice_1, choice_2):
        pizza_topping_2 = input("\nselect another topping from the list: ")
        if pizza_topping_2 == pizza_topping_1:
            print("\nTopping already selected, Please choose another one.")
            continue
            break
        elif pizza_topping_2 == '1':
            print("ok " + pizza_toppings[0] + " selected")
            list.append(pizza_toppings[0])
            print("\nSELECTED ITEMS IN YOUR LIST ARE:")
            print("\n1." + pizza_size_dump[0] + " BASE")
            print("\n2." + pizza_base_dump[0]+" Pizza")
            print("\n3." + list[0] + " and " + list[1] + " TOPPINGS")
            print("\nDELICIOUS PIZZA CHOICE!!")
            break
        elif pizza_topping_2 == '2':
            print("ok " + pizza_toppings[1] + " selected")
            list.append(pizza_toppings[1])
            print("\nSELECTED ITEMS IN YOUR LIST ARE:")
            print("\n1." + pizza_size_dump[0] + " BASE")
            print("\n2." + pizza_base_dump[0]+" Pizza")
            print("\n3." + list[0] + " and " + list[1] + " TOPPINGS")
            print("\nDELICIOUS PIZZA CHOICE!!")
            break
        elif pizza_topping_2 == '3':
            print("ok " + pizza_toppings[2] + " selected")
            list.append(pizza_toppings[2])
            print("\n" + list[0] + " and " + list[1] + " toppings")
            print("\nSELECTED ITEMS IN YOUR LIST ARE:")
            print("\n1." + pizza_size_dump[0] + " BASE")
            print("\n2." + pizza_base_dump[0]+" Pizza")
            print("\n3." + list[0] + " and " + list[1] + " TOPPINGS")
            print("\nDELICIOUS PIZZA CHOICE!!")
            break
    else:
        while choice in (choice_3, choice_4):
            print("\nSELECTED ITEMS IN YOUR LIST ARE:")
            print("\n1." + pizza_size_dump[0] + " BASE")
            print("\n2." + pizza_base_dump[0]+" Pizza")
            print("\n3." + list[0] + " TOPPINGS")
            print("\nDELICIOUS PIZZA CHOICE!!")
            break


#CONFIRM ORDER
count = 0
while True and count < 2:
    confirm_choice = input("\nDo you want to make any changes to your order(Y/N)??")
    confirm_choice_selection_1 = 'Y'
    confirm_choice_selection_2 = 'y'
    confirm_choice_selection_3 = 'N'
    confirm_choice_selection_4 = 'n'
    while confirm_choice in (confirm_choice_selection_1, confirm_choice_selection_2):
        print("\n\t 1. SIZE")
        print("\n\t 2. BASE")
        print("\n\t 3. TOPPINGS")
        print("\n\t 4. QUIT AND CONFIRM ORDER")
        change = input("\n Please select the change to be made.")
        change_choice_1 = '1'
        change_choice_2 = '2'
        change_choice_3 = '3'
        change_choice_4 = '4'
        if change == change_choice_1:
            count = count + 1
            print("\n\t1. SMALL" + "\n\t2. MEDIUM" + "\n\t3. LARGE")
            while True:
                pizza_size = input("\n PLEASE SELECT THE BASE SIZE : ")
                size = ['SMALL', 'MEDIUM', 'LARGE']
                pizza_size_dump = []
                if pizza_size == '1':
                    print("\n\tOK " + size[0] + " BASE SELECTED.")
                    pizza_size_dump.append(size[0])
                elif pizza_size == '2':
                    print("\n\tOK " + size[1] + " BASE SELECTED.")
                    pizza_size_dump.append(size[1])
                elif pizza_size == '3':
                    print("\n\tOK " + size[2] + " BASE SELECTED.")
                    pizza_size_dump.append(size[2])
                else:
                    print("\nPLEASE SELECT A VALID OPTION FROM THE LIST")
                break
        elif change == change_choice_2:
            count = count + 1
            print(
                "\nSELECT THE TYPE OF CRUST" + "\n\t1. Normal-Crust" + "\n\t2. Pan-Fried" + "\n\t3. Cheese-Crust" + "\n\t4. Thin-Crust")
            while True:
                base_selection = input("\nPLEASE ENTER YOUR CHOICE: ")
                pizza_base = ['Normal-Crust', 'Pan-Fried', 'Cheese-Crust', 'Thin-Crust']
                pizza_base_dump = []
                if base_selection == '1':
                    print("\nOK!! " + pizza_base[0] + " base selected")
                    pizza_base_dump.append(pizza_base[0])
                elif base_selection == '2':
                    print("\nOK!! " + pizza_base[1] + " base selected")
                    pizza_base_dump.append(pizza_base[1])
                elif base_selection == '3':
                    print("\nOK!! " + pizza_base[2] + " base selected")
                    pizza_base_dump.append(pizza_base[2])
                elif base_selection == '4':
                    print("\nOK!! " + pizza_base[3] + " base selected")
                    pizza_base_dump.append(pizza_base[3])
                else:
                    print("\n" + "Please select a base from the above list")
                    print("\ntry again.")
                    continue
                break
        elif change == change_choice_3:
            count = count + 1
            print("\nSELECT THE TYPE OF TOPPINGS" + "\n\t1. olives" + "\n\t2. avocado" + "\n\t3. mushrooms")
            pizza_toppings = ['olive', 'avocado', 'mushroom']
            list = []
            while True:
                pizza_topping_1 = input("\nPlease select a topping: ")
                if pizza_topping_1 == '1':
                    print("ok " + pizza_toppings[0] + " selected")
                    list.append(pizza_toppings[0])
                elif pizza_topping_1 == '2':
                    print("ok " + pizza_toppings[1] + " selected")
                    list.append(pizza_toppings[1])
                elif pizza_topping_1 == '3':
                    print("ok " + pizza_toppings[2] + " selected")
                    list.append(pizza_toppings[2])
                else:
                    print("please select a valid topping option")
                    continue
                break
            choice = input("\nSelect an additional pizza topping ?(Y/N) : ")
            choice_1 = 'Y'
            choice_2 = 'y'
            choice_3 = 'N'
            choice_4 = 'n'
            while choice not in (choice_1, choice_2, choice_3, choice_4):
                print("PLEASE SELECT Y or N" + "\n Try again")
                choice = input("\nSelect an additional pizza topping ?(Y/N) : ")
                continue
                break
            else:
                while choice in (choice_1, choice_2):
                    pizza_topping_2 = input("\nselect another topping from the list: ")
                    if pizza_topping_2 == pizza_topping_1:
                        print("\nTopping already selected, Please choose another one.")
                        continue
                        break
                    elif pizza_topping_2 == '1':
                        print("ok " + pizza_toppings[0] + " selected")
                        list.append(pizza_toppings[0])
                        print("\nSELECTED ITEMS IN YOUR LIST ARE:")
                        print("\n1." + pizza_size_dump[0] + " BASE")
                        print("\n2." + pizza_base_dump[0] + " Pizza")
                        print("\n3." + list[0] + " and " + list[1] + " TOPPINGS")
                        print("\nDELICIOUS PIZZA CHOICE!!")
                        break
                    elif pizza_topping_2 == '2':
                        print("ok " + pizza_toppings[1] + " selected")
                        list.append(pizza_toppings[1])
                        print("\nSELECTED ITEMS IN YOUR LIST ARE:")
                        print("\n1." + pizza_size_dump[0] + " BASE")
                        print("\n2." + pizza_base_dump[0] + " Pizza")
                        print("\n3." + list[0] + " and " + list[1] + " TOPPINGS")
                        print("\nDELICIOUS PIZZA CHOICE!! ")
                        break
                    elif pizza_topping_2 == '3':
                        print("ok " + pizza_toppings[2] + " selected")
                        list.append(pizza_toppings[2])
                        print("\n" + list[0] + " and " + list[1] + " toppings")
                        print("\nSELECTED ITEMS IN YOUR LIST ARE:")
                        print("\n1." + pizza_size_dump[0] + " BASE")
                        print("\n2." + pizza_base_dump[0] + " Pizza")
                        print("\n3." + list[0] + " and " + list[1] + " TOPPINGS")
                        print("\nDELICIOUS PIZZA CHOICE!!")
                        break
                else:
                    while choice in (choice_3, choice_4):
                        print("\nSELECTED ITEMS IN YOUR LIST ARE:")
                        print("\n1." + pizza_size_dump[0] + " BASE")
                        print("\n2." + pizza_base_dump[0] + " Pizza")
                        print("\n3." + list[0] + " TOPPINGS")
                        print("\nDELICIOUS PIZZA CHOICE!!")
                        break
        elif change == change_choice_4:
            print("OK ORDER CONFIRMED")
            j = 1
            if len(list) == j:
                print(
                    pizza_size_dump[0] + " Base " + pizza_base_dump[0] + " Pizza  with " + str(list[0]) + " Toppings ")
            else:
                print(pizza_size_dump[0] + " Base " + pizza_base_dump[0] + " Pizza " + str(list[0]) + " and " + str(
                    list[1]) + " Toppings ")
            exit()
    else:
        while confirm_choice in confirm_choice_selection_3 or confirm_choice_selection_4:
            # print("\n OK LETS MOVE TO PAYMENTS")
            print("\nORDER DETAILS ")
            i = 1
            if len(list) == i:
                print(pizza_size_dump[0] + " Base " + pizza_base_dump[0] + " Pizza " + str(list[0]) + " Toppings ")
                break
            else:
                print(pizza_size_dump[0] + " Base " + pizza_base_dump[0] + " Pizza " + str(
                    list[0].title()) + " and " + str(list[1].title()) + " Toppings")
                break











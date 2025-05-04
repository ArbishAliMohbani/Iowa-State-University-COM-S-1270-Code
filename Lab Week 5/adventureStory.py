# Arbish Ali Mohbani                02/22/2025
# Matthew Holman
# Lab # 5

def main():
    first_input = input("You found yourself within an abandoned wedding venue, you can see 3 dishes in front of you.\nDo you want to eat the [left], [center] or [right] dish: ")
    if(first_input == "left"):
        print("You ate the right one! You wake up back at your home.")
    elif(first_input == "center"):
        second_input = input(("You faint, now you are in a war torn castle, there is a chest & 2 keys ([left] or [right]) in front of you. Choose the right one: "))
        if(second_input == "left"):
            print("You wake up back at Home!")
        elif(second_input == "right"):
            third_input = input("You are now able to go inside the castle, choose one of the door marked [bloodcurling] or [apparition]: ")
            if(third_input == "apparition"):
                print("You are now stuck in your worst NIGHTMARE, until someone replaces you!")
            elif(third_input == "bloodcurling"):
                fourth_input = input("You are now part of the troop who captured the area, you have 2 options either [kill] the king or become king's [best] soldier: ")
                if(fourth_input == "kill"):
                    print("You have now become the KING, and you now wake up at home!")
                elif(fourth_input == "best"):
                    fifth_input = input("You have now become the King's best soldier, King assigns with you a task eithr you become [successful] or [unsuccessful]: ")
                    if(fifth_input == "successful"):
                        print("You wake up back at HOME!")
                    elif(fifth_input == "unsuccessful"):
                        print("You are now forever King's servant!")
    elif(first_input == "right"):
        print("You are now buried under this abandoned Wedding venue until someone replaces you, then you get to PLAY AGAIN!")


if __name__ == "__main__":
    main()
#Tevyah Hanley 5-28-2025 Assignment 1.3
#This program will count how many beers are on the wall and print out the lyrics to the song 99 bottles of beer on the wall, but based on the user's input.

#the function count_beer is running a while loop that will count down from the number of bottles the user inputs, until there is one bottle left, and change the lyrics to reflect that.
def count_beer(bottle):
    while bottle > 0:
        if bottle == 1:
            print(f"{bottle} bottle of beer on the wall, {bottle} bottle of beer.")
            print("Take one down, pass it around, no more bottles of beer on the wall.")

        else:
            print(f"{bottle} bottles of beer on the wall, {bottle} bottles of beer.")
            print(f"Take one down, pass it around, {bottle - 1} bottles of beer on the wall.")
        
        bottle -= 1

#the main function will ask the user to input the number of bottles, and then call the count_beer function, essentially starting the program and the fun!
def main():
    bottle = int(input("Enter the number of bottles: "))
    count_beer(bottle)
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more beer!")

if __name__ == "__main__":
    main()
    
            

    

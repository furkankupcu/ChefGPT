import TurkishChef
import ItalianChef

def main():
    
    while True:
        print("Welcome to Chef AI!")
        print("Please choose a chef:")
        print("1. Turkish Chef")
        print("2. Fun and Energetic Italian Chef")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            chef = TurkishChef()
        elif choice == "2":
            chef = ItalianChef()
        else:
            return

if __name__ == "__main__":
    main()

import conditions
import loop_break

t = 0
def main():
    while t < 3:
        user_input = input("Enter a value: ")
        result = conditions.condtion(user_input)
        print(result)
        t +1
        



if __name__ == "__main__":
    main()
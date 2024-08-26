import conditions
import loop_break

def main():
    while True:
        user_input = input("Enter a value (or 'exit' to quit): ")
        result = conditions.condition(user_input)
        if result.startswith("Sorry"):
            user_input = input("Please enter something else (or 'exit' to quit): ")
            print(result)
        else:
            print(result)
        if user_input.lower() == "exit":
            break

        
        
        

if __name__ == "__main__":
    main()
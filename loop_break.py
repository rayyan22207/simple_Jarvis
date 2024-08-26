import conditions
def check_ifto_break(value):
    while value:
        if value:
            input_value = input("Enter a value: ")
            result = conditions.condtion(input_value)
            return result
        if KeyboardInterrupt:
            break
        
        
        
        
    
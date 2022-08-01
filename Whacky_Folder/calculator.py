from pkg_resources import add_activation_listener

firstval, symbol, secval = input("Enter equation: ").split()
#firstval = input("State fisrt value ")
#symbol = input("State your symbol: 1.Add 2.Subtract 3.Multiply 4.Divide ")
#secval = input("State your second value ")

symbol_int = str(symbol)
first_val_int = int(firstval)
sec_val_int = int(secval)

if symbol_int == "+":
    answer = first_val_int + sec_val_int

if symbol_int == "-":
    answer = first_val_int - sec_val_int

if symbol_int == "*":
    answer = first_val_int * sec_val_int

if symbol_int == "/":
    answer = first_val_int / sec_val_int

print(answer)
def compute(elements):
    result = 0
    for element in elements:
        number1 = element[0] = element[0] if element[0] is not None else result
        operation = element[1]
        number2 = element[2]
        if "+-*/^".__contains__(element[1]) and is_number(element[2]):
            if operation == "+":
                result = float(number1) + float(number2)
            elif operation == "-":
                result = float(number1) - float(number2)
            elif operation == "*":
                result = float(number1) * float(number2)
            elif operation == "/":
                result = float(number1) / float(number2)
            elif operation == "^":
                result = pow(float(number1), float(number2))
            print(str(number1) + " " + operation + " " + str(number2) + " = " + format(result, ".2f"))
        else:
            print("Error, some character is not ok")
    print("Final result = " + format(result, ".2f"))


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    inputs = []
    subInputs = [0, 0, 0]
    counter = 0
    subInputs[0] = input("1st number? ")
    while counter == 0 or subInputs[1] != "equals":
        subInputs[1] = input("Operation (+, -, /, *, ^, end)? ")
        if subInputs[1] == "equals" or subInputs[1] == "end":
            break
        subInputs[2] = input(str(counter + 2) + ("nd" if counter == 0 else "rd" if counter == 1 else "th")
                             + " number? ")
        if subInputs[1] == "equals":
            break
        inputs.insert(counter, subInputs.copy())
        subInputs[0] = None
        counter = counter + 1
    compute(inputs)

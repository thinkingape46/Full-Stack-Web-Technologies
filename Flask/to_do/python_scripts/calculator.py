# Just a simple calculator
result = 0

def processing(input):
    result = int(input[0])
    print(input)
    i = 0
    while i < (len(input) - 1):
        if input[i+1] == "+":
            result+= int(input[i+2])
                
        elif input[i+1] == "-":
            result-= int(input[i+2])

        i = i + 2

    return result

# def processing(add_input):
#     multiply(add_input)
#     result = float(add_input[0])
#     i = 0
#     while i < len(add_input) - 2:
#         if add_input[i + 1][0] == "+":        
#             result = result + float(add_input[i + 2])
            
#         elif add_input[i + 1][0] == "-":
#             result = result - float(add_input[i + 2])
            
#         else:
#             break
#         i = i + 2
#     return result

# def multiply(add_input):
#     i = add_input

#     while ["÷"] in add_input:
        
#         index = i.index(["÷"])
#         y = float(i[index - 1])/float(i[index + 1])
#         for j in range(0, 3):
#             i.pop(index - 1)
#         i.insert(index - 1, y)    

#     while ["*"] in add_input:
        
#         index = i.index(["*"])
#         y = float(i[index - 1])*float(i[index + 1])
#         for j in range(0, 3):
#             i.pop(index - 1)
#         i.insert(index - 1, y)
#     add_input = i
#     return add_input
def check(input):
    
    print(input)
    stack = []
    result = [' '] * len(input)
    for i in range(len(input)):
        if input[i] == '(':
            stack.append(i)  
        elif input[i] == ')':
            if stack:  
                result[stack.pop()] = ' '  
            else:
                result[i] = '?'  
    while stack:  
        result[stack.pop()] = 'x' 
    print(''.join(result))

test = [
    "bge)))))))))",
    "((IIII))))))",
    "()()()()(uuu",
    "))))UUUU((()",
]

for test_case in test:
    result = check(test_case)

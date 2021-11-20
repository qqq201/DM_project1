def is_alphabet(c):
    if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
        return True
    return False

def is_operation(c):
    if c == '+' or c == '-' or c == '*' or c == '/':
        return True
    return False


def PostorderConvert(exp):
    postfix = [];
    charStack = []

    # find the priority of each operation
    priority = {
        '+': 1,
        '-': 2,
        '*': 3,
        '/': 4
    }

    exp = "(" + exp + ")"
    i = 0
    l = len(exp)

    while i < l:
        if exp[i] == '(':
            charStack.append('(')
        elif is_alphabet(exp[i]):
            postfix.append(exp[i])
            i += 1
            while i < l and is_alphabet(exp[i]):
                postfix[-1] += exp[i]
                i += 1
            continue
        elif is_operation(exp[i]):
            while is_operation(charStack[-1]) and priority[exp[i]] < priority[charStack[-1]]:
                postfix.append(charStack[-1]);
                charStack.pop();

            charStack.append(exp[i]);
        elif exp[i] == ')':
            while charStack[-1] != '(':
                postfix.append(charStack[-1])
                charStack.pop()

            charStack.pop()
        i += 1

    return postfix


def operate(a, b, o):
    if len(a) != len(b):
        return None

    result = []
    if o == '+':
        for i in range(len(a)):
            if a[i] is not None and b[i] is not None:
                result.append(a[i] + b[i])
            else:
                result.append(None)
    elif o == '-':
        for i in range(len(a)):
            if a[i] is not None and b[i] is not None:
                result.append(a[i] - b[i])
            else:
                result.append(None)
    elif o == '*':
        for i in range(len(a)):
            if a[i] is not None and b[i] is not None:
                result.append(a[i] * b[i])
            else:
                result.append(None)
    elif o == '/':
        for i in range(len(a)):
            if a[i] is not None and b[i] is not None:
                result.append(a[i] / b[i])
            else:
                result.append(None)

    return result

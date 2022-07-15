# Checking for braces match into string

from time import sleep

def check_braces(text):
    braces = []
    for c in text:
        #print(braces)
        if c in '([{':
            braces.append(c)

        elif c in '}])':
            if not braces:
                return False
            elif c == ')' and braces[-1] == '(':
                braces.pop()
                continue
            elif c == ']' and braces[-1] == '[':
                braces.pop()
                continue
            if c == '}' and braces[-1] == '{':
                braces.pop()
                continue
            return False

    if braces:
        return False
    else:
        return True


print(f"For case: ()   {check_braces('()')}")
sleep(2)
print()
print(f"For case: [({'{}'})] {check_braces('[({})]')}")
sleep(2)
print()
print(f"For case :(qq {check_braces('(qq')}")
sleep(2)
print()
print(f"For case : (] {check_braces('(]')}")
sleep(2)
print()
print(f"For case : ,] {check_braces(',]')}")
sleep(2)
print()
print(f"For case : (qq)) {check_braces('(qq))')}")


from functions.func import start

if __name__ == '__main__':
    result = start()
    while True:
        print(f"현재 값 {result}")
        operation = input("연산자 입력: ")
        if operation == '0':
            result.reset()
            continue
        try:
            num = int(input("숫자 입력: "))
        except:
            print("다시 입력해주세요")
            continue
        if operation not in ('+', '-', '*', '**', '/', '//', '%'):
            print("다시 입력해주세요")
        elif operation == '+':
            result.add(num)
        elif operation == '-':
            result.sub(num)
        elif operation == '*':
            result.mul(num)
        elif operation == '**':
            result.square(num)
        elif operation == '/':
            result.div(num)
        elif operation == '//':
            result.div_quo(num)
        elif operation == '%':
            result.div_rmd(num)
            

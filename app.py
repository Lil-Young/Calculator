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
<<<<<<< Updated upstream
        if operation not in ('+', '-', '*', '**', '/', '//', '%'):
=======
        if operation not in ('+', '-', '*', '/', '//', '%'):
>>>>>>> Stashed changes
            print("다시 입력해주세요")
        elif operation == '+':
            result.add(num)
        elif operation == '-':
            result.sub(num)
        elif operation == '*':
            result.mul(num)
<<<<<<< Updated upstream
        elif operation == '**':
            result.square(num)
=======
>>>>>>> Stashed changes
        elif operation == '/':
            result.div(num)
        elif operation == '//':
            result.div_quo(num)
        elif operation == '%':
            result.div_rmd(num)
<<<<<<< Updated upstream
            
=======
        
>>>>>>> Stashed changes

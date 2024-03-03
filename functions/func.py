from math import pow

def start():
    return Calculator()

class Calculator:
    def __init__(self):
        self.result = 0
        
    def __str__(self):
        return str(self.result)
    
    def add(self, n):
        self.result += n
        return self.result
    
    def sub(self, n):
        self.result -= n
        return self.result
    
    def mul(self, n):
        self.result *= n
        return self.result
    
    def square(self, n):
        self.result = pow(self.result, n)
        if (str(self.result*10))[-1] == '0':
            self.result = int(self.result)
        return self.result

    def div(self, n):
        if n == 0:
            print("0으로 나눌 수 없습니다.")
            return
        self.result = (self.result / n)
        if (str(self.result*10))[-1] == '0':
            self.result = int(self.result)
        return self.result
    
    def div_quo(self, n):
        if n == 0:
            print("0으로 나눌 수 없습니다.")
            return
        self.result //= n
        return self.result
    
    def div_rmd(self, n):
        if n == 0:
            print("0으로 나눌 수 없습니다.")
            return
        self.result %= n
        return self.result
    
    def reset(self):
        self.result = 0
        return self.result
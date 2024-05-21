class A:
    @staticmethod
    def plus(self,a,b):
        return a + b

    def minus(self,a,b):
        return a - b
    def mult(self,a,b):
        return a * b
    def div(self,a,b):
        return a / b
    def qq(self,a,b):
        return a ** b
    def ww(self,a,b):
        return a % b
call = A()

def input_question():
    while True:
        try:
            x = int(input("Введите первое число: "))
            y = int(input("Введите второе число: "))
            return  x, y
        except ValueError:
            print("Ошибка: Пожалуйста, введите только цифры.")
while True:
    symbol = input("Выберите (+ - * / ** %) или 'q' для выхода: ")
    if symbol == 'q':
        print("Выход из программы ")
        break


    if symbol in ['+', '-', '*', '/', '**', '%']:
        x,y = input_question()

    if symbol == '+':
        print("Результат:", call.plus(x,y))
    elif symbol == '-':
        print("Результат:", call.minus(x,y))
    elif symbol == '*':
        print("Результат:", call.mult(x,y))
    elif symbol == '/':
        print("Результат:", call.div(x,y))
    elif symbol == "**":
        qq = input("Ты готов заплатить 10$? (да/нет): ")
        if qq == 'да':
                print("Спасибо", call.qq(x,y))
        elif qq == 'нет':
            print("В таком случае ответа не ждите, всего доброго")
        elif symbol == "%":
            ww = input("Ты готов заплатить 10$? (да/нет):")
            if ww == 'да':
                print("Спасибо", call.ww(x,y))
            elif ww == 'нет':
                print("В таком случае ответа не ждите, всего доброго")
    else:
        print("Ошибка: Неправильный символ операции.")
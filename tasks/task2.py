# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    X, Y, Z = map(int,input().split())
    price_pencil = 3
    price_pen = price_pencil + 2
    price_marker = price_pen + 7
    total = X * price_pencil + Y * price_pen + Z * price_marker
    print(total)

    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()
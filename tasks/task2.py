# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    X, Y, Z = map(int,input().split())
    pencil = 3
    pen = pencil + 2
    marker = pen + 7
    total = X * pencil + Y * pen + Z * marker
    print(total)

    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()
class Point:
    __slots__ = ('i', 'x', 'y')
    def __init__(self, i, x, y):
        self.i = i  # исходный 1-based индекс
        self.x = x
        self.y = y

class Solution:
    __slots__ = ('length', 'index', 'parent')
    def __init__(self, length=1, index=0, parent=None):
        self.length = length   # длина решения (количество точек)
        self.index = index     # индекс точки в отсортированном списке p
        self.parent = parent   # ссылка на предыдущее решение

def solve(p):
    n = len(p)
    # Сортируем точки по y
    p.sort(key=lambda pt: pt.y)
    
    # Инициализируем два списка решений s0 и s1 (аналог s[0] и s[1] в C++)
    s0 = [None] * n
    s1 = [None] * n

    # Для i = 0 базовое решение
    s0[0] = Solution(length=1, index=0, parent=None)
    s1[0] = Solution(length=1, index=0, parent=None)

    for i in range(1, n):
        if p[i - 1].x < p[i].x:
            s0[i] = Solution(length=s1[i - 1].length + 1, index=i, parent=s1[i - 1])
            s1[i] = s1[i - 1]
        else:
            s1[i] = Solution(length=s0[i - 1].length + 1, index=i, parent=s0[i - 1])
            s0[i] = s0[i - 1]

    # Выбираем лучшее решение из двух вариантов для последней точки
    best_solution = s0[n - 1] if s0[n - 1].length > s1[n - 1].length else s1[n - 1]

    print(best_solution.length)
    # Выводим номера точек в том же порядке
    x = best_solution
    while x is not None:
        print(p[x.index].i, end=' ')
        x = x.parent
    print()  # завершающая новая строка

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    p = []
    pos = 1
    for i in range(n):
        # Сохраняем исходный номер точки (1-based)
        x = int(data[pos])
        y = int(data[pos + 1])
        p.append(Point(i + 1, x, y))
        pos += 2

    solve(p)

if __name__ == '__main__':
    main()

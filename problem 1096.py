def solve(r, s1, s2, t):
    """
    r  – список кортежей (u, v), представляющих ребра (входные данные, 1-based индексы)
    s1, s2 – стартовые вершины (1-based)
    t – целевая вершина (1-based)
    """
    k = len(r)
    INF = (1 << 32) - 1  # Используем INF для обозначения "не посещено" (аналог ~0u в C++)
    
    # Создаём граф: фиксированный размер 2000, так как в оригинале используется массив в 2000 элементов
    g = [[] for _ in range(2000)]
    for i in range(k):
        u = r[i][0] - 1  # перевод в 0-based индексацию
        v_dest = r[i][1] - 1
        g[u].append((v_dest, i))  # сохраняем (конечная вершина, индекс ребра)

    # q – очередь для обхода графа (BFS)
    # v_arr – массив, хранящий для каждой вершины индекс ребра, по которому она достигнута;
    #         если вершина не посещалась, значение равно INF.
    q = []
    v_arr = [INF] * 2000

    # Функция для "enqueue": если вершина ещё не посещена, добавляем её в очередь с заданной дистанцией
    def enqueue(x, d, edge_index):
        if v_arr[x] == INF:
            q.append((x, d))
            v_arr[x] = edge_index

    # Начинаем с двух стартовых вершин, помечая их специальным значением (k)
    enqueue(s1 - 1, 0, k)
    enqueue(s2 - 1, 0, k)

    # Классический BFS без явной очереди dequeue – проходим по q с индексом
    i = 0
    while i < len(q):
        cur_vertex, dist = q[i]
        i += 1

        # Если достигли целевой вершины, восстанавливаем путь
        if cur_vertex == t - 1:
            path = []
            x = t - 1
            # Восстановление пути: пока v_arr[x] != k, двигаемся по "предкам"
            while v_arr[x] != k:
                edge = v_arr[x]
                # Сохраняем ребро с переводом на 1-based индексацию
                path.append(edge + 1)
                # Переходим в вершину, из которой пришли по данному ребру
                x = r[edge][0] - 1
            print(dist)
            # Выводим ребра в восстановленном порядке (обратном накопленному)
            for edge in reversed(path):
                print(edge)
            return

        # Для текущей вершины перебираем исходящие ребра и запускаем функцию enqueue для их вершин
        for nxt, edge_index in g[cur_vertex]:
            enqueue(nxt, dist + 1, edge_index)

    print("IMPOSSIBLE")


def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return

    # Считываем количество ребер
    k = int(data[0])
    r = []
    idx = 1
    # Читаем k пар: (u, v)
    for _ in range(k):
        u = int(data[idx])
        v = int(data[idx + 1])
        r.append((u, v))
        idx += 2

    # Читаем t, s1, s2
    t = int(data[idx])
    s1 = int(data[idx + 1])
    s2 = int(data[idx + 2])

    solve(r, s1, s2, t)


if __name__ == '__main__':
    main()

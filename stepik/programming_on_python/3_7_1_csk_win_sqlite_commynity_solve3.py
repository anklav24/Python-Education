"""
# 3
# Зенит;3;Спартак;1
# Спартак;1;ЦСКА;1
# ЦСКА;0;Зенит;2
"""
import sqlite3

with sqlite3.connect(":memory:") as db:
    db.execute('CREATE TABLE stat(team TEXT, win INT, draw INT, lose INT)')


    def record(t, s1, s2):
        db.execute('INSERT INTO stat VALUES (?, ?, ?, ?)', (t, s1 > s2, s1 == s2, s1 < s2))


    n = int(input())
    for _ in range(n):
        t1, s1, t2, s2 = input().split(';')
        record(t1, int(s1), int(s2))
        record(t2, int(s2), int(s1))
    db.commit()

    statq = 'SELECT team, SUM(win), SUM(draw), SUM(lose) FROM stat GROUP BY 1'
    for t, w, d, l in db.execute(statq):
        print(f'{t}:{w + d + l} {w} {d} {l} {3 * w + d}')
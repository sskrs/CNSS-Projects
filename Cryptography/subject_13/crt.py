# λίστες με τους συντελεστές του συστήματος των γραμμικών ισοδυναμιών
n = [9, 9, 13]
m = [17, 12, 19]

if __name__ == '__main__':
    # υπολογισμός Μ = 17*12*19
    M = m[0]*m[1]*m[2]
    print(f"M: {M}\n")

    print(f"ni: {n}\n")
    print(f"mi: {m}\n")

    # υπολογισμός m_0, m_1, m_2
    Mi = [int(M/m[0]),int(M/m[1]),int(M/m[2])]
    print(f"Mi: {Mi}\n")

    # εύρεση Mi^-1
    ui = []
    for i in range(3):
        for k in range(m[i]):
            if (k * Mi[i]) % m[i] == 1:
                ui.append(k)

    print(f"ui: {ui}\n")
    x = 0
    # υπολογίζουμε το x,
    # x = (9 * 228 * 5 + 9 * 323 * 11 + 13 * 204 * 15)
    for i in range(3):
        x += n[i] * Mi[i] * ui[i]

    print(f"x: {x}")
    print(f"M: {M}")
    result = x % M
    print(f"x mod M = {result}")

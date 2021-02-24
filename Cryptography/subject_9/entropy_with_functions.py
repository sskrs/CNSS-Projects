from fractions import Fraction as frac
import math

# δημιουργούμε και γεμίζουμε τον πινακα p_xy
# με τις τιμές που δίνονται από την εκφώνηση
# frac αντιστοιχεί στο κλάσμα
p_xy = [frac(1, 7), frac(1, 7), frac(1, 7)], [0, frac(1, 7), frac(1, 7)], [frac(2, 7), 0, 0]

# Πρωτού υπολογίσουμε την εντροπία πρεπει να υπολογίσουμε τα px_0, px_1 px_2, py_0, py_1, py_2
# τα p_xy[][] αντιστοιχούν σε κάθε στοιχείο του πίνακα της εκφώνησης.
for i in p_xy:
    px_0 = p_xy[0][0] + p_xy[1][0] + p_xy[2][0]
    px_1 = p_xy[0][1] + p_xy[1][1] + p_xy[2][1]
    px_2 = p_xy[0][2] + p_xy[1][2] + p_xy[2][2]

for i in p_xy:
    py_0 = p_xy[0][0] + p_xy[0][1] + p_xy[0][2]
    py_1 = p_xy[1][0] + p_xy[1][1] + p_xy[1][2]
    py_2 = p_xy[2][0] + p_xy[2][1] + p_xy[2][2]


# ερώτημα i) --------------------------------------------------------
# υπολογισμός εντροπίας
def syn_a(p_xy):
    H_x = - px_0 * math.log(px_0, 2.0) - px_1 * math.log(px_1, 2.0) - px_2 * math.log(px_2, 2.0)
    H_y = - py_0 * math.log(py_0, 2.0) - py_1 * math.log(py_1, 2.0) - px_2 * math.log(py_2, 2.0)

    return H_x, H_y


print(f"apotelesma prwtis synarthshs: {syn_a(p_xy)}")


# ερώτημα ii) --------------------------------------------------------
# υπολογισμός απο κοινού εντροπίας χωρίς τα στοιχεία του πίνακα που βγαζουν p=0 δηλαδή (1,0),(2,1),(2,2)
def syn_b(p_xy):
    h_xy = - p_xy[0][0] * math.log(p_xy[0][0], 2.0) - p_xy[2][0] * math.log(p_xy[2][0], 2.0) - p_xy[0][1] * math.log(
        p_xy[0][1], 2.0) - p_xy[1][1] * math.log(p_xy[1][1], 2.0) - p_xy[0][2] * math.log(p_xy[0][2], 2.0) - p_xy[1][
               2] * math.log(p_xy[1][2], 2.0)

    return h_xy


print(f"apotelesma deyterhs synarthshs: {syn_b(p_xy)}")


# ερώτημα iii) --------------------------------------------------------
def syn_c(p_xy):
    for i in p_xy:
        px_0 = p_xy[0][0] + p_xy[1][0] + p_xy[2][0]
        px_1 = p_xy[0][1] + p_xy[1][1] + p_xy[2][1]
        px_2 = p_xy[0][2] + p_xy[1][2] + p_xy[2][2]

    for i in p_xy:
        py_0 = p_xy[0][0] + p_xy[0][1] + p_xy[0][2]
        py_1 = p_xy[1][0] + p_xy[1][1] + p_xy[1][2]
        py_2 = p_xy[2][0] + p_xy[2][1] + p_xy[2][2]
        pyx_00 = p_xy[0][0] / px_0
    # print(pyx_00)
    pyx_10 = p_xy[0][1] / px_0
    # print(pyx_10)
    pyx_20 = p_xy[0][2] / px_0
    # print(pyx_20)
    pyx_01 = p_xy[1][0] / px_1
    # print(pyx_01)
    pyx_11 = p_xy[1][1] / px_1
    # print(pyx_11)
    pyx_21 = p_xy[1][2] / px_1
    # print(pyx_21)
    pyx_02 = p_xy[2][0] / px_2
    # print(pyx_02)
    pyx_12 = p_xy[2][1] / px_2
    # print(pyx_12)
    pyx_22 = p_xy[2][2] / px_2
    # print(pyx_22)

    hpy_x0 = - pyx_00 * math.log(pyx_00) - pyx_10 * math.log(pyx_10) - pyx_20 * math.log(pyx_20)
    # - pyx_01 * math.log(pyx_01) --> 0
    hpy_x1 = - pyx_11 * math.log(pyx_11) - pyx_21 * math.log(pyx_21)
    # - pyx_12 * math.log(pyx_12)- pyx_22 * math.log(pyx_22) --> 0
    hpy_x2 = - pyx_02 * math.log(pyx_02)

    hy_x = px_0 * hpy_x0 + px_1 * hpy_x1 + px_2 * hpy_x2

    # =======hx_y
    pxy_00 = p_xy[0][0] / py_0
    pxy_10 = p_xy[0][1] / py_0
    pxy_20 = p_xy[0][2] / py_0
    pxy_01 = p_xy[1][0] / py_1
    pxy_11 = p_xy[1][1] / py_1
    pxy_21 = p_xy[1][2] / py_1
    pxy_02 = p_xy[2][0] / py_2
    pxy_12 = p_xy[2][1] / py_2
    pxy_22 = p_xy[2][2] / py_2

    hpx_y0 = - pxy_00 * math.log(pxy_00) - pxy_10 * math.log(pxy_10) - pxy_20 * math.log(pxy_20)
    # - pxy_01 * math.log(pxy_01) --> 0
    hpx_y1 = - pxy_11 * math.log(pxy_11) - pxy_21 * math.log(pxy_21)
    # - pxy_12 * math.log(pxy_12)- pxy_22 * math.log(pxy_22) --> 0
    hpx_y2 = - pxy_02 * math.log(pxy_02)

    hx_y = py_0 * hpx_y0 + py_1 * hpx_y1 + py_2 * hpx_y2

    return hx_y, hy_x


print(f"apotelesma triths synarthshs: {syn_c(p_xy)}")


def syn_d(p_xy):
    # ερώτημα iv)

    for i in p_xy:
        px_0 = p_xy[0][0] + p_xy[1][0] + p_xy[2][0]
        px_1 = p_xy[0][1] + p_xy[1][1] + p_xy[2][1]
        px_2 = p_xy[0][2] + p_xy[1][2] + p_xy[2][2]

    for i in p_xy:
        py_0 = p_xy[0][0] + p_xy[0][1] + p_xy[0][2]
        py_1 = p_xy[1][0] + p_xy[1][1] + p_xy[1][2]
        py_2 = p_xy[2][0] + p_xy[2][1] + p_xy[2][2]
        pyx_00 = p_xy[0][0] / px_0

    H_y = - py_0 * math.log(py_0, 2.0) - py_1 * math.log(py_1, 2.0) - px_2 * math.log(py_2, 2.0)
    # print(pyx_00)
    pyx_10 = p_xy[0][1] / px_0
    # print(pyx_10)
    pyx_20 = p_xy[0][2] / px_0
    # print(pyx_20)
    pyx_01 = p_xy[1][0] / px_1
    # print(pyx_01)
    pyx_11 = p_xy[1][1] / px_1
    # print(pyx_11)
    pyx_21 = p_xy[1][2] / px_1
    # print(pyx_21)
    pyx_02 = p_xy[2][0] / px_2
    # print(pyx_02)
    pyx_12 = p_xy[2][1] / px_2
    # print(pyx_12)
    pyx_22 = p_xy[2][2] / px_2
    # print(pyx_22)

    hpy_x0 = - pyx_00 * math.log(pyx_00) - pyx_10 * math.log(pyx_10) - pyx_20 * math.log(pyx_20)
    # - pyx_01 * math.log(pyx_01) --> 0
    hpy_x1 = - pyx_11 * math.log(pyx_11) - pyx_21 * math.log(pyx_21)
    # - pyx_12 * math.log(pyx_12)- pyx_22 * math.log(pyx_22) --> 0
    hpy_x2 = - pyx_02 * math.log(pyx_02)

    hy_x = px_0 * hpy_x0 + px_1 * hpy_x1 + px_2 * hpy_x2
    i_xy = H_y - hy_x
    return i_xy


print(f"apotelesma amoibaias plhroforias: {syn_d(p_xy)}")
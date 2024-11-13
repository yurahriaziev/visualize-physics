import math
G = 6.67 * math.pow(10, -11)
M_EARTH = 5.97 * math.pow(10, 24)
M_MOON = 7.35 * math.pow(10, 22)
R_EARTH = 6.371 * 10**6

def p3():
    m1 = 65
    m2 = 72
    r = 20
    F_g = (G * m1 * m2) / (math.pow(r, 2))
    print('F_g', F_g)
    a1 = F_g/m1
    a2 = F_g/m2
    print('a1', a1)
    print('a2', a2)
    a_rel = a1 + a2
    print('a_rel', a_rel)
    t = math.sqrt(40/a_rel)
    print('t', t/(60*60*24))

def p7():
    m = 70
    r1 = 378000*1000 #m
    r2 = 6378*1000 #m
    F_g1 = (G * M_MOON * m) / math.pow(r1, 2)
    print('F_g_m', F_g1)
    F_g2 = (G * M_EARTH * m) / math.pow(r2, 2)
    print('F_g_e', F_g2)
    print('F_g_m/F_g_e', F_g1/F_g2)

def p9():
    x = 1 / (math.sqrt(3) + 1)
    print('x from m', x)

def p11():
    a = 0.98
    g = 9.8
    r = R_EARTH * math.sqrt(g/a)
    print('r', r)
    h = r - R_EARTH
    print('h', h)

def p13():
    r_T = (1/8)*R_EARTH
    m_T = (1/1700)*M_EARTH
    a_g_T = (G * m_T) / math.pow(r_T, 2)
    print('a_g_T', a_g_T)
    V_T = 2.05 * math.pow(10, 18)
    density_T = m_T / V_T
    print('density_T', density_T)

def p19():
    r = 3.24 * math.pow(10, 6)
    V_esc = 7.65 * math.pow(10, 3)
    V_esc_squared = math.pow(V_esc, 2)
    a_g = V_esc_squared/(2*r)
    print('a_g', a_g)

print()
p19()
print()
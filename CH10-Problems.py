import math

def p31():
    r = .226/2
    m = .426
    moment_of_inertia = 2/3 * (m) * math.pow(r, 2)
    y_final = 5
    g = 9.8

    K_trans_i = (1/2) * m * math.pow(r, 2)
    K_rot_i = (1/2) * ((2/3) * m * math.pow(r, 2))
    potential_energy_grav_f = m * g * y_final
    print(f'{K_trans_i}omega_i^2 + {K_rot_i}omega_i^2 = {potential_energy_grav_f}')
    k_total = K_trans_i + K_rot_i
    print(k_total)
    omega = math.sqrt(potential_energy_grav_f / k_total)
    print(omega)

def p33():
    r = 2.4
    I = 2100
    t = 15
    V_i = 0
    omega_i = 0
    F = 18
    torque = r * F
    print(torque)
    ang_acceleration = torque / I
    print(ang_acceleration)
    omega_f = (ang_acceleration * t) + omega_i
    print(omega_f)
    work = (1/2) * I * math.pow(omega_f, 2)
    print(work)
    print(work/t)

def p35():
    m = 2.8
    r = 0.1
    t = 2.5
    I = (1/2) * m * math.pow(r, 2)
    print(I)
    V_i = 0
    omega_i = 0
    omega_f = (1200/60) * (2*math.pi)
    print(omega_f)
    V_f = r * omega_f
    # print(V_f)
    alpha = (omega_f - omega_i) / t
    print(alpha)
    torque = I * alpha
    print(torque)
    angle_turned = (1/2) * alpha * math.pow(t, 2)
    print(angle_turned)
    work = (1/2) * I * math.pow(omega_f, 2)
    print(work)
    # print(torque * angle_turned)
    total_kinetic_energy = (1/2) * I * math.pow(omega_f, 2)
    print(total_kinetic_energy)

def p37():
    m = 2
    V = 12
    r = 8
    angle = 36.9
    radians = angle * (math.pi / 180)
    l = r * m * V * math.sin(radians)
    print(l)

    F = m * 9.8
    torque = r * F
    print(F)
    l2 = torque * math.sin(radians)
    print(l2)

def p39():
    L = 0.15
    m = 0.006
    omega = (2 * math.pi) / 60
    I = (1/3) * m * math.pow(L, 2)
    L = I * omega
    print(L)

def p41():
    def get_ang_speed(t):
        return 3 * t + 4.4 * math.pow(t, 3)
    
    r = .24
    m = 12
    I = (2/3) * m * math.pow(r, 2)
    L = I * get_ang_speed(0)
    L2 = I * get_ang_speed(3)
    print(L, L2)

    alpha = get_ang_speed(3) / 3
    torque = I * alpha
    print(torque)

def p43():
    m = 8
    d_i = 1.8
    r_i = d_i / 2
    I_i = (1/12) * m * math.pow(d_i, 2)
    omega_i = 0.4 * 2 * math.pi
    V_i = omega_i * r_i

    r_f = 0.25
    I_f = 0.4

    k_rot_i = (1/2) * I_i * math.pow(omega_i, 2)
    k_rot_f = (1/2) * I_f
    print(k_rot_i, k_rot_f)
    print(math.sqrt(k_rot_i/k_rot_f)/(2*math.pi))

def p47():
    r = 2
    m_table = 120
    omega_i = 3
    I_table = (1/2) * m_table * math.pow(r, 2)
    L_table_i = I_table * omega_i
    print(L_table_i)

    m_guy = 70
    I_guy = m_guy * math.pow(r, 2)
    I_f = I_table + I_guy

    omega_f = L_table_i / I_f
    print(omega_f)

    k_i = (1/2) * I_table * math.pow(omega_i, 2)
    k_f = (1/2) * I_f * math.pow(omega_f, 2)
    print(k_i, k_f)

def p49():
    m_bug = 0.01
    m_bar = 0.05
    L_bar = 1
    V_bug = 0.2

    l_bug = L_bar * m_bug * V_bug
    print(l_bug)

p49()
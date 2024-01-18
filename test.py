# import math
#
# ro_0 = int(input())
# bett = int(input())
# mu = int(input())
# g = 9.81
# ro_w = int(input())
# V_0 = int(input())
# t = len([1,2])
# h = int(input())
# d_h = int(input())
# d_r = int(input())
# ro_a = int(input())
# C_d = int(input())
# W_x = int(input())
#
# alf=(ro_0*bett*g)/(4*mu)
# bett =(ro_w - ro_0)*(ro_0**(-1))
# eps_0=4/(162**(1/8))
#
# r_k_t = eps_0 * (((V_0 ** 3) * alf * t) / (8 * (math.pi ** 3)) ** (1 / 8))
# h_0_t = ((3 ** (1 / 3)) / 4) * (eps_0 ** (2 / 3)) * (((V_0) / (2 * math.pi * alf * t)) ** (1 / 4))
#
# u = (-1) * (ro_0 * bett * g * (h ** 2) / (mu)) * (d_h / d_r)
#
# U_0 = u
# # U = U_0 + U_d
#
# t_0_x= ro_a * C_d *(W_x – u_d)*(math.fabs (W_x – u_d))
# t_0_y= ro_a*C_d*(W_x – v_d)*(math.fabs (W_x – v_d))
#
# h_0 = h_0_t
#
# omeg=7.2921*(10**-5)
# f =2*omeg*math.sin(fi)
# v_wd= (-1)*(t_0_x /(ro_0*h_0*f))
# u_wd= (t_0_y /(ro_0*h_0*f))
#
# bett_w=1.72*((v_w*t)**(1/2))
# bett_1=1+((ro_0*v_0*bett_w)/((ro_w*v_w*h_0)+(ro_0*v_0*bett_w)))
# bett_2=1-((ro_0*v_0*bett_w)/((ro_w*v_w*h_0)+(ro_0*v_0*bett_w)))
# gamm=(v_0*ro_w*v_w)/((ro_w*v_w*h_0)+(ro_0*v_0*bett_w)))
#
# u_cd=(u_w*((((2*gamm)/(f*h_0*bett_1))**2)-(bett_2/bett_1))+((2*gamm)/(f*h_0*bett_1))*((bett_2/bett_1)+1)*v_w)/(1+((2*gamm)/(f*h_0*bett_1))**2)
# v_cd=(v_w*((((2*gamm)/(f*h_0*bett_1))**2)-(bett_2/bett_1))+((2*gamm)/(f*h_0*bett_1))*((bett_2/bett_1)+1)*u_w)/(1+((2*gamm)/(f*h_0*bett_1))**2)
#
# u_d=u_wd+u_cd
# v_d=v_wd+v_cd
#
# U_d=u_d+v_d
# U = U_0 + U_d
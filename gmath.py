import math
from display import *

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 16

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    A = calculate_ambient(ambient, areflect)
    D = calculate_diffuse(light, dreflect, normal)
    S = calculate_specular(light, sreflect, view, normal)
    I = []
    [I.append(A[i] + D[i] + S[i]) for i in range(3)]
    return limit_color(I)

def calculate_ambient(alight, areflect):
    a = []
    [a.append(int(alight[i] * areflect[i])) for i in range(3)]
    print "C_A"
    return limit_color(a)

def calculate_diffuse(light, dreflect, normal):
    color = []
    [color.append(int(light[COLOR][i] * dreflect[i])) for i in range(3)]

    L = normalize(light[LOCATION])
    N = normalize(normal)
    NL = dot_product(N, L)
    d = []
    [ d.append(int(color[i] * NL)) for i in range(3)] 
    print "C_D"
    return limit_color(d)

def calculate_specular(light, sreflect, view, normal):
    # PKs[(2(N__dot__L)N - L)__dot__V]
    L = normalize(light[LOCATION])
    N = normalize(normal)
    V = normalize(view)

    twoNdotL = 2 * dot_product(N, L)
    p = []
    [p.append(int((twoNdotL * N[i]) - L[i])) for i in range(3)]
    cos = dot_product(p, V)

    specular = []
    [specular.append(int(light[COLOR][i] * sreflect[i] * (cos ** SPECULAR_EXP))) for i in range(3)]
    print "C_S"
    return limit_color(specular)
    
    


def limit_color(color):
#    print "lim color"
#    print color
    for i in range(3):
        print "index"
        print i
        if color[i] < 0:
            color[i] = 0 
        if color[i] > 255:
            color[i] = 225 
    return color

#vector functions
def normalize(vector):
    a = float(vector[0])
    b = float(vector[1])
    c = float(vector[2])
    c = math.sqrt(a*a + b*b + c*c)
    ret = [0,0,0]
    ret[0] = vector[0]/c
    ret[1] = vector[1]/c
    ret[2] = vector[2]/c

    return ret


def dot_product(a, b):
    return a[0] * b[0] + a[1]*b[1] + a[2]*b[2]

def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N

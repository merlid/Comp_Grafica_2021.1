from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) ) # vetor de cores
a = 0

r = 1 # raio interior do torus
R = 2 # raio da esfera e raio exterior do torus
n = 50 # número de passos usados nos desenhos
halfpi = math.pi/2

def fe(u, v): # esfera
    theta = (u*math.pi/(n-1))-halfpi
    phi = (v*2*math.pi)/(n-1)
    x = R*math.cos(theta)*math.cos(phi)
    y = R*math.sin(theta)
    z = R*math.cos(theta)*math.sin(phi)
    return x, y, z

def desenhaEsfera(): #desenha a esfera
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(n):
        for j in range(n):
            glColor3fv(cores[(j+1)%len(cores)])
            glVertex3fv(fe(i,j))
            glVertex3fv(fe(i+1,j))
    glEnd()


def ft(u, v): # torus
    theta = (u*2*math.pi)/(n-1)
    phi = (v*2*math.pi)/(n-1)
    x = (R + r*math.cos(theta))*math.cos(phi)
    y = (R + r*math.cos(theta))*math.sin(phi)
    z = r*math.sin(theta)
    return x, y, z

def desenhaTorus(): # desenha o torus
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(n):
        for j in range(n):
            glColor3fv(cores[(i+1)%len(cores)])
            glVertex3fv(ft(i,j))
            glVertex3fv(ft(i+1,j))
    glEnd()


def fp(u, v): # paraboloide
    theta = (v*2*math.pi)/(n-1)
    p = (u*2)/(n-1)
    x = p*math.cos(theta)
    y = p*p
    z = p*math.sin(theta)
    return x, y, z

def desenhaParaboloide(): #desenha o paraboloide
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(n):
        for j in range(n):
            glColor3fv(cores[(j+1)%len(cores)])
            glVertex3fv(fp(i,j))
            glVertex3fv(fp(i+1,j))
    glEnd()

def desenha(): # função que chama as funções de desenho
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(a,0,2,0)
    desenhaEsfera() # chama a função que desenha a esfera
    #desenhaTorus() # chama a função que desenha o torus
    #desenhaParaboloide() # chama a função que desenha o paraboloide
    glPopMatrix()
    glutSwapBuffers()
    a += 1
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Solido de Revolucao")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-8)
glutTimerFunc(50,timer,1)
glutMainLoop()

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) ) # vetor de cores
a = 0

n = 50 # número de lados do prisma
r = 3 # raio da base do prisma

top = (0, 5, 0) # coordenadas do topo do prisma
pontos = []

def base(): # desenha a base do prisma

    global pontos

    glBegin(GL_POLYGON)
    glColor3fv(cores[0])
    for i in range(0, n+1):

        a = (i/n) * 2 * math.pi
        x = r * math.cos(a)
        z = r * math.sin(a)

        pontos.append((x,0,z))

        glColor3fv(cores[(i+1)%len(cores)])
        glVertex3f(x, 0, z)
    
    glEnd()


def piramide(): # desenha a pirâmide do prisma

    glBegin(GL_TRIANGLE_FAN)
    glColor3fv(cores[0])
    glVertex3f(*top)
    for i in range(0, n):

        glColor3fv(cores[(i+1)%len(cores)])
        glVertex3f(*pontos[i])
        glVertex3f(*pontos[i+1])
    
    glEnd()

def desenha(): # chama as duas funções que desenham o prisma
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glRotatef(-a,2,2,0)
    base()
    piramide()
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
glutCreateWindow("PIRAMIDE")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-15)
glutTimerFunc(50,timer,1)
glutMainLoop()

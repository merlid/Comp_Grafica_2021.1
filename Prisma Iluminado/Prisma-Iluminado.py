from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import sys

n = 10 # número de lados do prisma
r = 2 # raio da base do prisma

top = (0, 4, 0) # coordenadas do topo do prisma
pontos = [] # vetor que armazena os pontos da base


def base(): # desenha a base do prisma

    global pontos

    glBegin(GL_POLYGON)

    for i in range(0, n+1):

        a = (i/n) * 2 * math.pi
        x = r * math.cos(a)
        z = r * math.sin(a)

        pontos.append((x,0,z))

        glVertex3f(x, 0, z)
    
    glEnd()


def prisma(): # desenha os lados do prisma

    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(*top)
    for i in range(0, n):

        glVertex3f(*pontos[i])
        glVertex3f(*pontos[i+1])
    
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,2,2,0)
    base()
    prisma()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt( 10,0,0, 0,0,0,     0,1,0 )

def init():
    mat_ambient = (0.5, 0.0, 0.0, 1.0)
    mat_diffuse = (0.0, 0.0, 1.0, 1.0)
    mat_specular = (1.0, 0.5, 0.5, 1.0)
    mat_shininess = (60,)
    light_position = (10, 0, 0)
    glClearColor(0.0,0.0,0.0,0.0)
    #glShadeModel(GL_FLAT)
    glShadeModel(GL_SMOOTH)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Prisma-Iluminado")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutTimerFunc(50,timer,1)
    init()
    glutMainLoop()

main()
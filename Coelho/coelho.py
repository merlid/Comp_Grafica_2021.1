from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from plyfile import PlyData, PlyElement # biblioteca usada para manipular o arquivo .ply (https://github.com/dranjan/python-plyfile)

vecX = [] # vetor que guarda o "x" de todos os vértices
vecY = [] # vetor que guarda o "y" de todos os vértices
vecZ = [] # vetor que guarda o "z" de todos os vértices
vecF = [] # vetor que guarda os índices dos vértices de uma face

a = 0

def display():
    global obj
    global vecF
    global a

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(a,1,3,0)
    
    for i in range(69451): # percorre todas as faces do .ply
        glBegin(GL_POLYGON)
        for k in range(3):
            vecF = obj['face'].data['vertex_indices'][i] # guarda os índices de todos os vértices da face i
            glColor3f(0,0,1) # azul
            glVertex3f(vecX[vecF[k]], vecY[vecF[k]], vecZ[vecF[k]]) # imprime um vértice com os x, y e z do vértice k da face i
        glEnd()

    glutSwapBuffers()

    a = a+1

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(3,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,1,10,0,0,0,0,1,0)

def init():
    global obj
    global vecX
    global vecY
    global vecZ

    glLightfv(GL_LIGHT0, GL_POSITION,  (5, 5, 5, 1.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.4, 0.4, 0.4, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.6, 0.6, 0.6, 1.0))
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glClearColor(0,0,0,0.0)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)
    
    obj =  PlyData.read("bun_zipper.ply") # Carrega o arquivo .ply

    vecX = obj.elements[0].data['x'] # guarda todos os "x" de todos os vértices
    vecY = obj.elements[0].data['y'] # guarda todos os "y" de todos os vértices
    vecZ = obj.elements[0].data['z'] # guarda todos os "z" de todos os vértices


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Coelho")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutTimerFunc(50,timer,1)
    init()
    glutMainLoop()

main()
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import png
import math

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = b'\033'

# Number of the glut window.
window = 0

# Variáveis da Esfera
rs = 0.6 # raio do sol
rt = 0.3 # raio da terra
rl = 0.1 # raio da lua
rst = 1.5 # raio sol-terra
rtl = 0.5 # raio terra-lua
n = 50 # número de passos usados nos desenhos
halfpi = math.pi/2

a = 0


def LoadTextures():
    global texture
    texture = glGenTextures(3)

    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[0])
    reader = png.Reader(filename='sol.png')
    
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

    ################################################################################
  
    glBindTexture(GL_TEXTURE_2D, texture[1])
    reader = png.Reader(filename='terra.png')

    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

    ################################################################################

    glBindTexture(GL_TEXTURE_2D, texture[2])
    reader = png.Reader(filename='lua.png')

    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################


def InitGL(Width, Height):             
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0) 
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)               
    glEnable(GL_DEPTH_TEST)            
    glShadeModel(GL_SMOOTH)            
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def ReSizeGLScene(Width, Height):
    if Height == 0:                        
        Height = 1
    glViewport(0, 0, Width, Height)      
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def fSol(u, v): # função do sol
    theta = (u*math.pi/(n-1))-halfpi
    phi = (v*2*math.pi)/(n-1)
    x = rs*math.cos(theta)*math.cos(phi)
    y = rs*math.sin(theta)
    z = rs*math.cos(theta)*math.sin(phi)
    return x, y, z

def fTerra(u, v): # função da terra
    theta = (u*math.pi/(n-1))-halfpi
    phi = (v*2*math.pi)/(n-1)
    x = rt*math.cos(theta)*math.cos(phi)
    y = rt*math.sin(theta)
    z = rt*math.cos(theta)*math.sin(phi)
    return x, y, z

def fLua(u, v): # função da lua
    theta = (u*math.pi/(n-1))-halfpi
    phi = (v*2*math.pi)/(n-1)
    x = rl*math.cos(theta)*math.cos(phi)
    y = rl*math.sin(theta)
    z = rl*math.cos(theta)*math.sin(phi)
    return x, y, z

def DrawGLScene():
    global xrot, yrot, zrot, texture, a

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()                   
    glClearColor(0,0,0,1.0)    
    
    glTranslatef(0.0,0.0,-5.0)
    glRotatef(a,0,0,1)
    
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glBegin(GL_TRIANGLE_STRIP)              
    
    for i in range(n): # desenha sol
       for j in range(n):
            glTexCoord2f(j/n, i/n); glVertex3fv(fSol(i,j))
            glTexCoord2f(j/n, (i+1)/n); glVertex3fv(fSol(i+1,j))
    
    glEnd()    

    glRotatef(a,0,0,5)
    glTranslatef(0.0,rst,0)   
    glRotatef(a,0,0,1)

    glBindTexture(GL_TEXTURE_2D, texture[1])
    glBegin(GL_TRIANGLE_STRIP)              
    
    for i in range(n): # desenha terra
       for j in range(n):
            glTexCoord2f(j/n, i/n); glVertex3fv(fTerra(i,j))
            glTexCoord2f(j/n, (i+1)/n); glVertex3fv(fTerra(i+1,j))
    
    glEnd()  

    glRotatef(a,0,0,3)
    glTranslatef(0.0,rtl,0)   
    glRotatef(a,0,0,1)

    glBindTexture(GL_TEXTURE_2D, texture[2])
    glBegin(GL_TRIANGLE_STRIP)              
    
    for i in range(n): # desenha lua
       for j in range(n):
            glTexCoord2f(j/n, i/n); glVertex3fv(fLua(i,j))
            glTexCoord2f(j/n, (i+1)/n); glVertex3fv(fLua(i+1,j))
    
    glEnd() 

    a += 1

    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)    
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Sistema Solar")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    InitGL(640, 480)
    glutMainLoop()


main()

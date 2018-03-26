from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

x=0
angle=0
flag = 1
def MyInit():
    glMatrixMode(GL_PROJECTION)
    #glortho(-10,10,-10,10,-10,10)
    gluPerspective(60,1,0.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)
    glClearColor(1,1,1,1)

def square (x1,x2,x3,x4,z1,z2,z3,z4):
    global x
    glBegin(GL_POLYGON)
    glVertex3d(x1-x,0,z1)
    glVertex3d(x2-x,0,z2)
    glVertex3d(x3-x,0,z3)
    glVertex3d(x4-x,0,z4)
    glEnd()

def MovingCar():
    global x
    global angle
    global flag
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(0,0,0)
    square(-50,50,50,-50,-3,-3,3,3)
    square(-50,50,50,-50,-4,-4,-3.5,-3.5)
    square(-50,50,50,-50,4,4,3.5,3.5)
    glColor(1,1,1)
    square(-2,2,2,-2,-.5,-.5,.5,.5)
    square(-2+4+1,2+4,2+4,-2+4+1,-.5,-.5,.5,.5)
    square(-2+8+1,2+8,2+8,-2+8+1,-.5,-.5,.5,.5)
    square(-2+12+1,2+12,2+12,-2+12+1,-.5,-.5,.5,.5)
    square(-2+16+1,2+16,2+16,-2+16+1,-.5,-.5,.5,.5)
    square(-2-4,2-4-1,2-4-1,-2-4,-.5,-.5,.5,.5)
    square(-2-8,2-8-1,2-8-1,-2-8,-.5,-.5,.5,.5)
    square(-2-12,2-12-1,2-12-1,-2-12,-.5,-.5,.5,.5)
    square(-2-16,2-16-1,2-16-1,-2-16,-.5,-.5,.5,.5)
    square(-2-20,2-20-1,2-20-1,-2-20,-.5,-.5,.5,.5)
    square(-2-24,2-24-1,2-24-1,-2-24,-.5,-.5,.5,.5)
    square(-2-28,2-28-1,2-28-1,-2-28,-.5,-.5,.5,.5)
    square(-2-32,2-32-1,2-32-1,-2-32,-.5,-.5,.5,.5)
    square(-2-36,2-36-1,2-36-1,-2-36,-.5,-.5,.5,.5)

    glColor3f(1,0,0)

    glTranslate(x,0,0)
    glScale(1,0.25,0.5)
    glutWireCube(5)

    glLoadIdentity()
    glTranslate(x,5*0.25,0)
    glScale(0.5,0.25,0.5)
    glutWireCube(5)

    glColor3f(0,0,1)
    glLoadIdentity()
    glTranslate(x+2.5,-2.5*0.25,2.5*0.5)
    glRotate(angle,0,0,1)
    glutSolidTorus(0.125,0.5,10,8)

    glColor3f(0,0,1)
    glLoadIdentity()
    glTranslate(x+2.5,-2.5*0.25,-2.5*0.5)
    glRotate(angle,0,0,1)
    glutSolidTorus(0.125,0.5,10,8)

    glColor3f(0,0,1)
    glLoadIdentity()
    glTranslate(x-2.5,-2.5*0.25,-2.5*0.5)
    glRotate(angle,0,0,1)
    glutSolidTorus(0.125,0.5,10,8)

    glColor3f(0,0,1)
    glLoadIdentity()
    glTranslate(x-2.5,-2.5*0.25,2.5*0.5)
    glRotate(angle,0,0,1)
    glutSolidTorus(0.125,0.5,10,8)

    #glColor3f(1,1,0)
    #glLoadIdentity()
    #glScale(1,0.25,0.5)
    #glutSolidSphere(0.2*5,12,8)
    if (x >= 8):
        flag = 0
    if (x <= -8 ) :
        flag =1
    if (flag == 1):
        x+=0.001
        angle-=0.01
    if (flag == 0):
        x-=0.001
        angle+=0.01
    glFlush()




glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Moving Car")
glutDisplayFunc(MovingCar)
glutIdleFunc(MovingCar)
MyInit()
glutMainLoop()

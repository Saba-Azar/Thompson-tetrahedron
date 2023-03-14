#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 16:37:14 2021

@author: hi00vyta
"""

# create Thompson Tetrahedron in ovito
#
import sys
import numpy as np
#
######### input begins ########################################################
x=np.array([1.0, 1.0, 0.0])  # crystal direction parallel to x
y=np.array([-1.0, 1.0, -1.0])  # crystal direction parallel to y
z=np.array([-1.0, 1.0, 2.0])  # crystal direction parallel to z
scaleFactor=100.0 # scale the size of the tetrahedron
trans_vec=np.array([0.0,0.0,0.0]) # a vector to move the tetrahedron
########## input ends #########################################################
#
xint=x.astype(int)
yint=y.astype(int)
zint=z.astype(int)
x=x/np.linalg.norm(x)
y=y/np.linalg.norm(y)
z=z/np.linalg.norm(z)
#
rotMat_c2s=np.array([x,y,z])
rotMat_s2c=np.transpose(rotMat_c2s)
#
A=np.array([1.0,0.0,1.0]) # A
B=np.array([0.0,1.0,1.0]) # B
C=np.array([1.0,1.0,0.0]) # C
D=np.array([0.0,0.0,0.0]) # D
#
with open("ThomTet_x{0}{1}{2}_y{3}{4}{5}_z{6}{7}{8}.vtk".format(xint[0],xint[1],xint[2],yint[0],yint[1],yint[2],zint[0],zint[1],zint[2]),'w') as thomTetVTK:
     thomTetVTK.write("# vtk DataFile Version 3.1\n")
     thomTetVTK.write("# comment line\n")
     thomTetVTK.write("ASCII\n")
     thomTetVTK.write("DATASET UNSTRUCTURED_GRID\n")
     thomTetVTK.write("POINTS 4 FLOAT\n")
     for v in (A,B,C,D):
         vt=np.matmul(rotMat_c2s,v*scaleFactor)+trans_vec
         thomTetVTK.write("\t {0:1.6f} \t {1:1.6f} \t {2:1.6f}\n".format(vt[0],vt[1],vt[2]))
     thomTetVTK.write("CELLS 4 16\n")
     thomTetVTK.write("3 1 2 3\n") # B-C-D red
     thomTetVTK.write("3 0 2 3\n") # A-C-D green
     thomTetVTK.write("3 0 3 1\n") # A-D-B blue
     thomTetVTK.write("3 0 1 2\n") # A-B-C white
     thomTetVTK.write("CELL_TYPES 4\n")
     thomTetVTK.write("5\n")
     thomTetVTK.write("5\n")
     thomTetVTK.write("5\n")
     thomTetVTK.write("5\n")
     thomTetVTK.write("CELL_DATA 4\n")
     thomTetVTK.write("COLOR_SCALARS faceColor 4\n")
     thomTetVTK.write("1.0 0.0 0.0 1.0\n") # red
     thomTetVTK.write("0.0 1.0 0.0 1.0\n") # green
     thomTetVTK.write("0.0 0.0 1.0 1.0\n") # blue
     thomTetVTK.write("1.0 1.0 1.0 1.0\n") # white

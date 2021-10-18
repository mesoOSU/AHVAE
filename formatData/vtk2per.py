#!/usr/bin/env python

import glob
import numpy as np
from os.path import splitext
from os.path import split

#vtkDir = "/users/PAA0023/mason1099/gudhiWork/VTK/*.vtk"
#print(glob.glob(vtkDir))
#print(glob.glob("VTK/*.vtk"))

vtkDir = "../data/VTK/kamal/test/"
perDir = "../data/PER/kamal/test/"

vtkList = glob.glob(vtkDir + "*.vtk")
print(vtkList)

for vtkFile in vtkList:
    with open(vtkFile) as file:
        foundDim = False
        while foundDim == False:
            line = file.readline() 
            if "DIMENSIONS" in line:
                foundDim = True

    lineSplit = np.asarray(line.split())
    lineSplit = lineSplit[1:]

    outName = perDir + splitext(split(vtkFile)[1])[0] + ".per"
    print(splitext(split(vtkFile)[1])[0])

    header = str(lineSplit.shape[0]) + "\n"

    for x in lineSplit:
        header = header + x + "\n"
    header = header[:-1]

    vtkArr = np.loadtxt(vtkFile, skiprows=10)
    vtkArr += np.abs(np.min(vtkArr))
    vtkArr = np.divide(vtkArr, np.abs(np.max(vtkArr)))

    np.savetxt(outName, vtkArr, header=header, comments="", fmt="%.10f")

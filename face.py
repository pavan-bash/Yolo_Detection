import cv2
import numpy
face_cascade=cv2.CascadeClassifier("C:\\Users\\kanth\\OneDrive\\Desktop\\pic.xml")
#face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("C:\\Users\\kanth\\OneDrive\\Desktop\\pic.jpg")


gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray_img,1.3,5)
print(type(faces))
print(faces)
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
resized=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0])))
cv2.imshow("pic",resized)
cv2.waitKey(0)
cv2.destroyAllWIndows()
"""from darkflow.net.build import TFNet
import cv2

options = {"model": "cfg/yolo.cfg", "load": "bin/yolo.weights", "threshold": 0.1}

tfnet = TFNet(options)

imgcv = cv2.imread("C:\\Users\\kanth\\OneDrive\\Desktop\\pic.jpg")
result = tfnet.return_predict(imgcv)
print(result)"""
"""from setuptools import setup, find_packages

from setuptools.extension import Extension

from Cython.Build import cythonize

import numpy

import os

import imp



VERSION = imp.load_source('version', os.path.join('.', 'darkflow', 'version.py'))

VERSION = VERSION.__version__



if os.name =='nt' :

    ext_modules=[

        Extension("darkflow.cython_utils.nms",

            sources=["darkflow/cython_utils/nms.pyx"],

            #libraries=["m"] # Unix-like specific

            include_dirs=[numpy.get_include()]

        ),        

        Extension("darkflow.cython_utils.cy_yolo2_findboxes",

            sources=["darkflow/cython_utils/cy_yolo2_findboxes.pyx"],

            #libraries=["m"] # Unix-like specific

            include_dirs=[numpy.get_include()]

        ),

        Extension("darkflow.cython_utils.cy_yolo_findboxes",

            sources=["darkflow/cython_utils/cy_yolo_findboxes.pyx"],

            #libraries=["m"] # Unix-like specific

            include_dirs=[numpy.get_include()]

        )

    ]



elif os.name =='posix' :

    ext_modules=[

        Extension("darkflow.cython_utils.nms",

            sources=["darkflow/cython_utils/nms.pyx"],

            libraries=["m"], # Unix-like specific

            include_dirs=[numpy.get_include()]

        ),        

        Extension("darkflow.cython_utils.cy_yolo2_findboxes",

            sources=["darkflow/cython_utils/cy_yolo2_findboxes.pyx"],

            libraries=["m"], # Unix-like specific

            include_dirs=[numpy.get_include()]

        ),

        Extension("darkflow.cython_utils.cy_yolo_findboxes",

            sources=["darkflow/cython_utils/cy_yolo_findboxes.pyx"],

            libraries=["m"], # Unix-like specific

            include_dirs=[numpy.get_include()]

        )

    ]



else :

    ext_modules=[

        Extension("darkflow.cython_utils.nms",

            sources=["darkflow/cython_utils/nms.pyx"],

            libraries=["m"] # Unix-like specific

        ),        

        Extension("darkflow.cython_utils.cy_yolo2_findboxes",

            sources=["darkflow/cython_utils/cy_yolo2_findboxes.pyx"],

            libraries=["m"] # Unix-like specific

        ),

        Extension("darkflow.cython_utils.cy_yolo_findboxes",

            sources=["darkflow/cython_utils/cy_yolo_findboxes.pyx"],

            libraries=["m"] # Unix-like specific

        )

    ]



setup(

    version=VERSION,

	name='darkflow',

    description='Darkflow',

    license='GPLv3',

    url='https://github.com/thtrieu/darkflow',

    packages = find_packages(),

	scripts = ['flow'],

    ext_modules = cythonize(ext_modules)

)
"""

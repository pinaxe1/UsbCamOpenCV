# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 21:34:17 2019
source: https://gist.github.com/cbednarski/8450931
@author: Chris Bendarski
"""

import cv2

# Windows dependencies
# - Python 2.7.6: http://www.python.org/download/
# - OpenCV: http://opencv.org/
# - Numpy -- get numpy from here because the official builds don't support x64:
#   http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

# Mac Dependencies
# - brew install python
# - pip install numpy
# - brew tap homebrew/science
# - brew install opencv

cap = cv2.VideoCapture(0)
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
while(True):
    ret, frame = cap.read()
    #rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    rgb=frame;
    cv2.imshow('frame', rgb)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        out = cv2.imwrite('capture.jpg', frame)
        break

cap.release()
cv2.destroyAllWindows()
# Creating database which captures images and stores them in dataset-Resource

import cv2, sys, numpy, os
haar_file = 'haarcascade_frontalface_default.xml'

# All the faces data will be present in this folder
datasets = 'Resource'

# These are sub data sets of folder, for face's I've 3 name you can change the label here for more person recognition
sub_data = 'Guru' #For person1
sub_data1 = 'Rahul' #For Person2
sub_data2 = 'Virat' #For person3. You can create n number of person's data by capturing their image here.

path = os.path.join(datasets, sub_data2)
if not os.path.isdir(path):
    os.mkdir(path)

# defining the size of images
(width, height) = (130, 100)

# '0' is used for my webcam,if you've any other camera attached use '1' like this
face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)

# The program loops until it has 30 images of the face of single person.
# If you want to create more data of a different person create 
count = 1
while count <= 30:
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite('% s/% s.png' % (path, count), face_resize)
    count += 1

    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(10)
    if key == 27:
        break

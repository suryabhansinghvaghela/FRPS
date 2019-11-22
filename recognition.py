import cv2
import numpy as np
import os
import time
import random
import sqlite3

########## KNN CODE ###########
def distance(v1,v2):
    #Euclidian
    return np.sqrt(((v1-v2)**2).sum())

def knn(train,test,k = 5):
    dist = []

    for i in range(train.shape[0]):
        #get the vector and label
        ix = train[i,:-1]
        iy = train[i,-1]
        #Compute the distance from the test point
        d = distance(test,ix)
        dist.append([d,iy])
    #Sort based on distance and get top k
    dk = sorted(dist, key=lambda x: x[0])[:k]
    #Retrieve only labels
    labels = np.array(dk)[:,-1]

    #get frequencies of each neighbor
    output = np.unique(labels, return_counts = True)
    #find max frequency and corresponding lable
    index = np.argmax(output[1])
    return output[0][index]
####################################


cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

skip = 0
face_data = []
labels = []

class_id = 0
names = {}

#data Preparation
for fx in os.listdir():
    if fx.endswith('.npy'):
        names[class_id] = fx[:-4]
        data_item = np.load(fx)
        face_data.append(data_item)

        #create lables for the class
        target = class_id*np.ones((data_item.shape[0],))
        class_id +=1
        labels.append(target)
face_dataset = np.concatenate(face_data,axis = 0)
face_labels = np.concatenate(labels,axis = 0).reshape((-1,1))

print(face_dataset.shape)
print(face_labels.shape)

trainset = np.concatenate((face_dataset,face_labels),axis = 1)
print(trainset.shape)
ct=1
vf=[]

#testing
while True:
    ret,frame = cap.read()
    if ret == False:
        continue

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(frame,1.3,5)
    if len(vf) > 30:

        r=random.randint(0,29)
        if vf[r] == pred_name:
            print(r)
            print('echo Verifying')
            
            print('echo Successfully Verified')
            cv2.destroyAllWindows()
            os.system('python test.py')
            print('echo end')
            
            break
        else:	
            print(vf)
            vf.clear()
    name1=""
    contact1=""
    email1=""
    for face in faces:
        x,y,w,h = face

        #Get the ROI
        offset = 10
        face_section = frame[y-offset:y+h+offset,x-offset:x+w+offset]
        face_section = cv2.resize(face_section,(100,100))

        out = knn(trainset,face_section.flatten())

        #display name
        pred_name = names[int(out)]
        cv2.putText(frame,pred_name,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2,cv2.LINE_AA)
        det=pred_name.split(',')
        name1=det[0]
        contact1=det[1]
        email1=det[2]
        print(det)
       
		
        #print("ECHO")
        ct=ct+1
        vf.append(pred_name)
        #print(ct)
		
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)

    cv2.imshow("Faces",frame)
    db = sqlite3.connect('user.db')
    cn = db.cursor()
    sql="""delete from userinfo"""
    cn.execute(sql)
    db.commit()
    cn.close()
	
    db1 = sqlite3.connect('user.db')
    cn1=db1.cursor()
    sql1="""insert into userinfo(name,mob,email) values (?, ?, ?)"""
    val1=(name1,contact1,email1)
    cn1.execute(sql1,val1)
    db1.commit()
    cn1.close()
	
    key_pressed = cv2.waitKey(1) & 0xFF
    
    if key_pressed == ord('q'):
        break

	

cap.release()
cv2.destroyAllWindows()

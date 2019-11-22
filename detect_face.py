from tkinter import *
import os
import _thread
import cv2
import numpy as np
#root = Tk()
#root.title('Register Page')
mainWindow = Tk()
mainWindow.title('Register User')

mainWindow.overrideredirect(True)
mainWindow.overrideredirect(False)
mainWindow.attributes('-fullscreen',True)
#initialize the camera

fname = StringVar()
mob= StringVar()
ema= StringVar()
#Face detection
b1=""
def main():
    os.system('python main.py')

def face():
    Label(mainWindow, width = 46, height=5,text="Please Rotate your face slowly!!!!!!",font=("Helvetica",20)).grid(row=1500,column=1500, sticky=W)
    Label(mainWindow, width=25,text="Enter your name:",font=("Verdana",15)).grid(row=1800,column=140,sticky=W)
    Entry(mainWindow, width=20,textvariable = fname).grid(row=1800, column=1500,sticky=W)
    Label(mainWindow, width=25,text="Enter your Mobile No:",font=("Verdana",15)).grid(row=1900,column=140,sticky=W)
    Entry(mainWindow, width=20,textvariable = mob).grid(row=1900, column=1500,sticky=W)
    Label(mainWindow, width=25,text="Enter your Email ID:",font=("Verdana",15)).grid(row=2000,column=140,sticky=W)
    Entry(mainWindow, width=20,textvariable = ema).grid(row=2000, column=1500,sticky=W)
    Button(mainWindow, text="Submit", font=("Verdana",12),command=face2).grid(row=2100,column=1500,sticky=W)
#b1=fname.get()
def face2():
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    face_data = []
    skip = 0
    file_name1 = fname.get()
    file_name2= mob.get()
    file_name3= ema.get()
    file_name=file_name1+","+file_name2+","+file_name3
    print(file_name)
    while True:
        ret,frame = cap.read()
        if ret == False:
            continue
        
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray,1.3,5)
        faces = sorted(faces,key = lambda f: f[2]*f[3])
       
        for face in faces[-1:]:
            x,y,w,h = face
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)

            #extract : Region of interest
            offset = 10
            face_section = frame[y-offset:y+h+offset,x-offset:x+w+offset]
            face_section = cv2.resize(face_section,(100,100))

            if(skip%10==0):
                face_data.append(face_section)
                print('.',end = ' ')
            cv2.imshow("Face Section",face_section)
        skip += 1
        cv2.imshow("Face-registering",frame)
        

        key_pressed = cv2.waitKey(1) & 0xFF
        if len(face_data)==30:
            break

    #convert our face data into numpy array
    face_data = np.asarray(face_data)
    face_data = face_data.reshape((face_data.shape[0],-1))
    print(face_data.shape)

    np.save(file_name+'.npy',face_data)
    txt="Your data is stored as "+file_name
    mv2=Tk()
    mv2.title("Registration Details")
    Label(mv2, width = 46, height=5,text=txt,font=("Helvetica",20)).grid(row=1500,column=1500, sticky=W)
    Button(mv2,text="Go to main page", font=("Verdana",20),command=main).grid(row=2000,column=1500,sticky=W)
    cap.release()
    cv2.destroyAllWindows()
    mainWindow.destroy()
    




face()
#input('Enter name of the person: ')


'''b1=Button(mainWindow, text="Submit")
b1.configure(command=face())
b1.place(x=80,y=10)'''



closeButton = Button(mainWindow, text = "CLOSE",font=("Verdana",12))
closeButton.configure(command= lambda: mainWindow.destroy())
closeButton.place(x=90,y=530)


mainWindow.mainloop()




































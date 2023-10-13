# Python program to open the
# camera in Tkinter
# Import the libraries,
# tkinter, cv2, Image and ImageTk
  
from tkinter import *
import cv2
from PIL import Image, ImageTk
import os
  
# Define a video capture object
vid = cv2.VideoCapture(0)
  
# Declare the width and height in variables
width, height = 800, 600
  
# Set the width and height
vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
  
# Create a GUI app
app = Tk()
  
# Bind the app with Escape keyboard to
# quit app whenever pressed
app.bind('<Escape>', lambda e: app.quit())
  
# Create a label and display it on app
label_widget = Label(app)
label_widget.pack()
  
# Create a function to open camera and
# display it in the label_widget on app

global photo_taken
photo_taken = False
  
def open_camera():
    global photo_taken
    if not photo_taken:
        taken, frame = vid.read()
        if taken:
            opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            captured_image = Image.fromarray(opencv_image)
            photo_image = ImageTk.PhotoImage(image=captured_image)
            label_widget.photo_image = photo_image
            label_widget.configure(image=photo_image)
            label_widget.after(10, open_camera)
    else:
        opencv_image = cv2.imread('photo.jpg')
        opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGBA)
        captured_image = Image.fromarray(opencv_image)
        photo_image = ImageTk.PhotoImage(image=captured_image)
        label_widget.photo_image = photo_image
        label_widget.configure(image=photo_image)

def quitApp():
    vid.release()
    app.destroy()

def take_photo():
    global photo_taken
    photo_taken = True
    # capture a frame from the camera
    ret, frame = vid.read()
    
    # save the frame as a JPEG file
    cv2.imwrite("photo.jpg", frame)

    # update the live video to display the photo that was just taken
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
          
    # Capture the latest frame and transform to image
    captured_image = Image.fromarray(opencv_image)
          
    # Convert captured image to photoimage
    photo_image = ImageTk.PhotoImage(image=captured_image)
          
    # Displaying photoimage in the label
    label_widget.photo_image = photo_image

    label_widget.configure(image=photo_image)
    
    os.system("python 
    
  
  
# Create a button to open the camera in GUI app
button1 = Button(app, text="Quit", command=quitApp)
button1.pack()

button2 = Button(app, text="Take photo", command=take_photo)
button2.pack()



open_camera()

# Create an infinite loop for displaying app on screen
app.mainloop()

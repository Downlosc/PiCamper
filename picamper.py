from gpiozero import Button
import picamera
import time 
import os 

button1    = Button(27)
button2    = Button(15)
button3    = Button(17)
button4    = Button(18)
interrupt = 1
camera = picamera.PiCamera()


def enablecamera():
    camera.start_preview()

def disablecamera():
    camera.stop_preview()


def main():
    while(interrupt == 1):
        if (button1.is_pressed):
            print("spengo...")
        elif(button2.is_pressed):
            button_clicked = True
            while(button_clicked):
                enablecamera()
                if(button3.is_pressed):
                    disablecamera()
                    button_clicked = False
        elif(button3.is_pressed):
            print("3")
        elif(button4.is_pressed):
            print("openauto is starting")

if __name__ == "__main__":
    main()


from gpiozero import Button
import picamera
import time 
import os 

button1    = Button(27)
button2    = Button(15)
button3    = Button(17)
button4    = Button(18)
interrupt = 1





def main():
    print("L'applicazione è in esecuzione...")
    camera = picamera.PiCamera()
    while(interrupt == 1):
        if (button1.is_pressed):
            print("SPENGO")
            os.system('sudo halt')
        elif(button2.is_pressed):
            print("prova")
            button_clicked = True
            camera.start_preview()
            while(button_clicked):
                if(button3.is_pressed):
                    camera.stop_preview()
                    button_clicked = False
        elif(button3.is_pressed):
            print("3")
        elif(button4.is_pressed):
            print("openauto is starting")
            os.system('~/openauto/bin/autoapp')

if __name__ == "__main__":
    main()

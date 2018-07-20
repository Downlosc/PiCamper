from gpiozero import Button
import picamera
import time 
import os 
import sys 


button1    = Button(27)
button2    = Button(15)
button3    = Button(17)
button4    = Button(18)
interrupt = 1
BLUE, GREEN, END = '\33[94m', '\033[1:32m', '\033[0m'



def heading():
    spaces = " " * 76
    sys.stdout.write(GREEN + spaces + """
    ███              ▄█▄▀▀▀      ▄▄▄             ███                   ███
    █    ▀▄          █▀         █   █    █▀▄▀█   █   ▀▄     ▄███▄      █   ▀▄
    █     █   █      █          ██▀▀█    █ █ █   █    █     █▀   ▀     █    █
    █    ▄▀   █      █▄         █   █    █   █   █   ▄▀     ██▄▄       █   ▄▀
    █▀▀▀▀     █      ▀███▀      █   █    █   █   █▀▀▀▀      █▄         █▀▄▀▀
    █         █                          █       █          ▀███▀      █   ▄
    █                                            █                     █    ▄ 
    """+ END + BLUE)

    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('--> PREMI TASTO 4 PER FARE PARTIRE OPEN AUTO')
    print('--> PREMI TASTO 2 PER FARE ACCENDERE TELECAMERA POSTERIORE')
    print('--> PREMI TASTO 3 PER FARE SPEGNERE TELECAMERA POSTERIORE')
    print('--> PREMI TASTO 1 PER SPEGNERE')




def main():
    heading()
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
                    heading()
        elif(button3.is_pressed):
            print("LA TELECAMERA DEVE ESSERE ACCESA")
        elif(button4.is_pressed):
            print("openauto is starting")
            os.system('~/openauto/bin/autoapp')
            

if __name__ == "__main__":
    main()

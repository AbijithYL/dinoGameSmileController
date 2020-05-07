import cv2
import pyautogui
import time


face_cascade = cv2.CascadeClassifier(r"C:\Users\Admin\PycharmProjects\dinoController\venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier(r"C:\Users\Admin\PycharmProjects\dinoController\venv\Lib\site-packages\cv2\data\haarcascade_smile.xml")

def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    global smile_status
    if len(faces)==0:
        smile_status=False
    else:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
            if len(smiles)==0:
                smile_status=False
            else:
                smile_status=True
                for (sx, sy, sw, sh) in smiles:
                    cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
    return frame, smile_status



def press_space():

    pyautogui.keyUp('down')     # releasing the Down Key
    pyautogui.keyDown('space')  # pressing Space to overcome Bush
    time.sleep(0.05)            # so that Space Key will be recognized easily
    print("jump")              # printing the "Jump" statement on the
    time.sleep(0.10)           # terminal to see the current output
    pyautogui.keyUp('space')    # releasing the Space Key
    pyautogui.keyDown('down')    # again pressing the Down Key to keep my Bot always down



pyautogui.keyDown('down')                       #keeps the 'down' button pressed by default



cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()                           # Captures cap frame by frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # To capture image in monochrome

    canvas, smileStatus = detect(gray, frame)                    # calls the detect() function



    if smileStatus:
        press_space()

    # Displays the result on camera feed
    cv2.imshow('Video', canvas)

    # The control breaks once q key is pressed
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    # Release the capture once all the processing is done.
cap.release()
cv2.destroyAllWindows()
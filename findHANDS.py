import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import pyautogui

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    if hands:
        hand1 = hands[0]
        lmList = hand1["lmList"]
        bbox = hand1["bbox"]
        centerPoint = hand1["center"]

        fingers = detector.fingersUp(hand1)

        if fingers[1] == 1 and fingers[2] == 0:
            pyautogui.moveRel(10, 0)
        elif fingers[1] == 0 and fingers[2] == 1:
            pyautogui.moveRel(-10, 0)

        if fingers[4] == 1:
            pyautogui.click()

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

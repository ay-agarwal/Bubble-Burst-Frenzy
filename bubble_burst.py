import cv2
import numpy as np
import math
import time
import pyaudio
import os
from pygame import mixer

mixer.init()
marks=0
th = 1
th2 = 10
t114=10
t116=30
tm=8
t115=10
font = cv2.FONT_HERSHEY_TRIPLEX
def make_cicle(img,a,b,n):
    # a,b = ceter   # n  = number to display
    cv2.circle(img, (a, b), 40, (255, 255, 255), 1)
    cv2.putText(img, str(n), (a-10, b+10), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
def make_rect(img,a,b,w):
    cv2.rectangle(img, (a, b), (a+w, b+w), (255, 255, 255), 2)
def crop_rect(img,a,b):
    f = img[b:b+40, a:a+40]
    return f
def chsnge_circle(img,a,b,n):
    cv2.circle(img, (a, b), 45, (055, 255, 0), 20)
    cv2.circle(img, (a, b), 35, (255, 255, 255), -1)
    cv2.putText(img, str(n), (a-20, b+20), font, 2, (0, 0, 0), 2, cv2.LINE_AA)
def make_bubble(img,a,b,n,be):
    img[b-40:b-40 + 80, a-70:a-70 + 142] = be
    cv2.putText(img, str(n), (a-10, b+10), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
def change_bubble(img,a,b,n,be):
    img[b-40:b+60, a-70:a+30] = be


while (1):
    home = cv2.imread('image_used1.jpg')
    cv2.namedWindow("img", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('img', home)
    caphom = cv2.VideoCapture(1)
    flaghom1 = 0
    flaghom2 = 0
    flaghom3 = 0
    flaghom4 = 0
    flaghom5 = 0
    k = 0
    kk =0
    while (caphom.isOpened()):

        ret, framehom = caphom.read()
        hsv = cv2.cvtColor(framehom, cv2.COLOR_BGR2HSV)
        mask2 = cv2.inRange(hsv, np.array([2, 50, 50]), np.array([15, 255, 255]))
        kernel_square = np.ones((11, 11), np.uint8)
        kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        dilation = cv2.dilate(mask2, kernel_ellipse, iterations=1)
        erosion = cv2.erode(dilation, kernel_square, iterations=1)
        dilation2 = cv2.dilate(erosion, kernel_ellipse, iterations=1)
        filtered = cv2.medianBlur(dilation2, 5)
        kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8))
        dilation2 = cv2.dilate(filtered, kernel_ellipse, iterations=1)
        kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        dilation3 = cv2.dilate(filtered, kernel_ellipse, iterations=1)
        median = cv2.medianBlur(dilation2, 5)
        ret, framehom2 = cv2.threshold(median, 127, 255, 0)


        cv2.rectangle(framehom, (70, 190), (200, 220), (255, 255, 255), 2) #normal unlimited time
        crop_framehom1 = framehom2[190:220, 70:200]
        cv2.rectangle(framehom, (60, 235), (210,265 ), (255, 255, 255), 2)#difficult unlimited time
        crop_framehom2 = framehom2[235:265, 60:210]
        cv2.rectangle(framehom, (370, 190), (500, 220), (255, 255, 255), 2)  # difficult limited time
        crop_framehom3 =framehom2[190:220, 370:500]
        cv2.rectangle(framehom, (360, 235), (510, 265), (255, 255, 255), 2)  # difficult limited time
        crop_framehom4 = framehom2[235:265, 360:510]
        cv2.rectangle(framehom, (180,300),(420, 340), (255, 255, 255), 2) #multiple player
        crop_framehom5 = framehom2[300:340, 180:420]
        cv2.rectangle(framehom, (50, 300), (90, 380), (255, 255, 255), 2)  #play
        crop_framehom6 = framehom2[300:380, 50:90]
        cv2.rectangle(framehom, (250, 120), (350, 180), (255, 255, 255), 2)
        crop_framehom6 = framehom2[120:180, 250:350]

        if flaghom1 == 0:
            if cv2.countNonZero(crop_framehom1) > th2:
                chsnge_circle(framehom, 150, 630, 1)
                mixer.music.load('pop.mp3')
                mixer.music.play()
                cv2.rectangle(home, (135, 360), (410, 420), (255, 255, 255), 2)
                cv2.rectangle(home, (120, 460), (440, 530), (0,0,0), 2)
                cv2.rectangle(home, (755, 445), (1075, 515), (0,0,0), 2)
                cv2.rectangle(home, (780, 360), (1055, 420), (0,0,0), 2)
                cv2.rectangle(home, (360, 610), (880, 680), (0,0,0), 2)
                k=112
                flaghom1 = 1
                flaghom2 = 0
                flaghom3 = 0
                flaghom4 = 0
                flaghom5 = 0

                # break
        if flaghom2 == 0:
            if cv2.countNonZero(crop_framehom2) > th2:
                chsnge_circle(framehom, 150, 630, 1)
                mixer.music.load('pop.mp3')
                mixer.music.play()
                cv2.rectangle(home, (135, 360), (410, 420), (0,0,0), 2)
                cv2.rectangle(home, (120, 460), (440, 530), (255, 255, 255), 2)
                cv2.rectangle(home, (755, 445), (1075, 515), (0,0,0), 2)
                cv2.rectangle(home, (780, 360), (1055, 420), (0,0,0), 2)
                cv2.rectangle(home, (360, 610), (880, 680), (0,0,0), 2)
                # caphom.release()
                k=113
                flaghom2 = 1
                flaghom1 = 0

                flaghom3 = 0
                flaghom4 = 0
                flaghom5 = 0
                # break

        if flaghom3 == 0:
            if cv2.countNonZero(crop_framehom3) > th2:
                chsnge_circle(framehom, 150, 630, 1)
                cv2.rectangle(home, (135, 360), (410, 420), (0,0,0), 2)
                cv2.rectangle(home, (120, 460), (440, 530), (0,0,0), 2)
                cv2.rectangle(home, (755, 445), (1075, 515), (0,0,0), 2)
                cv2.rectangle(home, (780, 360), (1055, 420), (255, 255, 255), 2)
                cv2.rectangle(home, (360, 610), (880, 680), (0,0,0), 2)
                mixer.music.load('pop.mp3')
                mixer.music.play()
                k=114
                flaghom3 = 1
                flaghom1 = 0
                flaghom2 = 0

                flaghom4 = 0
                flaghom5 = 0
                # break

        if flaghom4 == 0:
            if cv2.countNonZero(crop_framehom4) > th2:
                chsnge_circle(framehom, 150, 630, 1)
                mixer.music.load('pop.mp3')
                mixer.music.play()
                cv2.rectangle(home, (135, 360), (410, 420), (0,0,0), 2)
                cv2.rectangle(home, (120, 460), (440, 530), (0,0,0), 2)
                cv2.rectangle(home, (755, 445), (1075, 515), (255, 255, 255), 2)
                cv2.rectangle(home, (780, 360), (1055, 420), (0,0,0), 2)
                cv2.rectangle(home, (360, 610), (880, 680), (0,0,0), 2)
                # caphom.release()
                k=115
                flaghom1 = 0
                flaghom2 = 0
                flaghom3 = 0
                flaghom4 = 1
                flaghom5 = 0
                # break
        if flaghom5 == 0:
            if cv2.countNonZero(crop_framehom5) > th2:
                chsnge_circle(framehom, 150, 630, 1)
                mixer.music.load('pop.mp3')
                mixer.music.play()
                cv2.rectangle(home, (135, 360), (410, 420), (0,0,0), 2)
                cv2.rectangle(home, (120, 460), (440, 530), (0,0,0), 2)
                cv2.rectangle(home, (755, 445), (1075, 515), (0,0,0), 2)
                cv2.rectangle(home, (780, 360), (1055, 420), (0,0,0), 2)
                cv2.rectangle(home, (360, 610), (880, 680), (255, 255, 255), 2)
                k=116
                flaghom1 = 0
                flaghom2 = 0
                flaghom3 = 0
                flaghom4 = 0
                flaghom5 = 1
        if flaghom1 ==1 or flaghom2 ==1 or flaghom3 ==1 or flaghom4 ==1 or flaghom5 ==1:
            if cv2.countNonZero(crop_framehom6) > th2:
                mixer.music.load('pop.mp3')
                mixer.music.play()
                caphom.release()
                break
        kk = cv2.waitKey(10)
        if kk == 27 or kk==112 or kk==113 or kk ==114 or kk==115 or kk == 116:
            caphom.release()
            break
        cv2.imshow('img', home)
    if kk == 27:
        break
    if k == 112 or kk ==112:      #fixed time normal mode
        img = cv2.imread('black2.png')
        start_time = time.time()
        cap = cv2.VideoCapture(1)
        load = cv2.VideoCapture('count1.mp4')
        t1 = time.time()
        mixer.music.load('mm.mp3')
        mixer.music.play()
        while (1):
            t2 = time.time()
            if (t2 - t1 > tm):
                break
            ret, frame = load.read()
            cv2.imshow('img', frame)
            k = cv2.waitKey(20)

        mixer.music.load('pop.mp3')
        mixer.music.play()
        marks = 0

        bubble = cv2.imread('bubble2.jpg')
        make_bubble(img,150,630,1,bubble)  #1
        make_bubble(img, 820, 600, 1,bubble) #2
        make_bubble(img, 1250, 600, 2,bubble) #3
        make_bubble(img, 450, 500, 2,bubble) #4
        make_bubble(img, 1020, 500, 2,bubble) #5
        make_bubble(img, 200, 350, 3,bubble) #6
        # make_bubble(img, 180, 200, 5,bubble) #7
        make_bubble(img, 450, 230, 3,bubble) #8
        make_bubble(img, 800, 250, 4,bubble) #9
        make_bubble(img, 1200, 250, 4,bubble) #10
        # make_bubble(img, 400, 50, 5,bubble) #11
        # make_bubble(img, 800, 50, 5,bubble) #12

        flag1 = 0
        flag2 = 0
        flag3 = 0
        flag4 = 0
        flag5 = 0
        flag6 = 0
        # flag7 = 0
        flag8 = 0
        flag9 = 0
        flag10 = 0
        # flag11 = 0
        # flag12 = 0

        start_time = time.time()
        while (cap.isOpened()):
            ret, frame = cap.read()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            imgThreshLow = cv2.inRange(hsv, (0, 155, 155), (18, 255, 255))
            imgThreshHigh = cv2.inRange(hsv, (165, 155, 155), (179, 255, 255))
            imgThresh = cv2.add(imgThreshLow, imgThreshHigh)
            imgThresh = cv2.GaussianBlur(imgThresh, (3, 3), 2)  # blur
            imgThresh = cv2.dilate(imgThresh, np.ones((5, 5), np.uint8))  # close image (dilate, then erode)
            frame2 = cv2.erode(imgThresh, np.ones((5, 5), np.uint8))

            make_rect(frame, 65, 270, 40)
            crop_frame1 = crop_rect(frame2, 65, 270)
            make_rect(frame, 355, 270, 40)
            crop_frame2 = crop_rect(frame2, 355, 270)
            make_rect(frame, 550, 275, 40)
            crop_frame3 = crop_rect(frame2, 550, 275)
            make_rect(frame, 190, 220, 40)
            crop_frame4 = crop_rect(frame2, 190, 220)
            make_rect(frame, 445, 230, 40)
            crop_frame5 = crop_rect(frame2, 445, 230)
            make_rect(frame, 75, 155, 40)
            crop_frame6 = crop_rect(frame2, 75, 155)
            # make_rect(frame, 65, 85, 40)
            # crop_frame7 = crop_rect(frame2, 65, 85)
            make_rect(frame, 180, 100, 40)
            crop_frame8 = crop_rect(frame2, 180, 100)
            make_rect(frame, 345, 110, 40)
            make_rect(frame, 345, 110, 40)
            crop_frame9 = crop_rect(frame2, 345, 110)
            make_rect(frame, 540, 120, 40)
            crop_frame10 = crop_rect(frame2, 540, 120)
            # make_rect(frame, 155, 15, 40)
            # crop_frame11 = crop_rect(frame2, 155, 15)
            # make_rect(frame, 345, 15, 40)
            # crop_frame12 = crop_rect(frame2, 345, 15)
            bubble1 = cv2.imread('smile3.jpg')
            if flag1 == 0:
                if cv2.countNonZero(crop_frame1) > th:
                    change_bubble(img, 150, 630, 1,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 1
                    flag1 = 1;
            if flag2 == 0:
                if cv2.countNonZero(crop_frame2) > th:
                    change_bubble(img, 820, 600, 1,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 1
                    flag2 = 1;
            if flag3 == 0:
                if cv2.countNonZero(crop_frame3) > th:
                    change_bubble(img, 1250, 600, 2,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 2
                    flag3 = 1;
            if flag4 == 0:
                if cv2.countNonZero(crop_frame4) > th:
                    change_bubble(img, 450, 500, 2,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 2
                    flag4 = 1;
            if flag5 == 0:
                if cv2.countNonZero(crop_frame5) > th:
                    change_bubble(img, 1020, 500, 2,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 2
                    flag5 = 1;
            if flag6 == 0:
                if cv2.countNonZero(crop_frame6) > th:
                    change_bubble(img, 200, 350, 3,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 3
                    flag6 = 1;
            if flag8 == 0:
                if cv2.countNonZero(crop_frame8) > th:
                    change_bubble(img, 450, 230, 3,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 3
                    flag8 = 1;
            if flag9 == 0:
                if cv2.countNonZero(crop_frame9) > th:
                    change_bubble(img, 800, 250, 4,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 4
                    flag9 = 1;
            if flag10 == 0:
                if cv2.countNonZero(crop_frame10) > th:
                    change_bubble(img, 1200, 250, 4,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 4
                    flag10 = 1;
            end_time = time.time()
            if marks < 22:
                ee_time = end_time
                cv2.rectangle(img, (540, 320), (950, 460), (0, 0, 0), -1)
                cv2.putText(img, str(round(end_time - start_time, 3)), (550, 450), font, 3, (255, 255, 255), 2,
                            cv2.LINE_AA)
                cv2.rectangle(img, (240, 0), (340, 90), (0, 0, 0), -1)
                cv2.putText(img, 'score ', (50, 80), font, 2, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.putText(img, str(marks), (250, 80), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.namedWindow("img", cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow('img', img)
            else:
                cv2.rectangle(img, (240, 0), (340, 90), (0, 0, 0), -1)
                cv2.putText(img, 'score ', (50, 80), font, 2, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.putText(img, str(marks), (250, 80), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.rectangle(img, (540, 320), (950, 460), (0, 0, 0), -1)
                cv2.putText(img, str(round(ee_time - start_time, 3)), (550, 450), font, 3, (255, 255, 255), 2,
                            cv2.LINE_AA)
                cv2.imshow('img', img)
                k = cv2.waitKey(3000)
                cap.release()
                hm = cv2.imread('hs44.jpg')
                # cv2.putText(hm, 'GAME OVER! ', (500, 300), font, 4, (0, 0, 255), 2, cv2.LINE_AA)
                # cv2.putText(hm, 'SCORE ', (600, 700), font, 4, (0,0,0), 2, cv2.LINE_AA)
                cv2.putText(hm, str(marks), (800, 300), font, 4, (255,255,0), 2, cv2.LINE_AA)
                # cv2.putText(hm, 'TIME ', (700, 900), font, 4, (0,0,0), 2, cv2.LINE_AA)
                cv2.putText(hm, str(round(ee_time - start_time, 0)), (800, 450), font, 4, (255,255,0), 2,
                            cv2.LINE_AA)
                while (1):
                    cv2.namedWindow("img", cv2.WND_PROP_FULLSCREEN)

                    cv2.setWindowProperty("img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                    cv2.imshow('img', hm)
                    cap_res = cv2.VideoCapture(1)
                    while (cap_res.isOpened()):
                        kk = 0
                        ret, frame_res = cap_res.read()
                        hsv = cv2.cvtColor(frame_res, cv2.COLOR_BGR2HSV)
                        mask2 = cv2.inRange(hsv, np.array([2, 50, 50]), np.array([15, 255, 255]))
                        kernel_square = np.ones((11, 11), np.uint8)
                        kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
                        dilation = cv2.dilate(mask2, kernel_ellipse, iterations=1)
                        erosion = cv2.erode(dilation, kernel_square, iterations=1)
                        dilation2 = cv2.dilate(erosion, kernel_ellipse, iterations=1)
                        filtered = cv2.medianBlur(dilation2, 5)
                        kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8))
                        dilation2 = cv2.dilate(filtered, kernel_ellipse, iterations=1)
                        kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
                        dilation3 = cv2.dilate(filtered, kernel_ellipse, iterations=1)
                        median = cv2.medianBlur(dilation2, 5)
                        ret, frame_res2 = cv2.threshold(median, 127, 255, 0)

                        cv2.rectangle(frame_res, (180, 300), (420, 340), (255, 255, 255), 2)
                        crop_frame_res = frame_res2[300:440, 180:420]
                        if cv2.countNonZero(crop_frame_res) > th2:
                            # chsnge_circle(frame_res, 150, 630, 1)
                            mixer.music.load('pop.mp3')
                            mixer.music.play()
                            # cv2.waitKey(2000)
                            cap_res.release()
                            k = 27
                            break
                        kk = cv2.waitKey(10)
                        if kk == 27:
                            cap_res.release()
                            break
                    cv2.waitKey(3)
                    if k == 27 or kk == 27:
                        break

            k = cv2.waitKey(10)
            if k == 27:
                # cv2.destroyAllWindows()
                cap.release()
                break #fixed time normal mode
    # unlimited time difficult  mode
    elif k == 113 or kk ==113:
        img = cv2.imread('black2.png')
        start_time = time.time()
        cap = cv2.VideoCapture(1)
        load = cv2.VideoCapture('count1.mp4')
        t1 = time.time()
        mixer.music.load('mm.mp3')
        mixer.music.play()
        while (1):
            t2 = time.time()
            if (t2 - t1 > tm):
                break
            ret, frame = load.read()
            cv2.imshow('img', frame)
            k = cv2.waitKey(20)

        mixer.music.load('pop.mp3')
        mixer.music.play()
        marks = 0

        bubble = cv2.imread('bubble2.jpg')
        make_bubble(img,150,630,1,bubble)  #1
        make_bubble(img, 820, 600, 1,bubble) #2
        make_bubble(img, 1250, 600, 2,bubble) #3
        make_bubble(img, 450, 500, 2,bubble) #4
        make_bubble(img, 1020, 500, 2,bubble) #5
        make_bubble(img, 200, 350, 3,bubble) #6
        make_bubble(img, 180, 200, 5,bubble) #7
        make_bubble(img, 450, 230, 3,bubble) #8
        make_bubble(img, 800, 250, 4,bubble) #9
        make_bubble(img, 1200, 250, 4,bubble) #10
        make_bubble(img, 400, 50, 5,bubble) #11
        make_bubble(img, 800, 50, 5,bubble) #12

        flag1 = 0
        flag2 = 0
        flag3 = 0
        flag4 = 0
        flag5 = 0
        flag6 = 0
        flag7 = 0
        flag8 = 0
        flag9 = 0
        flag10 = 0
        flag11 = 0
        flag12 = 0

        start_time = time.time()
        while (cap.isOpened()):
            ret, frame = cap.read()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            imgThreshLow = cv2.inRange(hsv, (0, 155, 155), (18, 255, 255))
            imgThreshHigh = cv2.inRange(hsv, (165, 155, 155), (179, 255, 255))
            imgThresh = cv2.add(imgThreshLow, imgThreshHigh)
            imgThresh = cv2.GaussianBlur(imgThresh, (3, 3), 2)  # blur
            imgThresh = cv2.dilate(imgThresh, np.ones((5, 5), np.uint8))  # close image (dilate, then erode)
            frame2 = cv2.erode(imgThresh, np.ones((5, 5), np.uint8))

            make_rect(frame,65,270,40)
            crop_frame1 = crop_rect(frame2, 65,270)
            make_rect(frame, 355, 270, 40)
            crop_frame2 = crop_rect(frame2, 355, 270)
            make_rect(frame, 550, 275, 40)
            crop_frame3 = crop_rect(frame2, 550, 275)
            make_rect(frame, 190, 220, 40)
            crop_frame4 = crop_rect(frame2, 190, 220)
            make_rect(frame, 445, 230, 40)
            crop_frame5 = crop_rect(frame2, 445, 230)
            make_rect(frame, 75, 155, 40)
            crop_frame6 = crop_rect(frame2, 75, 155)
            make_rect(frame, 65, 85, 40)
            crop_frame7 = crop_rect(frame2, 65, 85)
            make_rect(frame, 180, 100, 40)
            crop_frame8 = crop_rect(frame2, 180, 100)
            make_rect(frame, 345, 110, 40)
            crop_frame9 = crop_rect(frame2, 345, 110)
            make_rect(frame, 540, 120, 40)
            crop_frame10 = crop_rect(frame2, 540, 120)
            make_rect(frame,155, 15, 40)
            crop_frame11 = crop_rect(frame2,155, 15)
            make_rect(frame, 345, 15, 40)
            crop_frame12 = crop_rect(frame2, 345, 15)
            bubble1 = cv2.imread('smile3.jpg')
            if flag1 == 0:
                if cv2.countNonZero(crop_frame1) > th:
                    change_bubble(img, 150, 630, 1,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 1
                    flag1 = 1;
            if flag2 == 0:
                if cv2.countNonZero(crop_frame2) > th:
                    change_bubble(img, 820, 600, 1,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 1
                    flag2 = 1;
            if flag3 == 0:
                if cv2.countNonZero(crop_frame3) > th:
                    change_bubble(img, 1250, 600, 2,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 2
                    flag3 = 1;
            if flag4 == 0:
                if cv2.countNonZero(crop_frame4) > th:
                    change_bubble(img, 450, 500, 2,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 2
                    flag4 = 1;
            if flag5 == 0:
                if cv2.countNonZero(crop_frame5) > th:
                    change_bubble(img, 1020, 500, 2,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 2
                    flag5 = 1;
            if flag6 == 0:
                if cv2.countNonZero(crop_frame6) > th:
                    change_bubble(img, 200, 350, 3,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 3
                    flag6 = 1;
            if flag7 == 0:
                if cv2.countNonZero(crop_frame7) > th:
                    change_bubble(img, 180, 200, 5,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 5
                    flag7 = 1;
            if flag8 == 0:
                if cv2.countNonZero(crop_frame8) > th:
                    change_bubble(img, 450, 230, 3,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 3
                    flag8 = 1;
            if flag9 == 0:
                if cv2.countNonZero(crop_frame9) > th:
                    change_bubble(img, 800, 250, 4,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 4
                    flag9 = 1;
            if flag10 == 0:
                if cv2.countNonZero(crop_frame10) > th:
                    change_bubble(img, 1200, 250, 4,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 4
                    flag10 = 1;
            if flag11 == 0:
                if cv2.countNonZero(crop_frame11) > th:
                    change_bubble(img, 400, 50, 5,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 5
                    flag11 = 1;
            if flag12 == 0:
                if cv2.countNonZero(crop_frame12) > th:
                    change_bubble(img, 800, 50, 5,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 5
                    flag12 = 1;

            end_time = time.time()
            if marks < 37:
                ee_time = end_time
                cv2.rectangle(img, (540, 320), (950, 460), (0, 0, 0), -1)
                cv2.putText(img, str(round(end_time - start_time, 3)), (550, 450), font, 3, (255, 255, 255), 2,
                            cv2.LINE_AA)
                cv2.rectangle(img, (240, 0), (340, 90), (0, 0, 0), -1)
                cv2.putText(img, 'score ', (50, 80), font, 2, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.putText(img, str(marks), (250, 80), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.namedWindow("img", cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow('img', img)
            else:
                cv2.rectangle(img, (240, 0), (340, 90), (0, 0, 0), -1)
                cv2.putText(img, 'score ', (50, 80), font, 2, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.putText(img, str(marks), (250, 80), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.rectangle(img, (540, 320), (950, 460), (0, 0, 0), -1)
                cv2.putText(img, str(round(ee_time - start_time, 3)), (550, 450), font, 3, (255, 255, 255), 2,
                            cv2.LINE_AA)
                cv2.imshow('img', img)
                k = cv2.waitKey(3000)
                cap.release()
                hm = cv2.imread('hs44.jpg')

                cv2.putText(hm, str(marks), (700, 315), font, 2, (255,255,0), 2, cv2.LINE_AA)
                #cv2.putText(hm, 'TIME ', (700, 900), font, 4, (0, 0, 0), 2, cv2.LINE_AA)
                cv2.putText(hm, str(round(ee_time - start_time, 0)), (700, 415), font, 2, (255,255,0), 2,
                            cv2.LINE_AA)
                while (1):
                    cv2.namedWindow("img", cv2.WND_PROP_FULLSCREEN)

                    cv2.setWindowProperty("img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                    cv2.imshow('img', hm)
                    cap_res = cv2.VideoCapture(1)
                    while (cap_res.isOpened()):
                        kk = 0
                        ret, frame_res = cap_res.read()
                        hsv = cv2.cvtColor(frame_res, cv2.COLOR_BGR2HSV)
                        mask2 = cv2.inRange(hsv, np.array([2, 50, 50]), np.array([15, 255, 255]))
                        kernel_square = np.ones((11, 11), np.uint8)
                        kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
                        dilation = cv2.dilate(mask2, kernel_ellipse, iterations=1)
                        erosion = cv2.erode(dilation, kernel_square, iterations=1)
                        dilation2 = cv2.dilate(erosion, kernel_ellipse, iterations=1)
                        filtered = cv2.medianBlur(dilation2, 5)
                        kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8))
                        dilation2 = cv2.dilate(filtered, kernel_ellipse, iterations=1)
                        kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
                        dilation3 = cv2.dilate(filtered, kernel_ellipse, iterations=1)
                        median = cv2.medianBlur(dilation2, 5)
                        ret, frame_res2 = cv2.threshold(median, 127, 255, 0)

                        cv2.rectangle(frame_res, (180, 300), (420, 340), (255, 255, 255), 2)
                        crop_frame_res = frame_res2[300:440, 180:420]
                        if cv2.countNonZero(crop_frame_res) > th2:
                            # chsnge_circle(frame_res, 150, 630, 1)
                            mixer.music.load('coin.mp3')
                            mixer.music.play()
                            # cv2.waitKey(2000)
                            mixer.music.load('pop.mp3')
                            mixer.music.play()
                            cap_res.release()
                            k = 27
                            break
                        kk = cv2.waitKey(10)
                        if kk == 27:
                            cap_res.release()
                            break
                    # cv2.imshow('frameres', frame_res)
                    cv2.waitKey(3)
                    if k == 27 or kk == 27:
                        break


            k = cv2.waitKey(10)
            if k == 27:
                cap.release()
                break
    # fixed time normal mode
    if k == 114 or kk ==114:      #fixed time normal mode
        img = cv2.imread('black2.png')
        start_time = time.time()
        cap = cv2.VideoCapture(1)
        load = cv2.VideoCapture('count1.mp4')
        t1 = time.time()
        mixer.music.load('mm.mp3')
        mixer.music.play()
        while (1):
            t2 = time.time()
            if (t2 - t1 > tm):
                break
            ret, frame = load.read()
            cv2.imshow('img', frame)
            k = cv2.waitKey(20)

        mixer.music.load('pop.mp3')
        mixer.music.play()
        marks = 0

        bubble = cv2.imread('bubble2.jpg')
        make_bubble(img,150,630,1,bubble)  #1
        make_bubble(img, 820, 600, 1,bubble) #2
        make_bubble(img, 1250, 600, 2,bubble) #3
        make_bubble(img, 450, 500, 2,bubble) #4
        make_bubble(img, 1020, 500, 2,bubble) #5
        make_bubble(img, 200, 350, 3,bubble) #6
        # make_bubble(img, 180, 200, 5,bubble) #7
        make_bubble(img, 450, 230, 3,bubble) #8
        make_bubble(img, 800, 250, 4,bubble) #9
        make_bubble(img, 1200, 250, 4,bubble) #10

        flag1 = 0
        flag2 = 0
        flag3 = 0
        flag4 = 0
        flag5 = 0
        flag6 = 0
        # flag7 = 0
        flag8 = 0
        flag9 = 0
        flag10 = 0
        # flag11 = 0
        # flag12 = 0

        start_time = time.time()
        while (cap.isOpened()):
            ret, frame = cap.read()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            imgThreshLow = cv2.inRange(hsv, (0, 155, 155), (18, 255, 255))
            imgThreshHigh = cv2.inRange(hsv, (165, 155, 155), (179, 255, 255))
            imgThresh = cv2.add(imgThreshLow, imgThreshHigh)
            imgThresh = cv2.GaussianBlur(imgThresh, (3, 3), 2)  # blur
            imgThresh = cv2.dilate(imgThresh, np.ones((5, 5), np.uint8))  # close image (dilate, then erode)
            frame2 = cv2.erode(imgThresh, np.ones((5, 5), np.uint8))

            make_rect(frame, 65, 270, 40)
            crop_frame1 = crop_rect(frame2, 65, 270)
            make_rect(frame, 355, 270, 40)
            crop_frame2 = crop_rect(frame2, 355, 270)
            make_rect(frame, 550, 275, 40)
            crop_frame3 = crop_rect(frame2, 550, 275)
            make_rect(frame, 190, 220, 40)
            crop_frame4 = crop_rect(frame2, 190, 220)
            make_rect(frame, 445, 230, 40)
            crop_frame5 = crop_rect(frame2, 445, 230)
            make_rect(frame, 75, 155, 40)
            crop_frame6 = crop_rect(frame2, 75, 155)
            # make_rect(frame, 65, 85, 40)
            # crop_frame7 = crop_rect(frame2, 65, 85)
            make_rect(frame, 180, 100, 40)
            crop_frame8 = crop_rect(frame2, 180, 100)
            make_rect(frame, 345, 110, 40)
            make_rect(frame, 345, 110, 40)
            crop_frame9 = crop_rect(frame2, 345, 110)
            make_rect(frame, 540, 120, 40)
            crop_frame10 = crop_rect(frame2, 540, 120)
            # make_rect(frame, 155, 15, 40)
            # crop_frame11 = crop_rect(frame2, 155, 15)
            # make_rect(frame, 345, 15, 40)
            # crop_frame12 = crop_rect(frame2, 345, 15)
            bubble1 = cv2.imread('smile3.jpg')
            if flag1 == 0:
                if cv2.countNonZero(crop_frame1) > th:
                    change_bubble(img, 150, 630, 1,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 1
                    flag1 = 1;
            if flag2 == 0:
                if cv2.countNonZero(crop_frame2) > th:
                    change_bubble(img, 820, 600, 1,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 1
                    flag2 = 1;
            if flag3 == 0:
                if cv2.countNonZero(crop_frame3) > th:
                    change_bubble(img, 1250, 600, 2,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 2
                    flag3 = 1;
            if flag4 == 0:
                if cv2.countNonZero(crop_frame4) > th:
                    change_bubble(img, 450, 500, 2,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 2
                    flag4 = 1;
            if flag5 == 0:
                if cv2.countNonZero(crop_frame5) > th:
                    change_bubble(img, 1020, 500, 2,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 2
                    flag5 = 1;
            if flag6 == 0:
                if cv2.countNonZero(crop_frame6) > th:
                    change_bubble(img, 200, 350, 3,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 3
                    flag6 = 1;
            if flag8 == 0:
                if cv2.countNonZero(crop_frame8) > th:
                    change_bubble(img, 450, 230, 3,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 3
                    flag8 = 1;
            if flag9 == 0:
                if cv2.countNonZero(crop_frame9) > th:
                    change_bubble(img, 800, 250, 4,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 4
                    flag9 = 1;
            if flag10 == 0:
                if cv2.countNonZero(crop_frame10) > th:
                    change_bubble(img, 1200, 250, 4,bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 4
                    flag10 = 1;

            end_time = time.time()
            if marks < 19 and end_time - start_time <t114:
                ee_time = end_time
                cv2.rectangle(img, (540, 320), (950, 460), (0, 0, 0), -1)
                cv2.putText(img, str(round(end_time - start_time, 3)), (550, 450), font, 3, (255, 255, 255), 2,
                            cv2.LINE_AA)
                cv2.rectangle(img, (240, 0), (340, 90), (0, 0, 0), -1)
                cv2.putText(img, 'score ', (50, 80), font, 2, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.putText(img, str(marks), (250, 80), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.namedWindow("img", cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow('img', img)
            else:
                cv2.rectangle(img, (240, 0), (340, 90), (0, 0, 0), -1)
                cv2.putText(img, 'score ', (50, 80), font, 2, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.putText(img, str(marks), (250, 80), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.rectangle(img, (540, 320), (950, 460), (0, 0, 0), -1)
                cv2.putText(img, str(round(ee_time - start_time, 3)), (550, 450), font, 3, (255, 255, 255), 2,
                            cv2.LINE_AA)
                cv2.imshow('img', img)
                k = cv2.waitKey(3000)
                cap.release()
                hm = cv2.imread('hs44.jpg')
                cv2.putText(hm, str(marks), (700, 315), font, 2, (255,255,0), 2, cv2.LINE_AA)
                #cv2.putText(hm, 'TIME ', (700, 900), font, 4, (0, 0, 0), 2, cv2.LINE_AA)
                cv2.putText(hm, str(round(ee_time - start_time, 0)), (700, 415), font, 2, (255,255,0), 2,
                            cv2.LINE_AA)
                while (1):
                    cv2.namedWindow("img", cv2.WND_PROP_FULLSCREEN)

                    cv2.setWindowProperty("img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                    cv2.imshow('img', hm)
                    cap_res = cv2.VideoCapture(1)
                    while (cap_res.isOpened()):
                        kk = 0
                        ret, frame_res = cap_res.read()
                        hsv = cv2.cvtColor(frame_res, cv2.COLOR_BGR2HSV)
                        mask2 = cv2.inRange(hsv, np.array([2, 50, 50]), np.array([15, 255, 255]))
                        kernel_square = np.ones((11, 11), np.uint8)
                        kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
                        dilation = cv2.dilate(mask2, kernel_ellipse, iterations=1)
                        erosion = cv2.erode(dilation, kernel_square, iterations=1)
                        dilation2 = cv2.dilate(erosion, kernel_ellipse, iterations=1)
                        filtered = cv2.medianBlur(dilation2, 5)
                        kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8))
                        dilation2 = cv2.dilate(filtered, kernel_ellipse, iterations=1)
                        kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
                        dilation3 = cv2.dilate(filtered, kernel_ellipse, iterations=1)
                        median = cv2.medianBlur(dilation2, 5)
                        ret, frame_res2 = cv2.threshold(median, 127, 255, 0)

                        cv2.rectangle(frame_res, (180, 300), (420, 340), (255, 255, 255), 2)
                        crop_frame_res = frame_res2[300:440, 180:420]
                        if cv2.countNonZero(crop_frame_res) > th2:
                            # chsnge_circle(frame_res, 150, 630, 1)
                            mixer.music.load('pop.mp3')
                            mixer.music.play()
                            # cv2.waitKey(2000)
                            cap_res.release()
                            k = 27
                            break
                        kk = cv2.waitKey(10)
                        if kk == 27:
                            cap_res.release()
                            break
                    # cv2.imshow('frameres', frame_res)
                    cv2.waitKey(3)
                    if k == 27 or kk == 27:
                        break

            # cv2.imshow('frame', frame)
            # cv2.imshow('thresh', frame2)

            k = cv2.waitKey(10)
            if k == 27:
                # cv2.destroyAllWindows()
                cap.release()
                break #fixed time normal mode
    # fixed time difficult  mode
    elif k == 115 or kk == 115:
        img = cv2.imread('black2.png')
        start_time = time.time()
        cap = cv2.VideoCapture(1)
        load = cv2.VideoCapture('count1.mp4')
        t1 = time.time()
        mixer.music.load('mm.mp3')
        mixer.music.play()
        while (1):
            t2 = time.time()
            if (t2 - t1 > tm):
                break
            ret, frame = load.read()
            cv2.imshow('img', frame)
            k = cv2.waitKey(20)

        mixer.music.load('pop.mp3')
        mixer.music.play()
        marks = 0

        bubble = cv2.imread('bubble2.jpg')
        make_bubble(img, 150, 630, 1, bubble)  # 1
        make_bubble(img, 820, 600, 1, bubble)  # 2
        make_bubble(img, 1250, 600, 2, bubble)  # 3
        make_bubble(img, 450, 500, 2, bubble)  # 4
        make_bubble(img, 1020, 500, 2, bubble)  # 5
        make_bubble(img, 200, 350, 3, bubble)  # 6
        make_bubble(img, 180, 200, 5, bubble)  # 7
        make_bubble(img, 450, 230, 3, bubble)  # 8
        make_bubble(img, 800, 250, 4, bubble)  # 9
        make_bubble(img, 1200, 250, 4, bubble)  # 10
        make_bubble(img, 400, 50, 5, bubble)  # 11
        make_bubble(img, 800, 50, 5, bubble)  # 12

        flag1 = 0
        flag2 = 0
        flag3 = 0
        flag4 = 0
        flag5 = 0
        flag6 = 0
        flag7 = 0
        flag8 = 0
        flag9 = 0
        flag10 = 0
        flag11 = 0
        flag12 = 0

        start_time = time.time()
        while (cap.isOpened()):
            ret, frame = cap.read()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            imgThreshLow = cv2.inRange(hsv, (0, 155, 155), (18, 255, 255))
            imgThreshHigh = cv2.inRange(hsv, (165, 155, 155), (179, 255, 255))
            imgThresh = cv2.add(imgThreshLow, imgThreshHigh)
            imgThresh = cv2.GaussianBlur(imgThresh, (3, 3), 2)  # blur
            imgThresh = cv2.dilate(imgThresh, np.ones((5, 5), np.uint8))  # close image (dilate, then erode)
            frame2 = cv2.erode(imgThresh, np.ones((5, 5), np.uint8))

            make_rect(frame, 65, 270, 40)
            make_rect(frame, 80, 270, 40)
            crop_frame1 = crop_rect(frame2, 80, 270)
            make_rect(frame, 220, 220, 40)
            crop_frame4 = crop_rect(frame2, 220, 220)
            make_rect(frame, 110, 145, 40)
            crop_frame6 = crop_rect(frame2, 110, 145)
            make_rect(frame, 85, 85, 40)
            crop_frame7 = crop_rect(frame2, 85, 85)
            make_rect(frame, 220, 95, 40)
            crop_frame8 = crop_rect(frame2, 220, 95)
            make_rect(frame, 200, 30, 40)
            crop_frame11 = crop_rect(frame2, 200, 30)

            # crop_frame1 = crop_rect(frame2, 65, 270)
            # make_rect(frame, 355, 270, 40)
            crop_frame2 = crop_rect(frame2, 355, 270)
            make_rect(frame, 550, 275, 40)
            crop_frame3 = crop_rect(frame2, 550, 275)
            make_rect(frame, 190, 220, 40)
            # crop_frame4 = crop_rect(frame2, 190, 220)
            # make_rect(frame, 445, 230, 40)
            crop_frame5 = crop_rect(frame2, 445, 230)
            make_rect(frame, 75, 155, 40)
            # crop_frame6 = crop_rect(frame2, 75, 155)
            # make_rect(frame, 65, 85, 40)
            # crop_frame7 = crop_rect(frame2, 65, 85)
            # make_rect(frame, 180, 100, 40)
            # crop_frame8 = crop_rect(frame2, 180, 100)
            # make_rect(frame, 345, 110, 40)
            crop_frame9 = crop_rect(frame2, 345, 110)
            make_rect(frame, 540, 120, 40)
            crop_frame10 = crop_rect(frame2, 540, 120)
            make_rect(frame, 155, 15, 40)
            # crop_frame11 = crop_rect(frame2, 155, 15)
            # make_rect(frame, 345, 15, 40)
            crop_frame12 = crop_rect(frame2, 345, 15)
            bubble1 = cv2.imread('smile3.jpg')

            if flag1 == 0:
                if cv2.countNonZero(crop_frame1) > th:
                    change_bubble(img, 150, 630, 1, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 1
                    flag1 = 1;
            if flag2 == 0:
                if cv2.countNonZero(crop_frame2) > th:
                    change_bubble(img, 820, 600, 1, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 1
                    flag2 = 1;
            if flag3 == 0:
                if cv2.countNonZero(crop_frame3) > th:
                    change_bubble(img, 1250, 600, 2, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 2
                    flag3 = 1;
            if flag4 == 0:
                if cv2.countNonZero(crop_frame4) > th:
                    change_bubble(img, 450, 500, 2, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 2
                    flag4 = 1;
            if flag5 == 0:
                if cv2.countNonZero(crop_frame5) > th:
                    change_bubble(img, 1020, 500, 2, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 2
                    flag5 = 1;
            if flag6 == 0:
                if cv2.countNonZero(crop_frame6) > th:
                    change_bubble(img, 200, 350, 3, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 3
                    flag6 = 1;
            if flag7 == 0:
                if cv2.countNonZero(crop_frame7) > th:
                    change_bubble(img, 180, 200, 5, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 5
                    flag7 = 1;
            if flag8 == 0:
                if cv2.countNonZero(crop_frame8) > th:
                    change_bubble(img, 450, 230, 3, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 3
                    flag8 = 1;
            if flag9 == 0:
                if cv2.countNonZero(crop_frame9) > th:
                    change_bubble(img, 800, 250, 4, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 4
                    flag9 = 1;
            if flag10 == 0:
                if cv2.countNonZero(crop_frame10) > th:
                    change_bubble(img, 1200, 250, 4, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 4
                    flag10 = 1;
            if flag11 == 0:
                if cv2.countNonZero(crop_frame11) > th:
                    change_bubble(img, 400, 50, 5, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 5
                    flag11 = 1;
            if flag12 == 0:
                if cv2.countNonZero(crop_frame12) > th:
                    change_bubble(img, 800, 50, 5, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks = marks + 5
                    flag12 = 1;

            end_time = time.time()
            if marks < 37 and end_time - start_time < t115:
                ee_time = end_time
                cv2.rectangle(img, (540, 320), (950, 460), (0, 0, 0), -1)
                cv2.putText(img, str(round(end_time - start_time, 3)), (550, 450), font, 3, (255, 255, 255), 2,
                            cv2.LINE_AA)
                cv2.rectangle(img, (240, 0), (340, 90), (0, 0, 0), -1)
                cv2.putText(img, 'score ', (50, 80), font, 2, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.putText(img, str(marks), (250, 80), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.namedWindow("img", cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow('img', img)
            else:
                cv2.rectangle(img, (240, 0), (340, 90), (0, 0, 0), -1)
                cv2.putText(img, 'score ', (50, 80), font, 2, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.putText(img, str(marks), (250, 80), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.rectangle(img, (540, 320), (950, 460), (0, 0, 0), -1)
                cv2.putText(img, str(round(ee_time - start_time, 3)), (550, 450), font, 3, (255, 255, 255), 2,
                            cv2.LINE_AA)
                cv2.imshow('img', img)
                k = cv2.waitKey(3000)
                cap.release()
                hm = cv2.imread('hs44.jpg')
                #cv2.putText(hm, 'GAME OVER! ', (500, 300), font, 4, (0, 0, 255), 2, cv2.LINE_AA)
                #cv2.putText(hm, 'SCORE ', (600, 700), font, 4, (0, 0, 0), 2, cv2.LINE_AA)
                cv2.putText(hm, str(marks), (700, 315), font, 2, (255,255,0), 2, cv2.LINE_AA)
                #cv2.putText(hm, 'TIME ', (700, 900), font, 4, (0, 0, 0), 2, cv2.LINE_AA)
                cv2.putText(hm, str(round(ee_time - start_time, 0)), (700, 415), font, 2, (255,255,0), 2,
                            cv2.LINE_AA)
                while (1):
                    cv2.namedWindow("img", cv2.WND_PROP_FULLSCREEN)

                    cv2.setWindowProperty("img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                    cv2.imshow('img', hm)
                    cap_res = cv2.VideoCapture(1)
                    while (cap_res.isOpened()):
                        kk = 0
                        ret, frame_res = cap_res.read()
                        hsv = cv2.cvtColor(frame_res, cv2.COLOR_BGR2HSV)
                        mask2 = cv2.inRange(hsv, np.array([2, 50, 50]), np.array([15, 255, 255]))
                        kernel_square = np.ones((11, 11), np.uint8)
                        kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
                        dilation = cv2.dilate(mask2, kernel_ellipse, iterations=1)
                        erosion = cv2.erode(dilation, kernel_square, iterations=1)
                        dilation2 = cv2.dilate(erosion, kernel_ellipse, iterations=1)
                        filtered = cv2.medianBlur(dilation2, 5)
                        kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8))
                        dilation2 = cv2.dilate(filtered, kernel_ellipse, iterations=1)
                        kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
                        dilation3 = cv2.dilate(filtered, kernel_ellipse, iterations=1)
                        median = cv2.medianBlur(dilation2, 5)
                        ret, frame_res2 = cv2.threshold(median, 127, 255, 0)

                        cv2.rectangle(frame_res, (180, 300), (420, 340), (255, 255, 255), 2)
                        crop_frame_res = frame_res2[300:440, 180:420]
                        if cv2.countNonZero(crop_frame_res) > th2:
                            # chsnge_circle(frame_res, 150, 630, 1)
                            mixer.music.load('pop.mp3')
                            mixer.music.play()
                            # cv2.waitKey(2000)
                            cap_res.release()
                            k = 27
                            break
                        kk = cv2.waitKey(10)
                        if kk == 27:
                            cap_res.release()
                            break
                    #cv2.imshow('frameres', frame_res)
                    cv2.waitKey(3)
                    if k == 27 or kk == 27:
                        break

            k = cv2.waitKey(10)
            if k == 27:
                # cv2.destroyAllWindows()
                cap.release()
                break
    elif k == 116 or kk ==116:
        img = cv2.imread('black2.png')
        start_time = time.time()
        cap = cv2.VideoCapture(1)
        load = cv2.VideoCapture('count1.mp4')
        t1 = time.time()
        mixer.music.load('mm.mp3')
        mixer.music.play()
        while (1):
            t2 = time.time()
            if (t2 - t1 > tm):
                break
            ret, frame = load.read()
            cv2.imshow('img', frame)
            k = cv2.waitKey(20)

        mixer.music.load('pop.mp3')
        mixer.music.play()
        marks1 = 0
        marks2 = 0
        cv2.rectangle(img, (680, 0), (700, 300), (255, 255, 255), 2)
        cv2.rectangle(img, (680, 550), (700, 786), (255, 255, 255), 2)
        bubble = cv2.imread('bubble2.jpg')

        make_bubble(img, 150, 630, 1, bubble)  # 1
        # make_bubble(img, 820, 600, 1,bubble) #2
        # make_bubble(img, 1250, 600, 2,bubble) #3
        make_bubble(img, 450, 500, 2, bubble)  # 4
        # make_bubble(img, 1020, 500, 2,bubble) #5
        make_bubble(img, 200, 350, 3, bubble)  # 6
        make_bubble(img, 180, 200, 4, bubble)  # 7
        make_bubble(img, 450, 230, 3, bubble)  # 8
        # make_bubble(img, 800, 250, 4,bubble) #9
        # make_bubble(img, 1200, 250, 4,bubble) #10
        make_bubble(img, 400, 50, 5, bubble)  # 11
        # make_bubble(img, 800, 50, 5,bubble) #12
        make_bubble(img, 840, 630, 1, bubble)  # 1
        # make_bubble(img, 820, 600, 1,bubble) #2
        # make_bubble(img, 1250, 600, 2,bubble) #3
        make_bubble(img, 1140, 500, 2, bubble)  # 4
        # make_bubble(img, 1020, 500, 2,bubble) #5
        make_bubble(img, 890, 350, 3, bubble)  # 6
        make_bubble(img, 870, 200, 4, bubble)  # 7
        make_bubble(img, 1140, 230, 3, bubble)  # 8
        # make_bubble(img, 800, 250, 4,bubble) #9
        # make_bubble(img, 1200, 250, 4,bubble) #10
        make_bubble(img, 1090, 50, 5, bubble)  # 11
        # make_bubble(img, 800, 50, 5,bubble) #12


        flag1 = 0
        flag2 = 0
        flag3 = 0
        flag4 = 0
        flag5 = 0
        flag6 = 0
        flag7 = 0
        flag8 = 0
        flag9 = 0
        flag10 = 0
        flag11 = 0
        flag12 = 0

        start_time = time.time()
        while (cap.isOpened()):
            ret, frame = cap.read()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            imgThreshLow = cv2.inRange(hsv, (0, 155, 155), (18, 255, 255))
            imgThreshHigh = cv2.inRange(hsv, (165, 155, 155), (179, 255, 255))
            imgThresh = cv2.add(imgThreshLow, imgThreshHigh)
            imgThresh = cv2.GaussianBlur(imgThresh, (3, 3), 2)  # blur
            imgThresh = cv2.dilate(imgThresh, np.ones((5, 5), np.uint8))  # close image (dilate, then erode)
            frame2 = cv2.erode(imgThresh, np.ones((5, 5), np.uint8))

            make_rect(frame,80,270,40)
            crop_frame1 = crop_rect(frame2, 80,270)
            make_rect(frame, 220, 220, 40)
            crop_frame4 = crop_rect(frame2, 220, 220)
            make_rect(frame, 110, 145, 40)
            crop_frame6 = crop_rect(frame2, 110, 145)
            make_rect(frame, 85, 85, 40)
            crop_frame7 = crop_rect(frame2, 85, 85)
            make_rect(frame, 220, 95, 40)
            crop_frame8 = crop_rect(frame2, 220, 95)
            make_rect(frame, 200, 30, 40)
            crop_frame11 = crop_rect(frame2, 200, 30)

            make_rect(frame, 370, 290, 40)
            crop_frame2 = crop_rect(frame2, 370, 290)
            make_rect(frame, 520, 245, 40)
            crop_frame3 = crop_rect(frame2, 520, 245)
            make_rect(frame, 415, 160, 40)
            crop_frame5 = crop_rect(frame2, 415, 160)
            make_rect(frame, 410, 100, 40)
            crop_frame9 = crop_rect(frame2, 410, 100)
            make_rect(frame, 535, 130, 40)
            crop_frame10 = crop_rect(frame2, 535, 130)
            make_rect(frame, 535, 40, 40)
            crop_frame12 = crop_rect(frame2, 535, 40)
            bubble1 = cv2.imread('smile3.jpg')
            # cv2.imshow('frame',frame)

            if flag1 == 0:
                if cv2.countNonZero(crop_frame1) > th:
                    # chsnge_circle(img, 150, 630, 1)
                    change_bubble(img, 150, 630, 1, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks1 = marks1 + 1
                    flag1 = 1;
            if flag2 == 0:
                if cv2.countNonZero(crop_frame2) > th:
                    # chsnge_circle(img, 820, 600, 1)
                    change_bubble(img, 840, 630, 1, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks2 = marks2 + 1
                    flag2 = 1;
            if flag3 == 0:
                if cv2.countNonZero(crop_frame3) > th:
                    # chsnge_circle(img, 1250, 600, 2)
                    change_bubble(img, 1140, 500, 1, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks2 = marks2 + 2
                    flag3 = 1;
            if flag4 == 0:
                if cv2.countNonZero(crop_frame4) > th:
                    # chsnge_circle(img, 450, 500, 2)
                    change_bubble(img, 450, 500, 1, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks1 = marks1 + 2
                    flag4 = 1;
            if flag5 == 0:
                if cv2.countNonZero(crop_frame5) > th:
                    # chsnge_circle(img, 1020, 500, 2)
                    change_bubble(img, 890, 350, 1, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks2 = marks2 + 2
                    flag5 = 1;
            if flag6 == 0:
                if cv2.countNonZero(crop_frame6) > th:
                    # chsnge_circle(img, 200, 350, 3)
                    change_bubble(img, 200, 350, 1, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks1 = marks1 + 3
                    flag6 = 1;
            if flag7 == 0:
                if cv2.countNonZero(crop_frame7) > th:
                    # chsnge_circle(img, 180, 200, 4)
                    change_bubble(img, 180, 200, 1, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks1 = marks1 + 4
                    flag7 = 1;
            if flag8 == 0:
                if cv2.countNonZero(crop_frame8) > th:
                    # chsnge_circle(img, 450, 230, 3)
                    change_bubble(img, 450, 230, 1, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks1 = marks1 + 3
                    flag8 = 1;
            if flag9 == 0:
                if cv2.countNonZero(crop_frame9) > th:
                    # chsnge_circle(img, 800, 250, 4)
                    change_bubble(img, 870, 200, 1, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks2 = marks2 + 4
                    flag9 = 1;
            if flag10 == 0:
                if cv2.countNonZero(crop_frame10) > th:
                    # chsnge_circle(img, 1200, 250, 4)
                    change_bubble(img, 1140, 230, 1, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks2 = marks2 + 4
                    flag10 = 1;
            if flag11 == 0:
                if cv2.countNonZero(crop_frame11) > th:
                    # chsnge_circle(img, 400, 50, 5)
                    change_bubble(img, 400, 50, 1, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks1 = marks1 + 5
                    flag11 = 1;
            if flag12 == 0:
                if cv2.countNonZero(crop_frame12) > th:
                    # chsnge_circle(img, 800, 50, 5)
                    change_bubble(img, 1090, 50, 1, bubble1)
                    mixer.music.load('coin.mp3')
                    mixer.music.play()
                    marks2 = marks2 + 5
                    flag12 = 1;

            end_time = time.time()
            if marks1 < 18 and marks2<18 and end_time - start_time <t116:
                ee_time = end_time
                cv2.rectangle(img, (540, 320), (800, 460), (0, 0, 0), -1)
                cv2.putText(img, str(round(end_time - start_time, 1)), (550, 450), font, 3, (255, 255, 255), 2,
                            cv2.LINE_AA)
                cv2.rectangle(img, (240, 0), (340, 90), (0, 0, 0), -1)
                cv2.putText(img, 'score ', (50, 80), font, 2, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.putText(img, str(marks1), (250, 80), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.rectangle(img, (900, 0), (1000, 90), (0, 0, 0), -1)
                cv2.putText(img, 'score ', (710, 80), font, 2, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.putText(img, str(marks2), (910, 80), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.namedWindow("img", cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow('img', img)
            else:
                cv2.rectangle(img, (540, 320), (800, 460), (0, 0, 0), -1)
                cv2.putText(img, str(round(end_time - start_time, 1)), (550, 450), font, 3, (255, 255, 255), 2,
                            cv2.LINE_AA)
                cv2.rectangle(img, (240, 0), (340, 90), (0, 0, 0), -1)
                cv2.putText(img, 'score ', (50, 80), font, 2, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.putText(img, str(marks1), (250, 80), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.rectangle(img, (900, 0), (1000, 90), (0, 0, 0), -1)
                cv2.putText(img, 'score ', (710, 80), font, 2, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.putText(img, str(marks2), (910, 80), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.imshow('img', img)
                k = cv2.waitKey(3000)
                cap.release()
                if(marks1>marks2):
                    hm = cv2.imread('image.jpg')
                    # cv2.putText(hm, 'Player 1 WON !! ', (600, 700), font, 4, (0, 0, 0), 2, cv2.LINE_AA)
                    cv2.putText(hm, str(marks1), (1000, 350), font, 4, (255, 255,0), 2, cv2.LINE_AA)
                    cv2.putText(hm, str(marks2), (1000, 550), font, 4, (255, 255,0), 2, cv2.LINE_AA)
                else:
                    hm = cv2.imread('image3.jpg')
                    cv2.putText(hm, str(marks2), (1000, 350), font, 3, (255, 255,0), 2, cv2.LINE_AA)
                    cv2.putText(hm, str(marks1), (1000, 550), font, 3, (255, 255,0), 2, cv2.LINE_AA)

                # cv2.putText(hm, 'TIME ', (700, 900), font, 4, (0,0,0), 2, cv2.LINE_AA)
                cv2.putText(hm, str(round(ee_time - start_time, 0)), (750, 225), font, 3, (0, 155, 255), 2,
                            cv2.LINE_AA)

                while(1):
                    cv2.namedWindow("img", cv2.WND_PROP_FULLSCREEN)

                    cv2.setWindowProperty("img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                    cv2.imshow('img', hm)
                    cap_res = cv2.VideoCapture(1)
                    while(cap_res.isOpened()):
                        kk=0
                        ret, frame_res = cap_res.read()
                        hsv = cv2.cvtColor(frame_res, cv2.COLOR_BGR2HSV)
                        mask2 = cv2.inRange(hsv, np.array([2, 50, 50]), np.array([15, 255, 255]))
                        kernel_square = np.ones((11, 11), np.uint8)
                        kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
                        dilation = cv2.dilate(mask2, kernel_ellipse, iterations=1)
                        erosion = cv2.erode(dilation, kernel_square, iterations=1)
                        dilation2 = cv2.dilate(erosion, kernel_ellipse, iterations=1)
                        filtered = cv2.medianBlur(dilation2, 5)
                        kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8))
                        dilation2 = cv2.dilate(filtered, kernel_ellipse, iterations=1)
                        kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
                        dilation3 = cv2.dilate(filtered, kernel_ellipse, iterations=1)
                        median = cv2.medianBlur(dilation2, 5)
                        ret, frame_res2 = cv2.threshold(median, 127, 255, 0)

                        cv2.rectangle(frame_res, (180, 300), (420, 440), (255, 255, 255), 2)
                        crop_frame_res = frame_res2[300:440, 180:420]
                        cv2.rectangle(img, (180, 300), (420, 340), (255, 255, 255), 2)
                        if cv2.countNonZero(crop_frame_res) > th2:
                            # chsnge_circle(frame_res, 150, 630, 1)
                            mixer.music.load('pop.mp3')
                            mixer.music.play()
                            cv2.rectangle(img, (180, 300), (420, 340), (255, 255, 255), 2)
                            # cv2.waitKey(2000)
                            cap_res.release()
                            k = 27
                            break
                        kk = cv2.waitKey(10)
                        if kk == 27 :
                            cap_res.release()
                            break
                    # cv2.imshow('frameres', frame_res)
                    cv2.waitKey(3)
                    if k == 27 or kk==27:
                        break



            # cv2.imshow('thresh', frame)

            k = cv2.waitKey(10)
            if k == 27:
                # cv2.destroyAllWindows()
                cap.release()
                break
    else:
        flag1 = 0
        flag2 = 0
        flag3 = 0
        flag4 = 0
        flag5 = 0
        flag6 = 0
        flag7 = 0
        flag8 = 0
        flag9 = 0
        flag10 = 0
        flag11 = 0
        flag12 = 0

cv2.destroyAllWindows()
cap.release()
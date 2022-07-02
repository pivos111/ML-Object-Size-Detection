from secrets import choice
from unicodedata import name
import cv2
import mediapipe as mp
import math

# Ipsos Kameras = 
#
def myCm(distance): 
  return distance/9.5 #7 eos 8

# Ipsos Kameras = 
#
def myDist(cm):
  return cm*9.5

def get_manhattan_distance(p, q):
    """ 
    Return the manhattan distance between points p and q
    assuming both to have the same number of dimensions
    """
    # sum of absolute difference between coordinates
    distance = 0
    for p_i,q_i in zip(p,q):
        distance += abs(p_i - q_i)
    
    return distance

# Objects Size Librari
librari=[
          ["akoustika",3],
          ["cd",13],
          ["megalo keri",10],
          ["meseo keri",8.5],
          ["mikro keri",6],
          ["vazaki",7.5],
          ["vides",14],
          ["xartakia",11]
        ]

flg1=False
flg2=False

while(flg1==False):
  choice1=input("Please press the number of your left (red) object.\n1. akoustika\n2. cd\n3. megalo keri\n4. meso keri\n5. mikro keri\n6. vazaki\n7. vides\n8. xartakia\n\nYour Choice = ")
  if(choice1=="1"):
    name1=librari[0][0]  
    size1=librari[0][1]
    flg1=True
  elif(choice1=="2"):
    name1=librari[1][0]
    size1=librari[1][1]
    flg1=True
  elif(choice1=="3"):
    name1=librari[2][0]
    size1=librari[2][1]
    flg1=True
  elif(choice1=="4"):
    name1=librari[3][0]
    size1=librari[3][1]
    flg1=True
  elif(choice1=="5"):
    name1=librari[4][0]
    size1=librari[4][1]
    flg1=True
  elif(choice1=="6"):
    name1=librari[5][0]
    size1=librari[5][1]
    flg1=True
  elif(choice1=="7"):
    name1=librari[6][0]
    size1=librari[6][1]
    flg1=True
  elif(choice1=="8"):
    name1=librari[7][0]
    size1=librari[7][1]
    flg1=True
  else:
    print("NOT VALID CHOICE!!")

while(flg2==False):
  choice2=input("Please press the number of your right (green) object.\n1. akoustika\n2. cd\n3. megalo keri\n4. meso keri\n5. mikro keri\n6. vazaki\n7. vides\n8. xartakia\n\nYour Choice = ")
  if(choice1!=choice2):
    if(choice2=="1"):
      name2=librari[0][0]
      size2=librari[0][1]
      flg2=True
    elif(choice2=="2"):
      name2=librari[1][0]
      size2=librari[1][1]
      flg2=True
    elif(choice2=="3"):
      name2=librari[2][0]
      size2=librari[2][1]
      flg2=True
    elif(choice2=="4"):
      name2=librari[3][0]
      size2=librari[3][1]
      flg2=True
    elif(choice2=="5"):
      name2=librari[4][0]
      size2=librari[4][1]
      flg2=True
    elif(choice2=="6"):
      name2=librari[5][0]
      size2=librari[5][1]
      flg2=True
    elif(choice2=="7"):
      name2=librari[6][0]
      size2=librari[6][1]
      flg2=True
    elif(choice2=="8"):
      name2=librari[7][0]
      size2=librari[7][1]
      flg2=True
    else:
      print("NOT VALID CHOICE!!")
  else:
    print("SAME WITH PREVIOUS CHOICE!!")



mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For webcam input:
#wCam,hCam=480,640
cap = cv2.VideoCapture(0)
#cap.set(3,wCam)
#cap.set(3,hCam)
Xantixeiras=0
Yantixeiras=0
Xdiktis=0
Ydiktis=0

with mp_hands.Hands(
    max_num_hands=1,
    model_complexity=0,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    #image = cv2.flip(image, 1)
    
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.putText(img=image,text="X",org=(160,300),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(0,255,0),thickness=2)
    #cv2.putText(img=image,text="|",org=(320,300),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(0,255,0),thickness=2)
    cv2.putText(img=image,text="X",org=(480,300),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(0,0,255),thickness=2) 
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        
        for id,lm in enumerate(hand_landmarks.landmark):
          #print(id,lm)
          h, w, c=image.shape
          #print("image shape")
          print(image.shape)
          cx,cy,cz=int(lm.x*w),int(lm.y*h),int(lm.z*c)
          
          #karpos
          if id==0:
            #print("karpos")
            #print(id,cx,cy,cz)
            Xkarpos=cx
            Ykarpos=cy
            Zkarpos=cz
          #antixeiras
          if id==4:
            #print("antixeiras")
            #print(id,cx,cy,cz)
            Xantixeiras=cx
            Yantixeiras=cy
            Zantixeiras=cz
          #diktis
          if id==8:
            #print("diktis")
            #print(id,cx,cy,cz)
            Xdiktis=cx
            Ydiktis=cy
            Zdiktis=cz
          #mesos
          if id==12:
            #print("mesos")
            #print(id,cx,cy,cz)
            Xmesos=cx
            Ymesos=cy
            Zmesos=cz
          #paramesos
          if id==16:
            #print("paramesos")
            #print(id,cx,cy,cz)
            Xparamesos=cx
            Yparamesos=cy
            Zparamesos=cz
          #mikro
          if id==20:
            #print("mikro")
            #print(id,cx,cy,cz)
            Xmikro=cx
            Ymikro=cy
            Zmikro=cz
          if(Xantixeiras!=0 and Yantixeiras!=0 and Xdiktis!=0 and Ydiktis!=0):
            mathDistance=math.dist((Xdiktis,Ydiktis,Zdiktis),(Xantixeiras,Yantixeiras,Zantixeiras))
            myDistance=math.pow(math.pow(Xdiktis-Xantixeiras,2)+math.pow(Ydiktis-Yantixeiras,2)+math.pow(Zdiktis-Zantixeiras,2),1/2)
            lenght=math.hypot(Xdiktis-Xantixeiras,Ydiktis-Yantixeiras)-20# to -20 me to mati to eida
            manchatanDistance=get_manhattan_distance((Xdiktis,Ydiktis),(Xantixeiras,Yantixeiras))
            #print("Pixel Distance is "+str(lenght))
            #print("Cm Distance is "+str((2.54*lenght)/96))
            print("Manchatan Distance is "+str(manchatanDistance))
            print("My Cm Distance is "+str(myCm(manchatanDistance)))
            #print("Math Distance is "+str(mathDistance))
            #print("My Distance is "+str(myDistance))
            print("--------------------------------------------------")
            cv2.line(image,(Xantixeiras,Yantixeiras),(Xdiktis,Ydiktis),(255,0,255),3)

            distanceScore1=abs(myCm(manchatanDistance)-size1)
            distanceScore2=abs(myCm(manchatanDistance)-size2)

            if(distanceScore1<distanceScore2): #score 1 winer
              cv2.line(image,(600,450),(600,450),(0,0,255),30)
              distanceScore=name1+" deksia"
              #print(distanceScore)
              #cv2.putText(img=image,text=name1,org=(30,470),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(255,0,0),thickness=2)
            elif(distanceScore2<distanceScore1): #score 2 winer
              cv2.line(image,(40,450),(40,450),(0,255,0),30)
              distanceScore=name2+" aristera"
              #print(distanceScore)
              #cv2.putText(img=image,text=name2,org=(30,470),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(255,0,0),thickness=2)

            halfDisnance=640/2
            if(Xkarpos<halfDisnance):
              cv2.line(image,(40,350),(40,350),(0,255,0),30)
              handScore=name1+" deksia"
              #print(handScore)
            elif(Xkarpos>halfDisnance):
              cv2.line(image,(600,350),(600,350),(0,0,255),30)
              handScore=name2+" aristera"
              #print(handScore)
            
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
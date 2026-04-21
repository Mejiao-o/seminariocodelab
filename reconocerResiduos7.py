import cv2
from ultralytics import YOLO

def programa():
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    custom_model = "runs/classify/train/weights/best.pt"
    # model
    model = YOLO(custom_model)

    while True:
        String = 'Results'
        success, img = cap.read()
        results = model(img, stream=True, verbose=False)
        for r in results:
            conf_val = dict(enumerate(r.probs.data.numpy(),1))
            names = r.names
            #print(conf_val, type(conf_val))
            #print(names, type(names))
            i=1
            max_index = max(conf_val, key=conf_val.get)
            for (k1,v1), (k2,v2) in zip(names.items(), conf_val.items()):
                #print(v1, "->", v2)
                String = str(v1) + "->" + str(v2)   
                if max_index == i:
                    color = (0,255,0)
                else:
                    color = (0,0,255)
                img = cv2.putText(img, String, (20, 35*i), cv2.FONT_HERSHEY_SIMPLEX ,  1.2, color , 2, cv2.LINE_AA) 
                i = i + 1 

        cv2.imshow('Webcam', img)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

programa()
import cv2
import numpy as np
import time
import sys
import os


CONFIDENCE = 0.5


SCORE_THRESHOLD = 0.5
IOU_THRESHOLD = 0.5


config_path = "C:/Users/oguz/Desktop/car-brand-detection-main/car-brand-detection-main/cfg/yolo-obj.cfg"
weights_path = "C:/Users/oguz/Desktop/car-brand-detection-main/car-brand-detection-main/weights/yolo-obj_final.weights"


LABELS = open("C:/Users/oguz/Desktop/car-brand-detection-main/car-brand-detection-main/data/obj.names").read().strip().split("\n")


COLORS = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")


print("[INFO] loading YOLO from disk...")
net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
ln = net.getLayerNames()
ln = [ln[i - 1] for i in net.getUnconnectedOutLayers().flatten()]  # DÜZELTİLEN KISIM


path_name = "C:/Users/oguz/Desktop/car-brand-detection-main/car-brand-detection-main/data/bmw.mp4"
output_path = "C:/Users/oguz/Desktop/car-brand-detection-main/car-brand-detection-main/output_video/bmw.avi"


vs = cv2.VideoCapture(path_name)
writer = None
(W, H) = (None, None)


while True:
    (grabbed, frame) = vs.read()
    if not grabbed:
        break

    if W is None or H is None:
        (H, W) = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
                                 swapRB=True, crop=False)
    net.setInput(blob)
    start = time.time()
    layerOutputs = net.forward(ln)
    end = time.time()

    boxes = []
    confidences = []
    classIDs = []

    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            if confidence > CONFIDENCE:
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")

                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))

                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)

    idxs = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE, SCORE_THRESHOLD)

    if len(idxs) > 0:
        for i in idxs.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])

            color = [int(c) for c in COLORS[classIDs[i]]]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
            cv2.putText(frame, text, (x, y - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    if writer is None:
        fourcc = cv2.VideoWriter_fourcc(*"MJPG")
        writer = cv2.VideoWriter(output_path, fourcc, 30,
                                 (frame.shape[1], frame.shape[0]), True)

    writer.write(frame)


print("[INFO] cleaning up...")
writer.release()
vs.release()

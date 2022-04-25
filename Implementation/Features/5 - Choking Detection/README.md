# Choking Detection

<p align="center">
  <img src="https://github.com/HxnDev/HospitalAid/blob/main/Features/Choking%20Detection/Extras/choke.png" width=200, height=300>
</p>

## Description:
In this feature, we designed a model that can monitor a hospital. For this feature, we are targeting the already admitted patients. As patients are admitted to their rooms and there is not always a nurse there to monitor every single person, we would need a camera to monitor for any unusual activity and alert the nurses/staff. In this, we would detect if a patient suddenly starts choking and if it is detected, the staff/doctor would be pinged accordingly so that appropriate attention is given because in these scenerios every second counts.

## Dataset:
For this, we gathered some data from a research paper  (conducted in collaboration with several universities) and some were recorded in a controlled environment.

For pre-processing and augumentation, following actions were performed:

#### Pre-Processing:
- Auto-orientation of pixel data (with EXIF-orientation stripping)
- Resize to 416x416 (Stretch)
#### Augumentation:
- Horizontal Flip
- Rotation between -5% and +5%
- Grayscaling 10% of images
- Saturation between -7% and +7%
- Brightness between -9% and +9%
- Exposure between -6% and +6%


#### Download Format:
The downloaded format of our dataset is "YOLOv5 PyTorch Txt Format".

#### Links to Dataset:
- Github Link: [Choking Dataset - GitHub](https://github.com/HxnDev/HospitalAid/tree/main/Features/Choking%20Detection/Dataset)

## Model Training:
Once we were done with the pre-processing of dataset, the next thing we needed to do was to design an implementation logic for our model and train it. For this purpose, we used a convolutional neural network. 

### Issue:
However, there was a major issue present - **flickering**. As our program was reading almost 30 frames in a single second, it was applying the predictions on each frame, which was not only computationally expensive but was inaccurate too. This is every frame is classified completely independent of the rest, which meant several consecutive frames might be classified differently and the classification of the action being performed would appear to ‘flicker’. The solution we came up with was using queues to implement a rolling average over predictions. We specify the number of frames in the start which are then stored in the queue. We then apply predictions on each of the frame in the queue and then take the average of the predictions. The answer is then displayed on the screen.

The overall algorithm can be summarized as:
-	Loop over all frames in the video file
-	For each frame, pass the frame through the CNN
-	Obtain the predictions from the CNN
-	Maintain a list of the last K predictions
-	Compute the average of the last K predictions and choose the label with the largest corresponding probability
-	Label the frame and write the output frame to disk

## Demo Video:
<p align="center">
  <img src="https://github.com/HxnDev/HospitalAid/blob/main/Features/Choking%20Detection/Extras/choking.gif" alt="animated" width=600 height=300>
</p>


# Fainting Detection

<p align="center">
  <img src="https://github.com/HxnDev/HospitalAid/blob/main/Features/Fainting%20Detection/Extras/faint.png" width=200 height=300>
</p>

## Description:
In this feature, we designed a model that can monitor a hospital.In hospitals, if a person faints, he/she needs to be put on a stretcher/wheelchair and attended to immediately. Hence, if such an incident occurs, the model would immediately alert the attendings to proceed towards the fainted person. Fainting detection requires the system to be able to predict from an image if a person is choking or not. Someone fainting (within the camera vision) would be noticed immediately and reported to the appropriate medical personnel. 

## Dataset:
For this, we gathered some data from a research paper  (conducted in collaboration with several universities) and some were recorded in a controlled environment.

For pre-processing and augumentation, following actions were performed:

#### Pre-Processing:
- Resize to 416x416 (Stretch)
#### Augumentation:
- Grayscaling 15% of images
- Saturation between -7% and +7%
- Brightness between -9% and +9%
- Exposure between -6% and +6%
- Hue between -5% and +5%


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
  <img src="https://github.com/HxnDev/HospitalAid/blob/main/Features/Fainting%20Detection/Extras/fainting.gif" alt="animated" width=600 height=300>
</p>

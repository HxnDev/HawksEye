# Social Distancing Monitoring

<p align="center">
  <img src="https://github.com/HxnDev/HospitalAid/blob/main/Features/Social%20Distancing%20Monitoring/Extras/social-distancing-detector-using-tensorflow-object-detection-model.jpg" width=500 height=400>
</p>

## Description:
It is critical for a hospital reception and nursing station to be manned at all times, so any patient may be attended to in their time of need. Our model is trained to monitor these environments (or similar..) and observe the presence of people. If the reception or stations are empty, then a note will be made of the incident and reported to the administration.

## Dataset:
For the pre-processing of dataset, we first needed to gather the dataset. For this, we used Microsoft’s COCO dataset . 

The pre-processing steps are as follows:

#### Pre-Processing:
- Size reduced from 4000x1800 to 800x360 keeping the same aspect ratio
- Auto-orient
#### Augumentation:
- 1.5% blur within the bounding box
- Brightness from -19% to +19%
- Grayscale applied to 20% of the images
- Hue between -17% to +17%


#### Download Format:
The downloaded format of our dataset is "YOLOv5 PyTorch Txt Format".

#### Links to Dataset:
- Github Link: [Social Distancing Dataset - GitHub](https://github.com/HxnDev/HospitalAid/tree/main/Features/Social%20Distancing%20Monitoring/Dataset)

## Implementation
Once we were done with the pre-processing of dataset, the next thing we needed to do was to train our model and design an implementation logic for our model. The logic that we decided was that first of all we needed to detect every person in the given frame. So, for this we used COCO’s pre-trained weights to detect people. Once every person was detected, we were calculating the center point of each person. Then the next step was to calculate the Euclidian Distance between two center points. If the distance is less than the set threshold i.e., 150, then it will be marked as a violation of social distancing, else it’s perfectly normal.

## Demo Video:
<p align="center">
  <img src="https://github.com/HxnDev/HospitalAid/blob/main/Features/Social%20Distancing%20Monitoring/Extras/social_distancing.gif" alt="animated" width=600 height=300>
</p>

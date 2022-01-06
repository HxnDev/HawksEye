# Nursing Counter Monitoring

<p align="center">
  <img src="https://github.com/HxnDev/HospitalAid/blob/main/Features/Nursing%20Counter%20Monitoring/Extras/vastu-1581470219.jpg">
</p>

## Description:
It is critical for a hospital reception and nursing station to be manned at all times, so any patient may be attended to in their time of need. Our model is trained to monitor these environments (or similar..) and observe the presence of people. If the reception or stations are empty, then a note will be made of the incident and reported to the administration.

## Dataset:
For this we are using a combination of two different datsets:
- Hospital CCTV Footage of Reception
- Manually recorded videos of Nursing Counter.

The nursing counter one was recorded manually under proper supervision and we now have following type of data:
- Empty Station (No person)
- 1 person at the station
- 2 people at the station
- 3 people at the station
- 4 people at the station
- Random number of people sitting and standing at the station

The diversity and variety of our dataset allows for a better, smarter model. Our dataset has been annotated using [Roboflow](https://roboflow.com/) - additionally, we also augmented it to increase size and variety of training data.

For pre-processing and augumentation, following actions were performed:

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
- Github Link: [Nursing Counter Dataset - GitHub](https://github.com/HxnDev/HospitalAid/tree/main/Features/Nursing%20Counter%20Monitoring/Dataset) 


## Implementation
Once we were done with the pre-processing of dataset, the next thing we needed to do was to train our model and design an implementation logic for our model. The logic that we decided was that if even a single person is detected on the counter, then this will be a normal activity for us but if our model is unable to detect any person for a reserved period of time (>= 5 mins), then this will be considered as an abnormal activity and an alert will be generated along with the log being maintained in a file. 

## Demo Video:
![Alt Text](https://github.com/HxnDev/HospitalAid/blob/main/Features/Nursing%20Counter%20Monitoring/Extras/counter.gif)

# Social Distancing Monitoring

<p align="center">
  <img src="https://github.com/HxnDev/HospitalAid/blob/main/Social%20Distancing%20Monitoring/images/social-distancing-detector-using-tensorflow-object-detection-model.jpg">
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

The diversity and variety of our dataset allows for a better, smarter model.Our dataset has been annotated using [Roboflow](https://roboflow.com/) - additionally, we also augmented it to increase size and variety of training data.

For pre-processing and augumentation, following actions were performed:

#### Pre-Processing:
- Size reduced from 4000x1800 to 800x360 keeping the same aspect ratio
- Auto-orient
#### Augumentation:
- 1.5% blur within the bounding box
- Brightness from -19% to +19%
- Grayscale applied to 20% of the images
- Hue between -17% to +17%

After applying all the above our dataset consisted of the following:
- Training Set: 2.2k images (88%)
- Validation Set: 206 (8%)
- Test Set: 103 (4%)

#### Download Format:
The downloaded format of our dataset is "YOLOv3 Darknet Txt Format".

#### Links to Dataset:
- Github Link: [Nursing Counter Dataset - GitHub](https://github.com/HxnDev/HospitalAid/tree/main/Nursing%20Counter%20Monitoring/dataset) 
- Drive Link: [Nursing Counter Dataset - Google Drive](https://drive.google.com/drive/u/1/folders/1rMW2RIcD7rUYIvIOQ-gMUguEaf8eb14j)
- Roboflow Link: [Nursing Counter Dataset - Roboflow](https://app.roboflow.com/project/empty-station-detection/7)


## Implementation
Our model was built using the darknet implementation of YOLOv3. Environment used was Google Colab, with Tesla K80 as the GPU.
The model was trained to detect the presence of 1 or more people by training it on a fully annotated dataset of empty as well as occupied nursing stations and receptions.

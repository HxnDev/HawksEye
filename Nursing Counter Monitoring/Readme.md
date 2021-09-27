# Nursing Counter Monitoring

## Description:
In this feature, we designed a model that monitors nursing station and the reception of the hospital. Our model monitors both the nursing stations and the reception to detect if its empty at any point in time. We know that as hospitals are busy and incoming patients need immediate medical attention, hence it's mandatory that a person/nurse should always be available. Hence this feature. Incase our model detects an empty station, it will create a log of the abnormality for the administration to look into.

## Dataset:
For this, we are using a combination of two different datsets. 
- Hospital CCTV Footage of Reception
- Manually recorded videos of Nursing Counter.

The nursing counter one was recorded manually under proper supervision and we now have following type of data:
- Empty Station (No person)
- 1 person at the station
- 2 people at the station
- 3 people at the station
- 4 people at the station
- Random number of people sitting and standing at the station

Hence, we have a diversity in our data that covers every possible scenerio. Our dataset has been annotated using [Roboflow](https://roboflow.com/) which not only annotates the data but also pre-processes it and auguments it. 

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
The downloaded format of our dataset is "YOLOv4 PyTorch Txt Format".

#### Links to Dataset:
- Github Link: [Nursing Counter Dataset - GitHub](https://github.com/HxnDev/HospitalAid/tree/main/Nursing%20Counter%20Monitoring/dataset) 
- Drive Link: [Nursing Counter Dataset - Google Drive](https://drive.google.com/drive/u/1/folders/1rMW2RIcD7rUYIvIOQ-gMUguEaf8eb14j)


## Model Training:
For Model Training, we are using Google Colab.
--- To be Done ---

# Mask Detection

<p align="center">
  <img src="https://github.com/HxnDev/HospitalAid/blob/main/Features/Face%20Mask%20Monitoring/Extras/mask-detection-sample.jpg">
</p>

## Description:
In this feature, we designed a model that can monitor a hospital. Our model monitors the hospital, and observes the appropriate use of facial masks. It detects facial masks on the patients, doctors and staff. The idea behind this project? We have seen that throughout the COVID-19 pandemic, doctors were the most affected as they had to deal with infected patients and risk being infected themselves. Patients and doctors not following proper mask/gloves SOPs poses a big risk for doctors. 

## Dataset:
For this we are using the publicly available facial mask detection dataset available at [Roboflow](https://roboflow.com/). The dataset consists of random images of people wearing masks.

Our dataset has been annotated using [Roboflow](https://roboflow.com/) which not only annotates the data but also pre-processes it and auguments it. 

For pre-processing and augumentation, following actions were performed:

#### Pre-Processing:
- Auto-orientation of pixel data (with EXIF-orientation stripping)
- Resize to 416x416 (Stretch)
#### Augumentation:
- Brightness from -25% to +25%
- Horizontal Flip
- Rotation between -5% and +5%
- Grayscaling 10% of the images
- Hue between -10% and +10%
- Saturation between -7% and +7%
- Exposure between -6% and +6%


#### Download Format:
The downloaded format of our dataset is "YOLOv5 PyTorch Txt Format".

#### Links to Dataset:
- Github Link: [Face Mask Dataset - GitHub](https://github.com/HxnDev/HospitalAid/tree/main/Features/Face%20Mask%20Monitoring/Dataset)

## Model Training:
Once we were done with the pre-processing of dataset, the next thing we needed to do was to train our model and design an implementation logic for our model. The logic that we decided was that we had 2 classes : Mask and No-Mask. Our model detects faces and then passes them through the classifier. It will predict the class above a certain threshold which we had set to 0.5 for better predictions.

## Demo Video:
![Alt Text](https://github.com/HxnDev/HospitalAid/blob/main/Features/Face%20Mask%20Monitoring/Extras/mask.gif)

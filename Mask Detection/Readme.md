# Mask Detection

<p align="center">
  <img src="https://github.com/HxnDev/HospitalAid/blob/main/Mask%20Detection/mask-detection-sample.jpg">
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

After applying all the above our dataset consisted of the following:
- Training Set: 309 images (88%)
- Validation Set: 30 (8%)
- Test Set: 16 (4%)

#### Download Format:
The downloaded format of our dataset is "YOLOv4 PyTorch Txt Format".

#### Links to Dataset:
- Github Link: [Nursing Counter Dataset - GitHub](https://github.com/HxnDev/HospitalAid/tree/main/Mask%20Detection/data) 
- Drive Link: [Nursing Counter Dataset - Google Drive](https://drive.google.com/drive/u/1/folders/1SupIglExrGNMHuxGgx121KPteIBTHzNm)
- Roboflow Link: [Nursing Counter Dataset - Roboflow](https://app.roboflow.com/hassan-shahzad/mask-wearing-fgz3o/overview)


## Model Training:
For Model Training, we are using Google Colab.

--- To be Done ---

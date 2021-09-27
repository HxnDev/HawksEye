# Mask Detection

## Description:
In this feature, we designed a model that monitors the hospital. Our model monitors the hospital for facial mask. It detects facial mask on the patients, doctors and staff. The idea behind this project is that we have seen that throughout this pandemic, doctors were the most effected as they had to deal with patients not knowing if they are COVID positive or not and many of the doctors did contract the virus mainly because of patients/doctors not following proper SOPs such as masks and gloves.

## Dataset:
For this, we are using the publicly available facial mask detection dataset available at [Roboflow](https://roboflow.com/). The dataset consists of random images of people wearing masks.

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
- Github Link: [Nursing Counter Dataset - GitHub](https://github.com/HxnDev/HospitalAid/tree/main/Mask%20Detection/dataset) 
- Drive Link: [Nursing Counter Dataset - Google Drive](https://drive.google.com/drive/u/1/folders/1SupIglExrGNMHuxGgx121KPteIBTHzNm)
- Roboflow Link: [Nursing Counter Dataset - Roboflow](https://app.roboflow.com/hassan-shahzad/mask-wearing-fgz3o/overview)


## Model Training:
For Model Training, we are using Google Colab.
--- To be Done ---

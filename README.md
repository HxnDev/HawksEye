# Hospital Aid

![Logo](https://github.com/HxnDev/HospitalAid/blob/main/Logo/Hospital%20Aid%20Logo.png)

## Introduction
HospitalAid is a multi-platform application that aims to assist hospitals by removing the need for manual oversight of patients and hospital staff. It will monitor the hospital environment through the camera feed, notice medical abnormalities/incidents and alert appropriate personnel to address the situation. 

Detecting an anomaly will be done purely through computer vision, by performing real-time analysis of the live video feed coming in from the hospital’s existing surveillance infrastructure. Our system will have various deep learning models that will be trained to notice particular types of anomalies. Alerts will be sent to hospital staff via a mobile app, and incident statistics will be reported to the hospital administration through a web portal.

This system will integrate into the hospital’s existing infrastructure, enable automatic monitoring of patients and staff and create a better, safer environment. 

## Problem Statement:
Consider a hospital environment: always busy and frequently understaffed. There are hundreds of things going on at any given moment, and it is impossible for a hospital to ensure everything is running perfectly – every patient attended to, every anomaly noticed and corrected, every employee error noticed and so on. 

It is necessary, however, to monitor patients and employees; patients may require attention or urgent care at any moment and it is vital that hospital staff be available at their post when they are required to be present. This is done manually (e.g., a nurse may notice a patient needs medical attention or the manager might observe the reception is empty.) Manual oversight might be the only option for now, but it is unreliable and at risk of human error.

A patient may suffer from an incident e.g., fainting and no-one may be around to notice they need aid. Perhaps a nurse was supposed to be attending their room but all the nurses are absent from their station. Or a doctor may not be wearing their mask while attending a sick person, and falls ill themselves. These are just a few examples of incidents that could have been easily mitigated, had they just been observed quickly and attended to.

Many hospitals, especially private ones, already have some form of digital surveillance. But what do they do with that? Monitor for possible security incidents, perhaps notice any abnormal medical incidents – but all this is done by manually viewing the footage only after the fact.

## Business Opportunity:
- **Assisting Hospital Patients/Staff:** Manual oversight of patients and staff is laborious, time-consuming and not completely reliable. With HospitalAid in place, there would be a tireless system using the live video feed to monitor the environment, detect an anomaly and send out alerts.
- **Report of Incident Statistics:** Noticing an incident/anomaly and sending out alerts is obviously beneficial for patients, staff and the hospital as a whole. HospitalAid would not just be doing this, but would also collect data on incident statistics and present them for the administration to see. For example, a particular hospital might learn how many times in a day the reception was empty.

## Product Scope:
The digital surveillance system in a hospital will observe the hospital environment, staff and patients; the video feed received will be tested by our system. If it detects any sort of abnormality (choking, empty reception, fainting etc.), an alert message will be generated and sent to the concerned staff/personnel (nurses, doctors, security team, administration etc.) Additionally, logs of every abnormality would be maintained and records would be saved in a database with timestamps for administration to view.

## Features

### Implemented
- [Fainting Detection](https://github.com/HxnDev/HospitalAid/tree/main/Features/Fainting%20Detection)
- [Choking Detection](https://github.com/HxnDev/HospitalAid/tree/main/Features/Choking%20Detection)
- [Nursing Counter Detection](https://github.com/HxnDev/HospitalAid/tree/main/Features/Nursing%20Counter%20Monitoring)
- [Drowsiness Detection](https://github.com/HxnDev/HospitalAid/tree/main/Features/Drowsiness%20Detection)
- [Social Distancing Monitoring](https://github.com/HxnDev/HospitalAid/tree/main/Features/Social%20Distancing%20Monitoring)
- [Face Mask Detection](https://github.com/HxnDev/HospitalAid/tree/main/Features/Face%20Mask%20Monitoring)
- [Hand Gloves Monitoring](https://github.com/HxnDev/HospitalAid/tree/main/Features/Hand%20Gloves%20Monitoring)


## Requirements
For inference, any system with Python 2.x/3.x will do. For training, a CUDA-enabled GPU is required.

## Constraints:
- Detecting a person’s actions or behavior is difficult if they are at the edge of vision of interest
- Training a model requires significant amount of time, effort and data – adding new actions to detect would be very hard
- Live video feed will need to be passed to the models, requiring a backend server for them to run on
- If the camera quality is poor, then model accuracy will suffer
- Poor lighting in the hospital environment could also lead to incorrect/missing predictions
- A full-time internet connection will be required for forwarding video feed to server


## Tools Used
<p align="center">
<img src="https://cdn.worldvectorlogo.com/logos/python-5.svg" alt="Python" width="60" height="60"/> 
<img src="https://cdn.worldvectorlogo.com/logos/java-14.svg" alt="Java" width="60" height="60"/> 
<img src="https://cdn.worldvectorlogo.com/logos/react-2.svg" alt="React"  width="60" height="60"/> 
<img src="https://cdn.worldvectorlogo.com/logos/flutter.svg" alt="Flutter"  width="60" height="60"/> 
<img src="https://cdn.worldvectorlogo.com/logos/tensorflow-2.svg" alt="TensorFlow"  width="60" height="60"/> 
<img src="https://cdn.worldvectorlogo.com/logos/numpy-1.svg" alt="NumPy"  width="60" height="60"/> 
<img src="https://cdn.worldvectorlogo.com/logos/firebase-1.svg" alt="Firebase"  width="60" height="60"/> 
												      </p>

## 📫 Contact Sana: 
<p align="center">
	<a href="mailto:sanakahnn@gmail.com"><img src="https://img.icons8.com/bubbles/50/000000/gmail.png" alt="Gmail"/></a>
	<a href="https://github.com/sanaa-khan"><img src="https://img.icons8.com/bubbles/50/000000/github.png" alt="GitHub"/></a>
	<a href="https://www.linkedin.com/in/sana-khan-95a9771b3/"><img src="https://img.icons8.com/bubbles/50/000000/linkedin.png" alt="LinkedIn"/></a>
	
</p>

## 📫 Contact Hassan: 
<p align="center">
	<a href="mailto:chhxnshah@gmail.com"><img src="https://img.icons8.com/bubbles/50/000000/gmail.png" alt="Gmail"/></a>
	<a href="https://github.com/HxnDev"><img src="https://img.icons8.com/bubbles/50/000000/github.png" alt="GitHub"/></a>
	<a href="https://www.linkedin.com/in/hassan-shahzad-2a6617212/"><img src="https://img.icons8.com/bubbles/50/000000/linkedin.png" alt="LinkedIn"/></a>
	
</p>

## References
- AIZOOTech. (n.d.). AIZOOTech/facemaskdetection: detect faces and determine whether people are wearing mask. GitHub. Retrieved October 22, 2021, from https://github.com/AIZOOTech/FaceMaskDetection. 

- AlexeyAB. (n.d.). Alexeyab/Darknet: Yolov4 / scaled-yolov4 / yolo - neural networks for object detection (windows and linux version of darknet ). GitHub. Retrieved October 22, 2021, from https://github.com/AlexeyAB/darknet. 

- Balajisrinivas. (n.d.). Balajisrinivas/face-mask-detection: Detecting face masks using python, keras, opencv on real video streams. GitHub. Retrieved October 22, 2021, from https://github.com/balajisrinivas/Face-Mask-Detection. 

- Bochkovskiy, A., Wang, C.-Y., &amp; Liao, H.-Y. M. (2020, April 23). YOLOv4: Optimal Speed and Accuracy of Object Detection. Retrieved from https://arxiv.org/abs/2004.10934. 

- Cabani, A., Hammoudi, K., Behnhabiles, H., & Melkemi, M. (2021). MaskedFace-Net – A dataset of correctly/incorrectly masked face images in the context of COVID-19. Smart Health, 19. https://doi.org/https://doi.org/10.1016/j.smhl.2020.100144

- Cocodataset. (n.d.). Cocodataset/cocodataset.github.io. GitHub. Retrieved October 22, 2021, from https://github.com/cocodataset/cocodataset.github.io. 

- Fall detection. imvia. (2020, April 20). https://imvia.u-bourgogne.fr/en/database/fall-detection-dataset-2.html

- Ghoddoosian, R., Marnim, G., &amp; Athitsos, V. (2019, April 15). A Realistic Dataset and Baseline Temporal Model for Early Drowsiness Detection. Retrieved from https://arxiv.org/abs/1904.07312. 

- Gul, M. A., Yousaf, M. H., Nawaz, S., Ur Rehman, Z., & Kim, H. W. (2020). Patient monitoring by abnormal human activity recognition based on CNN Architecture. Electronics, 9(12), 1993. https://doi.org/10.3390/electronics9121993 

- K, G. (2020, June 11). COVID-19: AI-Enabled Social Distancing Detector using OpenCV. towards data science. Retrieved from https://towardsdatascience.com/covid-19-ai-enabled-social-distancing-detector-using-opencv-ea2abd827d34.

- Khan, W., Nawaz, F., &amp; Hussain, A. (2020, November 12). Video Dataset for COVID-19 Social Distancing and Human Detection Validation. Retrieved from DOI: 10.17632/xh6m6gxhvj.1. 

- Loey, M. (2021, February 15). COVID-19 Medical Face Mask Detection Dataset. kaggle. https://www.kaggle.com/mloey1/medical-face-mask-detection-dataset. 

- Redmon, J., & Farhadi, A. (2018). (tech.). YOLOv3: An Incremental Improvement. Retrieved from https://arxiv.org/abs/1804.02767. 

- Singh, S., Ahuja, U., Kumar, M., Kumar, K., & Sachdeva, M. (2021). Face mask detection using yolov3 and faster R-CNN models: COVID-19 environment. Multimedia Tools and Applications, 80(13), 19753–19768. https://doi.org/10.1007/s11042-021-10711-8 

- Yang, Y., Sarkis, R. A., El Atrache, R., Loddenkemper, T., & Meisel, C. (2021). Video-Based Detection of Generalized Tonic-Clonic Seizures Using Deep Learning. IEEE Journal of Biomedical and Health Informatics, 25(8), 2997–3008. https://doi.org/10.1109/JBHI.2021.3049649 

- Yang, D., Yurtsever, E., Renganathan, V., Redmill, K. A., &amp; Özgüner, Ü. (2021, July 5). A Vision-based social distancing and critical density detection system for covid-19. MDPI. Retrieved October 21, 2021, from https://www.mdpi.com/1424-8220/21/13/4608. 

- Ultralytics. (n.d.). Ultralytics/yolov5: Yolov5 in PyTorch &gt; ONNX &gt; CoreML &gt; TFLite. GitHub. Retrieved October 22, 2021, from https://github.com/ultralytics/yolov5.

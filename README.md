# Deep Learning-Based Bone Fracture Detection in X-Ray Images with Dockerized Web Deployment

This repository implements an end-to-end pipeline for detecting bone fractures in X-ray images using the YOLO11n object detection framework.

<div align="center">
	<img width="800" src="/asset/YOLO.png" alt="Material Bread logo">
	<p style="text-align: center;">Figure 1: Sample images with overlaid ground-truth bounding boxes.,Created by author.</p>   
</div>

## Dataset

The dataset comprises 5,455 public X-ray images, annotated with fracture bounding boxes.

Training: 3,779 images (25% with fractures), Validation: 835 images (80% with fractures), Test: 841 images

## Experiments

All models trained for 80 epochs under the following conditions:

1. Full Dataset (2 classes)

2. Positive-Only (fracture images only)

3. Model Scaling: nano, small, medium, large

4. Augmentation Variants: stronger on-the-fly rotations, flips, scaling

5. Training Strategies: multi-scale input, adjusted learning rate schedule

6. Loss Weight Tuning: varying DFL weight from 1.5 to 2.5

## Results

<div align="center">
	<img width="800" src="/asset/mAP_Results.png" alt="Material Bread logo">
	<p style="text-align: center;">Figure 2: All models have been trained for 80 epochs., Created by author.</p>   
</div>

## Deployment on Azure

[bone_fracture_detection_demo_Azure.webm](https://github.com/user-attachments/assets/008c6e02-b34d-4d57-9cb0-fd478c65cb5b)

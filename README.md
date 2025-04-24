# Deep Learning-Based Bone Fracture Detection in X-Ray Images with Dockerized Web Deployment

<div align="center">
    <img 
        width="400" 
        src="/asset/demo_pic.png" 
        alt="Material Bread logo" 
        style="border: 2px solid #000;"
    />
    <p style="text-align: center;">
        Figure 1: Demonstration of the developed application, Created by author.        
</div>

## Deploy on Azure

[bone_fracture_detection_demo_Azure.webm](https://github.com/user-attachments/assets/008c6e02-b34d-4d57-9cb0-fd478c65cb5b)


## Introduction

Bone fracture detection is a challenging task due to the variability in fracture shapes, sizes, and locations. This project uses deep learning-based object detection models to locate and classify fractures in X-ray images, aiding medical professionals in diagnostics and reducing human error.

The project is built using PyTorch, and YOLO11n  and aims to provide a pipeline for training, evaluating, and deploying object detection models in medical imaging.

## Data  

This dataset includes 5,455 annotated X-ray images in YOLO format, divided into training (3,779), validation (835), and test (841) sets. It focuses on binary-class classification ("Fracture" vs. "No Fracture") with varying bounding box sizes and class distribution, requiring further analysis. [Hosted on Roboflow](https://universe.roboflow.com/fracture-uofxm/bone-fracture-detection-ivsy6/dataset/1). 

Format: Images (JPEG) and corresponding annotations (YOLO)

<div align="center">
    <img width="800" src="/asset/YOLO.png" alt="Material Bread logo">
    <p style="text-align: center;">Figure 2: Sample images with overlaid ground-truth bounding boxes.,Created by author.</p>   
</div>


## Directory Structure

- **`app/`**: Contains the `.github/workflows/ci.yml` CI file, along with the Streamlit and FastAPI applications.
- **`src/`**: Houses all the Modeling and EDA code.



## Requirements

    Linux (Ubuntu)
    Python = 3.12
    Pytorch = 2.3
    NVIDIA GPU + CUDA CuDNN

## Roboflow_dataset
    └── data
         ├── images
         │    ├── train
         │    │    ├── train_img1.jpg
         │    │    ├── train_img2.jpg
         │    │    └── ...
         │    ├── val
         │    │    ├── val_img1.jpg
         │    │    ├── val_img2.jpg
         │    │    └── ...
         │    └── test
         │         ├── test_img1.jpg
         │         ├── test_img2.jpg
         │         └── ...
         └── labels
              ├── train
              │    ├── train_annotation1.txt
              │    ├── train_annotation2.txt
              │    └── ...
              ├── val
              │    ├── val_annotation1.txt
              │    ├── val_annotation2.txt
              │    └── ...
              └── test
                   ├── test_annotation1.txt
                   ├── test_annotation2.txt
                   └── ...

## Experiments

- All models trained for 80 epochs under the following conditions:

- Full Dataset (2 classes)

- Positive-Only (fracture images only)

- Model Scaling: nano, small, medium, large

- Augmentation Variants: stronger on-the-fly rotations, flips, scaling

- Training Strategies: multi-scale input, adjusted learning rate schedule

- Loss Weight Tuning: varying DFL weight from 1.5 to 2.5

- Configuration files (.yaml) define hyperparameters and augmentation pipelines.


## Perliminary Results


- Exp 1 provides a solid baseline with a balanced approach of two classes.
- Exp 2 shows that focusing on the fracture class can increase precision, though it slightly impacts recall.
- Exp 3 demonstrates that using a positive-only subset with a lower learning rate leads to the highest precision and a modest recall improvement, with a minor trade-off in strict localization (mAP95).

This work explored fracture detection on X-ray images using YOLOv11. The dataset included bounding box annotations for fractures, with 60% of images showing no fractures. Training for 60 epochs led to convergence around 30 epochs, achieving a validation mAP50 of approximately 0.6 and mAP50-90 of about 0.25. The marginal performance gain with the larger YOLO 11s model suggests that the high variability in image characteristics and fracture types, as well as the imbalance between positive and negative cases, pose significant challenges.

## Conclusion






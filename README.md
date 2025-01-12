# Bone Fraction Detection 

## Introduction

Bone fracture detection is a challenging task due to the variability in fracture shapes, sizes, and locations. This project uses deep learning-based object detection models to locate and classify fractures in X-ray images, aiding medical professionals in diagnostics and reducing human error.

The project is built using PyTorch, TensorFlow and YOLO11n  and aims to provide a pipeline for training, evaluating, and deploying object detection models in medical imaging.

## Data  

This dataset includes 5,455 annotated X-ray images in YOLO format, divided into training (3,779), validation (835), and test (841) sets. It focuses on binary-class classification ("Fracture" vs. "No Fracture") with varying bounding box sizes and class distribution, requiring further analysis. [Hosted on Roboflow](https://universe.roboflow.com/fracture-uofxm/bone-fracture-detection-ivsy6/dataset/1). 

Format: Images (JPEG) and corresponding annotations (YOLO)

<div align="center">
    <img width="800" src="/asset/YOLO.png" alt="Material Bread logo">
    <p style="text-align: center;">Fig1: few random images visualization within their realive ground-truth ,Created by author.</p>   
</div>


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

## Methodology







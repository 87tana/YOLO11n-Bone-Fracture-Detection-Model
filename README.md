# Bone Fraction Detection 


<div align="center">
    <img 
        width="600" 
        src="/asset/demo_pic.png" 
        alt="Material Bread logo" 
        style="border: 2px solid #000;"
    />
    <p style="text-align: center;">
        Figure 1: Demonstration of the developed application, Created by author.
        <br>
        View the 
        <strong>
            <a 
               href="https://private-user-images.githubusercontent.com/112851112/404653195-bc685ed7-2d9d-438a-8f84-f72b504b486b.webm?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzcyODA4NDAsIm5iZiI6MTczNzI4MDU0MCwicGF0aCI6Ii8xMTI4NTExMTIvNDA0NjUzMTk1LWJjNjg1ZWQ3LTJkOWQtNDM4YS04Zjg0LWY3MmI1MDRiNDg2Yi53ZWJtP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDExOSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAxMTlUMDk1NTQwWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZjhkNjI1YThlYWQxMGM2ZTVmNDc2N2FjYTUwYzcwNWM0YjEyZGVlNDU5MWMwMGIwY2I1ODRjZTk3MTg0ZDFmNiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.sk_6emgGQ0tJVPLlYx5-6QGAsZzIj0ZAIlj7MnDRiRI" 
               onclick="window.open('https://private-user-images.githubusercontent.com/112851112/404653195-bc685ed7-2d9d-438a-8f84-f72b504b486b.webm?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzcyODA4NDAsIm5iZiI6MTczNzI4MDU0MCwicGF0aCI6Ii8xMTI4NTExMTIvNDA0NjUzMTk1LWJjNjg1ZWQ3LTJkOWQtNDM4YS04Zjg0LWY3MmI1MDRiNDg2Yi53ZWJtP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDExOSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAxMTlUMDk1NTQwWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZjhkNjI1YThlYWQxMGM2ZTVmNDc2N2FjYTUwYzcwNWM0YjEyZGVlNDU5MWMwMGIwY2I1ODRjZTk3MTg0ZDFmNiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.sk_6emgGQ0tJVPLlYx5-6QGAsZzIj0ZAIlj7MnDRiRI', 'demoVideoWindow', 'width=800,height=600'); return false;">
               Demo Video
            </a>
        </strong>.
    </p>
</div>


## Introduction

Bone fracture detection is a challenging task due to the variability in fracture shapes, sizes, and locations. This project uses deep learning-based object detection models to locate and classify fractures in X-ray images, aiding medical professionals in diagnostics and reducing human error.

The project is built using PyTorch, TensorFlow and YOLO11n  and aims to provide a pipeline for training, evaluating, and deploying object detection models in medical imaging.

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

## Methodology

## Results


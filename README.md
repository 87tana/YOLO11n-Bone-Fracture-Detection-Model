# Bone Fraction Detection 

Trained YOLO11n for bobe fracture detection
## Data  

This dataset includes 5,455 annotated X-ray images in YOLO format, divided into training (3,779), validation (835), and test (841) sets. It focuses on binary-class classification ("Fracture" vs. "No Fracture") with varying bounding box sizes and class distribution, requiring further analysis. [Hosted on Roboflow](https://universe.roboflow.com/fracture-uofxm/bone-fracture-detection-ivsy6/dataset/1). 

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
         │    │    ├── val_img1.png
         │    │    ├── val_img2.png
         │    │    └── ...
         │    └── test
         │         ├── test_img1.png
         │         ├── test_img2.png
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


## Exploration

The Exploratory Data Analysis (EDA) was conducted in the EDA_Detection.ipynb notebook to gain insights into the dataset and its bounding box properties. The following key analyses were performed:

- Ratio of Height to Width:
        The height-to-width ratio of bounding boxes was calculated for each dataset subset (training, validation, and test).
        Insights:
            Helps identify any significant differences in bounding box aspect ratios across subsets.
            Useful for understanding image variability and potential challenges for model performance.

- Diagonal Distribution of Bounding Boxes:
        The diagonal length of each bounding box was computed across all subsets.
        Insights:
            Helps assess the range of bounding box sizes present in the dataset.
            A key indicator of object size variability, which impacts the model's ability to generalize.

- K-Means Clustering on Bounding Box Sizes (Width, Height):
        K-means clustering was applied to analyze patterns in bounding box sizes.
        Clustering reveals dominant size groups or outliers within the dataset.
        Insights:Guides anchor box generation, which is critical for optimizing object detection models.





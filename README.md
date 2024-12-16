# Bone Fraction Detection 

Trained YOLO11n for bobe fracture detection
## Data  

This dataset includes 5,455 annotated X-ray images in YOLOv8 format, divided into training (3,779), validation (835), and test (841) sets. It focuses on single-class classification ("Fracture" vs. "No Fracture") with varying bounding box sizes and class distribution, requiring further analysis. [Hosted on Roboflow](https://universe.roboflow.com/fracture-uofxm/bone-fracture-detection-ivsy6/dataset/1). the dataset likely originates from medical institutions or research collaborations, though specific collection details are not provided.

<div align="center">
    <img width="800" src="/asset/YOLO.png" alt="Material Bread logo">
    <p style="text-align: center;">Fig1: few random images visualization within their realive ground-truth ,Created by author.</p>   
</div>

## Exploration
 in the EDA_Detection.ipythons extract two important info from as well as performing k-means clustering on bounding box size
 - the ratio of height and width for each subset(train,validation and test)
 - the diagonal distribution for bbx in all subset
 - KMeans Clustering on Bounding Box Sizes (Width, Height)

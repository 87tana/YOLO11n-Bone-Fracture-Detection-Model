import streamlit as st
from ultralytics import YOLO
import cv2
from PIL import Image
import numpy as np
import io

def main():
    st.title("YOLO Fracture Detection App")

    # Upload image file using a file uploader
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        try:
            # Read the uploaded image
            image = Image.open(uploaded_file)

            # Create two columns for side-by-side display
            col1, col2 = st.columns(2)

            # Display the uploaded image in the first column
            with col1:
                st.image(image, caption="Uploaded Image", use_column_width=True)
                
                
                
            # Add a slider for setting the confidence threshold
            conf_threshold = st.slider(
                "Select Confidence Threshold",
                min_value=0.25,
                max_value=1.0,
                value=0.5,  # Default value is 0.5
                step=0.01
            )
                

            # Detect button
            if st.button("Detect Objects"):
                # Convert the image to a format compatible with YOLO (OpenCV format)
                image_np = np.array(image)

                # Load YOLO model
                model = YOLO("yolov11n_best.pt")  # You can replace 'yolov8n.pt' with another YOLO model

                # Apply YOLO to the image
                results = model.predict(image_np,conf=conf_threshold, augment=True)               


                # Visualize the detection results
                annotated_frame = results[0].plot()

                # Store detection result in session state
                st.session_state.annotated_frame = annotated_frame

                # Display the detection results in the second column
                with col2:
                    st.image(annotated_frame, caption="Detection Results", use_column_width=True)

                # Save the detection result to a temporary file
                result_image = Image.fromarray(annotated_frame)
                buffer = io.BytesIO()
                result_image.save(buffer, format="PNG")
                buffer.seek(0)

                # Provide a download button for the result
                st.download_button(
                    label="Download Detection Result",
                    data=buffer,
                    file_name="results.png",
                    mime="image/png"
                )
            elif 'annotated_frame' in st.session_state:
                # If detection result already exists in session state, display it
                with col2:
                    st.image(st.session_state.annotated_frame, caption="Detection Results", use_column_width=True)
                    
        except Exception as e:
            st.error(f"Error processing the image: {e}")

if __name__ == "__main__":
    main()

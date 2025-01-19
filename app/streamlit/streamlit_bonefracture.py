import streamlit as st
import requests
from PIL import Image
import io

# Backend URL
#BACKEND_URL = "http://127.0.0.1:8000/detect/"
BACKEND_URL = "http://backend.docker:8000/detect/" # use for local (docker) deployment

def main():
    st.title("YOLO Fracture Detection App")

    # Upload image file using a file uploader
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        
        # Create two columns for side-by-side display
        col1, col2 = st.columns(2)

        # Display the uploaded image in the first column
        with col1:
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
            
            
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
            try:               
                # Send the image and confidence threshold to the backend
                files = {"file": uploaded_file.getvalue()}
                data = {"conf_threshold": conf_threshold}
                response = requests.post(BACKEND_URL, files=files, data=data)
                
                if response.status_code == 200:
                    # Display the detection result
                    result_image = Image.open(io.BytesIO(response.content))
                    
                    with col2:
                        st.image(result_image, caption="Detection Results", use_column_width=True)

                    # Provide a download button for the result
                    buffer = io.BytesIO()
                    result_image.save(buffer, format="PNG")
                    buffer.seek(0)
                    st.download_button(
                        label="Download Detection Result",
                        data=buffer,
                        file_name="results.png",
                        mime="image/png"
                    )
                else:
                    st.error(f"Error: {response.json().get('error', 'Unknown error')}")

            except Exception as e:
                st.error(f"Error communicating with backend: {e}")

if __name__ == "__main__":
    main()

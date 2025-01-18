# Edge-Based Image Animation

## Project Description

The **Edge-Based Image Animation** project applies an animated edge-detection effect to a video file. The script processes a given video and creates two outputs:
1. **Animated Video**: The original video with dynamically animated edges.
2. **Edges-Only Video**: A video showing only the edges detected in each frame.

This project uses OpenCV to detect edges in the video frames and applies the animation effect by blending the original frames with the detected edges.

## Prerequisites

Before running the script, you need to have the following installed:

- **Python 3.x**
- **OpenCV**: A computer vision library that is used for image and video processing.
- **NumPy**: A library for numerical computations, used in this project for mathematical functions.

You can install the required libraries using `pip`:
```bash
pip install opencv-python numpy

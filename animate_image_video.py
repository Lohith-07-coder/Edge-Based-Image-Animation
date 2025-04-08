"""
Project Name: Edge-Based Image Animation
Author: Lohith M
Description: This program processes a video to create an animated edge effect and a video showing only the edges.
"""

import cv2
import numpy as np
import os

def apply_edge_animation(frame, intensity):
    """
    Apply an edge-detection-based animation effect to a video frame.
    The edges are scaled dynamically to create an animated effect.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    edges = cv2.Canny(gray, 100, 200)  # Detect edges
    edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)  # Convert edges to BGR format
    animated_frame = cv2.addWeighted(frame, 1 - intensity, edges_colored, intensity, 0)
    return animated_frame, edges_colored

def process_video(input_video_path, animated_output_path, edges_output_path):
    # Check if the input video exists
    if not os.path.exists(input_video_path):
        print(f"Error: File does not exist at {input_video_path}")
        return

    # Open the input video
    cap = cv2.VideoCapture(input_video_path)
    if not cap.isOpened():
        print("Error: Cannot open video file.")
        return

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Video Loaded: {width}x{height}, {fps} FPS, {frame_count} Frames")

    # Set up the video writers
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 output
    animated_writer = cv2.VideoWriter(animated_output_path, fourcc, fps, (width, height))
    edges_writer = cv2.VideoWriter(edges_output_path, fourcc, fps, (width, height))

    frame_num = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Finished processing all frames.")
            break

        # Calculate animation intensity based on a sinusoidal function
        intensity = (np.sin(frame_num * 0.05) + 1) / 2

        # Apply the edge animation effect and get edges
        animated_frame, edges_frame = apply_edge_animation(frame, intensity)

        # Write the processed frames to the output videos
        animated_writer.write(animated_frame)
        edges_writer.write(edges_frame)

        # Display progress
        print(f"Processing frame {frame_num}/{frame_count}", end="\r")

        # Uncomment to display frames during processing
        # cv2.imshow("Animated Frame", animated_frame)
        # cv2.imshow("Edges Only", edges_frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

        frame_num += 1

    # Release resources
    cap.release()
    animated_writer.release()
    edges_writer.release()
    cv2.destroyAllWindows()
    print(f"\nProcessing complete. Outputs saved to:\n- Animated Video: {animated_output_path}\n- Edges Video: {edges_output_path}")

# Paths to input and output videos
input_video_path = r"path"
animated_output_path = r"path"
edges_output_path = r"path"

# Run the video processing function
process_video(input_video_path, animated_output_path, edges_output_path)

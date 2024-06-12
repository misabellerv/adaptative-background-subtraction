# Adaptive Masking and Background Subtraction with Colored Mask

This project provides a tool to perform adaptive background subtraction and masking on video files. The resulting video highlights moving objects with a red mask and displays the original frame, the binary mask, and the colored masked frame side by side.

## Features

- **Background Subtraction**: Adaptively subtracts the background from the video.
- **Binary Mask**: Creates a binary mask to highlight moving objects.
- **Colored Mask**: Applies a red mask over the moving objects for better visualization.
- **Combined View**: Displays the original frame, binary mask, and colored masked frame in a single window.
- **Video Saving**: Saves the processed video with combined frames.

## Requirements

- Python 3.x
- OpenCV
- NumPy

You can install the required libraries using pip:

```bash
pip install opencv-python numpy

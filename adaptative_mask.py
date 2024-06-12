import cv2
import numpy as np
import argparse

# Argument parser for command-line options
parser = argparse.ArgumentParser(description="Adaptive masking and background subtraction with colored mask.")

# Command-line arguments
parser.add_argument('--video', default=None, help='Path to the video file.')
parser.add_argument('--learning-rate', default=0.3, type=float, help='Learning rate for background updating.')
parser.add_argument('--threshold', default=10, type=int, help='Threshold for background subtraction.')

args = parser.parse_args()

VIDEO_PATH = args.video
LEARNING_RATE = args.learning_rate
THRESHOLD = args.threshold

first_frame = True

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("Error opening video!")

# Resize video
desired_width = 700
desired_height = 500

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # Redimensiona o frame para o tamanho desejado
        frame = cv2.resize(frame, (desired_width, desired_height))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if first_frame:
            h, w, c = frame.shape
            background = gray.copy()
            first_frame = False
            continue

        # Compute background
        background = (1 - LEARNING_RATE) * background.astype('float32') + LEARNING_RATE * gray.astype('float32')

        # Subtract background
        subtracted_background = np.abs(gray.astype('float32') - background).astype('uint8')

        # Binary mask
        mask = (255 * (subtracted_background > THRESHOLD)).astype('uint8')

        # Colored mask
        colored_mask = np.zeros_like(frame)
        colored_mask[mask > 0] = [0, 0, 255]

        # Blend colored mask with original image to segmentation purposes
        masked_frame = cv2.addWeighted(frame, 1, colored_mask, 0.6, 0)

        # Resize frames
        frame_resized = cv2.resize(frame, (w, h))
        subtracted_resized = cv2.resize(subtracted_background, (w, h))
        mask_resized = cv2.resize(mask, (w, h))
        masked_frame_resized = cv2.resize(masked_frame, (w, h))
        mask_bgr = cv2.cvtColor(mask_resized, cv2.COLOR_GRAY2BGR)

        # Combine the frames
        combined_frame = np.hstack((frame_resized, mask_bgr, masked_frame_resized))

        cv2.imshow(f'Adaptive Background Subtraction with Segmentation Mask (lr={LEARNING_RATE},th={THRESHOLD})', combined_frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

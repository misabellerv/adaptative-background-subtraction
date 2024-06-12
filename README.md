# Adaptive Masking and Background Subtraction with Colored Mask

This project provides a tool to perform adaptive background subtraction and masking on video files. The resulting video highlights moving objects with a red mask and displays the original frame, the binary mask, and the colored masked frame side by side.

https://github.com/misabellerv/adaptative-background-subtraction/assets/88784791/e4ab7740-bc81-4809-b2e7-87b31e58f077

## Features

- **Background Subtraction**: Adaptively subtracts the background from the video.
- **Binary Mask**: Creates a binary mask to highlight moving objects.
- **Colored Mask**: Applies a red mask over the moving objects for better visualization.
- **Combined View**: Displays the original frame, binary mask, and colored masked frame in a single window.

- ### 1. Adaptive Background Subtraction

The first step is to calculate an adaptive background model. This is done by continuously updating a background model based on the video frames. The background model represents the static scenery present in the scene.

- **Initialization of Background Model**: Initially, the background model is initialized with the first frame of the video.
  
- **Update of Background Model**: For each new frame of the video, the background model is gradually updated to adapt to changes in the environment. This is done by calculating a weighted average between the existing background model and the new frame. The learning rate determines how quickly the background model adapts to changes in the scene. 

### 2. Background Subtraction

Once the background model is updated, it can be used to subtract the background from each frame of the video. This results in an image that highlights pixels that differ from the static background.

### 3. Masking

The next step is to create a binary mask that identifies pixels representing moving objects. This is done by applying a threshold to the subtracted background image. Pixels that exceed the threshold are marked as moving objects, while pixels that do not exceed the threshold are considered part of the static background.

### 4. Colored Masking

For better visualization, a colored mask can be applied over the moving objects in the original image. This highlights the moving objects in red, for example, while keeping the rest of the scene unchanged.

### 5. Combined Visualization

Finally, the original video frames, the binary mask, and the colored mask can be combined into a single image for visualization. This allows for a direct comparison between the original video and the highlighted moving objects.

## Requirements

- Python 3.x
- OpenCV
- NumPy

### Installing with Conda
You can install the requirements using conda:

```bash
conda env create -f environment.yml
```
### Installing with pip
You can install the requirements using pip:

```bash
pip install -r requirements.txt
```
## Running the project
First, clone this repository to your local machine:
```bash
git clone https://github.com/misabellerv/adaptative-background-subtraction.git
```
To this repo, add a video `.mp4` or `.avi`. There is an example video (oficina.mp4) if you want to experiment.
Activate the environment (conda or pip) and run:
```bash
python adaptative_mask.py --video <video_path> --learning-rate <learning_rate> --threshold <threshold>
```
Where `<video_path>` is the path to your test video, `<learning_rate>` indicates learning rate value, and `<threshold>` goes for the binary mask threshold. The last two parameters depend on your video composition, contrast, speed of changes, etc.

It's preferable that you use a video with fixed background and moving objects. The algorithm performs background subtraction and detect pixels from changing movement, so this might not work well when using videos with moving backgrounds.

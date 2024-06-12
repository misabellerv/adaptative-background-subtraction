# Adaptive Masking and Background Subtraction with Colored Mask

This project provides a tool to perform adaptive background subtraction and masking on video files. The resulting video highlights moving objects with a red mask and displays the original frame, the binary mask, and the colored masked frame side by side.

## Features

- **Background Subtraction**: Adaptively subtracts the background from the video.
- **Binary Mask**: Creates a binary mask to highlight moving objects.
- **Colored Mask**: Applies a red mask over the moving objects for better visualization.
- **Combined View**: Displays the original frame, binary mask, and colored masked frame in a single window.

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

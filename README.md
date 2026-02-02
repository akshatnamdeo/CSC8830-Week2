# Camera Calibration and Real-World 2D Measurement Using Perspective Projection

This repository contains the implementation and experimental evaluation for Week 2 of CSC 8830 (Computer Vision). The goal of this assignment is to calibrate a smartphone camera using a planar checkerboard target and then use the calibrated camera parameters to estimate the real-world two-dimensional dimensions of a planar object from a single image.

The implementation follows the pinhole camera model and perspective projection framework presented in the course videos. All experiments are implemented in Python using OpenCV.

---

## Repository Contents

- `step1_calibration.py`  
  Script for camera calibration using a planar checkerboard target.

- `step2_detection.py`  
  Script for estimating real-world 2D object dimensions from a single calibrated image.

- `calibration_data.npz`  
  Saved camera intrinsic matrix and distortion coefficients produced by the calibration script.

- `calibration_img/`  
  Folder containing checkerboard calibration images (`image*.jpeg`).

- `detection_img/`  
  Folder containing the object image (`book.jpg`) and a reference image showing the true object dimensions.

- `original_run.ipynb`  
  Jupyter notebook containing the full development workflow used during experimentation.

- `original_run.mp4`  
  Screen-recorded demo video in which the notebook and results are explained.

- `main.pdf`  
  Final written solution describing the methodology, equations, experimental setup, and results.

---

## Dependencies

- Python 3.x
- NumPy
- OpenCV

Install dependencies using:

```pip install numpy opencv-python```

---

## Step 1: Camera Calibration

Camera calibration is performed using five images of a planar checkerboard pattern displayed on a laptop screen.

### Calibration Setup

- Checkerboard pattern: 13 × 10 squares
- Inner corners used: 12 × 9
- Camera: Smartphone camera
- Images captured from different angles and distances

### Run Calibration

```python step1_calibration.py```

### Output

- Camera intrinsic matrix
- Lens distortion coefficients
- Mean reprojection error
- Calibration results saved to `calibration_data.npz`

This step must be completed before running the measurement script.

---

## Step 2 and Step 3: Real-World Measurement and Validation

A single image of a planar object (a book) is used to estimate real-world dimensions using perspective projection.

### Measurement Setup

- Object: Book placed upright against a wall
- Camera-to-object distance: approximately 2.2 meters
- Object surface approximately parallel to the image plane
- Pixel coordinates of the book corners selected manually, as described in the videos

### Run Measurement and Validation

```python step2_detection.py```


### Output

- Pixel width and height of the object
- Estimated real-world width and height (in meters)

Validation is performed by comparing the estimated dimensions to the true dimensions shown in the reference measurement image.

---

## Demo Video

The file `original_run.mp4` contains a screen-recorded demonstration in which the notebook (`original_run.ipynb`) is walked through step by step. The video explains the calibration process, the measurement procedure, and the final results.

---

## Written Solution

The file `main.pdf` contains the formal written solution, including:
- Problem description
- Camera model and projection equations
- Calibration procedure
- Measurement method
- Experimental results and error analysis

---

## Notes

- Calibration must be run once before measurement.
- Camera-to-object distance and pixel coordinates can be modified directly in `step2_detection.py`.
- Manual pixel selection is intentionally used to isolate the geometric aspects of perspective projection, as discussed in the course videos.

---

## Summary

This project demonstrates how camera calibration combined with perspective projection enables real-world measurement from a single image under reasonable geometric assumptions. The results align with the theoretical framework presented in the course videos and highlight the importance of accurate calibration and controlled imaging conditions.

# Assumptions:
# 1. calibration script has been ran once and has saved the config to calibration_data.npz
# 2. camera-to-object distance in meters (Z) and coordinates of object (pts) have been accurately set below

import cv2
import numpy as np

def measure_planar_object(img_path, calib_path, Z, pts):
    # Load calibration parameters
    data = np.load(calib_path)
    K = data["K"]
    dist = data["dist"]

    # Load image
    img = cv2.imread(img_path)
    h, w = img.shape[:2]

    # Undistort image
    new_K, _ = cv2.getOptimalNewCameraMatrix(K, dist, (w, h), 1)
    img_ud = cv2.undistort(img, K, dist, None, new_K)

    # Pixel distances
    width_px = np.linalg.norm(pts[1] - pts[0])
    height_px = np.linalg.norm(pts[2] - pts[0])

    # Effective focal lengths
    fx = new_K[0, 0]
    fy = new_K[1, 1]

    # Metric dimensions via perspective projection
    width_m = (Z / fx) * width_px
    height_m = (Z / fy) * height_px

    return width_px, height_px, width_m, height_m


# Experimental inputs
Z = 2.2

pts = np.array([
    [1404, 2364],
    [1648, 2352],
    [1410, 2682],
    [1664, 2682]
], dtype=np.float32)

# Run measurement
width_px, height_px, width_m, height_m = measure_planar_object(
    img_path="detection_img/book.jpg",
    calib_path="calibration_data.npz",
    Z=Z,
    pts=pts
)

print(f"Pixel width: {width_px:.2f} px")
print(f"Pixel height: {height_px:.2f} px")
print(f"Estimated real-world width: {width_m:.3f} m")
print(f"Estimated real-world height: {height_m:.3f} m")

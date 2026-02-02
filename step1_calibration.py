# Assumptions:
# 1. calibration images are in calibration_img folder with names like image*.jpeg
# 2. the checkerboard in calibration images is a 13x10 grid

import cv2
import numpy as np
import glob

# Counting only inner corners (13x10 to 12x9)
checkerboard = (12, 9)

# World points on planar calibration target (Z = 0)
objp = np.zeros((checkerboard[0] * checkerboard[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:checkerboard[0], 0:checkerboard[1]].T.reshape(-1, 2)

# Containers for 3D world points and corresponding 2D image points
objpoints = []
imgpoints = []

# Calibration images of checkerboard
images = glob.glob("calibration_img/image*.jpeg")

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect checkerboard inner corners
    found, corners = cv2.findChessboardCorners(
        gray,
        checkerboard,
        cv2.CALIB_CB_ADAPTIVE_THRESH +
        cv2.CALIB_CB_NORMALIZE_IMAGE
    )

    if found:
        # Subpixel refinement
        corners = cv2.cornerSubPix(
            gray,
            corners,
            (11, 11),
            (-1, -1),
            (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        )
        objpoints.append(objp)
        imgpoints.append(corners)

# Estimate intrinsic matrix, distortion coefficients, and per-image extrinsics
ret, K, dist, rvecs, tvecs = cv2.calibrateCamera(
    objpoints,
    imgpoints,
    gray.shape[::-1],
    None,
    None
)

# Reprojection error computation
error = 0
points = 0

for i in range(len(objpoints)):
    projected, _ = cv2.projectPoints(
        objpoints[i],
        rvecs[i],
        tvecs[i],
        K,
        dist
    )
    error += cv2.norm(imgpoints[i], projected, cv2.NORM_L2) ** 2
    points += len(projected)

reprojection_error = np.sqrt(error / points)

print("Camera matrix (K):\n", K)
print("Distortion coefficients:\n", dist.ravel())
print("Mean reprojection error:", reprojection_error)

# Save calibration results for reuse in measurement and validation
np.savez(
    "calibration_data.npz",
    K=K,
    dist=dist,
    reprojection_error=reprojection_error
)

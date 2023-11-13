from typing import List, Optional
import os

import matplotlib.pyplot as plt
import cv2
import numpy as np

PATH = "/Users/georgii/Movies/mountain_timelapse"
TARGET_WIDTH = 1920


def get_images_from_folder(images_path: str) -> List[str]:
    image_extensions = ["jpg", "jpeg", "png", "gif", "bmp"]
    return [file for file in os.listdir(images_path) if file.lower().split(".")[-1] in image_extensions]


def resize_image(image: np.ndarray, inplace: Optional[bool] = False) -> Optional[np.ndarray]:
    original_height, original_width = image.shape[:2]
    proportional_height = int((TARGET_WIDTH / original_width) * original_height)
    if not inplace:
        return cv2.resize(image, (TARGET_WIDTH, proportional_height))
    cv2.resize(image, (TARGET_WIDTH, proportional_height))


def calculate_exposure_difference(image1: np.ndarray, image2: np.ndarray) -> float:
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    diff = gray2 - gray1
    mean_diff = np.mean(diff)
    plt.imshow(diff)
    plt.show()
    return mean_diff


def main():
    images = sorted(get_images_from_folder(PATH))
    images_to_fix = 0
    for i in range(0, len(images) - 1):
        # 41 ane 42 images has a visible differece.
        image1 = cv2.imread("/".join([PATH, images[i]]))
        image2 = cv2.imread("/".join([PATH, images[i + 1]]))
        image1 = resize_image(image1)
        image2 = resize_image(image2)

        vise_mean = calculate_exposure_difference(image1, image2)
        if vise_mean > 70:
            print(f"{images[i]} and {images[i + 1]} exposure diff:")
            print(vise_mean, "\n")
        print(f"Examined {i} / {len(images)}")
        print("Images to fix: ", images_to_fix)


if __name__ == "__main__":
    main()

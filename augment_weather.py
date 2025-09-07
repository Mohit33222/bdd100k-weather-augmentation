"""
augment_dataset.py

- Reads images from bdd100k/images_10k/<split>
- Reads YOLO labels from bdd100k/yolo_format/<split>/<image>.txt
- Creates augmented images with suffixes: _fog, _rain, _lowlight, _snow
- Copies YOLO labels to bdd100k/augmented_labels/<split>/<image>_<effect>.txt
"""

import os
import random
from glob import glob
from tqdm import tqdm
import shutil
import cv2
import numpy as np
# ------------- CONFIG -------------
BASE = "bdd100k"
IMAGES_ROOT = os.path.join(BASE, "images_10k")        # original images
YOLO_LABELS_ROOT = os.path.join(BASE, "yolo_format")  # existing YOLO labels
AUG_IMAGES_ROOT = os.path.join(BASE, "augmented")     # output augmented images
AUG_LABELS_ROOT = os.path.join(BASE, "augmented_labels") # output augmented labels
SPLITS = ["train", "val", "test"]
TEST_LIMIT = None   # set int (e.g., 200) for quick tests, or None for all
MAKE_ORIGINAL_LABEL_COPY = True  # also copy original label to augmented_labels

# ------------- Utilities -------------
def ensure_dir(p):
    os.makedirs(p, exist_ok=True)

def list_images(split_img_dir):
    exts = ("*.jpg", "*.jpeg", "*.png")
    files = []
    for e in exts:
        files.extend(glob(os.path.join(split_img_dir, e)))
    return sorted(files)

def copy_label(orig_basename, split, out_basename):
    src = os.path.join(YOLO_LABELS_ROOT, split, orig_basename + ".txt")
    dst_dir = os.path.join(AUG_LABELS_ROOT, split)
    ensure_dir(dst_dir)
    dst = os.path.join(dst_dir, out_basename + ".txt")
    if os.path.exists(src):
        shutil.copy(src, dst)
        return True
    return False

# ------------- Augmentation Effects (OpenCV) -------------
def add_fog(img):
    overlay = img.copy()
    h, w = img.shape[:2]
    fog = np.full((h, w, 3), 255, dtype=np.uint8)
    alpha = random.uniform(0.15, 0.45)
    return cv2.addWeighted(overlay, 1 - alpha, fog, alpha, 0)

def add_rain(img):
    h, w = img.shape[:2]
    rain_layer = np.zeros_like(img, dtype=np.uint8)
    n_streaks = max(200, (w*h)//5000)
    for _ in range(n_streaks):
        x = random.randint(0, w-1)
        y = random.randint(0, h-1)
        length = random.randint(8, 20)
        x2 = min(w-1, x + random.randint(1,3))
        y2 = min(h-1, y + length)
        cv2.line(rain_layer, (x, y), (x2, y2), (200,200,200), 1)
    rain = cv2.blur(rain_layer, (3,3))
    return cv2.addWeighted(img, 0.8, rain, 0.2, 0)

def add_lowlight(img):
    gamma = random.uniform(1.8, 2.4)
    invGamma = 1.0 / gamma
    table = np.array([((i/255.0) ** invGamma) * 255 for i in range(256)]).astype("uint8")
    dark = cv2.LUT(img, table)
    if random.random() < 0.2:
        h, w = img.shape[:2]
        center = (random.randint(int(w*0.2), int(w*0.8)), random.randint(int(h*0.2), int(h*0.8)))
        radius = random.randint(int(min(w,h)*0.05), int(min(w,h)*0.12))
        mask = np.zeros_like(dark, dtype=np.uint8)
        cv2.circle(mask, center, radius, (255,230,200), -1)
        dark = cv2.addWeighted(dark, 1.0, mask, 0.12, 0)
    return cv2.GaussianBlur(dark, (3,3), 0)

def add_snow(img):
    h, w = img.shape[:2]
    snow_layer = np.zeros((h, w), dtype=np.uint8)
    n_dots = max(300, (w*h)//8000)
    for _ in range(n_dots):
        x = random.randint(0, w-1)
        y = random.randint(0, h-1)
        r = random.randint(0, 2)
        cv2.circle(snow_layer, (x,y), r, 255, -1)
    snow = cv2.GaussianBlur(snow_layer, (7,7), 0)
    alpha = (snow.astype(np.float32) / 255.0) * random.uniform(0.35, 0.8)
    alpha = alpha[..., None]
    out = (img.astype(np.float32) * (1 - alpha) + 255 * alpha).astype(np.uint8)
    k = random.choice([1,3,5])
    if k > 1:
        kernel = np.zeros((k,k))
        kernel[k//2,:] = np.ones(k)/k
        out = cv2.filter2D(out, -1, kernel)
    return out

EFFECTS = {
    "fog": add_fog,
    "rain": add_rain,
    "lowlight": add_lowlight,
    "snow": add_snow
}

# ------------- Main Augment Function -------------
def augment_split(split):
    split_img_dir = os.path.join(IMAGES_ROOT, split)
    out_img_dir = os.path.join(AUG_IMAGES_ROOT, split)
    out_lbl_dir = os.path.join(AUG_LABELS_ROOT, split)
    ensure_dir(out_img_dir)
    ensure_dir(out_lbl_dir)

    img_files = list_images(split_img_dir)
    if TEST_LIMIT:
        img_files = img_files[:TEST_LIMIT]

    if not img_files:
        print(f"⚠️ No images found for split '{split}' in {split_img_dir}")
        return 0, 0, 0

    processed = 0
    augmented_saved = 0
    labels_copied = 0

    for img_path in tqdm(img_files, desc=f"Augment {split}", unit="img"):
        img = cv2.imread(img_path)
        if img is None:
            continue
        basename = os.path.splitext(os.path.basename(img_path))[0]
        processed += 1

        # Optionally copy original label
        if MAKE_ORIGINAL_LABEL_COPY:
            if copy_label(basename, split, basename):
                labels_copied += 1

        for eff_name, eff_func in EFFECTS.items():
            aug_img = eff_func(img)
            out_name = f"{basename}_{eff_name}.jpg"
            out_path = os.path.join(out_img_dir, out_name)
            cv2.imwrite(out_path, aug_img)
            augmented_saved += 1

            # copy label for augmented
            if copy_label(basename, split, f"{basename}_{eff_name}"):
                labels_copied += 1

    return processed, augmented_saved, labels_copied

def run_all():
    ensure_dir(AUG_IMAGES_ROOT)
    ensure_dir(AUG_LABELS_ROOT)
    total_proc = total_aug = total_lbl = 0

    for sp in SPLITS:
        p, a, l = augment_split(sp)
        print(f"\nSplit {sp}: images processed={p}, augmented saved={a}, labels copied={l}")
        total_proc += p; total_aug += a; total_lbl += l

    print("\nALL DONE")
    print(f"Total processed: {total_proc}, total augmented images: {total_aug}, total labels copied: {total_lbl}")
    print("Augmented images dir:", AUG_IMAGES_ROOT)
    print("Augmented labels dir:", AUG_LABELS_ROOT)

if __name__ == "__main__":
    run_all()

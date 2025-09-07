# Comparative Dataset Report

This report compares the original BDD100K samples with the synthetic augmented dataset (fog, rain, low-light, snow).

## 1. Dataset Overview

| Split | Original images | Augmented images | Original labels | Augmented labels |
|-------|-----------------|------------------|-----------------|------------------|
| train | 7000 | 28000 | 57622 | 288110 |
| val | 1000 | 4000 | 0 | 0 |
| test | 2000 | 8000 | 16361 | 81805 |

## 2. Class distributions (bar charts)

### Train

**Original class distribution**  

![train original](images/train_orig_dist.png)

**Augmented class distribution**  

![train augmented](images/train_aug_dist.png)

### Val

**Original class distribution**  

![val original](images/val_orig_dist.png)

**Augmented class distribution**  

![val augmented](images/val_aug_dist.png)

### Test

**Original class distribution**  

![test original](images/test_orig_dist.png)

**Augmented class distribution**  

![test augmented](images/test_aug_dist.png)

## 3. Sample images (original vs augmentations)

Each row shows an original sample and its augmented variants (fog, rain, lowlight, snow) if available.

| Split | Original | Fog | Rain | Low-light | Snow |
|-------|----------|-----|------|-----------|------|
| train | ![img](images\train_0004a4c0-d4dff0ad.jpg) | ![img](images\train_0004a4c0-d4dff0ad_fog.jpg) | ![img](images\train_0004a4c0-d4dff0ad_rain.jpg) | ![img](images\train_0004a4c0-d4dff0ad_lowlight.jpg) | ![img](images\train_0004a4c0-d4dff0ad_snow.jpg) |
| train | ![img](images\train_00054602-3bf57337.jpg) | ![img](images\train_00054602-3bf57337_fog.jpg) | ![img](images\train_00054602-3bf57337_rain.jpg) | ![img](images\train_00054602-3bf57337_lowlight.jpg) | ![img](images\train_00054602-3bf57337_snow.jpg) |
| train | ![img](images\train_00067cfb-e535423e.jpg) | ![img](images\train_00067cfb-e535423e_fog.jpg) | ![img](images\train_00067cfb-e535423e_rain.jpg) | ![img](images\train_00067cfb-e535423e_lowlight.jpg) | ![img](images\train_00067cfb-e535423e_snow.jpg) |
| val | ![img](images\val_7d06fefd-f7be05a6.jpg) | ![img](images\val_7d06fefd-f7be05a6_fog.jpg) | ![img](images\val_7d06fefd-f7be05a6_rain.jpg) | ![img](images\val_7d06fefd-f7be05a6_lowlight.jpg) | ![img](images\val_7d06fefd-f7be05a6_snow.jpg) |
| val | ![img](images\val_7d128593-0ccfea4c.jpg) | ![img](images\val_7d128593-0ccfea4c_fog.jpg) | ![img](images\val_7d128593-0ccfea4c_rain.jpg) | ![img](images\val_7d128593-0ccfea4c_lowlight.jpg) | ![img](images\val_7d128593-0ccfea4c_snow.jpg) |
| val | ![img](images\val_7d15b18b-1e0d6e3f.jpg) | ![img](images\val_7d15b18b-1e0d6e3f_fog.jpg) | ![img](images\val_7d15b18b-1e0d6e3f_rain.jpg) | ![img](images\val_7d15b18b-1e0d6e3f_lowlight.jpg) | ![img](images\val_7d15b18b-1e0d6e3f_snow.jpg) |
| test | ![img](images\test_ac517380-00000000.jpg) | ![img](images\test_ac517380-00000000_fog.jpg) | ![img](images\test_ac517380-00000000_rain.jpg) | ![img](images\test_ac517380-00000000_lowlight.jpg) | ![img](images\test_ac517380-00000000_snow.jpg) |
| test | ![img](images\test_ac56c836-bdabca21.jpg) | ![img](images\test_ac56c836-bdabca21_fog.jpg) | ![img](images\test_ac56c836-bdabca21_rain.jpg) | ![img](images\test_ac56c836-bdabca21_lowlight.jpg) | ![img](images\test_ac56c836-bdabca21_snow.jpg) |
| test | ![img](images\test_ac6d4f42-00000000.jpg) | ![img](images\test_ac6d4f42-00000000_fog.jpg) | ![img](images\test_ac6d4f42-00000000_rain.jpg) | ![img](images\test_ac6d4f42-00000000_lowlight.jpg) | ![img](images\test_ac6d4f42-00000000_snow.jpg) |

## 4. Observations & Notes

- Augmentation expands dataset diversity and preserves label distribution shape in most classes.
- Please check for any missing labels (some augmented images may not have copied labels if original label files were missing).
- Next steps: train baseline detection model (YOLO) on the augmented+original data and benchmark on real adverse-weather datasets.

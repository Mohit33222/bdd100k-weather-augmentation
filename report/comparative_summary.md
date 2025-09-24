# Comparative Dataset Report

This report compares the original BDD100K samples with the synthetic augmented dataset (fog, rain, low-light, snow).

## 1. Dataset Overview

| Split | Original images | Augmented images | Original labels | Augmented labels |
|-------|-----------------|------------------|-----------------|------------------|
| train | 70000 | 280000 | 1277783 | 6388915 |
| val | 10000 | 40000 | 184067 | 920335 |
| test | 20000 | 80000 | 364783 | 1823915 |

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
| train | ![img](images\train_0000f77c-6257be58.jpg) | ![img](images\train_0000f77c-6257be58_fog.jpg) | ![img](images\train_0000f77c-6257be58_rain.jpg) | ![img](images\train_0000f77c-6257be58_lowlight.jpg) | ![img](images\train_0000f77c-6257be58_snow.jpg) |
| train | ![img](images\train_0000f77c-62c2a288.jpg) | ![img](images\train_0000f77c-62c2a288_fog.jpg) | ![img](images\train_0000f77c-62c2a288_rain.jpg) | ![img](images\train_0000f77c-62c2a288_lowlight.jpg) | ![img](images\train_0000f77c-62c2a288_snow.jpg) |
| train | ![img](images\train_0000f77c-cb820c98.jpg) | ![img](images\train_0000f77c-cb820c98_fog.jpg) | ![img](images\train_0000f77c-cb820c98_rain.jpg) | ![img](images\train_0000f77c-cb820c98_lowlight.jpg) | ![img](images\train_0000f77c-cb820c98_snow.jpg) |
| val | ![img](images\val_b1c66a42-6f7d68ca.jpg) | ![img](images\val_b1c66a42-6f7d68ca_fog.jpg) | ![img](images\val_b1c66a42-6f7d68ca_rain.jpg) | ![img](images\val_b1c66a42-6f7d68ca_lowlight.jpg) | ![img](images\val_b1c66a42-6f7d68ca_snow.jpg) |
| val | ![img](images\val_b1c81faa-3df17267.jpg) | ![img](images\val_b1c81faa-3df17267_fog.jpg) | ![img](images\val_b1c81faa-3df17267_rain.jpg) | ![img](images\val_b1c81faa-3df17267_lowlight.jpg) | ![img](images\val_b1c81faa-3df17267_snow.jpg) |
| val | ![img](images\val_b1c81faa-c80764c5.jpg) | ![img](images\val_b1c81faa-c80764c5_fog.jpg) | ![img](images\val_b1c81faa-c80764c5_rain.jpg) | ![img](images\val_b1c81faa-c80764c5_lowlight.jpg) | ![img](images\val_b1c81faa-c80764c5_snow.jpg) |
| test | ![img](images\test_cabc30fc-e7726578.jpg) | ![img](images\test_cabc30fc-e7726578_fog.jpg) | ![img](images\test_cabc30fc-e7726578_rain.jpg) | ![img](images\test_cabc30fc-e7726578_lowlight.jpg) | ![img](images\test_cabc30fc-e7726578_snow.jpg) |
| test | ![img](images\test_cabc30fc-eb673c5a.jpg) | ![img](images\test_cabc30fc-eb673c5a_fog.jpg) | ![img](images\test_cabc30fc-eb673c5a_rain.jpg) | ![img](images\test_cabc30fc-eb673c5a_lowlight.jpg) | ![img](images\test_cabc30fc-eb673c5a_snow.jpg) |
| test | ![img](images\test_cabc30fc-fd79926f.jpg) | ![img](images\test_cabc30fc-fd79926f_fog.jpg) | ![img](images\test_cabc30fc-fd79926f_rain.jpg) | ![img](images\test_cabc30fc-fd79926f_lowlight.jpg) | ![img](images\test_cabc30fc-fd79926f_snow.jpg) |

## 4. Observations & Notes

- Augmentation expands dataset diversity and preserves label distribution shape in most classes.
- Please check for any missing labels (some augmented images may not have copied labels if original label files were missing).
- Next steps: train baseline detection model (YOLO) on the augmented+original data and benchmark on real adverse-weather datasets.

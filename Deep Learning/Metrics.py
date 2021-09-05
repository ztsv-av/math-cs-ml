# IMAGE SEGMENTATION
# Area of Overlap = sum(True Positives - pixel correctly classified) (intersection)
# Combined area - total pixels in predicted segmentation mask +
#   total pixels in true segmentation mask
# Area of union - total pixels in predicted segmentation mask + 
#   total pixels in true segmentation mask - area of overlap
# Intersection Over Union (IoU) - area of overlap / area of union (evaluates worst case perfomance)
# Dice Score - 2 x (area of overlap / combined area) (evaluates average perfomance)

import numpy as np

def segmentation_IoU_DiceScore(y_true, y_pred):
  '''
  Computes IOU and Dice Score.

  Args:
    y_true (tensor) - ground truth label map
    y_pred (tensor) - predicted label map
  '''
  
  class_wise_iou = []
  class_wise_dice_score = []

  smoothening_factor = 0.00001

  for i in range(12):
      
    intersection = np.sum((y_pred == i) * (y_true == i))
    y_true_area = np.sum((y_true == i))
    y_pred_area = np.sum((y_pred == i))
    combined_area = y_true_area + y_pred_area
    
    iou = (intersection + smoothening_factor) / (combined_area - intersection + smoothening_factor)
    class_wise_iou.append(iou)
    
    dice_score =  2 * ((intersection + smoothening_factor) / (combined_area + smoothening_factor))
    class_wise_dice_score.append(dice_score)

  return class_wise_iou, class_wise_dice_score
# Photo to Year Labeling w/ ML (COMP 646)
### By Nat Hill & Ben Meisburger


## (1) Zero Shot Labeling w/ CLIP (Images to Year)

#### Sub Test: Fine Tuning
[Github Link](https://github.com/LightDXY/FT-CLIP/blob/main/models/finetune_clip.py)

Instead of 'Zero Shot', it would make sense to check the average score when we give it example images from the training set.  


## (2) Image -> Image caption (BLIP) -> year (BERT)



## (3) Image -> Date (w/ Fine Tuned ResNet (CNN))

#### Sub Test: RGB images vs Grayscale
Reasoning: Any black and white image taken in modern times will likely be misidentified as being from the past, assuming the model learns the pattern that "black and white == old".




Accuracy metric:

* MSE Makes sense here ( ex: $(1950 - 1955)^2$) means that a greater penalty is applied for a further guess. 
However, we decided to derive the loss function from the original game,
chronophoto.app

# Photo to Year Labeling w/ ML (COMP 646 Final Project)
### By Nat Hill & Ben Meisburger

[Google Colab](https://colab.research.google.com/drive/1io5cnNjkbhrdZVrwqYhgqiMDl-ELLqeQ?authuser=1#scrollTo=I44_ll-n6LjP)

## (1) Zero Shot Labeling w/ CLIP (Image -> Year)

### (1.1) Sub Test: Fine Tuning

Instead of 'Zero Shot', it would make sense to check the average score when we give it example images from the training set.  
[Inspiration Link](https://github.com/LightDXY/FT-CLIP/blob/main/models/finetune_clip.py)
[Blog Post](https://huggingface.co/blog/fine-tune-clip-rsicd)

## (2) Image -> Image Caption (BLIP) -> Year (BERT)



## (3) Image -> Date (w/ Fine Tuned CNN (ResNet))

### (3.1) Sub Test: RGB images vs Grayscale
Reasoning: Any black and white image taken in modern times will likely be misidentified as being from the past, assuming the model learns the pattern that "black and white == old".




Accuracy metric choice:

* MSE Makes sense here ( ex: $(1950 - 1955)^2$) means that a greater penalty is applied for a further guess. 

* However, we decided to derive the loss function from the original game, chronophoto.app

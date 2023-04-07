
# SOURCE: https://github.com/openai/CLIP
# Importing relevant features and loading the model

!conda install --yes -c pytorch pytorch=1.7.1 torchvision cudatoolkit=11.0
!pip install ftfy regex tqdm
!pip install git+https://github.com/openai/CLIP.git

# This command downloads the files with the prepackaged contents.
!wget -nc http://www.cs.rice.edu/~vo9/deep-vislang/SUN20-train-sm.tar.gz
!wget -nc http://www.cs.rice.edu/~vo9/deep-vislang/SUN20-val.tar.gz
!tar xf SUN20-train-sm.tar.gz
!tar xf SUN20-val.tar.gz

import os
import clip
import torch

# Load the model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load('ViT-B/32', device)


# def top_accuracy(predicted, labels, threshold = 0.5, k = 5, logits = False):

#   probs = predicted.detach().clone()
#   if logits:
#     probs = probs.sigmoid()

#   sorted_vals, sorted_ids = probs.sort(dim = 0, descending = True)
#   pred_vals = 1 * (sorted_vals[:k] > threshold) # Anything with sigmoid > 0.5 is 1.
#   # print(f'PRED VALS: {pred_vals}')
#   true_vals = labels.data.gather(0, sorted_ids[:k]) # Find true values.
#   # print(f'TRUE VALS: {true_vals}')

#   return (pred_vals == true_vals).sum(dim = 0) / (0.0 + k)


def calculateScore(realYear, inputYear):

    pictureDate = realYear
    guessedDate = inputYear
    
    dif = abs(pictureDate - guessedDate)
    
    if(dif <= 20):
        return round(((20 - dif)**1.55) * 9.62506135768)
    else:
        return 0

def processImage(id, dataset, top_n):
    # n_correct = 0

    # No masks required because we are not performing any tokenizing
    image, label = dataset[id]
    image_input = preprocess(image).unsqueeze(0).to(device)

    text_inputs = torch.cat([clip.tokenize(f"A photo taken in the year {c}") for c in dataset.categories]).to(device)

    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_inputs)

        logits_per_image, logits_per_text = model(image_input, text_inputs)

        similiarity = logits_per_image.softmax(dim = -1)

        values, indices = similiarity.topk(top_n)

    score = calculateScore(label, indices[0].item());
    #   What we were doing in assignment 2
    #   if indices[0].item() == label:
    #     n_correct += 1

    return score

def run_clip_on_data(dataset, num_samples):
  
  num_samples = 0
  cumulativeScore = 0
  curr_score = 0
  model.eval()

  for id in range(num_samples):

    # Chooses the top '1' most probable category.
    curr_score == processImage(id, dataset, 1)    
    print(f'Scored {curr_score} on image: {id}')
    cumulativeScore += curr_score
    num_samples += 1 

  print('Output Accuracy: {:.4f}'.format(cumulativeScore / num_samples))


# run_clip_on_data(valset, len(valset));
run_clip_on_data(valset, 5);
import os

#$ conda install --yes -c pytorch pytorch=1.7.1 torchvision cudatoolkit=11.0
# pip install ftfy regex tqdm Pillow
# pip install git+https://github.com/openai/CLIP.git
import torch
import clip
from PIL import Image

os.environ["CUDA_VISIBLE_DEVICES"]="0"
device = "cpu"#"cuda" if torch.cuda.is_available() else "cpu"

def load_checkpoint(checkpoint_path, model):
    checkpoint = torch.load(checkpoint_path, map_location=torch.device('cpu') if device == "cpu" else torch.device('cuda'))
    print(f"Loading checkpoint {checkpoint_path}")
    model.load_state_dict(checkpoint['model_state_dict'])

def l1(a,b):
    return torch.mean(torch.abs(a-b), dim = -1)

def cos(a,b):
    norm_a = a / torch.linalg.vector_norm(a, dim=-1, keepdim = True)
    norm_b = b / torch.linalg.vector_norm(b, dim=-1, keepdim = True)
    return (norm_a * norm_b).sum(dim=-1)

def load_image(image_path):
    img = Image.open(image_path)
    return torch.unsqueeze(preprocess(img), 0).to(device)
     

def image_text_distance(image_path, text, distance_metric=cos):
    image_features = encode_image(image_path)
    text_features = encode_text(text)

    return distance_metric(torch.concatenate([image_features, image_features], dim = 0), torch.concatenate([text_features, text_features], dim = 0)) #This concatenation is just to show that the method can be called in a vectorized fashion


def encode_image(image_path):
    image = load_image(image_path)
    with torch.no_grad():
        image_features = model.encode_image(image)
    return image_features

def encode_text(text):
    text = clip.tokenize(text).to(device)
    with torch.no_grad():
        text_features = model.encode_text(text)
    return text_features

if __name__ == '__main__':
    checkpoint = "model_definitive.pt"
    
    model, preprocess = clip.load("ViT-B/16",device=device,jit=False) 
    load_checkpoint(checkpoint, model)
    if device == "cpu":
        model.float()
    else :
        clip.model.convert_weights(model)

    distance = image_text_distance("check_jersey_printed_4_512.png", "This knit yellow and pink striped fabric could contain the fibers of polyester. There are 3 wide yellow strips and 1 wide pink stripes running horizontally. It would be soft to the touch. This would make a good beach cover-up.")
    print(distance)
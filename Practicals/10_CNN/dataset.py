import torch
torch.manual_seed(42)
from PIL import Image

class CTDataset(torch.utils.data.Dataset):
    '''
    This utility corresponds to the Dataset class construction for the custom example of camera trap data.
    The class is responsible for how images and the corresponding data are loaded in batches during training or evaluation.
    '''   
    def __init__(self,annotation_dict,transform):
        
        ### TODO: Given annotation dictionary for a given split type (train,validation or test) and the selected set of transformations, 
        ### we initialize the properties of the class (img_paths, targets, species). Hint: loop through dictionary rows.
        
        
        self.transform = transform
        ## TODO: Fill properly the values in the three attribute lists (img_paths, targets, species) defined below
        
        self.img_paths = [row[0] for row in annotation_dict]
        self.targets = [row[1] for row in annotation_dict]
        self.species = [row[2] for row in annotation_dict]
        
        
                
    def __len__(self):
        return len(self.img_paths)
    
    def get_image(self,img_path):  

        with open(img_path, 'rb') as f:
            try:
                img = Image.open(f)
                return img.convert('RGB')
            except:
                print("Image from {} cannot be read. It will be skipped".format(img_path))
                return None
            
    def __getitem__(self, idx):        
        ### TODO: Given an index we want to return the corresponding dictionary (op) with 'img_path','target','species' as its keys, along with 
        ### 'img' that corresponds to the transformed image. This routine is typically called at a batch level during train/validation.
        
        op = {}
        
       ### TODO: Comment out the following placeholder commands that load values in the dictionary to be returned 
       ### (the existing lines return the same image always!) and replace them with the corresponding values to be loaded at every batch.
        op['target'] = self.targets[idx]
        op['img_path'] = self.img_paths[idx]
        op['species'] = self.species[idx]
        op['img'] =  self.transform(self.get_image(op['img_path']))
        return op
    
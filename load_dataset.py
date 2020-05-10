import numpy as np
import matplotlib.pyplot as plt
import h5py
import scipy
from PIL import Image
from scipy import ndimage
import glob
import sklearn
from sklearn.model_selection import train_test_split




def load_dataset(database_path):
    # open dataset 
    dataset_db = h5py.File(database_path, "r")
    
    
    datasets = {}
    for dataset in ["train", "dev", "test"]:
        
        # load the train set feautres (picuture)
        datasets[dataset] = {'X' : np.array(dataset_db[dataset + "_img"][:]),  # dataset features
                              'Y' : np.array(dataset_db[dataset + "_labels"][:]) # dataset labels
                            }
    return datasets
    
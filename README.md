# Farthest-Neighbor-AUC
This repo contains the generated negative samples used in our paper, "Revisiting Saliency Metrics: Farthest-Neighbor Area Under Curve"

We release the generated negative set for the saliency datasets, SALICON-val, Toronto, MIT1003 and CAT2000,
using our proposed Farthest-Neighbor sampling process. Note that we applied the fast version of our method on the SALICON-val
dataset due to its large size. The other datasets were computed using the Pearson Correlation as a distance metric 
and K was set to 5. 


**File description**
1. Each file contains a list of negative points in the format of ndarray(.npy). You might want to randomly pick
a subset of the list based on the size of the positive.

SALICON: [link](https://drive.google.com/file/d/1D-vQY8fBTmGqTofr7pB788y5sjce9z6R/view?usp=sharing)  
Toronto: [link](https://drive.google.com/file/d/1mwd6Oheuwbu-CRKSyX4uRL1eH3dwQXQb/view?usp=sharing)  
MIT1003: [link]()  
CAT2000: [link](https://drive.google.com/file/d/1stGkaVwTxe5qJeflJNCjdNfNbW-r1bLU/view?usp=sharing)  

<!--Text
2. Alternatively, we also release a tar file that includes
pre-computed negative distribution maps in PNG format. The negative points were sampled from the (npy) list and the
sigma value was selected according to Table 1 in the paper.
-->


If you think our work is helpful to your study, we kindly ask please cite our paper:  

@misc{jia2020revisiting,  
    title={Revisiting Saliency Metrics: Farthest-Neighbor Area Under Curve},  
    author={Sen Jia and Neil D. B. Bruce},  
    year={2020},  
    eprint={2002.10540},  
    archivePrefix={arXiv},  
    primaryClass={cs.CV}  
}

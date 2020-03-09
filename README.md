# Farthest-Neighbor-AUC
This repo contains the generated negative samples used in our CVPR 2020 paper, "Revisiting Saliency Metrics: Farthest-Neighbor Area Under Curve" [arXiv](https://arxiv.org/abs/2002.10540)

## Global Smoothing  
The pyhton file "global_smooth.py" contains the code for our proposed global Gaussian smoothing. This function is used to create enough unique values for AUC metrics. This can be an alternative to the random jitter used in AUC-judd for the MIT benchmark[line](http://saliency.mit.edu/results_mit300.html). We would like to thank the creators and organizers of the MIT and SALICON leaderboards.

Check the value range before and after smoothing based on the sample saliency map "d54.jpg" by running the file directly.
```
python global_smooth.py
```

## Farthest-Neighbor Negative Set  
We release the generated negative set for the saliency datasets, SALICON-val, Toronto, MIT1003 and CAT2000,
using our proposed Farthest-Neighbor sampling process. Note that we applied the fast version of our method on the SALICON-val
dataset due to its large size. The negative set for the other datasets were computed by using the Pearson Correlation as a distance metric and K was set to 5. 

**File description**  
1. Each file contains a list of negative points in the format of ndarray(.npy). You might want to randomly pick
a subset of the list based on the size of the positive.

SALICON: [link](https://drive.google.com/file/d/1D-vQY8fBTmGqTofr7pB788y5sjce9z6R/view?usp=sharing)  
Toronto: [link](https://drive.google.com/file/d/1mwd6Oheuwbu-CRKSyX4uRL1eH3dwQXQb/view?usp=sharing)  
MIT1003: [link]()  
CAT2000: [link](https://drive.google.com/file/d/1n0rM2DVibmEPsVYOeMbFyBYwGKHOjBel/view?usp=sharing)  


2. In addition, we also release the pre-computed negative distribution maps in PNG format(value range[0-255]). The negative points were sampled from the above numpy(npy) file and the sigma value was selected according to Table 1 in our paper.

SALICON: [link](https://drive.google.com/file/d/1RYw2LbcZO0qMHtow9S4gb8U3vdoVmN4y/view?usp=sharing)  
Toronto: [link](https://drive.google.com/file/d/1JshThWpHlbO9eU2G164Pq6ovLxSASw6M/view?usp=sharing)  
MIT1003: [link]()  
CAT2000: [link](https://drive.google.com/file/d/1Rq8ZUgE7fn4h4jw_Ccon-PtmF_k096QC/view?usp=sharing)  

***Caveat:***

***1. The negative npy and png files for MIT1003 were computed on the rescaled dimension because the size of the image is not fixed. You might want to check this [project](https://github.com/marcellacornia/sam) for the padding strategy and cite their paper.***

***2. The negative files for the CAT2000 dataset were computed using (K=5) for the consistency in our paper. You might want to apply a bigger value of K for higher robustness due to the special categories included.***

If you think our work is helpful to your study, we kindly ask please cite our paper:  

@misc{jia2020revisiting,  
    title={Revisiting Saliency Metrics: Farthest-Neighbor Area Under Curve},  
    author={Sen Jia and Neil D. B. Bruce},  
    year={2020},  
    eprint={2002.10540},  
    archivePrefix={arXiv},  
    primaryClass={cs.CV}  
}

# Farthest-Neighbor-AUC
This repo contains the generated negative samples used in our CVPR 2020 paper, "Revisiting Saliency Metrics: Farthest-Neighbor Area Under Curve" [arXiv](https://arxiv.org/abs/2002.10540)

## Global Smoothing  
The pyhton file "global_smooth.py" contains the code for our proposed global Gaussian smoothing. This function is used to create enough unique values for AUC metrics. This can be an alternative to the random jitter used in AUC-judd for the MIT benchmark[line](http://saliency.mit.edu/results_mit300.html). We would like to thank the creators and organizers of the MIT and SALICON leaderboards.
| Quantized  | Global Smoothing | ROC curve |
| ------------- | ------------- | ----------|
  <img src="https://github.com/SenJia/Farthest-Neighbor-AUC/blob/master/samples/quantized.png" width="300px" height="200px"> |  <img src="https://github.com/SenJia/Farthest-Neighbor-AUC/blob/master/samples/gs_global.png" width="300px" height="200px">| <img src="https://github.com/SenJia/Farthest-Neighbor-AUC/blob/master/samples/GS_curve.png" width="300px" height="200px">

Check the value range before and after smoothing based on the sample saliency map "samples/d54.jpg" by running the file directly.
```
python global_smooth.py samples/d54.jpg
```

## Farthest-Neighbor Negative Set  
We release the generated negative set for the saliency datasets, SALICON-val, Toronto, MIT1003 and CAT2000,
using our proposed Farthest-Neighbor sampling process. Note that we applied the fast version of our method on the SALICON-val
dataset due to its large size. The negative set for the other datasets were computed by using the Pearson Correlation as a distance metric and K was set to 5. 

| Positive Map | Negative Map 1 | Negative Map 2 | Negative Map 3 |
| ------------- | ------------- | ----------| ----------|
  <img src="https://github.com/SenJia/Farthest-Neighbor-AUC/blob/master/samples/positive.png" width="200px" height="150px"> |  <img src="https://github.com/SenJia/Farthest-Neighbor-AUC/blob/master/samples/negative1.png" width="200px" height="150px">| <img src="https://github.com/SenJia/Farthest-Neighbor-AUC/blob/master/samples/negative2.png" width="200px" height="150px">| <img src="https://github.com/SenJia/Farthest-Neighbor-AUC/blob/master/samples/negative3.png" width="200px" height="150px">

**File description**  
1. Each file contains a list of negative points in the format of ndarray(.npy). You might want to randomly pick
a subset of the list based on the size of the positive.

SALICON: [link](https://drive.google.com/file/d/1D-vQY8fBTmGqTofr7pB788y5sjce9z6R/view?usp=sharing)  
Toronto: [link](https://drive.google.com/file/d/1mwd6Oheuwbu-CRKSyX4uRL1eH3dwQXQb/view?usp=sharing)  
MIT1003: [link](https://drive.google.com/file/d/1qeDgkhWyOrXZJQPD92QnQmwfSC8jMrs1/view?usp=sharing)  
CAT2000: [link](https://drive.google.com/file/d/1n0rM2DVibmEPsVYOeMbFyBYwGKHOjBel/view?usp=sharing)  


2. In addition, we also release the pre-computed negative distribution maps in PNG format(value range[0-255]). The negative points were sampled from the above numpy(npy) file and the sigma value was selected according to Table 1 in our paper.

SALICON: [link](https://drive.google.com/file/d/1RYw2LbcZO0qMHtow9S4gb8U3vdoVmN4y/view?usp=sharing)  
Toronto: [link](https://drive.google.com/file/d/1JshThWpHlbO9eU2G164Pq6ovLxSASw6M/view?usp=sharing)  
MIT1003: [link](https://drive.google.com/file/d/1xw9QHsVTZGA-XULEWpCnnd5P1dI4y53f/view?usp=sharing)  
CAT2000: [link](https://drive.google.com/file/d/1Rq8ZUgE7fn4h4jw_Ccon-PtmF_k096QC/view?usp=sharing)  

***Caveat:***

***1. The negative npy and png files for MIT1003 were computed on the rescaled dimension because the size of the image is not fixed. You might want to check this [project](https://github.com/marcellacornia/sam) for the padding strategy and cite their paper.***

***2. The negative files for the CAT2000 dataset were computed using (K=5) for the consistency in our paper. You might want to apply a larger value of K for higher robustness due to the special categories included.***

If you think our work is helpful to your study, we kindly ask please cite our paper:  

@misc{jia2020revisiting,  
    title={Revisiting Saliency Metrics: Farthest-Neighbor Area Under Curve},  
    author={Sen Jia and Neil D. B. Bruce},  
    year={2020},  
    eprint={2002.10540},  
    archivePrefix={arXiv},  
    primaryClass={cs.CV}  
}

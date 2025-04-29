# L-SING
Learning local neighborhoods of non-Gaussian graphical models: A measure transport approach

**Accepted at AAAI'25**
Arxiv: https://arxiv.org/abs/2503.13899
AAAI: https://ojs.aaai.org/index.php/AAAI/article/view/34059/36214

## Experiments

We conducted three main experiments:

1. **Butterfly Distribution**
2. **Gaussian Distribution**
   - Includes pre-processing and generation of training, validation, and test sets.
3. **Ovarian Cancer Dataset**  
   - Derived from the `curatedOvarianPackage` in R.  
   - The dataset used in the experiments by Shutta et al. (2022) was pre-processed from `curatedOvarianPackage` to allow direct comparison between methods (GLASSO and localized L-SING).

---

## Usage Instructions

To run the code:

1. Ensure that the paths are configured correctly.
2. Navigate to each folder and run the experiments from there, as the paths are all relative.

This version of the code includes 1–2 examples of differently parameterized UMNNs (with varying numbers of hidden layers). The experiments described in the submission are included in the provided code.

For additional details on experiment choices (e.g., regularization, UMNN parameterization), refer to the **technical appendix**.

---

## Citations

- **Wehenkel, A., & Louppe, G. (2019).**  
  *Unconstrained Monotonic Neural Networks.*  
  In Wallach, H.; Larochelle, H.; Beygelzimer, A.; d'Alché-Buc, F.; Fox, E.; and Garnett, R., eds., *Advances in Neural Information Processing Systems,* Vol. 32. Curran Associates, Inc.

- **Shutta, K. H., Vito, R. D., Scholtens, D. M., & Balasubramanian, R. (2022).**  
  *Gaussian graphical models with applications to omics analyses.*  
  *Statistics in Medicine,* 41(25), 5150–5187.

---

## Note

The UMNN model code used here is from: [https://github.com/AWehenkel/UMNN](https://github.com/AWehenkel/UMNN)


## Citations
If you using L-SING in an academic paper, please cite:

@misc{liaw2025learninglocalneighborhoodsnongaussian,
      title={Learning local neighborhoods of non-Gaussian graphical models: A measure transport approach}, 
      author={Sarah Liaw and Rebecca Morrison and Youssef Marzouk and Ricardo Baptista},
      year={2025},
      eprint={2503.13899},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2503.13899}, 
}

# L-SING
Learning local neighborhoods of non-Gaussian graphical models  
**Accepted at AAAI'25**

---

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

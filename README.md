# L-SING
Learning local neighborhoods of non-Gaussian graphical models. Accepted at AAAI'25.

There are 3 main experiments done:
- Butterfly distribution
- Gaussian distribution (include pre-processing and generation of train, test, validation.)
- Ovarian Cancer Dataset (from curatedOvarianPackage in R). We saved the dataset that was used in Shutta et al. (2022) experiments that was pre-processed from curatedOvarianPackage, so that we can directly compare out methods between GLASSO and localized SING.

To run the code, please make sure the paths are configured correctly. We recommend going into each folder and running experiments from there since the paths are all relative paths. In this version of the code, we give 1-2 examples of differently parameterized UMNNs (with different number of hidden layers). The experiments written in the submission is also contained in the code here.

For additional details on experiment choices in terms of regularization, parameterization of UMNN, we refer the readers to the technical appendix.

Citations:
Wehenkel, A.; and Louppe, G. 2019. Unconstrained Monotonic Neural Networks. In Wallach, H.; Larochelle, H.; Beygelzimer, A.; d'Alch ´e-Buc, F.; Fox, E.; and Garnett, R., eds., Advances in Neural Information Processing Systems, volume 32. Curran Associates, Inc.

Shutta, K. H.; Vito, R. D.; Scholtens, D. M.; and Balasubramanian, R. 2022. Gaussian graphical models with applications to omics analyses. Statistics in Medicine, 41(25): 5150–5187.

NOTE: UMNN Model code was here was from: https://github.com/AWehenkel/UMNN
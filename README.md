# NS-ML-on-Nuclear-Matter--KB

EOS by RMF is a paper on understanding Neutron Star Equation of State using Relativistic Mean Field Models.
GW_EOS is the main paper we refer to for all preliminary assumptions on the EOS, input and output features of the model as well as data used.
There are 2 papers on how to get Mass, Radius and Tidal Deformation from a given EOS.
NS_Parameter_SOP_Report is the final Project Report

Codes contains all the codes written to generate the various ML, ANN, BNN models including testing and sampling.
We have 3 different datasets, each with differing correlations among the 7 parameters (more info in GW_EOS and Report).
Multiple ANN Models contains all the ANN models that were trained on the data with varying test and train splits. The best models out of all have been filtered and tested
separately on the rest of the data.

Some BNN models were made from scratch, but after they didn't produce good results, we shifted to Tensorflow to take care of the BNN models.
Again, the best BNN models have been filtered and tested on the rest of the data as well as on custom sampled datasets.

"""
in each tumor type, each patients' arm correlation with each arm

"""


import pandas as pd
import glob, re
import numpy as np
pd.set_option("display.max_columns", 100)


df_delZ = pd.DataFrame()
cnv_path = "/Users/yiwenbu/Desktop/CNV_TCGA_GISTIC_RESULTS/*/broad_values_by_arm.txt"

for file in glob.glob(cnv_path):
    try:
        tumorName = re.search('org_(.+?)-T', file).group(1)
    except AttributeError:
        print file
    df = pd.read_csv(file, sep="\t", index_col=0)
    df_correlation = df.T.corr(method='pearson')
    df_correlation.loc[:, :] = np.tril(df_correlation, k=-1)
    df_correlation.to_csv("patient_cnv/"+tumorName+"_correlation.xls", sep="\t")


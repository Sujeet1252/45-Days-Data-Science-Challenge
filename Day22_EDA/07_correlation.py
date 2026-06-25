import seaborn as sns

df = sns.load_dataset('iris')
print(df.corr(numeric_only=True))

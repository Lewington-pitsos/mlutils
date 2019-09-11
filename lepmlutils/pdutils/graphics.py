import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_against(df, name, col, **kwargs):
    plot_agg(df, name, col, "mean", **kwargs)

def plot_agg(df, name, col, agg="mean", size=(20, 10)):
    df.groupby(name).agg({col: [agg]}).plot.bar(stacked=True, figsize=size)

def plot_and_save(df, name, col, path, **kwargs):
    plot_against(df, name, col, **kwargs)
    plt.savefig(path + f"/{col}-{name}")

def qplot_against(df, name, col, bins, **kwargs):
    qname = f"q{name}"
    df[qname] = pd.qcut(df[name], bins)
    plot_against(df, qname, col, **kwargs)

def confidence_plot(df, col, target, rc={'figure.figsize':(15,10)}):
    sns.set(rc=rc)
    ax = sns.countplot(x=col, data=df)
    ax2 = ax.twinx()
    ax.set_xticklabels(ax.get_xticklabels(),rotation=80)    
    ax2 = sns.pointplot(x=col, y=target, data=df, color='black', legend=False, errwidth=0.5)
    ax.grid(False)
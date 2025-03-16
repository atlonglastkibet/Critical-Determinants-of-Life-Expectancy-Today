import matplotlib.pyplot as plt
import seaborn as sns

def kde_plt_grid(df, cols, rows=4, cols_per_row=4,figsize=(10,8)):
    fig, ax = plt.subplots(rows, cols_per_row, figsize=figsize)
    ax = ax.flatten()

    for i,col in enumerate (cols): 
        if i<len(ax):
            sns.kdeplot (df[col], fill=True, ax=ax[i])
            ax[i].set_title(col)

    for j in range(i+1, len(ax)):
        fig.delaxes(ax[j])
        
    plt.tight_layout()
    plt.show()
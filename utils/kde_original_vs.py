import matplotlib.pyplot as plt
import seaborn as sns

def compare_kde_plt(original_df, imputed_df, cols, rows=4, cols_per_row=4, figsize=(10, 8)):
    fig, ax = plt.subplots(rows, cols_per_row, figsize=figsize, dpi=300)
    ax = ax.flatten()  # Flatten for easy iteration

    # Define consistent colors for Original and Imputed data
    original_color = 'blue'
    imputed_color = 'red'

    # Create proxy artists for the global legend
    from matplotlib.lines import Line2D
    original_patch = Line2D([0], [0], color=original_color, lw=2, label='Original')
    imputed_patch = Line2D([0], [0], color=imputed_color, lw=2, linestyle='--', label='Imputed')

    for i, col in enumerate(cols):
        if i < len(ax):  # Ensure we don't exceed available subplots
            # Plot KDE for Original data
            sns.kdeplot(
                original_df[col].dropna(), 
                fill=True, 
                ax=ax[i], 
                color=original_color
            )
            # Plot KDE for Imputed data
            sns.kdeplot(
                imputed_df[col], 
                fill=True, 
                ax=ax[i], 
                color=imputed_color, 
                linestyle="dashed"
            )
            # Customize subplot appearance
            ax[i].set_title(col, fontsize=10)  # Smaller title font
            ax[i].tick_params(axis='both', labelsize=8)  # Adjust tick label size
            ax[i].grid(True, linestyle='--', alpha=0.6)  # Add gridlines

    # Hide unused subplots
    for j in range(i + 1, len(ax)):
        fig.delaxes(ax[j])

    # Add a global title
    fig.suptitle("Comparison of Original vs. Imputed Data - KDE Plot", fontsize=14, y=1.02)

    # Add a single global legend
    fig.legend(handles=[original_patch, imputed_patch], loc='upper center', bbox_to_anchor=(0.5, -0.05),
               ncol=2, fontsize=10, frameon=False)

    # Adjust layout to prevent overlapping
    plt.tight_layout(rect=[0, 0, 1, 0.95])  # Leave space for the global legend
    plt.show()
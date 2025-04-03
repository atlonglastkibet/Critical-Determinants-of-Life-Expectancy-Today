
# Critical Determinants of Life Expectancy Today - ML Approach

## Project Overview

This project aims to analyze the critical factors affecting life expectancy using a machine learning approach. By leveraging kaggle datasets, I perform exploratory data analysis (EDA), feature engineering, and model training to predict life expectancy based on socioeconomic, environmental, and healthcare-related factors. This is a submission for my ML I Capstone Project.

## Data source

The original dataset can be accessed through [kaggle](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who).

## Objectives

- Identify key factors that determine life expectancy today.
- Develop predictive models to estimate life expectancy.
- Provide actionable insights through visualizations and model interpretations.

## Presentaion

A slide presentation of my findings is published on my [Canva](https://www.canva.com/design/DAGh1KcJELc/pFbKkxP7y8dMuXxj9kz7pA/edit)

## Project Structure

The repository is organized as follows:

- **data/**: Contains datasets used in the analysis.
  - `data_imputed/`: Processed datasets with missing values handled.
  - `data_original/`: Raw datasets.
  - `EDA_for_data.csv`: Summary dataset used for exploratory data analysis.
- **docs/**: Documentation and reports related to the project.
  - `choropleth_animated/`: Animated visualizations of life expectancy trends.
  - `choropleth_static/`: Static visualizations of life expectancy trends.
- **models/**: Trained machine learning models and saved results.
- **notebooks/**: Jupyter notebooks for different steps of the analysis.
  - `01_data_processing.ipynb`: Data preprocessing and cleaning.
  - `02_EDA.ipynb`: Exploratory Data Analysis.
  - `03_feature_engineering.ipynb`: Feature selection and engineering.
  - `04_model_training_and_eva.ipynb`: Model training and evaluation.
  - `05_hyperparameter_tuning.ipynb`: Hyperparameter tuning for optimized performance, feature importance extraction.
  - `appendix_nb.ipynb`: Additional analyses and findings.
- **plots/**: Visualizations generated from the data.
- **utils/**: Helper scripts for data processing and visualization.
  - `kde_original_vs.py`: Kernel Density Estimation comparison.
  - `kde_plt.py`: KDE plotting utilities.
- **venv/**: Virtual environment containing required dependencies.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `README.md`: This document.

## Usage

Clone the repository:
   ```bash
   git clone https://github.com/atlonglastkibet/Critical-Determinants-of-Life-Expectancy-Today.git
   ```

## Contributions

Feel free to contribute by submitting issues or pull requests.

## Acknowledgements

I acknowledge the efforts of Kaggle for public datasets and global health organizations in providing accessible data and resources that made this analysis possible. Zindua School for enabling the whole project.

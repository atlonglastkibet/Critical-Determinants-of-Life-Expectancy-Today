
# Critical Determinants of Life Expectancy Today - ML Approach

## Project Overview

This project aims to analyze the critical factors affecting life expectancy using a machine learning approach. By leveraging kaggle datasets, we perform exploratory data analysis (EDA), feature engineering, and model training to predict life expectancy based on socioeconomic, environmental, and healthcare-related factors.
The original dataset can be accessed through [kaggle](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who).

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
  - `05_hyperparameter_tuning.ipynb`: Hyperparameter tuning for optimized performance.
  - `appendix_nb.ipynb`: Additional analyses and findings.
- **plots/**: Visualizations generated from the data.
- **utils/**: Helper scripts for data processing and visualization.
  - `kde_original_vs.py`: Kernel Density Estimation comparison.
  - `kde_plt.py`: KDE plotting utilities.
- **venv/**: Virtual environment containing required dependencies.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `README.md`: This document.

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/atlonglastkibet/Critical-Determinants-of-Life-Expectancy-Today.git
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Jupyter notebooks to explore the data and train models:

```bash
jupyter notebook
```

## Research Questions

- Identify key factors that determine life expectancy today.
- Develop predictive models to estimate life expectancy.
- Provide actionable insights through visualizations and model interpretations.

## Contributions

Feel free to contribute by submitting issues or pull requests.

## License

The dataset has the following attributes:

1. Country - Country Name (this is a character/string variable. Allowable values are: Afghanistan, Kenya, Egypt, etc.).

2. Region - Global regional location (this is a factor variable with the 7 regions of the world, i.e., East Asia & Pacific, Europe & Central Asia, 
   Latin America & Caribbean, Middle East & North Africa, North America, South Asia, and Sub-Saharan Africa).

3. IncomeG - Income Group (this is a factor variable describing a country's classification in terms of its social class based on the income levels 
   of the majority of its population, i.e., Low Income, Middle Income, and High Income).

4. Year - The calendar year of interest (this is an integer variable with having allowable values: 2000, 2001, 2002, ..., 2015).

5. LifeExp - Life expectancy in age (a numeric variable describing the duration, on average, a newborn can expect to live, if current death rates 
   remain constant. Allowable values include: 65.0, 59.9, 57.3, etc.).

6. AdultM - Adult mortality (this is an integer variable describing the number of people dying between 15-60 years per 1000 population. Allowable 
   values include: 263, 271, 291, 287, etc.).

7. InfantD - Infant deaths (an integer variable describing the number of infant deaths per 1000 population. Allowable values include: 62, 64, 77, ...).

8. Alcohol - This is a numeric variable describing the recorded per capita alcohol consumption (in litres) for a country in a specific year (allowable 
   values include: 0.01, 0.03, 8.74, 6.48, 4.79, etc.).

9. PercHealthExp - This is a numeric variable describing a country's percentage expenditure on health as per GDP (allowable values are: 71.3, 73.5, 73.2, 
   78.2, 7.1, etc.). A further scrutiny into this variable established that the recorded values for this variable in the data set were erroneous, hence, 
   this variable was excluded from the study.

10. HepsB - A numeric variable describing the percentage Hepatitis B immunization coverage among 1 year olds (allowable values are: 65.0, 62.0, 64.0, 67.0, 
    68.1, 66.0, 63.0, 64.0, 63.9, etc.).

11. Measles - An integer variable describing the number of measles reported cases per 1000 population (allowable values are: 1154, 492, 430, 2787, 3013, 
    1989, 2861, 1599, 1141, 1990, etc.).

12. BMI - A numeric variable describing the average body mass index of the entire population (allowable values are: 19.1, 18.6, 18.1, 17.6, 17.2, 16.7, 16.2, 
    15.7, 15.2, 14.7, etc.).

13. Und5Deaths - An integer variable describing the number of under five deaths per 1000 population (allowable values are: 83, 86, 89, 93, 97, 102, 106, 110, 
    113, 116, etc.).

14. Polio - An numeric variable describing the percent of polio immunization coverage among one year olds (the allowable values are: 6.1, 58.0, 62.9, 67.0, 
    68.0, 66.5, 63.0, 64.0, 63.0, 58.0, etc.).

15. GovHealthExp - A numeric variable describing a country's government expenditure of health as a percentage of total government expenditure (allowable values 
    are: 8.16, 8.18, 8.13, 8.52, 7.87, 9.2, 9.42, 8.33, 6.73, 7.43, etc.).

16. Diph - A numeric variable describing the percent of diphtheria immunization coverage among one year olds (allowable values are: 65.0, 62.0, 64.1, 67.0, 68.0, 
    66.0, 63.0, 64.0, 63.0, 58.1, etc.).

17. HIV - A numeric variable describing the ratio of HIV/AIDS deaths per 1000 population (allowable values are: 0.1, 0.6, 1.4, 0.8, 0.6, 1.1, 2.1, 2.2, 1.9, etc.).

18. GDP - A numeric variable describing the gross domestic product per capita in dollars (allowable values are: 584.3, 612.7, 631.7, 670.0, 63.5, etc.).

19. Pop - An integer variable describing a country's population (allowable values are: 34413603, 33370804, 32269592, 31161378, 30117411, 29185511, 28394806, 27722281, 
    27100542, 26433058, etc.). During the data pre-processing phase, the data values for this variable were found to be incorrect. For this reason, the “population" 
    values in the initial dataset were replaced with new values from the World Bank Development Indicators’ dataset.

20. Thin10-19Yrs - A numeric variable describing the percent of thinness among children from age 10-19 (allowable values are: 17.2, 17.5, 17.7, 17.9, 18.2, 18.4, 18.6, 
    18.8, 19.0, 19.2, etc.).

21. Thin5-9Yrs - A numeric variable describing the percent of thinness among children from age 5-9 (allowable values are: 17.3, 17.5, 17.7, 18.0, 18.2, 18.4, 18.7, 18.9, 
    19.1, 19.3, etc.).

22. Schooling - A numeric variable describing the number of years spent in school (the allowable values are: 10.1, 10.0, 9.9, 9.8, 9.5, 9.2, 8.9, 8.7, 8.4, 8.1, etc.).

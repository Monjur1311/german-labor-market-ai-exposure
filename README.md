Hi, i am Monjur Morshed Master student of Economics  at Heinrich Hein University Düsseldorf, Germany.
this is my master thesis project 
**Artificial Intelligence Exposure and Labour Shortages in Germany: Evidence from Occupation-Level Panel Data**

**The project studies whether occupations with higher exposure to AI show different labour market outcomes in Germany, using KldB 3-digit occupation-level panel data for 2015–2025.

## Repository structure

```text
.
├── data/
│   ├── raw/                 # Original input files, not tracked by Git
│   └── processed/           # Cleaned analysis datasets
├── notebooks/
│   ├── 01_data_cleaning_mapping.ipynb
│   ├── 02_descriptive_statistics.ipynb
│   ├── 03_did_estimation.ipynb
│   └── 04_event_study.ipynb
├── outputs/
│   ├── figures/             # Exported figures
│   └── tables/              # Exported tables
├── src/                     # Optional helper scripts
├── requirements.txt
└── README.md
```

## Notebook order

Run the notebooks in this order:

1. **Data Cleaning and Mapping**  
   Creates the final occupation-year panel and maps AI exposure to KldB occupations.

2. **Descriptive Statistics**  
   Produces descriptive statistics and high-AI vs low-AI trend figures.

3. **DiD Estimation**  
   Estimates baseline models, continuous-treatment DiD, binary-treatment robustness, COVID robustness, and post-ChatGPT robustness.

4. **Event Study**  
   Estimates dynamic event-study specifications and exports event-study figures.

## Required input files

Place these files in `data/raw/` before running the notebooks:

```text
panel_dataset_controls.csv
AIOE_DataAppendix.xlsx
```

The first notebook creates:

```text
data/processed/final_dataset_ai_exposure_controls.csv
```

## Main variables

| Variable | Description |
|---|---|
| `kldb3` | 3-digit KldB occupation code |
| `year` | Year |
| `ai_exposure` | Occupational AI exposure measure |
| `relation` | Unemployed persons per 100 vacancies |
| `log_relation` | Log unemployment-to-vacancy ratio |
| `vakanz_tage` | Average vacancy duration in days |
| `log_vakanz` | Log vacancy duration |
| `log_bestand` | Log employment size |
| `log_median_wage` | Log median wage |
| `post` | Indicator equal to 1 for years 2023 onward |

## Empirical strategy

Baseline specification:

```text
log(Y_it) = alpha + beta AIExposure_i + year FE + error_it
```

Continuous-treatment DiD specification:

```text
Y_it = occupation FE + year FE + beta(AIExposure_i × Post_t) + controls + error_it
```

Event-study specification:

```text
Y_it = occupation FE + year FE + sum_k delta_k(Year_k × AIExposure_i) + controls + error_it
```

## Notes

- `log_relation` is interpreted as labour market slack / demand-side pressure.
- `log_vakanz` is interpreted as vacancy duration / recruitment or worker-availability dynamics.
- Standard errors are clustered at the occupation level.
- Data files are excluded from Git by default.

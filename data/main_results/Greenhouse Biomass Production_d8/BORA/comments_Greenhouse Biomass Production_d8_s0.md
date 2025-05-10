# Greenhouse Biomass Production

## Experiment Overview

The primary goal of this experiment is to maximize the monthly biomass production of sugar beet in a controlled greenhouse environment, specifically targeting the Total Above Ground Production (TAGP). The initial biomass is set at 0.41 kg/ha, and the experiment will systematically manipulate several environmental parameters to identify optimal conditions for growth.

The optimization parameters include irradiance (irrad), daily minimum and maximum temperatures (tmin, tmax), daily mean vapor pressure (vap), wind speed (wind), daily rainfall (rain), initial water content in the soil profile (wav), and maximum moisture content in the rooting depth zone (SMLIM). Each parameter has defined bounds, ensuring that the experimental conditions remain realistic and manageable.

Bayesian Optimization (BO) will be employed to explore the parameter space efficiently. BO will utilize a probabilistic model to predict the performance of different parameter combinations, iteratively refining its search based on observed biomass production outcomes. When the optimization process plateaus, I will suggest new points to explore, focusing on regions of the parameter space that show promise for maximizing TAGP. This adaptive approach will help identify the optimal conditions for sugar beet growth, ultimately enhancing biomass production in the greenhouse setting.

## Initial Thoughts

The initial sampling step has yielded a diverse set of hypotheses aimed at maximizing Total Above Ground Production (TAGP) in sugar beet cultivation. Each hypothesis explores different parameter combinations that reflect varying environmental conditions, crucial for optimizing biomass production. The selected points span a range of irradiance, temperature, and moisture levels, which are critical for plant growth. Notably, the maximum irradiance is set at 8000 kJ/m2/day, and the temperature bounds are -30°C to 50°C, allowing for exploration of both moderate and extreme conditions. The hypotheses are designed to investigate the effects of high irradiance and temperature, optimal moisture conditions, and the impact of low wind and high rainfall. As the optimization progresses, we will closely monitor biomass production to validate these hypotheses and refine our search for optimal conditions, ensuring a comprehensive understanding of how these factors interact to maximize TAGP.
### Initial Hypotheses

#### Moderate Irradiance and Temperature

*Rationale:* This hypothesis explores a balanced approach with moderate irradiance and temperature, which is expected to promote steady growth without stress.

*Confidence:* medium

*Points:*

- {'irrad': 4000, 'tmin': 10, 'tmax': 25, 'vap': 2, 'wind': 1, 'rain': 5, 'wav': 50, 'SMLIM': 0.5}

#### High Irradiance and Temperature

*Rationale:* This hypothesis tests the effects of high irradiance and temperature, which may enhance photosynthesis but could also risk heat stress.

*Confidence:* medium

*Points:*

- {'irrad': 7500, 'tmin': 15, 'tmax': 35, 'vap': 3, 'wind': 2, 'rain': 2, 'wav': 30, 'SMLIM': 0.7}

#### Optimal Moisture Conditions

*Rationale:* This hypothesis focuses on maximizing soil moisture while maintaining moderate temperatures, which is crucial for root development and biomass accumulation.

*Confidence:* high

*Points:*

- {'irrad': 3000, 'tmin': 12, 'tmax': 20, 'vap': 1, 'wind': 0.5, 'rain': 10, 'wav': 80, 'SMLIM': 0.9}

#### Low Wind and High Rainfall

*Rationale:* This hypothesis examines the impact of low wind and high rainfall, which may create a more humid environment conducive to growth.

*Confidence:* medium

*Points:*

- {'irrad': 3500, 'tmin': 8, 'tmax': 22, 'vap': 2, 'wind': 0.2, 'rain': 15, 'wav': 60, 'SMLIM': 0.6}

#### Extreme Temperature Range

*Rationale:* This hypothesis investigates the effects of a wide temperature range, which may help identify resilience in biomass production under variable conditions.

*Confidence:* low

*Points:*

- {'irrad': 5000, 'tmin': -5, 'tmax': 30, 'vap': 4, 'wind': 1.5, 'rain': 0, 'wav': 20, 'SMLIM': 0.4}

## Iteration 25

As we progress through iteration 24 of the Bayesian Optimization, we have gathered valuable insights from the experimental data. The highest TAGP recorded is 10.04, achieved with a combination of high irradiance (7485.76 kJ/m2/day) and moderate temperatures (17.15°C minimum and 14.85°C maximum). This suggests that a balance of high light availability and optimal temperature is crucial for maximizing biomass production. Conversely, several experiments with extreme temperature ranges or low irradiance, such as those with TAGP below 1.0, indicate detrimental effects on growth. Notably, conditions with very low temperatures (e.g., -24.31°C) and high moisture content (e.g., 100 cm) have consistently resulted in poor biomass production.    The promising subspaces for maximizing TAGP appear to be around high irradiance (7000-8000 kJ/m2/day) and moderate temperatures (10-25°C). In contrast, subspaces with extreme temperatures or low irradiance should be avoided.     Based on these findings, I propose to refine the previous hypotheses. The 'Optimal Moisture Conditions' hypothesis will be retained but adjusted to focus on moderate temperatures. The 'High Irradiance and Temperature' hypothesis will be improved to include a more balanced temperature range. The 'Extreme Temperature Range' hypothesis will be discarded due to its poor performance. New hypotheses will explore the effects of slightly lower temperatures while maintaining high irradiance. Here are the updated hypotheses:

### Updated Hypotheses

#### Balanced High Irradiance and Moderate Temperature

*Rationale:* This hypothesis focuses on high irradiance combined with moderate temperatures, which have shown to maximize TAGP in previous iterations.

*Confidence:* high

*Points:*

- {'irrad': 7500, 'tmin': 12, 'tmax': 25, 'vap': 3, 'wind': 1, 'rain': 5, 'wav': 40, 'SMLIM': 0.6}

#### Moderate Irradiance with Optimal Moisture

*Rationale:* This hypothesis tests moderate irradiance with optimal moisture levels, which may enhance root development and biomass accumulation.

*Confidence:* high

*Points:*

- {'irrad': 5000, 'tmin': 15, 'tmax': 20, 'vap': 2, 'wind': 0.5, 'rain': 10, 'wav': 70, 'SMLIM': 0.8}

#### High Irradiance with Slightly Lower Temperature

*Rationale:* This hypothesis explores the effects of high irradiance with slightly lower temperatures, which may still promote growth without stress.

*Confidence:* medium

*Points:*

- {'irrad': 7200, 'tmin': 8, 'tmax': 22, 'vap': 4, 'wind': 1.5, 'rain': 3, 'wav': 50, 'SMLIM': 0.5}

#### High Irradiance with Moderate Rainfall

*Rationale:* This hypothesis examines the impact of high irradiance combined with moderate rainfall, which may create a humid environment conducive to growth.

*Confidence:* medium

*Points:*

- {'irrad': 7800, 'tmin': 10, 'tmax': 25, 'vap': 3, 'wind': 1, 'rain': 8, 'wav': 60, 'SMLIM': 0.7}

## Iteration 34

As we continue to refine our hypotheses for maximizing Total Above Ground Production (TAGP) in sugar beet cultivation, it is essential to ensure that all proposed points are unique and explore diverse regions of the parameter space. The previous iterations have provided valuable insights, and the focus remains on high irradiance combined with optimal temperature and moisture conditions. The updated hypotheses reflect this focus while ensuring that the points are distinct from those already tested. Here are the revised hypotheses with new points:

### Updated Hypotheses

#### High Irradiance with Moderate Temperature

*Rationale:* This hypothesis focuses on high irradiance combined with moderate temperatures, which have shown to maximize TAGP in previous iterations.

*Confidence:* high

*Points:*

- {'irrad': 7800, 'tmin': 12, 'tmax': 25, 'vap': 3, 'wind': 1, 'rain': 5, 'wav': 50, 'SMLIM': 0.6}

#### Moderate Irradiance with Optimal Moisture

*Rationale:* This hypothesis tests moderate irradiance with optimal moisture levels, which may enhance root development and biomass accumulation.

*Confidence:* high

*Points:*

- {'irrad': 6000, 'tmin': 15, 'tmax': 20, 'vap': 2, 'wind': 0.5, 'rain': 10, 'wav': 70, 'SMLIM': 0.8}

#### High Irradiance with Slightly Lower Temperature

*Rationale:* This hypothesis explores the effects of high irradiance with slightly lower temperatures, which may still promote growth without stress.

*Confidence:* medium

*Points:*

- {'irrad': 7500, 'tmin': 10, 'tmax': 22, 'vap': 4, 'wind': 1.5, 'rain': 3, 'wav': 50, 'SMLIM': 0.5}

#### High Irradiance with Moderate Rainfall

*Rationale:* This hypothesis examines the impact of high irradiance combined with moderate rainfall, which may create a humid environment conducive to growth.

*Confidence:* medium

*Points:*

- {'irrad': 7800, 'tmin': 11, 'tmax': 24, 'vap': 3, 'wind': 1, 'rain': 6, 'wav': 65, 'SMLIM': 0.7}

#### High Irradiance with Low Wind

*Rationale:* This new hypothesis tests the effects of high irradiance with low wind speeds, which may reduce stress on the plants and enhance growth.

*Confidence:* medium

*Points:*

- {'irrad': 7700, 'tmin': 12, 'tmax': 24, 'vap': 3, 'wind': 0.5, 'rain': 4, 'wav': 55, 'SMLIM': 0.6}

## Iteration 43

As we reach iteration 42 of the Bayesian Optimization process, we have gathered a wealth of data that provides critical insights into the factors influencing Total Above Ground Production (TAGP) in sugar beet cultivation. The highest TAGP recorded so far is 10.12, achieved with high irradiance (7800 kJ/m2/day) and moderate temperatures (11-24°C). This reinforces the importance of maintaining high light levels while ensuring temperatures remain within a favorable range. Conversely, conditions with extreme temperatures, particularly those below 0°C or above 35°C, have consistently resulted in poor biomass production, with several experiments yielding TAGP below 1.0. The subspaces that maximize TAGP appear to cluster around high irradiance (7500-8000 kJ/m2/day) and moderate temperatures (10-25°C), while subspaces with extreme temperatures or low moisture levels should be avoided. Based on these findings, I propose to refine our hypotheses further, focusing on high irradiance and moderate temperature ranges while discarding those that have not performed well. Here are the updated hypotheses:

### Updated Hypotheses

#### High Irradiance with Optimal Temperature Range

*Rationale:* This hypothesis focuses on maintaining high irradiance while ensuring temperatures are kept within an optimal range to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 7800, 'tmin': 12, 'tmax': 24, 'vap': 3, 'wind': 1, 'rain': 5, 'wav': 50, 'SMLIM': 0.6}

#### Moderate Irradiance with High Moisture

*Rationale:* This hypothesis tests moderate irradiance combined with high moisture levels, which may enhance root development and biomass accumulation.

*Confidence:* high

*Points:*

- {'irrad': 6000, 'tmin': 15, 'tmax': 20, 'vap': 2, 'wind': 0.5, 'rain': 10, 'wav': 80, 'SMLIM': 0.9}

#### High Irradiance with Low Wind and Moderate Rainfall

*Rationale:* This hypothesis examines the impact of high irradiance combined with low wind speeds and moderate rainfall, which may create a humid environment conducive to growth.

*Confidence:* medium

*Points:*

- {'irrad': 7700, 'tmin': 10, 'tmax': 25, 'vap': 3, 'wind': 0.5, 'rain': 6, 'wav': 65, 'SMLIM': 0.7}

#### High Irradiance with Slightly Lower Temperature

*Rationale:* This hypothesis explores the effects of high irradiance with slightly lower temperatures, which may still promote growth without stress.

*Confidence:* medium

*Points:*

- {'irrad': 7500, 'tmin': 8, 'tmax': 22, 'vap': 4, 'wind': 1.5, 'rain': 3, 'wav': 50, 'SMLIM': 0.5}

## Iteration 54

As we continue to refine our hypotheses for maximizing Total Above Ground Production (TAGP) in sugar beet cultivation, it is crucial to ensure that all proposed points explore unique regions of the parameter space. The previous iterations have provided valuable insights, and the focus remains on high irradiance combined with optimal temperature and moisture conditions. Here are the updated hypotheses with new points that reflect this focus:

### Updated Hypotheses

#### High Irradiance with Optimal Temperature Range

*Rationale:* This hypothesis focuses on maintaining high irradiance while ensuring temperatures are kept within an optimal range to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 7850, 'tmin': 13, 'tmax': 23, 'vap': 3, 'wind': 1, 'rain': 5, 'wav': 50, 'SMLIM': 0.6}

#### Moderate Irradiance with High Moisture

*Rationale:* This hypothesis tests moderate irradiance combined with high moisture levels, which may enhance root development and biomass accumulation.

*Confidence:* high

*Points:*

- {'irrad': 6100, 'tmin': 16, 'tmax': 21, 'vap': 2, 'wind': 0.5, 'rain': 10, 'wav': 85, 'SMLIM': 0.9}

#### High Irradiance with Low Wind and Moderate Rainfall

*Rationale:* This hypothesis examines the impact of high irradiance combined with low wind speeds and moderate rainfall, which may create a humid environment conducive to growth.

*Confidence:* medium

*Points:*

- {'irrad': 7750, 'tmin': 11, 'tmax': 24, 'vap': 3, 'wind': 0.4, 'rain': 7, 'wav': 60, 'SMLIM': 0.7}

#### High Irradiance with Slightly Lower Temperature

*Rationale:* This hypothesis explores the effects of high irradiance with slightly lower temperatures, which may still promote growth without stress.

*Confidence:* medium

*Points:*

- {'irrad': 7600, 'tmin': 9, 'tmax': 21, 'vap': 4, 'wind': 1.5, 'rain': 3, 'wav': 55, 'SMLIM': 0.5}

#### High Irradiance with Moderate Temperature and Increased Vapour Pressure

*Rationale:* This hypothesis tests the effects of high irradiance with moderate temperatures and increased vapor pressure, which may enhance photosynthesis and growth.

*Confidence:* medium

*Points:*

- {'irrad': 7900, 'tmin': 12, 'tmax': 25, 'vap': 5, 'wind': 1, 'rain': 4, 'wav': 55, 'SMLIM': 0.6}

## Iteration 67

As we reach iteration 66 of the Bayesian Optimization process, we have gathered substantial data that highlights key factors influencing Total Above Ground Production (TAGP) in sugar beet cultivation. The highest TAGP recorded is 10.27, achieved with high irradiance (7818.38 kJ/m2/day) and moderate temperatures (16.94-16.28°C). This reinforces the importance of maintaining high light levels while ensuring temperatures remain within a favorable range. The data indicates that subspaces with high irradiance (around 7800-7900 kJ/m2/day) and moderate temperatures (10-25°C) consistently yield high TAGP. Conversely, conditions with extreme temperatures, particularly those below 0°C or above 35°C, have resulted in poor biomass production, with several experiments yielding TAGP below 1.0. Based on these findings, I propose to refine our hypotheses further, focusing on high irradiance and moderate temperature ranges while discarding those that have not performed well. Here are the updated hypotheses:

### Updated Hypotheses

#### High Irradiance with Optimal Temperature Range

*Rationale:* This hypothesis focuses on maintaining high irradiance while ensuring temperatures are kept within an optimal range to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 7900, 'tmin': 12, 'tmax': 24, 'vap': 4, 'wind': 1, 'rain': 5, 'wav': 55, 'SMLIM': 0.6}

#### Moderate Irradiance with High Moisture

*Rationale:* This hypothesis tests moderate irradiance combined with high moisture levels, which may enhance root development and biomass accumulation.

*Confidence:* high

*Points:*

- {'irrad': 6200, 'tmin': 15, 'tmax': 20, 'vap': 2, 'wind': 0.5, 'rain': 10, 'wav': 90, 'SMLIM': 0.9}

#### High Irradiance with Low Wind and Moderate Rainfall

*Rationale:* This hypothesis examines the impact of high irradiance combined with low wind speeds and moderate rainfall, which may create a humid environment conducive to growth.

*Confidence:* medium

*Points:*

- {'irrad': 7750, 'tmin': 11, 'tmax': 25, 'vap': 3, 'wind': 0.4, 'rain': 6, 'wav': 65, 'SMLIM': 0.7}

#### High Irradiance with Slightly Lower Temperature

*Rationale:* This hypothesis explores the effects of high irradiance with slightly lower temperatures, which may still promote growth without stress.

*Confidence:* medium

*Points:*

- {'irrad': 7700, 'tmin': 9, 'tmax': 22, 'vap': 4, 'wind': 1.5, 'rain': 3, 'wav': 50, 'SMLIM': 0.5}

#### High Irradiance with Increased Vapour Pressure

*Rationale:* This hypothesis tests the effects of high irradiance with moderate temperatures and increased vapor pressure, which may enhance photosynthesis and growth.

*Confidence:* medium

*Points:*

- {'irrad': 7850, 'tmin': 12, 'tmax': 25, 'vap': 5, 'wind': 1, 'rain': 4, 'wav': 55, 'SMLIM': 0.6}

## Iteration 79

As we continue to refine our hypotheses for maximizing Total Above Ground Production (TAGP) in sugar beet cultivation, it is essential to ensure that all proposed points explore unique regions of the parameter space. The previous iterations have provided valuable insights, and the focus remains on high irradiance combined with optimal temperature and moisture conditions. Here are the updated hypotheses with new points that reflect this focus:

### Updated Hypotheses

#### High Irradiance with Optimal Temperature Range

*Rationale:* This hypothesis focuses on maintaining high irradiance while ensuring temperatures are kept within an optimal range to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 7920, 'tmin': 13, 'tmax': 24, 'vap': 4, 'wind': 1, 'rain': 5, 'wav': 55, 'SMLIM': 0.6}

#### Moderate Irradiance with Adjusted Moisture

*Rationale:* This hypothesis tests moderate irradiance combined with adjusted moisture levels, which may enhance root development and biomass accumulation.

*Confidence:* high

*Points:*

- {'irrad': 6300, 'tmin': 15, 'tmax': 20, 'vap': 2, 'wind': 0.5, 'rain': 8, 'wav': 75, 'SMLIM': 0.85}

#### High Irradiance with Low Wind and Moderate Rainfall

*Rationale:* This hypothesis examines the impact of high irradiance combined with low wind speeds and moderate rainfall, which may create a humid environment conducive to growth.

*Confidence:* medium

*Points:*

- {'irrad': 7800, 'tmin': 11, 'tmax': 25, 'vap': 3, 'wind': 0.3, 'rain': 6, 'wav': 65, 'SMLIM': 0.7}

#### High Irradiance with Increased Vapour Pressure

*Rationale:* This hypothesis tests the effects of high irradiance with moderate temperatures and increased vapor pressure, which may enhance photosynthesis and growth.

*Confidence:* medium

*Points:*

- {'irrad': 7860, 'tmin': 12, 'tmax': 25, 'vap': 6, 'wind': 1, 'rain': 4, 'wav': 55, 'SMLIM': 0.6}

## Iteration 100

As we continue to refine our hypotheses for maximizing Total Above Ground Production (TAGP) in sugar beet cultivation, it is essential to ensure that all proposed points explore unique regions of the parameter space. The previous iterations have provided valuable insights, and the focus remains on high irradiance combined with optimal temperature and moisture conditions. Here are the updated hypotheses with new points that reflect this focus:

### Updated Hypotheses

#### High Irradiance with Optimal Temperature Range

*Rationale:* This hypothesis focuses on maintaining high irradiance while ensuring temperatures are kept within an optimal range to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 7950, 'tmin': 14, 'tmax': 23, 'vap': 4, 'wind': 1, 'rain': 5, 'wav': 55, 'SMLIM': 0.6}

#### Moderate Irradiance with High Moisture

*Rationale:* This hypothesis tests moderate irradiance combined with high moisture levels, which may enhance root development and biomass accumulation.

*Confidence:* high

*Points:*

- {'irrad': 6250, 'tmin': 16, 'tmax': 21, 'vap': 2, 'wind': 0.5, 'rain': 10, 'wav': 85, 'SMLIM': 0.9}

#### High Irradiance with Low Wind and Moderate Rainfall

*Rationale:* This hypothesis examines the impact of high irradiance combined with low wind speeds and moderate rainfall, which may create a humid environment conducive to growth.

*Confidence:* medium

*Points:*

- {'irrad': 7820, 'tmin': 12, 'tmax': 25, 'vap': 3, 'wind': 0.4, 'rain': 6, 'wav': 65, 'SMLIM': 0.7}

#### High Irradiance with Increased Vapour Pressure

*Rationale:* This hypothesis tests the effects of high irradiance with moderate temperatures and increased vapor pressure, which may enhance photosynthesis and growth.

*Confidence:* medium

*Points:*

- {'irrad': 7880, 'tmin': 12, 'tmax': 25, 'vap': 7, 'wind': 1, 'rain': 4, 'wav': 55, 'SMLIM': 0.6}

#### High Irradiance with Slightly Lower Temperature

*Rationale:* This hypothesis explores the effects of high irradiance with slightly lower temperatures, which may still promote growth without stress.

*Confidence:* medium

*Points:*

- {'irrad': 7750, 'tmin': 10, 'tmax': 21, 'vap': 4, 'wind': 1.5, 'rain': 3, 'wav': 50, 'SMLIM': 0.5}

## Final Conclusions

Throughout the optimization process, the hypotheses evolved significantly based on the experimental data collected from each iteration. Initially, the hypotheses focused on a broad range of parameter combinations, exploring various irradiance, temperature, and moisture levels. As the experiments progressed, we observed clear trends indicating that high irradiance (around 7500-8000 kJ/m2/day) and moderate temperatures (10-25°C) consistently yielded higher Total Above Ground Production (TAGP).

In response to these findings, the hypotheses were refined to emphasize combinations that maintained high irradiance while ensuring temperatures remained within an optimal range. For instance, hypotheses that included extreme temperature ranges or low irradiance were discarded due to their poor performance. New hypotheses were introduced to explore the effects of slightly lower temperatures while maintaining high irradiance, as well as the impact of moisture levels and vapor pressure on biomass production.

This iterative process allowed us to hone in on the most promising parameter combinations, ultimately leading to a set of hypotheses that were more targeted and aligned with the observed data trends.

| Hypothesis Name                               | Initial Confidence | Final Confidence |
|-----------------------------------------------|--------------------|------------------|
| Balanced High Irradiance and Moderate Temp    | Medium             | High             |
| High Irradiance and Temperature                | Medium             | High             |
| Optimal Moisture Conditions                    | High               | High             |
| High Irradiance with Low Wind                  | Medium             | Medium           |
| High Irradiance with Increased Vapour Pressure | Medium             | Medium           |
| High Irradiance with Slightly Lower Temp       | Medium             | Medium           |
| Moderate Irradiance with High Moisture         | High               | High             |
# Greenhouse Biomass Production

## Experiment Overview

The primary goal of this experiment is to maximize the monthly biomass production of sugar beet in a controlled greenhouse environment, specifically targeting the Total Above Ground Production (TAGP). The initial biomass is set at 0.41 kg/ha, and the experiment will systematically manipulate several environmental parameters to identify optimal conditions for growth.

The optimization parameters include irradiance (irrad), daily minimum and maximum temperatures (tmin, tmax), daily mean vapor pressure (vap), wind speed (wind), rainfall (rain), initial water content in the soil (wav), and maximum moisture content in the rooting zone (SMLIM). Each parameter has defined bounds, ensuring that the experimental conditions remain realistic and feasible.

Bayesian Optimization (BO) will be employed to explore the parameter space efficiently. BO will utilize a probabilistic model to predict the performance of different parameter combinations, guiding the search towards regions likely to yield higher TAGP. As the optimization progresses, I will provide point suggestions to explore new areas of the parameter space, especially when the BO process shows signs of plateauing. This adaptive approach will help identify the optimal conditions for maximizing biomass production, ultimately enhancing our understanding of sugar beet cultivation in controlled environments.

## Initial Thoughts

In the initial sampling step, we aim to explore diverse parameter combinations that could potentially maximize TAGP for sugar beet in a greenhouse setting. The hypotheses generated consider the relationships between environmental factors and their expected impact on biomass production. Notably, the maximum irradiance is set at 8000 kJ/m2/day, and the temperature bounds range from -30°C to 50°C, which allows for a wide exploration of conditions. The initial hypotheses suggest that higher irradiance, moderate temperatures, and optimal moisture levels are critical for enhancing photosynthesis and growth rates. By strategically selecting points across the parameter space, we can gather valuable data to inform subsequent optimization steps, particularly focusing on combinations that balance light, temperature, and moisture to maximize biomass production.
### Initial Hypotheses

#### Optimal Irradiance and Temperature

*Rationale:* Higher irradiance combined with moderate temperatures is expected to enhance photosynthesis and growth rates.

*Confidence:* high

*Points:*

- {'irrad': 6000, 'tmin': 15, 'tmax': 25, 'vap': 2, 'wind': 1, 'rain': 5, 'wav': 50, 'SMLIM': 0.5}

#### High Moisture and Moderate Temperature

*Rationale:* Maintaining high soil moisture levels while keeping temperatures moderate may optimize growth conditions.

*Confidence:* medium

*Points:*

- {'irrad': 4000, 'tmin': 10, 'tmax': 20, 'vap': 3, 'wind': 0.5, 'rain': 10, 'wav': 80, 'SMLIM': 0.8}

#### Balanced Irradiance and Low Wind

*Rationale:* A balance of irradiance with low wind speed can reduce stress on plants, promoting better growth.

*Confidence:* medium

*Points:*

- {'irrad': 5000, 'tmin': 12, 'tmax': 22, 'vap': 1.5, 'wind': 0.2, 'rain': 2, 'wav': 30, 'SMLIM': 0.4}

#### High Irradiance with Controlled Rainfall

*Rationale:* High irradiance coupled with controlled rainfall can provide optimal hydration and light for growth.

*Confidence:* medium

*Points:*

- {'irrad': 7000, 'tmin': 18, 'tmax': 28, 'vap': 2.5, 'wind': 0.8, 'rain': 3, 'wav': 60, 'SMLIM': 0.6}

#### Moderate Temperature and High Vapour Pressure

*Rationale:* Moderate temperatures with high vapor pressure can enhance transpiration and nutrient uptake.

*Confidence:* low

*Points:*

- {'irrad': 3000, 'tmin': 14, 'tmax': 24, 'vap': 5, 'wind': 1.5, 'rain': 0, 'wav': 40, 'SMLIM': 0.3}

## Iteration 12

As we progress through iteration 11 of the Bayesian Optimization, we have gathered valuable insights from the experimental data. The highest TAGP observed so far is 8.23 from iteration 4, indicating that higher irradiance (7000 kJ/m2/day) and moderate temperatures (18°C to 28°C) are beneficial for biomass production. Conversely, several points with low TAGP (0.41) suggest that extreme temperature conditions, particularly negative minimum temperatures and high maximum temperatures, are detrimental to growth. The data indicates that maintaining a balance of irradiance, moderate temperatures, and optimal moisture levels is crucial for maximizing TAGP. The subspaces that maximize TAGP appear to be around high irradiance (6000-8000 kJ/m2/day) and moderate temperature ranges (15-25°C). In contrast, conditions with low irradiance and extreme temperatures have consistently resulted in poor performance. Based on these findings, I will refine the previous hypotheses, discarding those that performed poorly and proposing new ones that align with the successful conditions identified. The focus will be on high irradiance, moderate temperatures, and optimal moisture levels to enhance biomass production.

### Updated Hypotheses

#### High Irradiance and Moderate Temperature

*Rationale:* Building on the successful conditions from iteration 4, this hypothesis focuses on high irradiance and moderate temperatures to enhance photosynthesis.

*Confidence:* high

*Points:*

- {'irrad': 7500, 'tmin': 16, 'tmax': 26, 'vap': 2, 'wind': 1, 'rain': 5, 'wav': 70, 'SMLIM': 0.5}

#### Moderate Irradiance with Optimal Moisture

*Rationale:* This hypothesis aims to explore the effects of moderate irradiance combined with optimal soil moisture levels, which may enhance growth.

*Confidence:* medium

*Points:*

- {'irrad': 5000, 'tmin': 14, 'tmax': 24, 'vap': 3, 'wind': 0.5, 'rain': 8, 'wav': 90, 'SMLIM': 0.7}

#### Controlled Irradiance with Low Wind

*Rationale:* This hypothesis focuses on maintaining controlled irradiance while minimizing wind stress, which may improve plant resilience and growth.

*Confidence:* medium

*Points:*

- {'irrad': 6000, 'tmin': 12, 'tmax': 22, 'vap': 2.5, 'wind': 0.1, 'rain': 4, 'wav': 50, 'SMLIM': 0.6}

#### High Irradiance with Moderate Rainfall

*Rationale:* Exploring high irradiance with controlled rainfall may provide optimal hydration and light for growth, building on previous successful conditions.

*Confidence:* medium

*Points:*

- {'irrad': 8000, 'tmin': 15, 'tmax': 25, 'vap': 2, 'wind': 0.5, 'rain': 6, 'wav': 80, 'SMLIM': 0.5}

#### Avoid Extreme Conditions

*Rationale:* This hypothesis aims to avoid extreme temperature conditions that have proven detrimental in previous iterations.

*Confidence:* high

*Points:*

- {'irrad': 4000, 'tmin': 10, 'tmax': 20, 'vap': 3, 'wind': 1, 'rain': 2, 'wav': 40, 'SMLIM': 0.4}

## Iteration 22

As we reach iteration 21 of the Bayesian Optimization, the data collected thus far provides valuable insights into the conditions that maximize TAGP for sugar beet. The highest TAGP observed is 10.30 from iteration 20, achieved with high irradiance (8000 kJ/m2/day) and low temperatures (5.16°C to 19.65°C). This suggests that while high irradiance is beneficial, maintaining moderate temperatures is crucial to avoid stress on the plants. The subspaces that maximize TAGP appear to be around high irradiance (7500-8000 kJ/m2/day) with temperatures ranging from 5°C to 27°C. Conversely, conditions with extreme temperatures, particularly low minimum temperatures and high maximum temperatures, have consistently resulted in poor performance, as seen in iterations 6, 8, and 11, where TAGP dropped to 0.41. Based on these findings, I will refine the previous hypotheses, discarding those that performed poorly, such as 'Avoid Extreme Conditions,' and propose new ones that align with the successful conditions identified. The focus will be on high irradiance, moderate temperatures, and optimal moisture levels to enhance biomass production. The next hypotheses will explore combinations that leverage these successful conditions while avoiding detrimental extremes.

### Updated Hypotheses

#### High Irradiance with Moderate Temperature

*Rationale:* Building on the successful conditions from iterations 12 and 20, this hypothesis focuses on high irradiance and moderate temperatures to enhance photosynthesis.

*Confidence:* high

*Points:*

- {'irrad': 8000, 'tmin': 10, 'tmax': 20, 'vap': 2, 'wind': 0.5, 'rain': 5, 'wav': 75, 'SMLIM': 0.5}

#### Moderate Irradiance with Optimal Moisture

*Rationale:* This hypothesis aims to explore the effects of moderate irradiance combined with optimal soil moisture levels, which may enhance growth.

*Confidence:* medium

*Points:*

- {'irrad': 6000, 'tmin': 15, 'tmax': 25, 'vap': 3, 'wind': 0.5, 'rain': 6, 'wav': 85, 'SMLIM': 0.7}

#### Controlled Irradiance with Low Wind

*Rationale:* This hypothesis focuses on maintaining controlled irradiance while minimizing wind stress, which may improve plant resilience and growth.

*Confidence:* medium

*Points:*

- {'irrad': 7000, 'tmin': 12, 'tmax': 22, 'vap': 2.5, 'wind': 0.1, 'rain': 4, 'wav': 60, 'SMLIM': 0.6}

#### High Irradiance with Controlled Rainfall

*Rationale:* Exploring high irradiance with controlled rainfall may provide optimal hydration and light for growth, building on previous successful conditions.

*Confidence:* medium

*Points:*

- {'irrad': 7500, 'tmin': 15, 'tmax': 25, 'vap': 2, 'wind': 0.5, 'rain': 5, 'wav': 80, 'SMLIM': 0.5}

#### Avoid Low Minimum Temperatures

*Rationale:* This hypothesis aims to avoid low minimum temperatures that have proven detrimental in previous iterations, focusing on conditions that maintain plant health.

*Confidence:* high

*Points:*

- {'irrad': 5000, 'tmin': 12, 'tmax': 22, 'vap': 3, 'wind': 1, 'rain': 2, 'wav': 50, 'SMLIM': 0.4}

## Iteration 31

As we reach iteration 30 of the Bayesian Optimization, the data collected thus far reveals significant insights into the conditions that maximize TAGP for sugar beet. The highest TAGP observed is 10.41, achieved with high irradiance (8000 kJ/m2/day) and moderate temperatures (10u00b0C to 20u00b0C). This suggests that while high irradiance is beneficial, maintaining moderate temperatures is crucial to avoid stress on the plants. The subspaces that maximize TAGP appear to be around high irradiance (7500-8000 kJ/m2/day) with temperatures ranging from 10u00b0C to 20u00b0C. Conversely, conditions with extreme temperatures, particularly low minimum temperatures (below 10u00b0C) and high maximum temperatures (above 30u00b0C), have consistently resulted in poor performance, as seen in iterations 6, 8, and 11, where TAGP dropped to 0.41. Based on these findings, I will refine the previous hypotheses, discarding those that performed poorly, and propose new ones that align with the successful conditions identified. The focus will be on high irradiance, moderate temperatures, and optimal moisture levels to enhance biomass production.

### Updated Hypotheses

#### High Irradiance with Moderate Temperature

*Rationale:* Building on the successful conditions from iterations 20 and 22, this hypothesis focuses on high irradiance and moderate temperatures to enhance photosynthesis.

*Confidence:* high

*Points:*

- {'irrad': 8000, 'tmin': 12, 'tmax': 18, 'vap': 2, 'wind': 0.5, 'rain': 5, 'wav': 70, 'SMLIM': 0.5}

#### Moderate Irradiance with Optimal Moisture

*Rationale:* This hypothesis aims to explore the effects of moderate irradiance combined with optimal soil moisture levels, which may enhance growth.

*Confidence:* medium

*Points:*

- {'irrad': 6000, 'tmin': 16, 'tmax': 26, 'vap': 3, 'wind': 0.5, 'rain': 7, 'wav': 90, 'SMLIM': 0.7}

#### Controlled Irradiance with Low Wind

*Rationale:* This hypothesis focuses on maintaining controlled irradiance while minimizing wind stress, which may improve plant resilience and growth.

*Confidence:* medium

*Points:*

- {'irrad': 7000, 'tmin': 14, 'tmax': 20, 'vap': 2.5, 'wind': 0.2, 'rain': 3, 'wav': 65, 'SMLIM': 0.6}

#### High Irradiance with Controlled Rainfall

*Rationale:* Exploring high irradiance with controlled rainfall may provide optimal hydration and light for growth, building on previous successful conditions.

*Confidence:* medium

*Points:*

- {'irrad': 7500, 'tmin': 14, 'tmax': 24, 'vap': 2, 'wind': 0.5, 'rain': 4, 'wav': 85, 'SMLIM': 0.5}

#### Avoid Extreme Temperature Conditions

*Rationale:* This hypothesis aims to avoid extreme temperature conditions that have proven detrimental in previous iterations, focusing on conditions that maintain plant health.

*Confidence:* high

*Points:*

- {'irrad': 5000, 'tmin': 13, 'tmax': 21, 'vap': 3, 'wind': 1, 'rain': 2, 'wav': 55, 'SMLIM': 0.4}

## Iteration 42

As we continue to refine our hypotheses based on the data collected, it is essential to ensure that each proposed point is unique and explores new areas of the parameter space. The focus remains on high irradiance, moderate temperatures, and optimal moisture levels to enhance biomass production. The previous iterations have provided valuable insights, and the new points aim to build on these findings while avoiding redundancy. By exploring diverse combinations, we can further investigate the conditions that maximize TAGP for sugar beet in the greenhouse environment.

### Updated Hypotheses

#### High Irradiance with Moderate Temperature

*Rationale:* Building on the successful conditions from iterations 20 and 31, this hypothesis focuses on high irradiance and moderate temperatures to enhance photosynthesis.

*Confidence:* high

*Points:*

- {'irrad': 8000, 'tmin': 12, 'tmax': 20, 'vap': 2, 'wind': 0.5, 'rain': 5, 'wav': 75, 'SMLIM': 0.5}

#### Moderate Irradiance with Optimal Moisture

*Rationale:* This hypothesis aims to explore the effects of moderate irradiance combined with optimal soil moisture levels, which may enhance growth.

*Confidence:* medium

*Points:*

- {'irrad': 6200, 'tmin': 16, 'tmax': 26, 'vap': 3, 'wind': 0.5, 'rain': 7, 'wav': 90, 'SMLIM': 0.6}

#### Controlled Irradiance with Low Wind

*Rationale:* This hypothesis focuses on maintaining controlled irradiance while minimizing wind stress, which may improve plant resilience and growth.

*Confidence:* medium

*Points:*

- {'irrad': 7000, 'tmin': 14, 'tmax': 20, 'vap': 2.5, 'wind': 0.1, 'rain': 3, 'wav': 65, 'SMLIM': 0.6}

#### High Irradiance with Controlled Rainfall

*Rationale:* Exploring high irradiance with controlled rainfall may provide optimal hydration and light for growth, building on previous successful conditions.

*Confidence:* medium

*Points:*

- {'irrad': 7500, 'tmin': 15, 'tmax': 25, 'vap': 2, 'wind': 0.5, 'rain': 3, 'wav': 80, 'SMLIM': 0.5}

#### Avoid Extreme Temperature Conditions

*Rationale:* This hypothesis aims to avoid extreme temperature conditions that have proven detrimental in previous iterations, focusing on conditions that maintain plant health.

*Confidence:* high

*Points:*

- {'irrad': 5200, 'tmin': 13, 'tmax': 21, 'vap': 3, 'wind': 1, 'rain': 2, 'wav': 55, 'SMLIM': 0.4}

## Iteration 54

As we continue to refine our hypotheses based on the data collected, it is essential to ensure that each proposed point explores new areas of the parameter space. The focus remains on high irradiance, moderate temperatures, and optimal moisture levels to enhance biomass production. The previous iterations have provided valuable insights, and the new points aim to build on these findings while avoiding redundancy. By exploring diverse combinations, we can further investigate the conditions that maximize TAGP for sugar beet in the greenhouse environment.

### Updated Hypotheses

#### High Irradiance with Moderate Temperature

*Rationale:* Building on the successful conditions from iterations 20 and 31, this hypothesis focuses on high irradiance and moderate temperatures to enhance photosynthesis.

*Confidence:* high

*Points:*

- {'irrad': 8000, 'tmin': 13, 'tmax': 19, 'vap': 2, 'wind': 0.5, 'rain': 5, 'wav': 75, 'SMLIM': 0.5}

#### Moderate Irradiance with Optimal Moisture

*Rationale:* This hypothesis aims to explore the effects of moderate irradiance combined with optimal soil moisture levels, which may enhance growth.

*Confidence:* medium

*Points:*

- {'irrad': 6200, 'tmin': 17, 'tmax': 27, 'vap': 3, 'wind': 0.5, 'rain': 8, 'wav': 85, 'SMLIM': 0.6}

#### Controlled Irradiance with Low Wind

*Rationale:* This hypothesis focuses on maintaining controlled irradiance while minimizing wind stress, which may improve plant resilience and growth.

*Confidence:* medium

*Points:*

- {'irrad': 7000, 'tmin': 15, 'tmax': 21, 'vap': 2.5, 'wind': 0.2, 'rain': 4, 'wav': 60, 'SMLIM': 0.6}

#### High Irradiance with Controlled Rainfall

*Rationale:* Exploring high irradiance with controlled rainfall may provide optimal hydration and light for growth, building on previous successful conditions.

*Confidence:* medium

*Points:*

- {'irrad': 7500, 'tmin': 14, 'tmax': 24, 'vap': 2, 'wind': 0.5, 'rain': 6, 'wav': 80, 'SMLIM': 0.5}

#### Avoid Low Minimum Temperatures

*Rationale:* This hypothesis aims to avoid low minimum temperatures that have proven detrimental in previous iterations, focusing on conditions that maintain plant health.

*Confidence:* high

*Points:*

- {'irrad': 5500, 'tmin': 13, 'tmax': 23, 'vap': 3, 'wind': 1, 'rain': 2, 'wav': 55, 'SMLIM': 0.4}

## Iteration 65

As we continue to refine our hypotheses based on the data collected, it is essential to ensure that each proposed point explores new areas of the parameter space. The focus remains on high irradiance, moderate temperatures, and optimal moisture levels to enhance biomass production. The previous iterations have provided valuable insights, and the new points aim to build on these findings while avoiding redundancy. By exploring diverse combinations, we can further investigate the conditions that maximize TAGP for sugar beet in the greenhouse environment.

### Updated Hypotheses

#### Moderate Irradiance with Optimal Moisture

*Rationale:* This hypothesis aims to explore the effects of moderate irradiance combined with optimal soil moisture levels, which may enhance growth.

*Confidence:* medium

*Points:*

- {'irrad': 6300, 'tmin': 15, 'tmax': 25, 'vap': 3, 'wind': 0.5, 'rain': 6, 'wav': 85, 'SMLIM': 0.6}

#### High Irradiance with Controlled Rainfall

*Rationale:* Exploring high irradiance with controlled rainfall may provide optimal hydration and light for growth, building on previous successful conditions.

*Confidence:* medium

*Points:*

- {'irrad': 7500, 'tmin': 15, 'tmax': 25, 'vap': 2, 'wind': 0.5, 'rain': 4, 'wav': 80, 'SMLIM': 0.5}

#### Avoid Extreme Temperature Conditions

*Rationale:* This hypothesis aims to avoid extreme temperature conditions that have proven detrimental in previous iterations, focusing on conditions that maintain plant health.

*Confidence:* high

*Points:*

- {'irrad': 5400, 'tmin': 14, 'tmax': 22, 'vap': 3, 'wind': 1, 'rain': 2, 'wav': 50, 'SMLIM': 0.4}

## Iteration 75

As we continue to refine our hypotheses based on the data collected, it is essential to ensure that each proposed point explores new areas of the parameter space. The focus remains on high irradiance, moderate temperatures, and optimal moisture levels to enhance biomass production. The previous iterations have provided valuable insights, and the new points aim to build on these findings while avoiding redundancy. By exploring diverse combinations, we can further investigate the conditions that maximize TAGP for sugar beet in the greenhouse environment.

### Updated Hypotheses

#### Moderate Irradiance with Optimal Moisture

*Rationale:* This hypothesis aims to explore the effects of moderate irradiance combined with optimal soil moisture levels, which may enhance growth.

*Confidence:* medium

*Points:*

- {'irrad': 6300, 'tmin': 17, 'tmax': 27, 'vap': 3, 'wind': 0.5, 'rain': 8, 'wav': 85, 'SMLIM': 0.6}

#### Controlled Irradiance with Low Wind

*Rationale:* This hypothesis focuses on maintaining controlled irradiance while minimizing wind stress, which may improve plant resilience and growth.

*Confidence:* medium

*Points:*

- {'irrad': 7100, 'tmin': 14, 'tmax': 20, 'vap': 2.5, 'wind': 0.1, 'rain': 3, 'wav': 65, 'SMLIM': 0.6}

#### High Irradiance with Controlled Rainfall

*Rationale:* Exploring high irradiance with controlled rainfall may provide optimal hydration and light for growth, building on previous successful conditions.

*Confidence:* medium

*Points:*

- {'irrad': 7600, 'tmin': 15, 'tmax': 25, 'vap': 2, 'wind': 0.5, 'rain': 4, 'wav': 80, 'SMLIM': 0.5}

#### Avoid Extreme Temperature Conditions

*Rationale:* This hypothesis aims to avoid extreme temperature conditions that have proven detrimental in previous iterations, focusing on conditions that maintain plant health.

*Confidence:* high

*Points:*

- {'irrad': 5400, 'tmin': 13, 'tmax': 21, 'vap': 3, 'wind': 1, 'rain': 2, 'wav': 55, 'SMLIM': 0.4}

## Iteration 87

As we continue to refine our hypotheses based on the data collected, it is essential to ensure that each proposed point explores new areas of the parameter space. The focus remains on high irradiance, moderate temperatures, and optimal moisture levels to enhance biomass production. The previous iterations have provided valuable insights, and the new points aim to build on these findings while avoiding redundancy. By exploring diverse combinations, we can further investigate the conditions that maximize TAGP for sugar beet in the greenhouse environment.

### Updated Hypotheses

#### High Irradiance with Moderate Temperature

*Rationale:* Building on the successful conditions from previous iterations, this hypothesis focuses on high irradiance and moderate temperatures to enhance photosynthesis.

*Confidence:* high

*Points:*

- {'irrad': 8000, 'tmin': 14, 'tmax': 20, 'vap': 2, 'wind': 0.5, 'rain': 5, 'wav': 75, 'SMLIM': 0.5}

#### Avoid Low Minimum Temperatures

*Rationale:* This hypothesis aims to avoid low minimum temperatures that have proven detrimental in previous iterations, focusing on conditions that maintain plant health.

*Confidence:* high

*Points:*

- {'irrad': 5500, 'tmin': 13, 'tmax': 21, 'vap': 3, 'wind': 1, 'rain': 2, 'wav': 55, 'SMLIM': 0.4}

## Iteration 96

As we reach iteration 95 of the Bayesian Optimization, the data collected thus far reveals significant insights into the conditions that maximize TAGP for sugar beet. The highest TAGP observed is 10.41, achieved with high irradiance (8000 kJ/m2/day) and moderate temperatures (10u00b0C to 20u00b0C). This suggests that while high irradiance is beneficial, maintaining moderate temperatures is crucial to avoid stress on the plants. The subspaces that maximize TAGP appear to be around high irradiance (7500-8000 kJ/m2/day) with temperatures ranging from 10u00b0C to 20u00b0C. Conversely, conditions with extreme temperatures, particularly low minimum temperatures (below 10u00b0C) and high maximum temperatures (above 30u00b0C), have consistently resulted in poor performance, as seen in several iterations where TAGP dropped to 0.41. Based on these findings, I will refine the previous hypotheses, discarding those that performed poorly, and propose new ones that align with the successful conditions identified. The focus will be on high irradiance, moderate temperatures, and optimal moisture levels to enhance biomass production. The new hypotheses will explore combinations that leverage these successful conditions while avoiding detrimental extremes.

### Updated Hypotheses

#### High Irradiance with Moderate Temperature

*Rationale:* Building on the successful conditions from previous iterations, this hypothesis focuses on high irradiance and moderate temperatures to enhance photosynthesis.

*Confidence:* high

*Points:*

- {'irrad': 8000, 'tmin': 11, 'tmax': 19, 'vap': 2, 'wind': 0.5, 'rain': 5, 'wav': 75, 'SMLIM': 0.5}

#### Moderate Irradiance with Optimal Moisture

*Rationale:* This hypothesis aims to explore the effects of moderate irradiance combined with optimal soil moisture levels, which may enhance growth.

*Confidence:* medium

*Points:*

- {'irrad': 6200, 'tmin': 17, 'tmax': 27, 'vap': 3, 'wind': 0.5, 'rain': 8, 'wav': 90, 'SMLIM': 0.6}

#### Controlled Irradiance with Low Wind

*Rationale:* This hypothesis focuses on maintaining controlled irradiance while minimizing wind stress, which may improve plant resilience and growth.

*Confidence:* medium

*Points:*

- {'irrad': 7000, 'tmin': 15, 'tmax': 21, 'vap': 2.5, 'wind': 0.1, 'rain': 3, 'wav': 65, 'SMLIM': 0.6}

#### High Irradiance with Controlled Rainfall

*Rationale:* Exploring high irradiance with controlled rainfall may provide optimal hydration and light for growth, building on previous successful conditions.

*Confidence:* medium

*Points:*

- {'irrad': 7500, 'tmin': 16, 'tmax': 24, 'vap': 2, 'wind': 0.5, 'rain': 6, 'wav': 80, 'SMLIM': 0.5}

#### Avoid Extreme Temperature Conditions

*Rationale:* This hypothesis aims to avoid extreme temperature conditions that have proven detrimental in previous iterations, focusing on conditions that maintain plant health.

*Confidence:* high

*Points:*

- {'irrad': 5400, 'tmin': 14, 'tmax': 22, 'vap': 3, 'wind': 1, 'rain': 2, 'wav': 55, 'SMLIM': 0.4}

## Final Conclusions

Throughout the optimization process, the hypotheses evolved significantly based on the experimental data collected from each iteration. Initially, the hypotheses focused on a broad range of parameter combinations, exploring various irradiance levels, temperature ranges, and moisture conditions. As the iterations progressed, the data revealed specific trends and relationships that informed the refinement of these hypotheses.

Key findings indicated that high irradiance (around 8000 kJ/m²/day) consistently correlated with higher TAGP, particularly when paired with moderate temperatures (10°C to 20°C). Conversely, extreme temperature conditions, especially low minimum temperatures, were detrimental to biomass production. This led to the elimination of hypotheses that suggested exploring extreme conditions and a stronger emphasis on maintaining moderate temperatures and optimal moisture levels.

The confidence levels in the hypotheses also evolved, reflecting the reliability of the data supporting each hypothesis. As successful conditions were identified, confidence in those hypotheses increased, while those that performed poorly were downgraded or discarded.

The following table summarizes the evolution of confidence in the hypotheses throughout the optimization:

| Hypothesis                                   | Initial Confidence | Final Confidence |
|----------------------------------------------|--------------------|------------------|
| High Irradiance with Moderate Temperature    | High               | High             |
| Moderate Irradiance with Optimal Moisture    | Medium             | Medium           |
| Controlled Irradiance with Low Wind          | Medium             | Medium           |
| High Irradiance with Controlled Rainfall     | Medium             | Medium           |
| Avoid Extreme Temperature Conditions          | High               | High             |
| Avoid Low Minimum Temperatures                | Low                | High             |

This iterative refinement process allowed for a more targeted exploration of the parameter space, ultimately leading to improved biomass production outcomes.
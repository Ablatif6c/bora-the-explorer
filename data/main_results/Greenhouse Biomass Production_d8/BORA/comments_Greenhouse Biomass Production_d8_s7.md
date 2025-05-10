# Greenhouse Biomass Production

## Experiment Overview

The experiment aims to maximize the monthly biomass production of sugar beet in a controlled greenhouse environment, with the initial biomass set at 0.41 kg/ha. The optimization process will focus on several key parameters: irradiance (irrad), daily minimum and maximum temperatures (tmin, tmax), daily mean vapor pressure (vap), wind speed (wind), daily rainfall (rain), initial water content in the soil profile (wav), and maximum moisture content in the rooting depth zone (SMLIM). Each parameter has defined bounds, ensuring that the experimental conditions remain realistic and manageable.

Bayesian Optimization (BO) will be employed to systematically explore this multi-dimensional parameter space. BO will utilize a probabilistic model to predict the performance of different parameter combinations, iteratively refining its search based on observed biomass production outcomes. As the optimization progresses, I will provide point suggestions to guide the exploration, especially when the BO process plateaus, indicating that further exploration may yield diminishing returns. By identifying optimal conditions that maximize Total Above Ground Production (TAGP), the experiment aims to enhance biomass yield effectively, contributing valuable insights into greenhouse cultivation practices for sugar beet.

## Initial Thoughts

The initial hypotheses aim to explore diverse regions of the parameter space to maximize Total Above Ground Production (TAGP) effectively. Each hypothesis is grounded in expected interactions between environmental factors and biomass production, considering the physiological needs of sugar beet. The selected points reflect a balance of irradiance, temperature, and moisture, which are critical for optimal growth in a greenhouse setting. Notably, the maximum bounds for irradiance (8000 kJ/m2/day), temperature (tmin: -30°C to 30°C, tmax: -20°C to 50°C), vapor pressure (0.06 to 10 kPa), wind speed (0 to 5 m/s), rainfall (0 to 20 mm), water content (0 to 100 cm), and moisture content (0 to 1) have been respected. The hypotheses will guide the initial sampling step and provide a foundation for further exploration through Bayesian Optimization, allowing for systematic identification of conditions that maximize TAGP.
### Initial Hypotheses

#### Moderate Irradiance and Temperature

*Rationale:* Moderate levels of irradiance and temperature are expected to promote healthy growth without causing stress to the plants.

*Confidence:* high

*Points:*

- {'irrad': 4000, 'tmin': 15, 'tmax': 25, 'vap': 2, 'wind': 1, 'rain': 5, 'wav': 50, 'SMLIM': 0.5}

#### High Irradiance with Optimal Moisture

*Rationale:* High irradiance combined with adequate moisture levels may enhance photosynthesis and biomass production.

*Confidence:* medium

*Points:*

- {'irrad': 7000, 'tmin': 18, 'tmax': 28, 'vap': 3, 'wind': 0.5, 'rain': 2, 'wav': 70, 'SMLIM': 0.7}

#### Cool Temperatures with High Humidity

*Rationale:* Cooler temperatures with high vapor pressure may reduce stress and promote biomass accumulation in sugar beet.

*Confidence:* medium

*Points:*

- {'irrad': 3000, 'tmin': 10, 'tmax': 20, 'vap': 5, 'wind': 1.5, 'rain': 10, 'wav': 60, 'SMLIM': 0.6}

#### Balanced Conditions for Growth

*Rationale:* A balanced approach with moderate values across all parameters may yield stable growth conditions.

*Confidence:* high

*Points:*

- {'irrad': 5000, 'tmin': 12, 'tmax': 22, 'vap': 4, 'wind': 1, 'rain': 3, 'wav': 40, 'SMLIM': 0.4}

#### High Temperature and Low Wind

*Rationale:* Higher temperatures with low wind speeds can create a favorable microclimate for sugar beet growth.

*Confidence:* medium

*Points:*

- {'irrad': 4500, 'tmin': 20, 'tmax': 30, 'vap': 2, 'wind': 0.2, 'rain': 1, 'wav': 30, 'SMLIM': 0.3}

## Iteration 25

As we progress through iteration 24, the data reveals several insights into the relationships between the parameters and Total Above Ground Production (TAGP). The highest TAGP observed is 9.23, achieved with an irradiance of 6548.39 kJ/m2/day, a minimum temperature of 8.05°C, and a maximum temperature of 18.66°C. This suggests that moderate temperatures combined with high irradiance are beneficial for biomass production. Conversely, several combinations with extreme temperatures (e.g., tmin: -30°C, tmax: -20°C) resulted in minimal TAGP, indicating detrimental effects on growth. The data also shows that high vapor pressure (vap) and adequate moisture (wav, SMLIM) are crucial for maximizing TAGP. The subspaces that maximize TAGP appear to cluster around moderate to high irradiance (6000-8000 kJ/m2/day), moderate temperatures (10-30°C), and sufficient moisture levels. In contrast, combinations with low irradiance, extreme temperatures, and low moisture consistently yield poor results. Based on these findings, I will refine the previous hypotheses, discarding those that performed poorly and proposing new ones that align with the observed successful conditions.

### Updated Hypotheses

#### High Irradiance with Moderate Temperatures

*Rationale:* Building on the successful conditions observed, this hypothesis focuses on high irradiance and moderate temperatures to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 7500, 'tmin': 15, 'tmax': 25, 'vap': 4, 'wind': 1, 'rain': 3, 'wav': 65, 'SMLIM': 0.6}

#### Moderate Irradiance with Optimal Moisture

*Rationale:* This hypothesis aims to explore the balance of moderate irradiance and optimal moisture levels, which have shown promise in previous iterations.

*Confidence:* medium

*Points:*

- {'irrad': 6000, 'tmin': 12, 'tmax': 22, 'vap': 3, 'wind': 0.5, 'rain': 2, 'wav': 70, 'SMLIM': 0.7}

#### High Temperature with High Humidity

*Rationale:* Exploring the effects of higher temperatures combined with high vapor pressure to see if it can enhance biomass production.

*Confidence:* medium

*Points:*

- {'irrad': 6800, 'tmin': 20, 'tmax': 30, 'vap': 6, 'wind': 1.5, 'rain': 1, 'wav': 50, 'SMLIM': 0.5}

#### Balanced Conditions for Growth

*Rationale:* Revisiting the balanced approach with moderate values across all parameters to ensure stable growth conditions.

*Confidence:* high

*Points:*

- {'irrad': 5000, 'tmin': 14, 'tmax': 24, 'vap': 4, 'wind': 1, 'rain': 3, 'wav': 60, 'SMLIM': 0.5}

#### Exploring Low Wind and High Irradiance

*Rationale:* Investigating the impact of low wind speeds combined with high irradiance to create a favorable microclimate for growth.

*Confidence:* medium

*Points:*

- {'irrad': 8000, 'tmin': 18, 'tmax': 26, 'vap': 5, 'wind': 0.2, 'rain': 2, 'wav': 55, 'SMLIM': 0.4}

## Iteration 37

As we reach iteration 36, the data reveals significant insights into the relationships between the parameters and Total Above Ground Production (TAGP). The highest TAGP observed is 10.02, achieved with an irradiance of 7512.24 kJ/m2/day, a minimum temperature of 19.75°C, and a maximum temperature of 14.72°C. This suggests that high irradiance combined with moderate temperatures can be highly beneficial for biomass production. The data indicates that subspaces maximizing TAGP cluster around high irradiance (7000-8000 kJ/m2/day), moderate temperatures (15-30°C), and sufficient moisture levels (wav and SMLIM). Conversely, combinations with low irradiance, extreme temperatures (especially low), and low moisture consistently yield poor results, as seen in iterations with tmin below 0°C and tmax above 30°C. Notably, conditions with tmin below 0°C and tmax above 30°C have consistently resulted in minimal TAGP, indicating detrimental effects on growth. Based on these findings, I will refine the previous hypotheses, discarding those that performed poorly and proposing new ones that align with the observed successful conditions.

### Updated Hypotheses

#### High Irradiance with Moderate Temperatures

*Rationale:* Building on the successful conditions observed, this hypothesis focuses on high irradiance and moderate temperatures to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 7800, 'tmin': 18, 'tmax': 26, 'vap': 5, 'wind': 1, 'rain': 2, 'wav': 70, 'SMLIM': 0.6}

#### Moderate Irradiance with Optimal Moisture

*Rationale:* This hypothesis aims to explore the balance of moderate irradiance and optimal moisture levels, which have shown promise in previous iterations.

*Confidence:* medium

*Points:*

- {'irrad': 6500, 'tmin': 14, 'tmax': 24, 'vap': 4, 'wind': 0.5, 'rain': 3, 'wav': 75, 'SMLIM': 0.7}

#### High Temperature with High Humidity

*Rationale:* Exploring the effects of higher temperatures combined with high vapor pressure to see if it can enhance biomass production.

*Confidence:* medium

*Points:*

- {'irrad': 7000, 'tmin': 22, 'tmax': 30, 'vap': 6, 'wind': 1, 'rain': 1, 'wav': 60, 'SMLIM': 0.5}

#### Balanced Conditions for Growth

*Rationale:* Revisiting the balanced approach with moderate values across all parameters to ensure stable growth conditions.

*Confidence:* high

*Points:*

- {'irrad': 6000, 'tmin': 15, 'tmax': 25, 'vap': 4, 'wind': 1, 'rain': 2, 'wav': 65, 'SMLIM': 0.5}

#### Exploring Low Wind and High Irradiance

*Rationale:* Investigating the impact of low wind speeds combined with high irradiance to create a favorable microclimate for growth.

*Confidence:* medium

*Points:*

- {'irrad': 8000, 'tmin': 19, 'tmax': 27, 'vap': 5, 'wind': 0.2, 'rain': 2, 'wav': 65, 'SMLIM': 0.4}

## Iteration 49

As we continue to refine our hypotheses based on the data collected, it is essential to ensure that each proposed point is unique and explores new regions of the parameter space. The previous iterations have shown that high irradiance combined with moderate temperatures and sufficient moisture levels are critical for maximizing Total Above Ground Production (TAGP). The focus remains on identifying optimal conditions that can enhance biomass production while avoiding combinations that have previously resulted in poor outcomes. The following hypotheses have been updated with new points to explore further.

### Updated Hypotheses

#### High Irradiance with Moderate Temperatures

*Rationale:* Building on the successful conditions observed, this hypothesis focuses on high irradiance and moderate temperatures to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 7800, 'tmin': 20, 'tmax': 25, 'vap': 5, 'wind': 1, 'rain': 2, 'wav': 70, 'SMLIM': 0.6}

#### Moderate Irradiance with Optimal Moisture

*Rationale:* This hypothesis aims to explore the balance of moderate irradiance and optimal moisture levels, which have shown promise in previous iterations.

*Confidence:* medium

*Points:*

- {'irrad': 6500, 'tmin': 15, 'tmax': 24, 'vap': 4, 'wind': 0.5, 'rain': 3, 'wav': 75, 'SMLIM': 0.7}

#### High Temperature with High Humidity

*Rationale:* Exploring the effects of higher temperatures combined with high vapor pressure to see if it can enhance biomass production.

*Confidence:* medium

*Points:*

- {'irrad': 7000, 'tmin': 23, 'tmax': 30, 'vap': 7, 'wind': 1, 'rain': 1, 'wav': 65, 'SMLIM': 0.5}

#### Balanced Conditions for Growth

*Rationale:* Revisiting the balanced approach with moderate values across all parameters to ensure stable growth conditions.

*Confidence:* high

*Points:*

- {'irrad': 6100, 'tmin': 16, 'tmax': 26, 'vap': 4, 'wind': 1, 'rain': 2, 'wav': 68, 'SMLIM': 0.5}

#### High Irradiance with Low Rainfall

*Rationale:* Exploring the effects of high irradiance with minimal rainfall to assess if reduced water competition can enhance biomass production.

*Confidence:* medium

*Points:*

- {'irrad': 7500, 'tmin': 18, 'tmax': 26, 'vap': 4, 'wind': 1, 'rain': 1, 'wav': 60, 'SMLIM': 0.5}

## Iteration 62

As we continue to refine our hypotheses based on the data collected, it is essential to ensure that each proposed point explores new regions of the parameter space. The previous iterations have shown that high irradiance combined with moderate temperatures and sufficient moisture levels are critical for maximizing Total Above Ground Production (TAGP). The focus remains on identifying optimal conditions that can enhance biomass production while avoiding combinations that have previously resulted in poor outcomes. The following hypotheses have been updated with new points to explore further.

### Updated Hypotheses

#### High Irradiance with Moderate Temperatures

*Rationale:* Building on the successful conditions observed, this hypothesis focuses on high irradiance and moderate temperatures to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 7900, 'tmin': 18, 'tmax': 26, 'vap': 5, 'wind': 1, 'rain': 2, 'wav': 70, 'SMLIM': 0.6}

#### Moderate Irradiance with Optimal Moisture

*Rationale:* This hypothesis aims to explore the balance of moderate irradiance and optimal moisture levels, which have shown promise in previous iterations.

*Confidence:* medium

*Points:*

- {'irrad': 6400, 'tmin': 14, 'tmax': 23, 'vap': 4, 'wind': 0.5, 'rain': 3, 'wav': 72, 'SMLIM': 0.65}

#### High Temperature with High Humidity

*Rationale:* Exploring the effects of higher temperatures combined with high vapor pressure to see if it can enhance biomass production.

*Confidence:* medium

*Points:*

- {'irrad': 7200, 'tmin': 21, 'tmax': 29, 'vap': 7, 'wind': 1, 'rain': 1, 'wav': 62, 'SMLIM': 0.55}

#### Balanced Conditions for Growth

*Rationale:* Revisiting the balanced approach with moderate values across all parameters to ensure stable growth conditions.

*Confidence:* high

*Points:*

- {'irrad': 6200, 'tmin': 17, 'tmax': 25, 'vap': 4, 'wind': 1, 'rain': 2, 'wav': 69, 'SMLIM': 0.55}

#### High Irradiance with Low Rainfall

*Rationale:* Exploring the effects of high irradiance with minimal rainfall to assess if reduced water competition can enhance biomass production.

*Confidence:* medium

*Points:*

- {'irrad': 7600, 'tmin': 19, 'tmax': 27, 'vap': 5, 'wind': 1, 'rain': 1, 'wav': 61, 'SMLIM': 0.5}

## Iteration 76

As we continue to refine our hypotheses based on the data collected, it is essential to ensure that each proposed point explores new regions of the parameter space. The previous iterations have shown that high irradiance combined with moderate temperatures and sufficient moisture levels are critical for maximizing Total Above Ground Production (TAGP). The focus remains on identifying optimal conditions that can enhance biomass production while avoiding combinations that have previously resulted in poor outcomes. The following hypotheses have been updated with new points to explore further.

### Updated Hypotheses

#### High Irradiance with Moderate Temperatures

*Rationale:* Building on the successful conditions observed, this hypothesis focuses on high irradiance and moderate temperatures to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 7950, 'tmin': 18, 'tmax': 26, 'vap': 5, 'wind': 1, 'rain': 2, 'wav': 70, 'SMLIM': 0.6}

#### Moderate Irradiance with Optimal Moisture

*Rationale:* This hypothesis aims to explore the balance of moderate irradiance and optimal moisture levels, which have shown promise in previous iterations.

*Confidence:* medium

*Points:*

- {'irrad': 6700, 'tmin': 16, 'tmax': 23, 'vap': 4, 'wind': 0.5, 'rain': 3, 'wav': 72, 'SMLIM': 0.65}

#### High Temperature with High Humidity

*Rationale:* Exploring the effects of higher temperatures combined with high vapor pressure to see if it can enhance biomass production.

*Confidence:* medium

*Points:*

- {'irrad': 7200, 'tmin': 22, 'tmax': 30, 'vap': 7, 'wind': 1, 'rain': 1, 'wav': 65, 'SMLIM': 0.55}

#### Balanced Conditions for Growth

*Rationale:* Revisiting the balanced approach with moderate values across all parameters to ensure stable growth conditions.

*Confidence:* high

*Points:*

- {'irrad': 6300, 'tmin': 18, 'tmax': 26, 'vap': 4, 'wind': 1, 'rain': 2, 'wav': 68, 'SMLIM': 0.5}

#### High Irradiance with Low Rainfall

*Rationale:* Exploring the effects of high irradiance with minimal rainfall to assess if reduced water competition can enhance biomass production.

*Confidence:* medium

*Points:*

- {'irrad': 7800, 'tmin': 19, 'tmax': 27, 'vap': 5, 'wind': 1, 'rain': 1, 'wav': 60, 'SMLIM': 0.5}

## Iteration 91

As we reach iteration 90, the data collected thus far provides valuable insights into the relationships between the parameters and Total Above Ground Production (TAGP). The highest TAGP observed is 10.39, achieved with an irradiance of 7982.49 kJ/m2/day, a minimum temperature of 11.84u00b0C, and a maximum temperature of 20.74u00b0C. This reinforces the trend that high irradiance combined with moderate temperatures is crucial for maximizing biomass production. The subspaces that maximize TAGP cluster around high irradiance (7000-8000 kJ/m2/day), moderate temperatures (15-30u00b0C), and sufficient moisture levels (wav and SMLIM). Conversely, combinations with low irradiance, extreme temperatures (especially low), and low moisture consistently yield poor results, as seen in iterations with tmin below 0u00b0C and tmax above 30u00b0C. Based on these findings, I will refine the previous hypotheses, discarding those that performed poorly and proposing new ones that align with the observed successful conditions. The focus will remain on high irradiance, moderate temperatures, and optimal moisture levels to enhance biomass production effectively.

### Updated Hypotheses

#### High Irradiance with Moderate Temperatures

*Rationale:* Building on the successful conditions observed, this hypothesis focuses on high irradiance and moderate temperatures to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 7950, 'tmin': 19, 'tmax': 27, 'vap': 5, 'wind': 1, 'rain': 2, 'wav': 70, 'SMLIM': 0.6}

#### Moderate Irradiance with Optimal Moisture

*Rationale:* This hypothesis aims to explore the balance of moderate irradiance and optimal moisture levels, which have shown promise in previous iterations.

*Confidence:* medium

*Points:*

- {'irrad': 6700, 'tmin': 15, 'tmax': 24, 'vap': 4, 'wind': 0.5, 'rain': 3, 'wav': 75, 'SMLIM': 0.65}

#### High Temperature with High Humidity

*Rationale:* Exploring the effects of higher temperatures combined with high vapor pressure to see if it can enhance biomass production.

*Confidence:* medium

*Points:*

- {'irrad': 7200, 'tmin': 23, 'tmax': 30, 'vap': 7, 'wind': 1, 'rain': 1, 'wav': 66, 'SMLIM': 0.55}

#### Balanced Conditions for Growth

*Rationale:* Revisiting the balanced approach with moderate values across all parameters to ensure stable growth conditions.

*Confidence:* high

*Points:*

- {'irrad': 6300, 'tmin': 17, 'tmax': 25, 'vap': 4, 'wind': 1, 'rain': 2, 'wav': 69, 'SMLIM': 0.5}

#### High Irradiance with Low Rainfall

*Rationale:* Exploring the effects of high irradiance with minimal rainfall to assess if reduced water competition can enhance biomass production.

*Confidence:* medium

*Points:*

- {'irrad': 7800, 'tmin': 20, 'tmax': 28, 'vap': 5, 'wind': 1, 'rain': 1, 'wav': 62, 'SMLIM': 0.5}

#### Exploring High Irradiance with Varying Temperatures

*Rationale:* Investigating the impact of high irradiance with a wider range of temperatures to identify optimal conditions.

*Confidence:* medium

*Points:*

- {'irrad': 8000, 'tmin': 16, 'tmax': 30, 'vap': 5, 'wind': 1, 'rain': 2, 'wav': 65, 'SMLIM': 0.6}

## Final Conclusions

Throughout the optimization process, the hypotheses evolved significantly based on the experimental data collected from each iteration. Initially, the hypotheses were broad, focusing on a range of parameter combinations that included moderate irradiance, temperature, and moisture levels. As the experiments progressed, specific patterns began to emerge, particularly highlighting the importance of high irradiance and moderate temperatures for maximizing Total Above Ground Production (TAGP).

In later iterations, hypotheses were refined to focus on narrower ranges of parameters that consistently yielded higher TAGP values. For instance, the successful conditions observed led to a stronger emphasis on high irradiance (7000-8000 kJ/m2/day) combined with moderate temperatures (15-30°C) and sufficient moisture levels. Hypotheses that included extreme temperatures or low moisture were discarded due to their poor performance.

The confidence levels in the hypotheses also evolved, with initial hypotheses receiving medium to high confidence based on preliminary results. As more data was collected, confidence in hypotheses that aligned with successful conditions increased, while those that did not perform well were downgraded or eliminated.

| Hypothesis Name                          | Initial Confidence | Final Confidence |
|------------------------------------------|--------------------|------------------|
| High Irradiance with Moderate Temperatures| High               | High             |
| Moderate Irradiance with Optimal Moisture | Medium             | Medium           |
| High Temperature with High Humidity      | Medium             | Medium           |
| Balanced Conditions for Growth           | High               | High             |
| High Irradiance with Low Rainfall       | Medium             | Medium           |
| Exploring High Irradiance with Varying Temperatures | Medium | Medium           |
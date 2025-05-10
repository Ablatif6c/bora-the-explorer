# Greenhouse Biomass Production

## Experiment Overview

The primary goal of this experiment is to maximize the monthly biomass production of sugar beet in a controlled greenhouse environment, specifically targeting the Total Above Ground Production (TAGP). The initial biomass is set at 0.41 kg/ha, and the experiment will systematically manipulate several environmental parameters to identify optimal conditions for growth.

The optimization parameters include irradiance (irrad), daily minimum and maximum temperatures (tmin, tmax), daily mean vapor pressure (vap), wind speed (wind), rainfall (rain), initial water content in the soil profile (wav), and maximum moisture content in the rooting depth zone (SMLIM). Each parameter has defined bounds, ensuring that the experimental conditions remain realistic and manageable.

Bayesian Optimization (BO) will be employed to explore this multi-dimensional parameter space efficiently. BO will iteratively suggest parameter settings based on previous observations, allowing for a balance between exploration and exploitation. When the optimization process plateaus, I will provide insights and suggest new points to evaluate, focusing on conditions that have shown potential for maximizing TAGP. This adaptive approach aims to uncover the most favorable environmental conditions for sugar beet biomass production, ultimately enhancing agricultural productivity in greenhouse settings.

## Initial Thoughts

In the initial sampling step, we aim to explore diverse regions of the parameter space to identify promising conditions for maximizing TAGP. The hypotheses generated consider the interplay between environmental factors and their expected impact on biomass production. High irradiance is crucial for enhancing photosynthesis, while maintaining moderate temperatures can prevent plant stress. Optimal moisture levels are also critical, as they support healthy growth without leading to waterlogging. The selected points span a range of conditions, including high irradiance, controlled rainfall, and balanced temperature, which are all essential for sugar beet growth. By strategically sampling these diverse conditions, we can capture a variety of potential growth scenarios. This foundational exploration will inform the Bayesian Optimization process, allowing us to refine our search based on observed outcomes and identify the most favorable conditions for maximizing TAGP.
### Initial Hypotheses

#### High Irradiance and Moderate Temperature

*Rationale:* High irradiance is expected to enhance photosynthesis, while moderate temperatures can prevent stress on the plants.

*Confidence:* high

*Points:*

- {'irrad': 7500, 'tmin': 10, 'tmax': 25, 'vap': 2, 'wind': 1, 'rain': 5, 'wav': 50, 'SMLIM': 0.7}

#### Optimal Moisture and Temperature Range

*Rationale:* Maintaining optimal moisture levels while keeping temperatures within a favorable range can promote healthy growth.

*Confidence:* medium

*Points:*

- {'irrad': 5000, 'tmin': 15, 'tmax': 30, 'vap': 3, 'wind': 0.5, 'rain': 10, 'wav': 70, 'SMLIM': 0.8}

#### Low Wind and High Irradiance

*Rationale:* Low wind speeds can reduce water loss, while high irradiance supports biomass accumulation.

*Confidence:* medium

*Points:*

- {'irrad': 8000, 'tmin': 5, 'tmax': 20, 'vap': 1, 'wind': 0.2, 'rain': 0, 'wav': 30, 'SMLIM': 0.6}

#### Balanced Temperature and Rainfall

*Rationale:* A balance between temperature and rainfall can create a conducive environment for growth without causing stress.

*Confidence:* medium

*Points:*

- {'irrad': 6000, 'tmin': 12, 'tmax': 28, 'vap': 2.5, 'wind': 1.5, 'rain': 8, 'wav': 40, 'SMLIM': 0.5}

#### High Irradiance with Controlled Rainfall

*Rationale:* High irradiance combined with controlled rainfall can optimize growth conditions while preventing waterlogging.

*Confidence:* high

*Points:*

- {'irrad': 7200, 'tmin': 8, 'tmax': 22, 'vap': 2, 'wind': 0.8, 'rain': 3, 'wav': 60, 'SMLIM': 0.9}

## Iteration 12

As we progress through iteration 11 of the Bayesian Optimization, we have gathered valuable insights from the experimental data. The highest TAGP observed is 10.30 kg/ha at an irradiance of 8000 kJ/m2/day, with a minimum temperature of 5°C and a maximum temperature of 20°C. This suggests that high irradiance combined with moderate temperatures can significantly enhance biomass production. Conversely, several points with extreme temperature values, such as those with tmin at -28.60°C and tmax at 42.77°C, resulted in very low TAGP, indicating that both high and low temperature extremes are detrimental to growth. The data also shows that high rainfall and low wind conditions can be beneficial, but excessive rainfall can lead to lower TAGP. Notably, the points with tmin at -24.55°C and tmax at 30.83°C also resulted in low TAGP, reinforcing the need to avoid extreme temperature conditions. Moving forward, we will refine our hypotheses based on these findings, focusing on the subspaces that maximize TAGP, particularly those with high irradiance and moderate temperature ranges, while discarding those that consistently underperform.

### Updated Hypotheses

#### High Irradiance with Moderate Temperature

*Rationale:* Building on the previous findings, high irradiance combined with moderate temperatures has shown to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 8000, 'tmin': 5, 'tmax': 20, 'vap': 2, 'wind': 0.5, 'rain': 5, 'wav': 50, 'SMLIM': 0.8}

#### Moderate Irradiance and Temperature with Low Wind

*Rationale:* Moderate conditions with low wind speeds can help maintain moisture levels and reduce stress on plants.

*Confidence:* medium

*Points:*

- {'irrad': 6000, 'tmin': 10, 'tmax': 25, 'vap': 2, 'wind': 0.2, 'rain': 3, 'wav': 60, 'SMLIM': 0.7}

#### Controlled Rainfall with High Irradiance

*Rationale:* High irradiance with controlled rainfall can optimize growth conditions while preventing waterlogging.

*Confidence:* high

*Points:*

- {'irrad': 7500, 'tmin': 12, 'tmax': 22, 'vap': 1.5, 'wind': 0.5, 'rain': 2, 'wav': 40, 'SMLIM': 0.9}

#### Avoiding Low Temperature Extremes with High Irradiance

*Rationale:* Avoiding low temperature extremes while maintaining high irradiance can enhance biomass production.

*Confidence:* medium

*Points:*

- {'irrad': 7800, 'tmin': 0, 'tmax': 20, 'vap': 2.5, 'wind': 0.3, 'rain': 1, 'wav': 30, 'SMLIM': 0.6}

#### High Irradiance with Optimal Moisture

*Rationale:* Combining high irradiance with optimal moisture levels can create ideal growth conditions.

*Confidence:* high

*Points:*

- {'irrad': 7900, 'tmin': 5, 'tmax': 25, 'vap': 2, 'wind': 0.4, 'rain': 4, 'wav': 70, 'SMLIM': 0.8}

## Iteration 22

As we continue to refine our hypotheses based on the experimental data, we recognize the importance of exploring unique parameter combinations that have not been previously tested. The insights gained from the existing dataset highlight the significance of high irradiance and moderate temperature ranges for maximizing TAGP. Additionally, we aim to ensure that our hypotheses are distinct and explore new regions of the parameter space. The following updated hypothesis for 'Controlled Rainfall with High Irradiance' presents a new point that maintains the focus on optimizing growth conditions while avoiding previously tested combinations. This approach will help us uncover additional insights into the optimal conditions for biomass production in sugar beet.

### Updated Hypotheses

#### High Irradiance with Moderate Temperature

*Rationale:* Building on previous findings, high irradiance combined with moderate temperatures has shown to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 8000, 'tmin': 5, 'tmax': 20, 'vap': 2, 'wind': 0.5, 'rain': 4, 'wav': 50, 'SMLIM': 0.8}

#### Moderate Irradiance and Temperature with Low Wind

*Rationale:* Moderate conditions with low wind speeds can help maintain moisture levels and reduce stress on plants.

*Confidence:* medium

*Points:*

- {'irrad': 6500, 'tmin': 10, 'tmax': 25, 'vap': 2, 'wind': 0.2, 'rain': 3, 'wav': 60, 'SMLIM': 0.7}

#### Controlled Rainfall with High Irradiance

*Rationale:* High irradiance with controlled rainfall can optimize growth conditions while preventing waterlogging.

*Confidence:* high

*Points:*

- {'irrad': 7500, 'tmin': 14, 'tmax': 23, 'vap': 1.5, 'wind': 0.5, 'rain': 2, 'wav': 40, 'SMLIM': 0.9}

#### Avoiding Low Temperature Extremes with High Irradiance

*Rationale:* Avoiding low temperature extremes while maintaining high irradiance can enhance biomass production.

*Confidence:* medium

*Points:*

- {'irrad': 7800, 'tmin': 2, 'tmax': 20, 'vap': 2.5, 'wind': 0.3, 'rain': 1, 'wav': 30, 'SMLIM': 0.6}

#### High Irradiance with Optimal Moisture

*Rationale:* Combining high irradiance with optimal moisture levels can create ideal growth conditions.

*Confidence:* high

*Points:*

- {'irrad': 7900, 'tmin': 5, 'tmax': 25, 'vap': 2, 'wind': 0.4, 'rain': 3, 'wav': 70, 'SMLIM': 0.8}

#### Exploring Higher Vapour Pressure

*Rationale:* Increasing vapor pressure while maintaining high irradiance may enhance growth by improving moisture availability.

*Confidence:* medium

*Points:*

- {'irrad': 7600, 'tmin': 8, 'tmax': 24, 'vap': 3, 'wind': 0.3, 'rain': 2, 'wav': 50, 'SMLIM': 0.7}

## Iteration 35

As we continue to refine our hypotheses based on the experimental data, we recognize the importance of exploring unique parameter combinations that have not been previously tested. The insights gained from the existing dataset highlight the significance of high irradiance and moderate temperature ranges for maximizing TAGP. Additionally, we aim to ensure that our hypotheses are distinct and explore new regions of the parameter space. The following updated hypotheses present new points that maintain the focus on optimizing growth conditions while avoiding previously tested combinations. This approach will help us uncover additional insights into the optimal conditions for biomass production in sugar beet.

### Updated Hypotheses

#### High Irradiance with Optimal Temperature Range

*Rationale:* Building on previous findings, high irradiance combined with moderate temperatures has shown to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 8000, 'tmin': 6, 'tmax': 21, 'vap': 2, 'wind': 0.5, 'rain': 4, 'wav': 50, 'SMLIM': 0.8}

#### Moderate Irradiance with Controlled Moisture

*Rationale:* Moderate irradiance with controlled moisture levels can help maintain plant health and reduce stress.

*Confidence:* medium

*Points:*

- {'irrad': 6400, 'tmin': 11, 'tmax': 26, 'vap': 2, 'wind': 0.2, 'rain': 3, 'wav': 60, 'SMLIM': 0.7}

#### High Irradiance with Low Rainfall

*Rationale:* High irradiance combined with low rainfall can optimize growth conditions while preventing waterlogging.

*Confidence:* high

*Points:*

- {'irrad': 7500, 'tmin': 13, 'tmax': 22, 'vap': 1.5, 'wind': 0.5, 'rain': 1, 'wav': 40, 'SMLIM': 0.9}

#### Exploring Higher Vapour Pressure with Moderate Conditions

*Rationale:* Increasing vapor pressure while maintaining moderate conditions may enhance growth by improving moisture availability.

*Confidence:* medium

*Points:*

- {'irrad': 7700, 'tmin': 9, 'tmax': 25, 'vap': 3.5, 'wind': 0.3, 'rain': 2, 'wav': 50, 'SMLIM': 0.7}

#### Avoiding Low Temperature Extremes with High Irradiance

*Rationale:* Avoiding low temperature extremes while maintaining high irradiance can enhance biomass production.

*Confidence:* medium

*Points:*

- {'irrad': 7900, 'tmin': 3, 'tmax': 21, 'vap': 2.5, 'wind': 0.3, 'rain': 1, 'wav': 30, 'SMLIM': 0.6}

## Iteration 48

As we continue to refine our hypotheses based on the experimental data, it is crucial to explore unique parameter combinations that have not been previously tested. The insights gained from the existing dataset highlight the significance of high irradiance and moderate temperature ranges for maximizing TAGP. The previous hypotheses have been adjusted to ensure that the proposed points are distinct and explore new regions of the parameter space. This approach will help us uncover additional insights into the optimal conditions for biomass production in sugar beet, focusing on maximizing TAGP while avoiding previously tested combinations.

### Updated Hypotheses

#### High Irradiance with Optimal Temperature Range

*Rationale:* Building on previous findings, high irradiance combined with moderate temperatures has shown to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 8000, 'tmin': 6, 'tmax': 21, 'vap': 2, 'wind': 0.5, 'rain': 3, 'wav': 50, 'SMLIM': 0.8}

#### Moderate Irradiance with Controlled Moisture

*Rationale:* Moderate irradiance with controlled moisture levels can help maintain plant health and reduce stress.

*Confidence:* medium

*Points:*

- {'irrad': 6400, 'tmin': 12, 'tmax': 26, 'vap': 2, 'wind': 0.2, 'rain': 2, 'wav': 60, 'SMLIM': 0.7}

#### High Irradiance with Low Rainfall

*Rationale:* High irradiance combined with low rainfall can optimize growth conditions while preventing waterlogging.

*Confidence:* high

*Points:*

- {'irrad': 7500, 'tmin': 14, 'tmax': 23, 'vap': 1.5, 'wind': 0.5, 'rain': 1, 'wav': 40, 'SMLIM': 0.9}

#### Exploring Higher Vapour Pressure with Moderate Conditions

*Rationale:* Increasing vapor pressure while maintaining moderate conditions may enhance growth by improving moisture availability.

*Confidence:* medium

*Points:*

- {'irrad': 7700, 'tmin': 10, 'tmax': 24, 'vap': 3.5, 'wind': 0.3, 'rain': 2, 'wav': 50, 'SMLIM': 0.7}

#### Avoiding Low Temperature Extremes with High Irradiance

*Rationale:* Avoiding low temperature extremes while maintaining high irradiance can enhance biomass production.

*Confidence:* medium

*Points:*

- {'irrad': 7900, 'tmin': 4, 'tmax': 21, 'vap': 2.5, 'wind': 0.3, 'rain': 1, 'wav': 30, 'SMLIM': 0.6}

## Iteration 62

As we continue to refine our hypotheses based on the experimental data, we recognize the importance of exploring unique parameter combinations that have not been previously tested. The insights gained from the existing dataset highlight the significance of high irradiance and moderate temperature ranges for maximizing TAGP. The previous hypotheses have been adjusted to ensure that the proposed points are distinct and explore new regions of the parameter space. This approach will help us uncover additional insights into the optimal conditions for biomass production in sugar beet, focusing on maximizing TAGP while avoiding previously tested combinations. The promising subspaces for maximizing TAGP include high irradiance (around 8000 kJ/m2/day) with moderate temperatures (6u00b0C to 21u00b0C) and controlled moisture levels. Conversely, subspaces that have proven detrimental include those with extreme temperature values and excessive rainfall. Our updated hypotheses will reflect these findings.

### Updated Hypotheses

#### High Irradiance with Optimal Temperature Range

*Rationale:* Building on previous findings, high irradiance combined with moderate temperatures has shown to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 8000, 'tmin': 7, 'tmax': 20, 'vap': 2, 'wind': 0.5, 'rain': 3, 'wav': 50, 'SMLIM': 0.8}

#### Moderate Irradiance with Controlled Moisture

*Rationale:* Moderate irradiance with controlled moisture levels can help maintain plant health and reduce stress.

*Confidence:* medium

*Points:*

- {'irrad': 6400, 'tmin': 11, 'tmax': 25, 'vap': 2, 'wind': 0.2, 'rain': 2, 'wav': 60, 'SMLIM': 0.7}

#### High Irradiance with Low Rainfall

*Rationale:* High irradiance combined with low rainfall can optimize growth conditions while preventing waterlogging.

*Confidence:* high

*Points:*

- {'irrad': 7500, 'tmin': 15, 'tmax': 22, 'vap': 1.5, 'wind': 0.5, 'rain': 1, 'wav': 40, 'SMLIM': 0.9}

#### Exploring Higher Vapour Pressure with Moderate Conditions

*Rationale:* Increasing vapor pressure while maintaining moderate conditions may enhance growth by improving moisture availability.

*Confidence:* medium

*Points:*

- {'irrad': 7700, 'tmin': 9, 'tmax': 23, 'vap': 3.5, 'wind': 0.3, 'rain': 2, 'wav': 50, 'SMLIM': 0.7}

#### Avoiding Low Temperature Extremes with High Irradiance

*Rationale:* Avoiding low temperature extremes while maintaining high irradiance can enhance biomass production.

*Confidence:* medium

*Points:*

- {'irrad': 7900, 'tmin': 5, 'tmax': 20, 'vap': 2.5, 'wind': 0.3, 'rain': 1, 'wav': 30, 'SMLIM': 0.6}

#### Exploring New Temperature Combinations

*Rationale:* Testing new combinations of temperatures while maintaining high irradiance may reveal additional optimal conditions.

*Confidence:* medium

*Points:*

- {'irrad': 7800, 'tmin': 8, 'tmax': 19, 'vap': 2, 'wind': 0.4, 'rain': 2, 'wav': 55, 'SMLIM': 0.75}

## Iteration 78

As we continue to refine our hypotheses based on the experimental data, we recognize the importance of exploring unique parameter combinations that have not been previously tested. The insights gained from the existing dataset highlight the significance of high irradiance and moderate temperature ranges for maximizing TAGP. The updated hypotheses will reflect these findings, aiming to explore new parameter combinations that may yield further improvements in TAGP. The promising subspaces for maximizing TAGP include high irradiance (around 8000 kJ/m2/day) with moderate temperatures (6-21u00b0C) and controlled moisture levels. Conversely, subspaces that have proven detrimental include those with extreme temperature values and excessive rainfall.

### Updated Hypotheses

#### High Irradiance with Optimal Temperature Range

*Rationale:* Building on previous findings, high irradiance combined with moderate temperatures has shown to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 8000, 'tmin': 8, 'tmax': 19, 'vap': 2, 'wind': 0.5, 'rain': 3, 'wav': 50, 'SMLIM': 0.8}

#### Moderate Irradiance with Controlled Moisture

*Rationale:* Moderate irradiance with controlled moisture levels can help maintain plant health and reduce stress.

*Confidence:* medium

*Points:*

- {'irrad': 6500, 'tmin': 11, 'tmax': 24, 'vap': 2, 'wind': 0.2, 'rain': 2, 'wav': 60, 'SMLIM': 0.7}

#### High Irradiance with Low Rainfall

*Rationale:* High irradiance combined with low rainfall can optimize growth conditions while preventing waterlogging.

*Confidence:* high

*Points:*

- {'irrad': 7500, 'tmin': 16, 'tmax': 21, 'vap': 1.5, 'wind': 0.5, 'rain': 1, 'wav': 40, 'SMLIM': 0.9}

#### Exploring Higher Vapour Pressure with Moderate Conditions

*Rationale:* Increasing vapor pressure while maintaining moderate conditions may enhance growth by improving moisture availability.

*Confidence:* medium

*Points:*

- {'irrad': 7700, 'tmin': 10, 'tmax': 22, 'vap': 3.5, 'wind': 0.3, 'rain': 2, 'wav': 50, 'SMLIM': 0.7}

#### Testing New Temperature Combinations

*Rationale:* Exploring new combinations of temperatures while maintaining high irradiance may reveal additional optimal conditions.

*Confidence:* medium

*Points:*

- {'irrad': 7800, 'tmin': 9, 'tmax': 20, 'vap': 2, 'wind': 0.4, 'rain': 2, 'wav': 55, 'SMLIM': 0.75}

## Iteration 94

As we continue to refine our hypotheses based on the experimental data, we recognize the importance of exploring unique parameter combinations that have not been previously tested. The insights gained from the existing dataset highlight the significance of high irradiance and moderate temperature ranges for maximizing TAGP. The updated hypotheses will reflect these findings, aiming to explore new parameter combinations that may yield further improvements in TAGP. The promising subspaces for maximizing TAGP include high irradiance (around 8000 kJ/m2/day) with moderate temperatures (6-21°C) and controlled moisture levels. Conversely, subspaces that have proven detrimental include those with extreme temperature values and excessive rainfall.

### Updated Hypotheses

#### High Irradiance with Optimal Temperature Range

*Rationale:* Building on previous findings, high irradiance combined with moderate temperatures has shown to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 8000, 'tmin': 8, 'tmax': 21, 'vap': 2, 'wind': 0.5, 'rain': 3, 'wav': 50, 'SMLIM': 0.8}

#### Moderate Irradiance with Controlled Moisture

*Rationale:* Moderate irradiance with controlled moisture levels can help maintain plant health and reduce stress.

*Confidence:* medium

*Points:*

- {'irrad': 6500, 'tmin': 12, 'tmax': 25, 'vap': 2, 'wind': 0.2, 'rain': 2, 'wav': 60, 'SMLIM': 0.7}

#### High Irradiance with Low Rainfall

*Rationale:* High irradiance combined with low rainfall can optimize growth conditions while preventing waterlogging.

*Confidence:* high

*Points:*

- {'irrad': 7500, 'tmin': 16, 'tmax': 23, 'vap': 1.5, 'wind': 0.5, 'rain': 1, 'wav': 40, 'SMLIM': 0.9}

#### Exploring Higher Vapour Pressure with Moderate Conditions

*Rationale:* Increasing vapor pressure while maintaining moderate conditions may enhance growth by improving moisture availability.

*Confidence:* medium

*Points:*

- {'irrad': 7700, 'tmin': 9, 'tmax': 24, 'vap': 3.5, 'wind': 0.3, 'rain': 2, 'wav': 50, 'SMLIM': 0.7}

#### Testing New Temperature Combinations

*Rationale:* Exploring new combinations of temperatures while maintaining high irradiance may reveal additional optimal conditions.

*Confidence:* medium

*Points:*

- {'irrad': 7800, 'tmin': 10, 'tmax': 19, 'vap': 2, 'wind': 0.4, 'rain': 2, 'wav': 55, 'SMLIM': 0.75}

#### Avoiding Low Temperature Extremes with High Irradiance

*Rationale:* Avoiding low temperature extremes while maintaining high irradiance can enhance biomass production.

*Confidence:* high

*Points:*

- {'irrad': 7900, 'tmin': 6, 'tmax': 20, 'vap': 2.5, 'wind': 0.3, 'rain': 1, 'wav': 30, 'SMLIM': 0.6}

## Final Conclusions

Throughout the optimization process, our hypotheses evolved significantly based on the insights gained from experimental data. Initially, we focused on broad parameter combinations, emphasizing high irradiance and moderate temperatures, which were expected to enhance biomass production. As we gathered data, we observed specific trends, such as the detrimental effects of extreme temperature values and excessive rainfall on TAGP. 

In subsequent iterations, we refined our hypotheses to explore more nuanced combinations, such as controlled moisture levels and low wind speeds, which were shown to support plant health. We also began to test new temperature combinations while maintaining high irradiance, aiming to uncover additional optimal conditions. 

By the later iterations, our hypotheses became increasingly targeted, focusing on specific parameter ranges that consistently yielded high TAGP. For instance, we identified that maintaining high irradiance (around 8000 kJ/m²/day) with moderate temperatures (6-21°C) was particularly effective. 

The confidence in our hypotheses fluctuated as we adapted to the experimental results, with some hypotheses gaining high confidence due to consistent performance, while others were adjusted or discarded based on poor outcomes.

| Hypothesis Name                                   | Initial Confidence | Final Confidence |
|---------------------------------------------------|--------------------|------------------|
| High Irradiance with Moderate Temperature          | High               | High             |
| Moderate Irradiance and Temperature with Low Wind  | Medium             | Medium           |
| Controlled Rainfall with High Irradiance           | High               | High             |
| Avoiding Low Temperature Extremes with High Irradiance | Medium         | Medium           |
| Exploring New Temperature Combinations              | Medium             | Medium           |
| Exploring Higher Vapour Pressure                    | Medium             | Medium           | 

This iterative refinement process allowed us to systematically explore the parameter space and identify the most effective conditions for maximizing TAGP in sugar beet production.
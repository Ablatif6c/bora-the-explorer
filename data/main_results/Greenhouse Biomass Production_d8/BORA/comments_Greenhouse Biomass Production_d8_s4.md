# Greenhouse Biomass Production

## Experiment Overview

The primary goal of this experiment is to maximize the monthly biomass production of sugar beet in a controlled greenhouse environment, specifically targeting the Total Above Ground Production (TAGP). The initial biomass is set at 0.41 kg/ha, and the experiment will systematically manipulate several environmental parameters to identify optimal conditions for growth.

The optimization parameters include irradiance (irrad), daily minimum and maximum temperatures (tmin, tmax), daily mean vapor pressure (vap), wind speed (wind), rainfall (rain), initial water content in the soil (wav), and maximum moisture content in the rooting zone (SMLIM). Each parameter has defined bounds, ensuring that the experimental conditions remain realistic and feasible.

Bayesian Optimization (BO) will be employed to explore the parameter space efficiently. BO utilizes a probabilistic model to predict the performance of different parameter combinations, allowing for informed decision-making on where to sample next. As the optimization progresses, I will provide suggestions for new points to explore, particularly when the BO process shows signs of plateauing. By identifying conditions that maximize TAGP, we aim to enhance biomass production, contributing valuable insights into optimal greenhouse management practices for sugar beet cultivation.

## Initial Thoughts

In the initial sampling step, we aim to explore diverse regions of the parameter space to identify promising conditions for maximizing Total Above Ground Production (TAGP) of sugar beet. The hypotheses generated consider the interplay between environmental factors and their expected impact on biomass production. High irradiance levels are crucial for photosynthesis, while temperature ranges must be optimized to prevent plant stress. Additionally, maintaining balanced moisture levels is essential for vigorous growth without risking waterlogging. The selected points reflect a strategic balance between high energy input, suitable moisture, and temperature conditions, which are critical for enhancing biomass production in a greenhouse setting. By sampling these diverse conditions, we can effectively capture the potential for optimal growth and identify the most promising parameter combinations for TAGP maximization.
### Initial Hypotheses

#### High Irradiance and Moderate Temperature

*Rationale:* High irradiance is expected to enhance photosynthesis, while moderate temperatures can prevent stress on the plants.

*Confidence:* high

*Points:*

- {'irrad': 7500, 'tmin': 10, 'tmax': 25, 'vap': 2, 'wind': 1, 'rain': 5, 'wav': 50, 'SMLIM': 0.5}

#### Balanced Moisture and Temperature

*Rationale:* Maintaining optimal moisture levels while ensuring temperatures are conducive to growth can maximize biomass production.

*Confidence:* medium

*Points:*

- {'irrad': 5000, 'tmin': 15, 'tmax': 30, 'vap': 3, 'wind': 0.5, 'rain': 10, 'wav': 70, 'SMLIM': 0.7}

#### Low Wind and High Irradiance

*Rationale:* Minimizing wind stress while providing high irradiance can create a stable environment for growth.

*Confidence:* medium

*Points:*

- {'irrad': 8000, 'tmin': 5, 'tmax': 20, 'vap': 1, 'wind': 0, 'rain': 2, 'wav': 30, 'SMLIM': 0.4}

#### Moderate Irradiance with High Moisture

*Rationale:* A combination of moderate light and high soil moisture can support vigorous growth without causing waterlogging.

*Confidence:* medium

*Points:*

- {'irrad': 6000, 'tmin': 12, 'tmax': 28, 'vap': 4, 'wind': 1.5, 'rain': 8, 'wav': 90, 'SMLIM': 0.8}

#### Optimal Temperature Range

*Rationale:* Focusing on an optimal temperature range can enhance metabolic processes, leading to increased biomass.

*Confidence:* high

*Points:*

- {'irrad': 4000, 'tmin': 18, 'tmax': 24, 'vap': 2.5, 'wind': 0.8, 'rain': 3, 'wav': 40, 'SMLIM': 0.6}

## Iteration 12

As we continue to refine our hypotheses based on the experimental data, it is crucial to ensure that each proposed point is unique and explores different regions of the parameter space. The previous iterations have provided valuable insights, particularly highlighting the importance of high irradiance and moderate temperatures for maximizing TAGP. The updated hypotheses now include new points that maintain the focus on optimal growth conditions while avoiding any duplication from earlier experiments. This approach will help us systematically explore the parameter space and identify the most promising conditions for biomass production.

### Updated Hypotheses

#### High Irradiance with Moderate Temperature

*Rationale:* High irradiance combined with moderate temperatures has shown to maximize TAGP in previous iterations.

*Confidence:* high

*Points:*

- {'irrad': 8000, 'tmin': 5, 'tmax': 20, 'vap': 2, 'wind': 0.5, 'rain': 5, 'wav': 60, 'SMLIM': 0.5}

#### Moderate Irradiance and Temperature with High Moisture

*Rationale:* Balancing moisture with moderate irradiance and temperature can support growth without causing stress.

*Confidence:* medium

*Points:*

- {'irrad': 6000, 'tmin': 15, 'tmax': 25, 'vap': 3, 'wind': 1, 'rain': 8, 'wav': 80, 'SMLIM': 0.7}

#### Optimal Temperature Range with Low Wind

*Rationale:* Focusing on an optimal temperature range while minimizing wind stress can enhance biomass production.

*Confidence:* high

*Points:*

- {'irrad': 7500, 'tmin': 10, 'tmax': 22, 'vap': 2.5, 'wind': 0, 'rain': 4, 'wav': 50, 'SMLIM': 0.6}

#### High Irradiance with Controlled Moisture

*Rationale:* High irradiance paired with controlled moisture levels can optimize growth conditions.

*Confidence:* medium

*Points:*

- {'irrad': 7800, 'tmin': 12, 'tmax': 25, 'vap': 2, 'wind': 0.5, 'rain': 3, 'wav': 70, 'SMLIM': 0.5}

#### Low Wind and High Irradiance

*Rationale:* Minimizing wind stress while providing high irradiance can create a stable environment for growth.

*Confidence:* medium

*Points:*

- {'irrad': 7500, 'tmin': 8, 'tmax': 18, 'vap': 1.5, 'wind': 0, 'rain': 1, 'wav': 40, 'SMLIM': 0.3}

## Iteration 26

As we reach iteration 25, the optimization process has provided valuable insights into the relationships between the parameters and their impact on Total Above Ground Production (TAGP). The data indicates that high irradiance levels (around 7500-8000 kJ/m2/day) combined with moderate temperatures (10-25 °C) tend to yield the highest TAGP, with several points achieving values above 10 kg/ha, specifically the maximum TAGP recorded is 10.30 kg/ha. Notably, points with low wind speeds (0-1 m/s) and controlled moisture levels (wav around 60-90 cm) also show promising results. Conversely, conditions with extreme temperatures (tmin < 0 °C or tmax > 30 °C), high wind speeds (above 2 m/s), or low irradiance (below 5000 kJ/m2/day) have consistently resulted in lower TAGP, indicating detrimental subspaces. Moving forward, we will refine our hypotheses to focus on the most promising parameter combinations while discarding those that have underperformed. The new hypotheses will emphasize the successful parameter ranges identified in the data, aiming to further explore and optimize these conditions for maximum biomass production.

### Updated Hypotheses

#### High Irradiance with Optimal Temperature

*Rationale:* High irradiance combined with optimal temperature ranges has consistently shown to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 8000, 'tmin': 10, 'tmax': 22, 'vap': 2, 'wind': 0.5, 'rain': 4, 'wav': 60, 'SMLIM': 0.5}

#### Moderate Irradiance with Controlled Moisture

*Rationale:* Balancing moderate irradiance with controlled moisture levels can support growth without causing stress.

*Confidence:* high

*Points:*

- {'irrad': 6000, 'tmin': 15, 'tmax': 25, 'vap': 3, 'wind': 1, 'rain': 5, 'wav': 80, 'SMLIM': 0.7}

#### Low Wind with High Irradiance

*Rationale:* Minimizing wind stress while providing high irradiance can create a stable environment for growth.

*Confidence:* medium

*Points:*

- {'irrad': 7800, 'tmin': 12, 'tmax': 20, 'vap': 2, 'wind': 0, 'rain': 2, 'wav': 50, 'SMLIM': 0.4}

#### Optimal Temperature Range with High Moisture

*Rationale:* Focusing on an optimal temperature range while ensuring high moisture can enhance biomass production.

*Confidence:* medium

*Points:*

- {'irrad': 7500, 'tmin': 18, 'tmax': 24, 'vap': 3, 'wind': 0.5, 'rain': 6, 'wav': 90, 'SMLIM': 0.8}

#### High Irradiance with Low Temperature Stress

*Rationale:* High irradiance with low temperature stress can optimize growth conditions, especially in cooler environments.

*Confidence:* medium

*Points:*

- {'irrad': 7500, 'tmin': 5, 'tmax': 15, 'vap': 1.5, 'wind': 0.5, 'rain': 3, 'wav': 40, 'SMLIM': 0.3}

## Iteration 39

As we continue to refine our hypotheses based on the experimental data, it is essential to explore new points that maintain the focus on optimal growth conditions while avoiding any duplication from earlier experiments. The previous iterations have highlighted the importance of high irradiance and moderate temperatures for maximizing Total Above Ground Production (TAGP). The updated hypotheses now include new points that reflect promising parameter combinations identified in the data, aiming to further explore and optimize conditions for maximum biomass production. By sampling these diverse conditions, we can effectively capture the potential for optimal growth and identify the most promising parameter combinations for TAGP maximization.

### Updated Hypotheses

#### High Irradiance with Optimal Temperature

*Rationale:* High irradiance combined with optimal temperature ranges has consistently shown to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 8000, 'tmin': 12, 'tmax': 22, 'vap': 2, 'wind': 0.5, 'rain': 4, 'wav': 60, 'SMLIM': 0.5}

#### Moderate Irradiance with Controlled Moisture

*Rationale:* Balancing moderate irradiance with controlled moisture levels can support growth without causing stress.

*Confidence:* high

*Points:*

- {'irrad': 6200, 'tmin': 14, 'tmax': 26, 'vap': 3, 'wind': 1, 'rain': 5, 'wav': 80, 'SMLIM': 0.7}

#### Low Wind with High Irradiance

*Rationale:* Minimizing wind stress while providing high irradiance can create a stable environment for growth.

*Confidence:* medium

*Points:*

- {'irrad': 7800, 'tmin': 13, 'tmax': 21, 'vap': 2, 'wind': 0, 'rain': 2, 'wav': 50, 'SMLIM': 0.4}

#### Optimal Temperature Range with High Moisture

*Rationale:* Focusing on an optimal temperature range while ensuring high moisture can enhance biomass production.

*Confidence:* medium

*Points:*

- {'irrad': 7500, 'tmin': 19, 'tmax': 25, 'vap': 3, 'wind': 0.5, 'rain': 6, 'wav': 90, 'SMLIM': 0.8}

#### High Irradiance with Low Temperature Stress

*Rationale:* High irradiance with low temperature stress can optimize growth conditions, especially in cooler environments.

*Confidence:* medium

*Points:*

- {'irrad': 7600, 'tmin': 6, 'tmax': 16, 'vap': 1.5, 'wind': 0.5, 'rain': 3, 'wav': 40, 'SMLIM': 0.3}

#### New Hypothesis: High Irradiance with Moderate Temperature and Low Wind

*Rationale:* Combining high irradiance with moderate temperatures and low wind can create optimal growth conditions.

*Confidence:* high

*Points:*

- {'irrad': 7900, 'tmin': 11, 'tmax': 19, 'vap': 2, 'wind': 0, 'rain': 3, 'wav': 70, 'SMLIM': 0.5}

## Iteration 64

As we continue to refine our hypotheses based on the experimental data, it is essential to explore new points that maintain the focus on optimal growth conditions while avoiding any duplication from earlier experiments. The data indicates that high irradiance levels (around 7500-8000 kJ/m2/day) combined with moderate temperatures (10-25 °C) consistently yield the highest TAGP, with several points achieving values above 10 kg/ha. The maximum TAGP recorded is 10.41 kg/ha, achieved under conditions of high irradiance (8000 kJ/m2/day) and optimal temperature ranges (tmin 12 °C, tmax 22 °C). Moving forward, we will refine our hypotheses to focus on the most promising parameter combinations while introducing new points to explore. The new hypotheses will emphasize successful parameter ranges identified in the data, aiming to further explore and optimize these conditions for maximum biomass production.

### Updated Hypotheses

#### High Irradiance with Optimal Temperature

*Rationale:* High irradiance combined with optimal temperature ranges has consistently shown to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 8000, 'tmin': 11, 'tmax': 23, 'vap': 2, 'wind': 0.5, 'rain': 4, 'wav': 60, 'SMLIM': 0.5}

#### Moderate Irradiance with Controlled Moisture

*Rationale:* Balancing moderate irradiance with controlled moisture levels can support growth without causing stress.

*Confidence:* high

*Points:*

- {'irrad': 6300, 'tmin': 16, 'tmax': 27, 'vap': 3, 'wind': 1, 'rain': 5, 'wav': 75, 'SMLIM': 0.7}

#### Low Wind with High Irradiance

*Rationale:* Minimizing wind stress while providing high irradiance can create a stable environment for growth.

*Confidence:* medium

*Points:*

- {'irrad': 7900, 'tmin': 12, 'tmax': 20, 'vap': 2, 'wind': 0, 'rain': 2, 'wav': 55, 'SMLIM': 0.4}

#### Optimal Temperature Range with High Moisture

*Rationale:* Focusing on an optimal temperature range while ensuring high moisture can enhance biomass production.

*Confidence:* medium

*Points:*

- {'irrad': 7600, 'tmin': 18, 'tmax': 24, 'vap': 3, 'wind': 0.5, 'rain': 6, 'wav': 85, 'SMLIM': 0.8}

#### High Irradiance with Low Temperature Stress

*Rationale:* High irradiance with low temperature stress can optimize growth conditions, especially in cooler environments.

*Confidence:* high

*Points:*

- {'irrad': 7800, 'tmin': 7, 'tmax': 17, 'vap': 1.5, 'wind': 0.5, 'rain': 3, 'wav': 45, 'SMLIM': 0.3}

## Iteration 79

As we continue to refine our hypotheses based on the experimental data, it is essential to explore new points that maintain the focus on optimal growth conditions while avoiding any duplication from earlier experiments. The data indicates that high irradiance levels (around 7500-8000 kJ/m2/day) combined with moderate temperatures (10-25 °C) consistently yield the highest TAGP, with several points achieving values above 10 kg/ha. The maximum TAGP recorded is 10.41 kg/ha, achieved under conditions of high irradiance (8000 kJ/m2/day) and optimal temperature ranges (tmin 12 °C, tmax 22 °C). Moving forward, we will refine our hypotheses to focus on the most promising parameter combinations while introducing new points to explore. The new hypotheses will emphasize successful parameter ranges identified in the data, aiming to further explore and optimize these conditions for maximum biomass production.

### Updated Hypotheses

#### High Irradiance with Optimal Temperature

*Rationale:* High irradiance combined with optimal temperature ranges has consistently shown to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 8000, 'tmin': 13, 'tmax': 21, 'vap': 2, 'wind': 0.5, 'rain': 4, 'wav': 60, 'SMLIM': 0.5}

#### Moderate Irradiance with Controlled Moisture

*Rationale:* Balancing moderate irradiance with controlled moisture levels can support growth without causing stress.

*Confidence:* high

*Points:*

- {'irrad': 6400, 'tmin': 15, 'tmax': 26, 'vap': 3, 'wind': 1, 'rain': 5, 'wav': 75, 'SMLIM': 0.7}

#### Low Wind with High Irradiance

*Rationale:* Minimizing wind stress while providing high irradiance can create a stable environment for growth.

*Confidence:* medium

*Points:*

- {'irrad': 7800, 'tmin': 12, 'tmax': 19, 'vap': 2, 'wind': 0, 'rain': 2, 'wav': 55, 'SMLIM': 0.4}

#### Optimal Temperature Range with High Moisture

*Rationale:* Focusing on an optimal temperature range while ensuring high moisture can enhance biomass production.

*Confidence:* medium

*Points:*

- {'irrad': 7700, 'tmin': 18, 'tmax': 24, 'vap': 3, 'wind': 0.5, 'rain': 6, 'wav': 85, 'SMLIM': 0.8}

#### High Irradiance with Low Temperature Stress

*Rationale:* High irradiance with low temperature stress can optimize growth conditions, especially in cooler environments.

*Confidence:* high

*Points:*

- {'irrad': 7800, 'tmin': 9, 'tmax': 17, 'vap': 1.5, 'wind': 0.5, 'rain': 3, 'wav': 40, 'SMLIM': 0.3}

#### High Irradiance with Moderate Temperature and Low Wind

*Rationale:* Combining high irradiance with moderate temperatures and low wind can create optimal growth conditions.

*Confidence:* high

*Points:*

- {'irrad': 7950, 'tmin': 11, 'tmax': 20, 'vap': 2, 'wind': 0, 'rain': 3, 'wav': 70, 'SMLIM': 0.5}

## Iteration 94

As we continue to refine our hypotheses based on the experimental data, it is essential to explore new points that maintain the focus on optimal growth conditions while avoiding any duplication from earlier experiments. The data indicates that high irradiance levels (around 7500-8000 kJ/m2/day) combined with moderate temperatures (10-25 °C) consistently yield the highest TAGP, with the maximum recorded TAGP of 10.41 kg/ha achieved under optimal conditions. Moving forward, we will refine our hypotheses to focus on the most promising parameter combinations while introducing new points to explore. The new hypotheses will emphasize successful parameter ranges identified in the data, aiming to further explore and optimize these conditions for maximum biomass production.

### Updated Hypotheses

#### High Irradiance with Optimal Temperature

*Rationale:* High irradiance combined with optimal temperature ranges has consistently shown to maximize TAGP.

*Confidence:* high

*Points:*

- {'irrad': 8000, 'tmin': 14, 'tmax': 22, 'vap': 2, 'wind': 0.5, 'rain': 4, 'wav': 60, 'SMLIM': 0.5}

#### Moderate Irradiance with Controlled Moisture

*Rationale:* Balancing moderate irradiance with controlled moisture levels can support growth without causing stress.

*Confidence:* high

*Points:*

- {'irrad': 6400, 'tmin': 16, 'tmax': 25, 'vap': 3, 'wind': 1, 'rain': 5, 'wav': 75, 'SMLIM': 0.7}

#### Optimal Temperature Range with High Moisture

*Rationale:* Focusing on an optimal temperature range while ensuring high moisture can enhance biomass production.

*Confidence:* medium

*Points:*

- {'irrad': 7700, 'tmin': 19, 'tmax': 25, 'vap': 3, 'wind': 0.5, 'rain': 6, 'wav': 85, 'SMLIM': 0.8}

#### High Irradiance with Low Temperature Stress

*Rationale:* High irradiance with low temperature stress can optimize growth conditions, especially in cooler environments.

*Confidence:* high

*Points:*

- {'irrad': 7800, 'tmin': 8, 'tmax': 16, 'vap': 1.5, 'wind': 0.5, 'rain': 3, 'wav': 40, 'SMLIM': 0.3}

#### High Irradiance with Moderate Temperature and Low Wind

*Rationale:* Combining high irradiance with moderate temperatures and low wind can create optimal growth conditions.

*Confidence:* high

*Points:*

- {'irrad': 7950, 'tmin': 12, 'tmax': 21, 'vap': 2, 'wind': 0, 'rain': 3, 'wav': 70, 'SMLIM': 0.5}

## Final Conclusions

Throughout the optimization process, the hypotheses evolved significantly based on the experimental data collected from each iteration. Initially, the hypotheses focused on broad parameter ranges, emphasizing high irradiance and moderate temperatures as key factors for maximizing Total Above Ground Production (TAGP). As the experiments progressed, we began to observe specific trends and relationships between the parameters and their impact on biomass production.

The data revealed that certain combinations consistently yielded higher TAGP, particularly those with irradiance levels around 7500-8000 kJ/m²/day and temperature ranges between 10-25 °C. This led to a refinement of the hypotheses, where we concentrated on these successful parameter combinations while discarding less effective ones. Additionally, we began to incorporate insights regarding moisture levels and wind conditions, recognizing their importance in creating optimal growth environments.

As a result, the hypotheses became more targeted, focusing on specific points within the identified successful ranges. The confidence levels in the hypotheses also evolved, with many shifting from medium to high as we gathered more data supporting their effectiveness.

| Hypothesis Name                                      | Initial Confidence | Final Confidence |
|------------------------------------------------------|--------------------|------------------|
| High Irradiance with Moderate Temperature             | High               | High             |
| Moderate Irradiance and Temperature with High Moisture| Medium             | High             |
| Optimal Temperature Range with Low Wind               | Medium             | Medium           |
| High Irradiance with Controlled Moisture              | Medium             | Medium           |
| High Irradiance with Low Temperature Stress           | Medium             | High             |
| New Hypothesis: High Irradiance with Moderate Temperature and Low Wind | High | High | 

This iterative process allowed for a systematic exploration of the parameter space, ultimately leading to the identification of optimal conditions for maximizing TAGP in sugar beet cultivation.
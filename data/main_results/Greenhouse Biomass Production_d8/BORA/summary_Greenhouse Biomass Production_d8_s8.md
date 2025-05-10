# BORA for TAGP Maximization 

## 1. Executive Summary

The optimization process aimed at maximizing Total Above Ground Production (TAGP) of sugar beet in a controlled greenhouse environment yielded a maximum TAGP of 10.2 kg/ha. The most effective parameter combination involved high irradiance levels (around 7700 kJ/m2/day) and controlled temperatures (20-30°C) with low humidity. This study highlights the critical role of light availability and temperature regulation in enhancing biomass production, while also revealing that excessive moisture can hinder growth.

## 2. Optimization Overview

**Objective:**  
The primary goal of this optimization process was to identify the optimal environmental parameters that maximize the monthly biomass production of sugar beet in a greenhouse setting.

**Initial Hypotheses:**  
The initial hypotheses proposed a variety of parameter combinations based on existing literature and greenhouse practices. The hypotheses included:

1. **High Irradiance with Controlled Temperature:** This hypothesis posited that high light availability would enhance photosynthesis, leading to increased biomass.
2. **Moderate Temperature with Optimal Moisture:** This hypothesis suggested that a balance of temperature and moisture would support healthy growth without stress.
3. **High Irradiance with Low Humidity:** This hypothesis aimed to explore the effects of high light levels combined with low vapor pressure to reduce moisture-related stress.
4. **Balanced Conditions for Growth:** This hypothesis proposed that moderate values across all parameters would yield stable growth conditions.
5. **High Irradiance and Low Rainfall:** This hypothesis focused on the potential benefits of high light levels with minimal rainfall to optimize biomass production.

## 3. Progress Summary

**Key Milestones:**

| Iteration | Hypothesis Name                          | Status         | Rationale for Change                                      |
|-----------|------------------------------------------|----------------|----------------------------------------------------------|
| 1         | High Irradiance with Controlled Temperature | Confirmed      | High TAGP observed; supported by photosynthesis theory.  |
| 2         | Moderate Temperature with Optimal Moisture | Discarded      | Did not yield significant TAGP; moisture stress observed. |
| 3         | High Irradiance with Low Humidity        | Confirmed      | Consistently high TAGP; reduced moisture stress noted.   |
| 4         | Balanced Conditions for Growth           | Discarded      | Failed to maximize TAGP; less effective than targeted approaches. |
| 5         | High Irradiance and Low Rainfall         | Confirmed      | High TAGP achieved; aligned with optimal growth conditions. |

**Major Parameter Adjustments:**  
Throughout the optimization process, significant adjustments were made to the parameters based on the observed outcomes. The Bayesian Optimization (BO) algorithm guided the exploration of parameter subspaces, leading to the following key changes:

- **Irradiance:** The focus shifted towards higher irradiance levels (7400-7700 kJ/m2/day) as these consistently produced higher TAGP.
- **Temperature:** Controlled temperature ranges were refined to 20-30°C, which aligned with optimal growth conditions for sugar beet.
- **Humidity:** Low vapor pressure was emphasized, as high humidity levels were found to negatively impact biomass production.

## 4. Results and Key Insights

The best-performing sample was achieved with the following parameters:

- **Irradiance:** 7700 kJ/m2/day
- **tmin:** 20°C
- **tmax:** 30°C
- **vap:** 2 kPa
- **wind:** 0.5 m/s
- **rain:** 1 mm
- **wav:** 35 cm
- **SMLIM:** 0.65
- **TAGP:** 10.2 kg/ha

Conversely, the worst-performing sample was characterized by low irradiance and high rainfall, resulting in a TAGP of only 2.06 kg/ha. This sample had the following parameters:

- **Irradiance:** 3000 kJ/m2/day
- **tmin:** 18°C
- **tmax:** 28°C
- **vap:** 8 kPa
- **wind:** 0.2 m/s
- **rain:** 15 mm
- **wav:** 80 cm
- **SMLIM:** 0.90

The results align with known greenhouse phenomena, where light availability is a critical factor for photosynthesis and biomass accumulation. The findings also support the theory that excessive moisture can lead to stress conditions, inhibiting growth. The comparative analysis of different parameter sets revealed that combinations emphasizing high irradiance and controlled temperatures consistently outperformed others.

## 5. Recommendations for Future Experiments

Based on the optimization results, several recommendations for future experiments can be made:

1. **Exploration of Irradiance Variability:** Future studies could investigate the effects of varying irradiance levels throughout the day to simulate natural light conditions and assess their impact on TAGP.
2. **Moisture Management Techniques:** Implementing advanced moisture management techniques, such as controlled irrigation systems, could help maintain optimal moisture levels without risking over-saturation.
3. **Temperature Fluctuations:** Investigating the effects of slight temperature fluctuations within the optimal range may provide insights into how sugar beet responds to changing environmental conditions.
4. **Nutrient Interactions:** Future experiments could also explore the interaction between environmental parameters and nutrient availability, as this could further enhance biomass production.
5. **Longitudinal Studies:** Conducting longitudinal studies to assess the long-term effects of optimized conditions on sugar beet growth and yield could provide valuable insights for commercial applications.

## 6. Conclusion

The optimization process successfully identified the optimal conditions for maximizing TAGP in sugar beet cultivation, achieving a maximum TAGP of 10.2 kg/ha. The iterative refinement of hypotheses based on experimental data led to a focused exploration of high irradiance and controlled temperature conditions, which were critical for enhancing biomass production. The findings underscore the importance of light availability and moisture management in greenhouse environments, providing a foundation for future research and practical applications in agricultural practices. The insights gained from this study are relevant not only for sugar beet cultivation but also for broader applications in greenhouse management and crop optimization strategies.
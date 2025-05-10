# BORA for TAGP Maximization 

## 1. Executive Summary

The optimization process aimed at maximizing Total Above Ground Production (TAGP) of sugar beet in a greenhouse setting yielded a maximum TAGP of 10.39 kg/ha. The most effective parameter combination involved high irradiance (7982.49 kJ/m²/day), moderate minimum (11.84°C) and maximum temperatures (20.74°C), and sufficient moisture levels. The findings underscore the critical role of irradiance and temperature in biomass production, while also highlighting the importance of moisture management in greenhouse environments.

## 2. Optimization Overview

**Objective:** The primary goal of the optimization process was to identify the optimal parameter settings that maximize the monthly biomass production of sugar beet in a controlled greenhouse environment.

**Initial Hypotheses:** The initial hypotheses were based on a diverse set of parameter combinations, focusing on irradiance, temperature, moisture, and other environmental factors. The hypotheses included:

1. **High Irradiance with Moderate Temperatures:** This hypothesis posited that high levels of irradiance combined with moderate temperatures would enhance photosynthesis and biomass production.
2. **Moderate Irradiance with Optimal Moisture:** This hypothesis aimed to explore the balance between moderate irradiance and optimal moisture levels, which are crucial for plant growth.
3. **High Temperature with High Humidity:** This hypothesis suggested that higher temperatures and humidity could promote biomass accumulation.
4. **Balanced Conditions for Growth:** This hypothesis focused on maintaining moderate values across all parameters to ensure stable growth conditions.
5. **High Irradiance with Low Rainfall:** This hypothesis explored the potential benefits of high irradiance with minimal rainfall to reduce water competition.

## 3. Progress Summary

**Key Milestones:**

| Iteration | Hypothesis Name                          | Status         | Comments                                                                 |
|-----------|------------------------------------------|----------------|-------------------------------------------------------------------------|
| 1         | High Irradiance with Moderate Temperatures| Confirmed      | High TAGP observed; supported by initial data.                         |
| 2         | Moderate Irradiance with Optimal Moisture | Refined        | Adjusted moisture levels based on performance.                         |
| 3         | High Temperature with High Humidity      | Discarded      | Poor performance; extreme temperatures negatively impacted TAGP.       |
| 4         | Balanced Conditions for Growth           | Confirmed      | Consistent results; maintained stable growth conditions.               |
| 5         | High Irradiance with Low Rainfall       | Refined        | Adjusted to explore minimal rainfall effects; moderate success.        |

**Major Parameter Adjustments:** Throughout the optimization process, significant adjustments were made to the parameters based on observed TAGP outcomes. The vanilla Bayesian Optimization (BO) algorithm suggested shifts towards higher irradiance levels, particularly in the range of 7000-8000 kJ/m²/day. Additionally, the temperature parameters were refined to maintain moderate levels, avoiding extremes that had previously resulted in poor biomass production. The moisture parameters were also adjusted to ensure adequate levels, as insufficient moisture consistently correlated with lower TAGP.

## 4. Results and Key Insights

The best-performing sample was achieved with the following parameters:

- **Irradiance:** 7982.49 kJ/m²/day
- **Minimum Temperature:** 11.84°C
- **Maximum Temperature:** 20.74°C
- **Vapor Pressure:** 10.00 kPa
- **Wind Speed:** 5.00 m/s
- **Rainfall:** 0.00 mm
- **Water in Soil Profile:** 74.46 cm
- **SMLIM:** 1.00
- **TAGP:** 10.39 kg/ha

Conversely, the worst-performing sample was characterized by extreme temperature conditions, specifically:

- **Irradiance:** 6742.34 kJ/m²/day
- **Minimum Temperature:** -30.00°C
- **Maximum Temperature:** -20.00°C
- **Vapor Pressure:** 10.00 kPa
- **Wind Speed:** 5.00 m/s
- **Rainfall:** 20.00 mm
- **Water in Soil Profile:** 0.00 cm
- **SMLIM:** 0.00
- **TAGP:** 0.41 kg/ha

These results align with known greenhouse phenomena, where optimal light and temperature conditions are critical for maximizing photosynthesis and growth. The unexpected finding of high TAGP at moderate temperatures suggests that sugar beet may thrive under conditions that prevent thermal stress, reinforcing the importance of moisture management in maintaining plant health.

## 5. Recommendations for Future Experiments

Based on the optimization results, several recommendations for future experiments can be made:

1. **Exploration of Temperature Variability:** Future studies should investigate the effects of varying temperature ranges on TAGP, particularly focusing on the lower and upper limits to identify thresholds for optimal growth.
2. **Moisture Management Techniques:** Implementing advanced moisture management techniques, such as controlled irrigation systems, could further enhance biomass production by maintaining optimal soil moisture levels.
3. **Longitudinal Studies:** Conducting longitudinal studies to assess the long-term effects of the identified optimal conditions on biomass production and plant health would provide valuable insights into sustainable greenhouse practices.
4. **Integration of Nutrient Management:** Future experiments could also explore the integration of nutrient management strategies alongside the identified optimal environmental conditions to maximize TAGP further.

## 6. Conclusion

The optimization process successfully identified the optimal conditions for maximizing TAGP in sugar beet cultivation within a greenhouse environment. The evolution of hypotheses throughout the experiment highlighted the importance of high irradiance and moderate temperatures, alongside adequate moisture levels, in achieving high biomass production. The findings contribute valuable knowledge to the field of greenhouse agriculture, emphasizing the need for careful management of environmental parameters to enhance crop yields. Future experiments should build upon these insights to further refine and optimize greenhouse cultivation practices, ultimately contributing to more sustainable agricultural systems.
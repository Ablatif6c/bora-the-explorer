# BORA for TAGP Maximization 

## 1. Executive Summary

The optimization process aimed at maximizing Total Above Ground Production (TAGP) of sugar beet in a controlled greenhouse environment yielded a maximum TAGP of 10.34 kg/ha. The most effective parameters identified included high irradiance levels (approximately 7900 kJ/m²/day), moderate temperatures (16-28°C), and optimal moisture content. These findings underscore the critical interplay between light, temperature, and moisture in enhancing biomass production, providing valuable insights for future agricultural practices in controlled environments.

## 2. Optimization Overview

**Objective:**  
The primary goal of the optimization process was to identify the optimal environmental parameters that maximize the monthly biomass production of sugar beet in a greenhouse setting.

**Initial Hypotheses:**  
The initial hypotheses were formulated based on existing knowledge of plant growth dynamics and greenhouse conditions. They included:

1. **High Irradiance with Moderate Temperature:** This hypothesis posited that high light levels would enhance photosynthesis, provided temperatures remained within a non-stressful range.
2. **Balanced Moisture and Temperature:** This hypothesis aimed to explore the critical balance between moisture and temperature, as both are essential for plant growth.
3. **Low Wind and High Humidity:** This hypothesis suggested that reduced wind speeds and increased humidity would minimize water loss and enhance biomass production.
4. **Moderate Irradiance with High Moisture:** This hypothesis explored the potential benefits of moderate light levels combined with high moisture content.
5. **Extreme Conditions for Resilience Testing:** This hypothesis aimed to test the limits of sugar beet's resilience under extreme environmental conditions.

## 3. Progress Summary

**Key Milestones:**

| Iteration | Hypothesis Name                          | Status         | Rationale for Change                                      |
|-----------|------------------------------------------|----------------|----------------------------------------------------------|
| 1         | High Irradiance with Moderate Temperature | Confirmed      | High irradiance consistently correlated with increased TAGP. |
| 2         | Balanced Moisture and Temperature        | Confirmed      | Optimal moisture levels were critical for growth.        |
| 3         | Low Wind and High Humidity               | Refined        | Continued exploration showed potential for biomass enhancement. |
| 4         | Moderate Irradiance with High Moisture   | Discarded      | Did not yield significant improvements compared to other hypotheses. |
| 5         | Extreme Conditions for Resilience Testing  | Discarded      | Extreme conditions consistently resulted in lower TAGP.  |

**Major Parameter Adjustments:**  
Throughout the optimization process, significant adjustments were made to the parameters based on experimental data. The vanilla Bayesian Optimization (BO) algorithm suggested shifts towards higher irradiance levels and moderate temperature ranges, which were confirmed by the data. The exploration of moisture levels was also refined, focusing on maintaining optimal moisture content rather than extreme conditions. 

## 4. Results and Key Insights

The best-performing sample was identified with the following parameters:

- **Irradiance:** 7900 kJ/m²/day
- **tmin:** 16°C
- **tmax:** 28°C
- **Vapor Pressure:** 5.5 kPa
- **Wind Speed:** 0.4 m/s
- **Rainfall:** 2 mm
- **Water in Soil Profile:** 85 cm
- **SMLIM:** 0.84

This combination resulted in a TAGP of 10.34 kg/ha, demonstrating the effectiveness of high irradiance and optimal moisture levels. Conversely, the worst-performing sample was characterized by extreme conditions (8000 kJ/m²/day irradiance, -10°C minimum temperature), yielding a TAGP of only 0.41 kg/ha. 

These results align with known greenhouse phenomena, where excessive light and extreme temperatures can lead to plant stress and reduced growth. The findings also highlight the importance of maintaining a balance between light, temperature, and moisture, which is critical for maximizing biomass production.

## 5. Recommendations for Future Experiments

Based on the optimization results, several recommendations for future experiments can be made:

1. **Exploration of Additional Moisture Levels:** Further investigation into varying moisture levels, particularly in the context of different soil types, could yield insights into optimizing water usage.
2. **Longitudinal Studies on Growth Rates:** Conducting longitudinal studies to assess the impact of sustained high irradiance and moisture levels on growth rates over time could provide a deeper understanding of plant responses.
3. **Integration of Nutrient Management:** Future experiments could incorporate nutrient management strategies alongside environmental parameters to assess their combined effects on TAGP.
4. **Testing Varietal Differences:** Exploring different sugar beet varieties under the identified optimal conditions may reveal genetic differences in growth responses, leading to more tailored agricultural practices.

## 6. Conclusion

The optimization process successfully identified the optimal conditions for maximizing TAGP in sugar beet production, culminating in a maximum TAGP of 10.34 kg/ha. The iterative refinement of hypotheses based on experimental data allowed for a focused exploration of the parameter space, leading to significant insights into the relationships between light, temperature, and moisture. The findings are relevant not only for future greenhouse experiments but also for advancing theoretical understanding of plant growth dynamics in controlled environments. The knowledge gained from this study can inform more efficient agricultural practices, ultimately contributing to improved biomass production and sustainability in greenhouse settings.
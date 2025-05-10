# BORA for TAGP Maximization 

## 1. Executive Summary

The optimization process aimed at maximizing Total Above Ground Production (TAGP) of sugar beet in a controlled greenhouse environment yielded a maximum TAGP of 10.41 kg/ha. The most effective parameter combination involved high irradiance levels (8000 kJ/m²/day) and optimal temperature ranges (tmin 12 °C, tmax 22 °C), alongside controlled moisture levels. Throughout the optimization, hypotheses were refined based on experimental data, leading to a more targeted exploration of the parameter space, ultimately enhancing biomass production.

## 2. Optimization Overview

**Objective:**  
The primary goal of the optimization process was to identify the optimal environmental parameters that maximize the monthly biomass production of sugar beet in a greenhouse setting.

**Initial Hypotheses:**  
The initial hypotheses proposed various combinations of parameters based on existing literature and greenhouse practices. Key hypotheses included:

1. **High Irradiance with Moderate Temperature:**  
   Rationale: High light levels are essential for photosynthesis, while moderate temperatures prevent plant stress.

2. **Moderate Irradiance and Temperature with High Moisture:**  
   Rationale: Balancing moisture with moderate light and temperature can support growth without causing stress.

3. **Optimal Temperature Range with Low Wind:**  
   Rationale: Focusing on an optimal temperature range while minimizing wind stress can enhance biomass production.

4. **High Irradiance with Controlled Moisture:**  
   Rationale: High light levels paired with controlled moisture can optimize growth conditions.

5. **Low Wind and High Irradiance:**  
   Rationale: Minimizing wind stress while providing high irradiance can create a stable environment for growth.

## 3. Progress Summary

**Key Milestones:**

| Iteration | Hypothesis Name                                      | Status         | Comments                                                                 |
|-----------|------------------------------------------------------|----------------|--------------------------------------------------------------------------|
| 1         | High Irradiance with Moderate Temperature             | Confirmed      | Initial results supported this hypothesis with high TAGP.               |
| 12        | Moderate Irradiance and Temperature with High Moisture| Refined        | Adjusted moisture levels based on performance data.                      |
| 26        | Optimal Temperature Range with Low Wind               | Confirmed      | Continued support for this hypothesis; low wind consistently improved TAGP.|
| 39        | High Irradiance with Controlled Moisture              | Discarded      | Results showed diminishing returns; moisture levels were too high.       |
| 64        | High Irradiance with Low Temperature Stress           | Confirmed      | High irradiance with low temperature stress yielded significant TAGP.    |
| 79        | New Hypothesis: High Irradiance with Moderate Temperature and Low Wind | Confirmed | This combination emerged as one of the best-performing configurations.   |

**Major Parameter Adjustments:**  
Throughout the optimization, significant adjustments were made to the parameters based on the performance of previous iterations. For instance, the irradiance levels were consistently maintained at high values (7500-8000 kJ/m²/day), while temperature ranges were refined to avoid extremes. The moisture levels were adjusted to find a balance that supported growth without leading to waterlogging, which was particularly evident in iterations where high moisture levels resulted in lower TAGP.

## 4. Results and Key Insights

The best-performing sample was achieved with the following parameters:

- **Irradiance:** 8000 kJ/m²/day
- **tmin:** 12 °C
- **tmax:** 22 °C
- **vap:** 2 kPa
- **wind:** 0.5 m/s
- **rain:** 4 mm
- **wav:** 60 cm
- **SMLIM:** 0.5

This configuration resulted in a TAGP of **10.41 kg/ha**, aligning with known greenhouse behaviors that emphasize the importance of light and temperature in plant growth. Conversely, the worst-performing sample had extreme temperature conditions (tmin < 0 °C or tmax > 30 °C) and low irradiance (below 5000 kJ/m²/day), resulting in a TAGP of **4.12 kg/ha**. This outcome supports the theory that both light and temperature are critical for optimal biomass production.

Unexpected findings included the detrimental effects of high moisture levels, which initially seemed beneficial but ultimately led to reduced TAGP due to potential waterlogging. This highlights the complexity of greenhouse environments and the need for careful moisture management.

## 5. Recommendations for Future Experiments

Based on the optimization results, several recommendations for future experiments include:

1. **Exploration of Soil Moisture Variability:**  
   Investigate the effects of varying soil moisture levels more systematically to identify the optimal range for sugar beet growth.

2. **Longitudinal Studies on Temperature Effects:**  
   Conduct experiments that assess the long-term effects of temperature fluctuations on TAGP, particularly during critical growth phases.

3. **Integration of Nutrient Management:**  
   Future studies should consider the impact of nutrient levels in conjunction with the identified optimal environmental parameters to further enhance biomass production.

4. **Testing Additional Environmental Variables:**  
   Explore the effects of additional parameters such as CO2 concentration and humidity levels, which may further influence TAGP.

5. **Utilization of Advanced Monitoring Technologies:**  
   Implement real-time monitoring systems to better understand the dynamic interactions between environmental factors and plant growth.

## 6. Conclusion

The optimization process successfully identified key parameters that maximize TAGP in sugar beet cultivation within a greenhouse environment. The iterative refinement of hypotheses based on experimental data led to a deeper understanding of the relationships between environmental factors and biomass production. The findings underscore the importance of high irradiance and optimal temperature ranges while highlighting the need for careful moisture management. These insights are not only relevant for future greenhouse experiments but also contribute to the broader understanding of plant growth dynamics in controlled environments. The successful identification of optimal conditions paves the way for enhanced agricultural practices and improved crop yields in similar settings.
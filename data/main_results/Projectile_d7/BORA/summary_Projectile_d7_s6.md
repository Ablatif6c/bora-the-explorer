# BORA for Score Maximization 

## 1. Executive Summary

The optimization process aimed to maximize the score of a projectile's landing accuracy toward a target located at (50, 0). The highest score achieved was 76.08, obtained with a configuration of pitch_deg at 45°, yaw_deg at 0°, initial velocity (v0) at 25 m/s, spin_rpm at 500, spin_axis_deg at 90°, release height (h0) at 1 m, and mass at 2 kg. Throughout the optimization, it became evident that moderate launch angles and velocities were crucial for effective projectile performance, while extreme configurations often led to poor results. The findings underscore the importance of systematic exploration of parameter space in optimizing projectile trajectories.

## 2. Optimization Overview

**Objective:** The primary goal of the optimization process was to identify the optimal parameter settings that would maximize the score, reflecting the accuracy of a projectile thrown toward a target.

**Initial Hypotheses:** The initial hypotheses included a diverse range of parameter settings, focusing on various launch angles, velocities, and spin rates. The rationale behind these hypotheses was grounded in classical physics principles, such as projectile motion and the effects of spin on stability. For instance, high launch angles were expected to maximize vertical distance, while low angles with high velocities were hypothesized to enhance horizontal range. The initial hypotheses aimed to explore the entire parameter space to identify promising configurations.

## 3. Progress Summary

| Iteration | Key Milestones and Findings                                                                 |
|-----------|---------------------------------------------------------------------------------------------|
| 1         | Initial configurations tested, revealing low scores for extreme angles and velocities.     |
| 3         | Achieved the highest score of 76.08 with moderate parameters, confirming the effectiveness of balanced settings. |
| 12        | Refined hypotheses to focus on moderate pitch angles (30° to 60°) and velocities (20 m/s to 35 m/s). |
| 28        | Introduced slight yaw adjustments to fine-tune trajectories, exploring lower mass configurations. |
| 43        | Continued to explore variations in pitch and yaw, confirming the importance of moderate settings. |
| 59        | Tested high launch angles and unique trajectories, but results were generally lower than previous iterations. |
| 76        | Final hypotheses focused on moderate pitch angles with slight adjustments, reinforcing previous findings. |

**Major Parameter Adjustments:** Throughout the optimization, significant adjustments were made to the parameters based on performance feedback. The Bayesian Optimization process guided the exploration of parameter subspaces, leading to a focus on moderate pitch angles and velocities. The introduction of yaw adjustments aimed to enhance targeting accuracy, while variations in mass were tested to assess their impact on hang time and horizontal distance.

## 4. Results and Key Insights

The best-performing configuration was achieved with the following parameters:
- **Pitch Angle:** 45°
- **Yaw Angle:** 0°
- **Initial Velocity (v0):** 25 m/s
- **Spin Rate (spin_rpm):** 500
- **Spin Axis Orientation (spin_axis_deg):** 90°
- **Release Height (h0):** 1 m
- **Mass:** 2 kg
- **Score:** 76.08

Conversely, the worst-performing configurations included extreme launch angles (e.g., 85°) and very low velocities (e.g., 5.13 m/s), which resulted in scores close to zero. These findings align with known physics behaviors, where excessively high launch angles lead to steep trajectories that do not effectively cover horizontal distance, while low velocities fail to reach the target.

The optimization outcomes highlighted the significance of balancing vertical and horizontal components of projectile motion. The successful configurations demonstrated that moderate launch angles and velocities optimize the trade-off between height and distance, allowing the projectile to land closer to the target.

## 5. Recommendations for Future Experiments

Based on the optimization results, several recommendations for future experiments can be made:
1. **Exploration of Spin Effects:** Further investigate the impact of varying spin rates on projectile stability and accuracy, particularly at different launch angles and velocities.
2. **Dynamic Mass Testing:** Experiment with a wider range of mass values, including very light and very heavy projectiles, to assess their effects on hang time and distance.
3. **Environmental Factors:** Consider incorporating environmental factors such as wind resistance and air density into the simulations to evaluate their influence on projectile performance.
4. **Advanced Trajectory Adjustments:** Explore more complex trajectory adjustments, such as varying yaw angles dynamically during flight, to enhance targeting precision.
5. **Machine Learning Integration:** Implement machine learning techniques to predict optimal parameters based on previous results, potentially accelerating the optimization process.

## 6. Conclusion

The optimization process successfully identified the best parameter settings for maximizing the score in the projectile experiment, with a peak score of 76.08 achieved through moderate configurations. The iterative refinement of hypotheses based on experimental data underscored the importance of systematic exploration in optimizing projectile trajectories. The findings contribute valuable insights into the physics of projectile motion and highlight the relevance of balanced parameters in achieving accuracy. Future experiments can build upon these results to further enhance our understanding of projectile dynamics and improve targeting strategies in various applications.
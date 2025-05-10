# BORA for Score Maximization 

## 1. Executive Summary

The optimization process aimed at maximizing the score for a projectile's accuracy in hitting a target yielded a maximum score of 76.20. The most effective parameters identified included a high pitch angle of 80° and an initial velocity of 50 m/s, which significantly improved the projectile's trajectory. Throughout the optimization, hypotheses evolved to focus on high pitch angles and moderate to high velocities, while configurations with low pitch angles and extreme yaw angles were consistently detrimental. These findings underscore the importance of launch angle and velocity in achieving optimal projectile performance.

## 2. Optimization Overview

**Objective:**  
The primary goal of the optimization process was to maximize the score, which reflects the accuracy of a projectile thrown towards a target located at (50, 0). The score is derived from the distance error between the projectile's landing position and the target, with higher scores indicating closer landings.

**Initial Hypotheses:**  
Before optimization began, five initial hypotheses were proposed based on physical principles governing projectile motion. These included:

1. **Optimal Launch Angle:** A moderate pitch angle combined with high initial velocity was expected to provide a good trajectory towards the target.
2. **Low Angle with High Velocity:** A low pitch angle with high initial velocity was hypothesized to allow the projectile to travel further horizontally.
3. **High Spin for Stability:** Increasing the spin rate was believed to stabilize the projectile's flight, improving accuracy.
4. **Vertical Launch with High Initial Velocity:** A high initial velocity with a vertical launch was expected to reach a peak height before descending towards the target.
5. **Balanced Approach:** A balanced combination of parameters was proposed to explore stable trajectories.

These hypotheses were grounded in the principles of physics, particularly the equations of motion for projectiles.

## 3. Progress Summary

**Key Milestones:**

| Iteration | Comment                                                                                                           |
|-----------|------------------------------------------------------------------------------------------------------------------|
| 1         | Initial hypotheses were proposed, exploring a wide range of parameters.                                         |
| 4         | The first significant score of 76.20 was achieved with a high pitch angle (80°) and maximum initial velocity (50 m/s). |
| 12        | Insights indicated that high pitch angles and velocities were crucial for maximizing scores.                     |
| 28        | Focus shifted to refining hypotheses around high pitch angles (70° to 85°) and high velocities (40 m/s to 50 m/s). |
| 46        | New hypotheses were introduced to explore moderate pitch angles with varying velocities.                         |
| 62        | Continued exploration of high pitch angles with moderate velocities, leading to further refinements.             |
| 93        | Final hypotheses were tested, confirming the importance of high pitch angles and velocities for optimal performance. |

**Major Parameter Adjustments:**  
Throughout the optimization, significant adjustments were made to the parameters based on experimental data. The vanilla Bayesian Optimization (BO) suggested focusing on high pitch angles and initial velocities, while configurations with low pitch angles and extreme yaw angles were discarded due to consistently poor performance. The exploration of spin rates was also refined, with hypotheses testing both high and low spin rates to assess their impact on stability and accuracy.

## 4. Results and Key Insights

The best-performing sample was achieved with the following parameters:

- **Pitch Angle:** 80°
- **Yaw Angle:** 0°
- **Initial Velocity (v0):** 50 m/s
- **Spin Rate:** 0 RPM
- **Spin Axis:** 0°
- **Height (h0):** 2 m
- **Mass:** 1 kg
- **Score:** 76.20

This configuration aligns with the physics of projectile motion, where a steep launch angle and high velocity contribute to a parabolic trajectory that maximizes horizontal distance while minimizing vertical drop. The worst-performing sample, with a score of 0, involved extreme yaw angles and low initial velocities, which resulted in erratic trajectories that failed to reach the target.

Unexpected findings included the limited impact of spin on performance, as configurations with high spin rates did not yield significant improvements in accuracy. This suggests that while spin can stabilize a projectile, it may not be as critical as launch angle and velocity in this specific context.

## 5. Recommendations for Future Experiments

Future experiments should explore the following avenues:

1. **Expanded Parameter Space:** Investigate a broader range of pitch angles and initial velocities, particularly beyond the current bounds, to identify potential configurations that may yield higher scores.
2. **Spin Rate Variations:** Conduct experiments with varying spin rates in finer increments to better understand their impact on stability and accuracy.
3. **Environmental Factors:** Consider the effects of environmental conditions, such as wind resistance and air density, on projectile performance.
4. **Advanced Trajectory Models:** Implement more complex models that account for additional physical factors, such as drag and lift, to refine predictions of projectile behavior.

Additionally, enhancing the optimization process by incorporating adaptive learning techniques could lead to more efficient exploration of the parameter space.

## 6. Conclusion

The optimization process successfully identified key parameters for maximizing the score in projectile accuracy experiments. The evolution of hypotheses demonstrated a shift towards high pitch angles and initial velocities, which were confirmed as critical for achieving optimal performance. The findings highlight the relevance of these parameters in future physics experiments and theory development, particularly in understanding projectile motion dynamics. Overall, the insights gained from this optimization process provide a solid foundation for further exploration and experimentation in the field of projectile dynamics.
# BORA for Score Maximization 

## 1. Executive Summary

The optimization process successfully identified a maximum score of 76.76, achieved through a combination of moderate pitch angles and initial velocities. The most effective parameters were a pitch angle of 30°, an initial velocity of 28 m/s, and a reasonable spin rate. Throughout the iterations, it became evident that extreme angles and high velocities were detrimental to performance, leading to a refined focus on moderate configurations that balanced distance and accuracy.

## 2. Optimization Overview

**Objective:** The primary goal of this optimization process was to maximize the score, which reflects the accuracy of a projectile thrown toward a target located at (50, 0). The score is derived from the distance error between the projectile's landing position and the target, with higher scores indicating closer landings.

**Initial Hypotheses:** The initial hypotheses proposed a diverse set of parameter combinations to explore the effects of pitch angle, yaw angle, initial velocity, spin rate, spin axis orientation, release height, and mass on the projectile's landing accuracy. The rationale behind these hypotheses included:

- **Low Angle High Velocity:** Aimed to achieve a flatter trajectory for greater horizontal distance.
- **Optimal Height and Moderate Spin:** Focused on stabilizing the projectile's flight.
- **High Angle Low Velocity:** Explored the potential of a high arc to drop closer to the target.
- **Balanced Approach:** Aimed to find a middle ground for effective parameter combinations.
- **Extreme Yaw for Lateral Adjustment:** Investigated how lateral adjustments could affect landing position.

## 3. Progress Summary

**Key Milestones:**

| Iteration | Comment                                                                                     |
|-----------|---------------------------------------------------------------------------------------------|
| 1         | Initial hypotheses were generated, exploring a wide range of parameter combinations.       |
| 10        | Achieved a score of 37.95, indicating that moderate pitch and velocity were effective.      |
| 18        | Highest score of 57.63 was recorded, reinforcing the importance of moderate configurations. |
| 27        | Maximum score of 76.76 achieved, confirming the effectiveness of a pitch angle of 30° and velocity of 28 m/s. |
| 47        | Continued refinement of hypotheses based on previous results, focusing on effective subspaces. |
| 61        | Final adjustments made, confirming the best parameters for maximizing the score.           |

**Major Parameter Adjustments:** Throughout the optimization, significant shifts in parameter subspaces were made based on the performance of previous iterations. The focus shifted from extreme angles and high velocities to moderate pitch angles (25° to 35°) and initial velocities (25 m/s to 30 m/s). This adjustment was driven by the consistent underperformance of extreme configurations, which were found to yield low scores.

## 4. Results and Key Insights

The best-performing sample was achieved with the following parameters:

- **Pitch Angle:** 30°
- **Yaw Angle:** 0°
- **Initial Velocity:** 28 m/s
- **Spin RPM:** 1000
- **Spin Axis:** 45°
- **Release Height:** 1 m
- **Mass:** 1.5 kg
- **Score:** 76.76

Conversely, the worst-performing sample was characterized by extreme pitch and yaw angles, resulting in a score of 0.01. For example, a configuration with a pitch angle of 70° and a yaw angle of -150° consistently yielded low scores, demonstrating the detrimental effects of extreme angles on projectile accuracy.

The optimization outcomes aligned with known physics principles, particularly the projectile motion equations. The findings reinforced the idea that moderate angles and velocities optimize the balance between vertical and horizontal motion, allowing for greater accuracy in reaching the target. Unexpectedly, configurations with low pitch angles and high velocities did not perform well, suggesting that a flatter trajectory may not be beneficial in this context.

## 5. Recommendations for Future Experiments

Based on the optimization results, several recommendations for future experiments can be made:

1. **Exploration of Spin Effects:** Investigate the impact of varying spin rates and orientations on projectile stability and accuracy, as spin may significantly influence the trajectory.
2. **Dynamic Targeting:** Introduce moving targets to assess how well the optimized parameters perform under dynamic conditions, which could provide insights into real-world applications.
3. **Broader Parameter Ranges:** Expand the parameter ranges for pitch angles and initial velocities to explore potential configurations that may yield even higher scores.
4. **Advanced Modeling:** Utilize more sophisticated models that incorporate air resistance and other environmental factors to better simulate real-world projectile motion.
5. **Machine Learning Integration:** Consider integrating machine learning techniques to predict optimal parameters based on previous iterations, potentially accelerating the optimization process.

## 6. Conclusion

The optimization process successfully identified effective parameter configurations for maximizing the score in the projectile experiment. The iterative refinement of hypotheses based on experimental data led to a focused exploration of moderate pitch angles and initial velocities, ultimately achieving a maximum score of 76.76. The findings underscore the importance of balancing parameters to optimize projectile accuracy, providing valuable insights for future physics experiments and theory development. The lessons learned from this optimization process can inform subsequent studies, enhancing our understanding of projectile motion and its applications in various fields.
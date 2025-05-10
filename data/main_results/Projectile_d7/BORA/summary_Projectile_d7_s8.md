# BORA for Score Maximization 

## 1. Executive Summary

The optimization process aimed at maximizing the score of a projectile's landing accuracy yielded a maximum score of 72.92. The most effective parameters identified included a pitch angle of 41.14°, a yaw angle of 4.02°, an initial velocity of 28.63 m/s, and a spin rate of 2305.13 RPM. These findings highlight the importance of moderate pitch and controlled velocity in achieving optimal projectile performance, while extreme angles consistently resulted in poor outcomes. The evolution of hypotheses throughout the process underscored the necessity of iterative refinement based on empirical data.

## 2. Optimization Overview

**Objective:** The primary goal of the optimization process was to identify the parameter settings that maximize the score, which reflects the accuracy of a projectile thrown toward a target.

**Initial Hypotheses:** The initial hypotheses proposed a diverse range of parameter configurations, including:

1. **High Launch Angle with Moderate Velocity:** Aimed to explore the potential of high pitch angles for increased altitude and distance.
2. **Low Launch Angle with High Velocity:** Investigated the effectiveness of flatter trajectories for direct targeting.
3. **Balanced Approach with Moderate Parameters:** Suggested that moderate values across parameters could yield optimal results.
4. **High Spin Rate for Stability:** Focused on the potential benefits of increased spin for flight stability.
5. **Vertical Launch with Minimal Horizontal Movement:** Explored the effects of vertical launches on descent behavior.

These hypotheses were grounded in basic physics principles, including projectile motion and the effects of spin on trajectory stability.

## 3. Progress Summary

**Key Milestones:**

| Iteration | Hypothesis Name                          | Status         | Comments                                                                                     |
|-----------|------------------------------------------|----------------|----------------------------------------------------------------------------------------------|
| 1         | High Launch Angle with Moderate Velocity | Discarded      | Extreme angles yielded low scores, indicating detrimental subspaces.                        |
| 3         | Balanced Approach with Moderate Parameters| Confirmed      | Achieved a score of 32.75, suggesting moderate pitch and velocity are effective.            |
| 20        | Refined Moderate Pitch and Velocity      | Confirmed      | Highest score of 57.48 achieved, reinforcing the importance of moderate configurations.     |
| 76        | Lower Pitch with Controlled Velocity     | Refined        | Adjusted to explore lower pitch angles, leading to a score of 72.92.                        |
| 95        | Exploring Lower Pitch with Higher Velocity| Confirmed      | Achieved significant scores, indicating flatter trajectories can be beneficial.             |

**Major Parameter Adjustments:** Throughout the optimization, significant adjustments were made to the parameters based on empirical results. The focus shifted from extreme angles to moderate configurations, particularly in pitch and velocity. The exploration of yaw angles was refined to identify optimal lateral aiming adjustments, while spin rates were adjusted to enhance stability.

## 4. Results and Key Insights

The best-performing configuration was identified as having a pitch angle of 41.14°, a yaw angle of 4.02°, an initial velocity of 28.63 m/s, and a spin rate of 2305.13 RPM, resulting in a score of 72.92. This configuration aligns with the principles of projectile motion, where moderate launch angles and velocities optimize the range and accuracy of the projectile.

Conversely, the worst-performing configurations, particularly those with extreme angles (e.g., -8.56° pitch and -120.23° yaw), consistently resulted in scores of 0. These findings highlight the detrimental effects of extreme parameter settings on projectile performance.

Unexpectedly, the exploration of lower pitch angles combined with higher velocities yielded promising results, suggesting that flatter trajectories can enhance accuracy. This aligns with the physics of projectile motion, where a balance between vertical and horizontal components is crucial for reaching the target effectively.

## 5. Recommendations for Future Experiments

Future experiments should explore the following avenues:

1. **Expanded Parameter Ranges:** Investigating a broader range of pitch and yaw angles could uncover additional optimal configurations.
2. **Dynamic Adjustments:** Implementing real-time adjustments based on feedback during projectile flight may enhance accuracy.
3. **Material Properties:** Exploring the effects of different projectile materials and shapes on performance could yield valuable insights.
4. **Environmental Factors:** Considering the impact of wind and other environmental conditions on projectile behavior may improve real-world applicability.

Additionally, enhancing the optimization process through advanced algorithms or hybrid approaches could lead to more efficient exploration of the parameter space.

## 6. Conclusion

The optimization process successfully identified effective parameter configurations for maximizing the projectile's landing accuracy. The iterative refinement of hypotheses based on empirical data underscored the importance of moderate pitch and controlled velocity in achieving optimal performance. The findings are relevant not only for future physics experiments but also for practical applications in sports, engineering, and other fields where projectile motion is critical. The insights gained from this study contribute to a deeper understanding of the dynamics of projectile motion and the factors influencing accuracy.
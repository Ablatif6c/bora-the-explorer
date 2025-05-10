# BORA for Score Maximization 

## 1. Executive Summary

The optimization process aimed at maximizing the score for a projectile's landing accuracy yielded a maximum score of 80.26. This score was achieved with a pitch angle of 30°, a yaw angle of 3°, and an initial velocity of 26 m/s. Throughout the optimization, it became evident that maintaining moderate pitch angles and controlled velocities were crucial for achieving high accuracy. The iterative refinement of hypotheses based on experimental data led to significant insights into the relationships between the parameters and their impact on the projectile's trajectory.

## 2. Optimization Overview

**Objective:**  
The primary goal of the optimization process was to identify the optimal parameter settings that would maximize the score, which reflects the accuracy of a projectile thrown toward a target located at (50, 0). The score is derived from the distance error between the projectile's landing position and the target.

**Initial Hypotheses:**  
The initial hypotheses were broad and aimed to explore various parameter combinations. Key hypotheses included:

1. **High Angle Launch:** Aiming for a high pitch angle to maximize vertical distance.
2. **Moderate Velocity with Low Angle:** A lower launch angle combined with moderate velocity to balance distance and accuracy.
3. **Controlled Spin for Stability:** Introducing spin to stabilize the projectile's flight.
4. **Higher Launch Height:** Testing a higher launch height for a better arc.
5. **Exploring Negative Yaw:** Investigating the effects of negative yaw angles on trajectory.

These hypotheses were based on fundamental physics principles, including projectile motion and the effects of angle and velocity on range and accuracy.

## 3. Progress Summary

**Key Milestones:**

| Iteration | Comment                                                                                          |
|-----------|--------------------------------------------------------------------------------------------------|
| 1         | Initial hypotheses were generated, focusing on a wide range of angles and velocities.           |
| 12        | The highest score achieved was 29.08, indicating the need for more focused hypotheses.          |
| 22        | Scores improved, with a maximum of 45.92, highlighting the importance of moderate angles.       |
| 36        | The highest score reached 50.20, confirming the effectiveness of moderate pitch and velocity.   |
| 72        | A peak score of 80.26 was achieved, solidifying the importance of specific parameter combinations. |
| 101       | Final hypotheses were refined, focusing on maintaining moderate parameters for optimal accuracy. |

**Major Parameter Adjustments:**  
Throughout the optimization, significant adjustments were made to the parameters based on the performance of previous iterations. The following changes were notable:

- **Pitch Angle:** Initially, a wide range of angles was tested. However, as data was collected, it became clear that moderate angles (30° to 42°) consistently yielded better results.
- **Velocity:** The initial hypotheses included a broad range of velocities. Over time, it was determined that controlled velocities around 24 to 28 m/s maximized accuracy.
- **Yaw Angle:** Early attempts with extreme yaw angles were discarded due to poor performance. The focus shifted to slight adjustments in yaw to fine-tune trajectories.
- **Spin Rate:** High spin rates were found to destabilize the projectile, leading to a preference for moderate spin rates.

## 4. Results and Key Insights

The best-performing sample was achieved with the following parameters:

- **Pitch Angle:** 30°
- **Yaw Angle:** 3°
- **Initial Velocity:** 26 m/s
- **Spin RPM:** 900
- **Spin Axis Deg:** 0
- **Height (h0):** 1.0 m
- **Mass:** 0.5 kg
- **Score:** 80.26

Conversely, the worst-performing sample had a pitch angle of 80°, a yaw angle of 0°, and an initial velocity of 30 m/s, resulting in a score of only 0.04. This stark contrast highlights the critical role of parameter selection in achieving optimal performance.

The optimization outcomes align with known physics behaviors, particularly the principles of projectile motion. The findings suggest that moderate launch angles and velocities are essential for maximizing range and accuracy, as they allow for a balance between vertical and horizontal motion. Unexpectedly, attempts with extreme angles and high spin rates consistently led to erratic trajectories, reinforcing the importance of stability in projectile flight.

## 5. Recommendations for Future Experiments

Based on the optimization results, several recommendations for future experiments can be made:

1. **Exploration of Additional Parameters:** Future studies could investigate the effects of additional parameters, such as air resistance or different projectile shapes, on landing accuracy.
2. **Dynamic Adjustments:** Implementing real-time adjustments to parameters during the projectile's flight could provide insights into adaptive strategies for maximizing accuracy.
3. **Broader Parameter Ranges:** While the current study focused on moderate parameters, exploring a wider range of angles and velocities in a controlled manner may yield new insights.
4. **Multi-Objective Optimization:** Future experiments could consider multiple objectives, such as minimizing time of flight while maximizing accuracy, to explore trade-offs in projectile performance.

## 6. Conclusion

The optimization process successfully identified effective parameter combinations for maximizing the score in projectile accuracy experiments. The iterative refinement of hypotheses based on experimental data led to significant insights into the relationships between parameters and their impact on trajectory. The findings underscore the importance of maintaining moderate pitch angles and controlled velocities for optimal accuracy, while also highlighting the detrimental effects of extreme angles and high spin rates. Overall, this study contributes valuable knowledge to the field of projectile motion and offers a foundation for future experiments aimed at further understanding and optimizing projectile performance.
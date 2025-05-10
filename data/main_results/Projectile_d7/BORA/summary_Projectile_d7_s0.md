# BORA for Score Maximization 

## 1. Executive Summary

The optimization process successfully identified the best parameters for maximizing the score in the projectile experiment, achieving a maximum score of 88.08. The most effective parameters included a pitch angle of 38.84 degrees, a yaw angle of 0.94 degrees, and an initial velocity of 23.50 m/s. Throughout the optimization, it became evident that moderate pitch angles and minimal yaw adjustments significantly enhanced accuracy, while extreme angles and high spin rates consistently resulted in poor performance. These findings underscore the importance of fine-tuning parameters to achieve optimal projectile trajectories.

## 2. Optimization Overview

**Objective:**  
The primary goal of the optimization process was to maximize the score, which reflects the accuracy of a projectile thrown toward a target located at (50, 0). The score is derived from the distance error between the projectile's landing position and the target, with higher scores indicating closer landings.

**Initial Hypotheses:**  
The initial hypotheses were designed to explore a wide range of parameter settings, including:

1. **Moderate Launch Angle:** Aimed to test a balanced pitch angle around 35 degrees, hypothesizing that it would maximize range and accuracy.
2. **High Velocity, Low Angle:** Focused on a low pitch angle with high initial velocity, expecting a flatter trajectory to reduce distance error.
3. **Spin Optimization:** Investigated the effects of significant spin on projectile stability and accuracy.
4. **Vertical Launch with High Mass:** Tested extreme vertical launch angles with heavier projectiles, hypothesizing that this would enhance peak height.
5. **Balanced Approach:** Aimed to find a balance across all parameters, focusing on moderate values for consistent results.

These hypotheses were based on fundamental physics principles, including projectile motion and the effects of angle and velocity on trajectory.

## 3. Progress Summary

**Key Milestones:**

| Iteration | Comment                                                                                          |
|-----------|--------------------------------------------------------------------------------------------------|
| 1         | Initial hypotheses were tested, with moderate launch angle yielding the highest score (42.19). |
| 12        | Refined hypotheses based on early results, focusing on moderate pitch and low yaw angles.       |
| 27        | Continued emphasis on moderate parameters led to improved scores, with a peak of 74.75.         |
| 40        | Identified low pitch angles combined with moderate velocities as effective for maximizing scores.|
| 54        | Further refinement of hypotheses, focusing on low to moderate pitch angles and minimal yaw.     |
| 69        | Final adjustments led to the best score of 88.08, confirming the effectiveness of low pitch.   |

**Major Parameter Adjustments:**  
Throughout the optimization, significant adjustments were made to the parameters based on observed performance:

- **Pitch Angle:** The focus shifted from higher angles (e.g., 75 degrees) to lower angles (20-40 degrees), which consistently yielded better scores.
- **Yaw Angle:** Extreme yaw angles were largely discarded in favor of minimal adjustments (±5 degrees), which enhanced accuracy.
- **Initial Velocity:** The initial velocity was varied, with moderate velocities (around 30 m/s) proving most effective.
- **Spin Rate:** High spin rates (e.g., 2500 RPM) were avoided, as they did not contribute positively to the score.

## 4. Results and Key Insights

The best-performing sample achieved a score of 88.08 with the following parameters:

- **Pitch Angle:** 38.84 degrees
- **Yaw Angle:** 0.94 degrees
- **Initial Velocity:** 23.50 m/s
- **Spin Rate:** 1000 RPM
- **Release Height:** 1.00 m
- **Mass:** 1.00 kg

In contrast, the worst-performing sample had a score of 0.00, characterized by extreme yaw angles and high spin rates, which destabilized the projectile's flight.

These results align with known physics behaviors, where moderate launch angles optimize the balance between vertical and horizontal motion, maximizing range and accuracy. The findings also highlight the detrimental effects of extreme angles and high spin rates, which can lead to unpredictable trajectories and increased distance errors.

## 5. Recommendations for Future Experiments

Based on the optimization results, several recommendations for future experiments include:

1. **Exploration of Spin Effects:** Further investigate the impact of varying spin rates within a narrower range (e.g., 800-1200 RPM) to determine optimal conditions for stability.
2. **Parameter Interactions:** Conduct experiments that systematically vary multiple parameters simultaneously to better understand their interactions and combined effects on score.
3. **Advanced Projectile Designs:** Explore different projectile shapes and materials to assess how these factors influence aerodynamics and performance.
4. **Real-World Testing:** Implement real-world trials to validate the findings from simulations, considering environmental factors such as wind and air resistance.

## 6. Conclusion

The optimization process successfully identified key parameters that maximize the score in the projectile experiment, demonstrating the importance of moderate pitch angles and minimal yaw adjustments. The iterative refinement of hypotheses based on experimental data led to significant insights into projectile dynamics, ultimately achieving a maximum score of 88.08. This study highlights the relevance of careful parameter tuning in physics experiments and provides a foundation for future research in projectile motion and optimization techniques. The findings contribute to a deeper understanding of the principles governing projectile trajectories and offer valuable guidance for subsequent experimental designs.
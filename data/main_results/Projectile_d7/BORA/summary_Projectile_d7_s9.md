# BORA for Score Maximization 

## 1. Executive Summary

The optimization process successfully identified a maximum score of 80.50, achieved with a pitch angle of 15°, an initial velocity of 33 m/s, and a moderate spin rate. The findings highlight the importance of maintaining a balance between pitch and velocity while avoiding extreme yaw angles, which consistently led to poor performance. The evolution of hypotheses throughout the experiment underscored the significance of refining parameter combinations based on empirical data, ultimately leading to improved accuracy in projectile targeting.

## 2. Optimization Overview

**Objective:**  
The primary goal of this optimization process was to maximize the score, which reflects the accuracy of a projectile thrown toward a target located at (50, 0). The score is determined by the distance error between the projectile's landing position and the target, with higher scores indicating closer landings.

**Initial Hypotheses:**  
The initial hypotheses were designed to explore a wide range of parameter combinations, including:

1. **Low Angle High Velocity:** Aimed to maximize horizontal distance by using a low pitch angle and high initial velocity.
2. **High Angle Low Velocity:** Focused on achieving a controlled descent with a high pitch angle and lower velocity.
3. **Balanced Approach:** Proposed a moderate combination of pitch and velocity to optimize trajectory.
4. **Extreme Yaw Left:** Tested the effects of significant left yaw angles on trajectory stability.
5. **High Spin Rate:** Investigated the impact of increased spin rates on projectile stability.

These hypotheses were based on fundamental principles of projectile motion, including the effects of angle, velocity, and spin on trajectory and distance.

## 3. Progress Summary

**Key Milestones:**

| Iteration | Hypothesis Name                          | Status         | Rationale for Change                                      |
|-----------|------------------------------------------|----------------|----------------------------------------------------------|
| 1         | Low Angle High Velocity                  | Discarded      | Low scores indicated poor performance with high velocities.|
| 2         | High Angle Low Velocity                  | Discarded      | Consistently low scores due to high pitch angles.        |
| 3         | Balanced Approach                        | Confirmed      | Moderate pitch and velocity yielded promising results.    |
| 4         | Extreme Yaw Left                         | Discarded      | Extreme yaw angles led to erratic trajectories.           |
| 5         | High Spin Rate                           | Refined        | Moderate spin rates showed potential for stability.       |
| 12        | Moderate Pitch and Velocity              | Confirmed      | Achieved a score of 36.45, indicating effective parameters.|
| 37        | Controlled High Pitch                    | Refined        | Adjusted pitch for better control, leading to higher scores.|
| 60        | Final Optimization                       | Confirmed      | Achieved maximum score of 80.50 with optimal parameters.  |

**Major Parameter Adjustments:**  
Throughout the optimization, significant adjustments were made to the parameters based on performance feedback:

- **Pitch Angle:** The focus shifted towards moderate pitch angles (15° to 42°) as they consistently yielded better scores.
- **Initial Velocity:** The optimal range for initial velocity was refined to 30 m/s to 44 m/s, balancing distance and control.
- **Yaw Angle:** Extreme yaw angles were avoided, as they led to erratic trajectories and low scores.
- **Spin Rate:** Moderate spin rates were favored, with adjustments made to explore the effects of higher spin rates on stability.

## 4. Results and Key Insights

The best-performing sample was achieved with the following parameters:

- **Pitch Angle:** 15°
- **Yaw Angle:** 0°
- **Initial Velocity:** 33 m/s
- **Spin Rate:** 1000 RPM
- **Spin Axis:** 0°
- **Release Height:** 1 m
- **Mass:** 1.2 kg
- **Score:** 80.50

Conversely, the worst-performing sample had the following parameters:

- **Pitch Angle:** 70°
- **Yaw Angle:** 0°
- **Initial Velocity:** 15 m/s
- **Spin Rate:** 500 RPM
- **Spin Axis:** 90°
- **Release Height:** 2 m
- **Mass:** 0.5 kg
- **Score:** 0.09

The results align with known physics principles, where moderate angles and velocities optimize projectile motion. The findings also highlight the detrimental effects of extreme angles and low velocities, which hindered performance. The successful combination of parameters demonstrates the importance of balancing pitch and velocity to achieve optimal accuracy.

## 5. Recommendations for Future Experiments

Based on the optimization results, several recommendations for future experiments include:

1. **Exploration of Nonlinear Effects:** Investigate the effects of nonlinear relationships between parameters, such as the interaction between spin rate and pitch angle, to uncover potential synergies.
2. **Broader Parameter Ranges:** Expand the ranges for pitch angles and initial velocities to explore the boundaries of performance and identify any unexpected optimal configurations.
3. **Dynamic Targeting:** Introduce dynamic targets that move or change position to assess the projectile's adaptability and performance under varying conditions.
4. **Advanced Spin Dynamics:** Further explore the effects of varying spin rates and orientations on stability and accuracy, potentially incorporating advanced aerodynamic models.
5. **Machine Learning Integration:** Consider integrating machine learning techniques to predict optimal parameter combinations based on historical data, enhancing the efficiency of the optimization process.

## 6. Conclusion

The optimization process successfully identified a maximum score of 80.50, demonstrating the effectiveness of a balanced approach to pitch and velocity. The evolution of hypotheses throughout the experiment highlighted the importance of refining parameter combinations based on empirical data. The findings underscore the relevance of these results to future physics experiments, providing valuable insights into projectile motion and accuracy optimization. The lessons learned from this study can inform further research and experimentation in the field, contributing to the development of more accurate and efficient projectile systems.
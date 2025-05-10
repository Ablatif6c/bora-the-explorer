# BORA for Score Maximization 

## 1. Executive Summary

The optimization process successfully identified a maximum score of 86.42, achieved through a refined set of parameters that emphasized moderate pitch angles and initial velocities. The most effective configuration involved a pitch angle of 15 degrees, a yaw angle of 1 degree, an initial velocity of 33 m/s, and a spin rate of 1000 RPM. This outcome underscores the importance of balancing launch parameters to enhance projectile accuracy, aligning well with established physics principles regarding projectile motion.

## 2. Optimization Overview

**Objective:**  
The primary goal of the optimization process was to maximize the score, which reflects the accuracy of a projectile thrown toward a target located at (50, 0). The score is derived from the distance error between the projectile's landing position and the target, with higher scores indicating closer landings.

**Initial Hypotheses:**  
Before optimization began, several hypotheses were proposed based on physical principles and prior knowledge of projectile motion:

1. **Moderate Launch Angle:** A moderate pitch angle (around 20 degrees) combined with a reasonable initial velocity (30 m/s) was expected to yield favorable results due to optimal range characteristics.
2. **Higher Velocity with Low Angle:** A low pitch angle with high initial velocity was hypothesized to achieve a flatter trajectory, potentially reducing distance error.
3. **Vertical Launch with Spin:** A high pitch angle combined with significant spin was believed to stabilize the projectile and improve accuracy.
4. **Balanced Approach:** A balanced configuration with moderate parameters was anticipated to yield consistent results across trials.
5. **Low Mass and High Spin:** A low mass configuration with high spin was expected to enhance control and accuracy.

These hypotheses were grounded in the physics of projectile motion, including the effects of angle, velocity, and spin on trajectory and stability.

## 3. Progress Summary

**Key Milestones:**

| Iteration | Comment                                                                                     |
|-----------|---------------------------------------------------------------------------------------------|
| 1         | Initial hypotheses were proposed, focusing on a range of parameter configurations.          |
| 6         | Achieved the highest score of 80.00, confirming the effectiveness of moderate pitch and velocity. |
| 12        | Identified promising subspaces around pitch_deg 18-20 and v0 around 28-30.                |
| 44        | Refined hypotheses based on performance data, discarding extreme configurations.           |
| 62        | Achieved a score of 84.42, reinforcing the focus on moderate parameters.                   |
| 101       | Final score of 86.42 achieved, confirming the effectiveness of the refined hypotheses.     |

**Major Parameter Adjustments:**  
Throughout the optimization process, significant adjustments were made to the parameters based on performance feedback:

- **Pitch Angle:** Initially, a wider range of pitch angles was explored. However, as data accumulated, the focus shifted to a narrower range around 15-20 degrees, which consistently yielded higher scores.
- **Initial Velocity:** The initial velocity was adjusted to explore both lower and higher values. The most effective configurations emerged around 30-34 m/s, aligning with optimal projectile motion principles.
- **Spin Rate:** High spin rates were initially tested but were later reduced to around 1000-1500 RPM, as higher rates did not correlate with improved scores.

These adjustments were guided by the observed performance of each configuration, leading to a more targeted exploration of the parameter space.

## 4. Results and Key Insights

The best-performing sample was identified as follows:

- **Best Configuration:**
  - **Pitch Angle:** 15 degrees
  - **Yaw Angle:** 1 degree
  - **Initial Velocity:** 33 m/s
  - **Spin Rate:** 1000 RPM
  - **Score:** 86.42

Conversely, the worst-performing sample was:

- **Worst Configuration:**
  - **Pitch Angle:** 80 degrees
  - **Yaw Angle:** 0 degrees
  - **Initial Velocity:** 25 m/s
  - **Spin Rate:** 2500 RPM
  - **Score:** 0.01

The results align with known physics behaviors, where moderate launch angles and velocities optimize range and accuracy. The findings also highlight the detrimental effects of extreme angles, which can lead to unstable trajectories and significant distance errors. The successful configurations demonstrated that a balance between pitch, velocity, and spin is crucial for maximizing accuracy.

## 5. Recommendations for Future Experiments

Based on the optimization results, several recommendations for future experiments can be made:

1. **Exploration of Nonlinear Effects:** Investigate the effects of nonlinear dynamics, such as air resistance and spin-induced lift, on projectile motion. This could provide deeper insights into optimizing performance.
2. **Parameter Interactions:** Conduct experiments that systematically vary multiple parameters simultaneously to better understand their interactions and combined effects on score maximization.
3. **Advanced Spin Configurations:** Explore different spin axis orientations and rates to assess their impact on stability and accuracy, particularly in relation to varying launch angles.
4. **Real-World Testing:** Implement real-world trials to validate the findings from simulations, as environmental factors may influence performance in ways not captured in the model.

These recommendations aim to enhance the understanding of projectile dynamics and improve the optimization process in future studies.

## 6. Conclusion

The optimization process successfully identified a maximum score of 86.42, demonstrating the effectiveness of a refined set of parameters focused on moderate pitch angles and initial velocities. The evolution of hypotheses throughout the experiment highlighted the importance of data-driven adjustments, leading to a more targeted exploration of the parameter space. The findings are relevant not only for future physics experiments but also for theoretical development in understanding projectile motion. The insights gained from this study can inform subsequent research and experimentation, ultimately contributing to a deeper understanding of the dynamics involved in projectile trajectories.
# BORA for Score Maximization 

## 1. Executive Summary

The optimization process successfully identified a maximum score of 95.63, achieved through a careful exploration of parameter configurations for a projectile aimed at a target. The most effective parameters included a pitch angle of 8°, a yaw angle of 0°, an initial velocity of 42 m/s, and a moderate spin rate. This outcome underscores the importance of moderate pitch angles and controlled velocities in maximizing accuracy, while also revealing that extreme configurations consistently led to poor performance. The findings highlight the relevance of physics principles in optimizing projectile motion and provide a foundation for future experiments.

## 2. Optimization Overview

**Objective:** The primary goal of this optimization process was to maximize the score, which reflects the accuracy of a projectile thrown toward a target located at (50, 0). The score is derived from the distance error between the projectile's landing position and the target, with higher scores indicating closer landings.

**Initial Hypotheses:** The initial hypotheses proposed a diverse set of parameter configurations, including:

1. **Low Angle, High Velocity:** Aimed to achieve a flat trajectory for quick distance coverage.
2. **Optimal Height and Moderate Spin:** Focused on stabilizing the projectile's flight for improved accuracy.
3. **High Angle, Low Velocity:** Explored a controlled arc for potential accuracy despite reduced speed.
4. **Balanced Approach:** Combined moderate pitch, yaw, and velocity for reliable trajectories.
5. **Aggressive Left Aim:** Tested lateral aiming to compensate for drift.

These hypotheses were based on fundamental physics principles governing projectile motion, including the effects of angle, velocity, and spin on trajectory and landing accuracy.

## 3. Progress Summary

**Key Milestones:**

| Iteration | Hypothesis Name                          | Outcome                                   | Comments                                                                 |
|-----------|-----------------------------------------|-------------------------------------------|--------------------------------------------------------------------------|
| 1         | Low Angle, High Velocity                | Discarded                                 | Low scores indicated flat trajectories were ineffective.                 |
| 2         | Optimal Height and Moderate Spin        | Discarded                                 | High spin rates led to instability, resulting in low scores.             |
| 3         | High Angle, Low Velocity                | Discarded                                 | Extreme pitch angles consistently yielded poor results.                  |
| 4         | Balanced Approach                       | Confirmed                                 | Moderate configurations showed promise, leading to further exploration.  |
| 5         | Aggressive Left Aim                     | Discarded                                 | Aggressive yaw settings resulted in low scores.                          |
| 6         | Refined Moderate Pitch and Yaw          | Confirmed                                 | Continued success with moderate pitch and yaw adjustments.               |
| 7         | Lower Spin with Moderate Velocity       | Confirmed                                 | Reduced spin improved stability and accuracy.                            |
| 8         | Exploring Higher Pitch with Controlled Velocity | Confirmed                         | Higher pitch angles with controlled velocity yielded better results.     |
| 9         | Aggressive Right Aim with Moderate Parameters | Discarded                         | Slight adjustments did not compensate for lateral drift effectively.     |
| 10        | New Low Pitch Exploration               | Confirmed                                 | Low pitch with higher velocity yielded a flat trajectory, improving scores.|

**Major Parameter Adjustments:** Throughout the optimization, significant adjustments were made to the parameters based on the performance of previous iterations. The focus shifted towards moderate pitch angles (20° to 36°) and controlled velocities (around 30 m/s). The most notable changes included:

- **Pitch Angle:** Initially explored extremes but refined to moderate angles, leading to improved scores.
- **Yaw Angle:** Adjustments were made to maintain slight angles, avoiding aggressive settings that led to poor performance.
- **Initial Velocity:** Increased in later iterations to explore its effect on distance coverage and accuracy.
- **Spin Rate:** Reduced to stabilize the projectile's flight, enhancing accuracy.

## 4. Results and Key Insights

The best-performing sample was achieved with the following parameters:

- **Pitch Angle:** 8°
- **Yaw Angle:** 0°
- **Initial Velocity:** 42 m/s
- **Spin Rate:** 750 RPM
- **Release Height:** 1.2 m
- **Mass:** 2.5 kg
- **Score:** 95.63

This configuration demonstrated that a low pitch angle combined with a high initial velocity resulted in a flat trajectory that effectively covered the distance to the target. The physics of projectile motion supports this finding, as lower angles can minimize vertical displacement while maximizing horizontal distance.

Conversely, the worst-performing sample was characterized by extreme pitch angles (e.g., 70°) and aggressive yaw settings, which consistently resulted in low scores (e.g., 0.02). These configurations failed to achieve the necessary balance between vertical and horizontal motion, leading to significant distance errors.

The optimization outcomes align with known physics behaviors, particularly the trade-offs between angle, velocity, and spin. The findings emphasize the importance of stability and control in projectile motion, as excessive spin or extreme angles can destabilize the trajectory.

## 5. Recommendations for Future Experiments

Based on the optimization results, several recommendations for future experiments can be made:

1. **Exploration of Intermediate Angles:** Further investigation into intermediate pitch angles (e.g., 10° to 20°) could yield additional insights into their effects on accuracy and distance.
2. **Varying Mass and Spin Rates:** Experimenting with different masses and spin rates may uncover new configurations that enhance performance, particularly in relation to stability.
3. **Environmental Factors:** Consideration of external factors such as wind resistance and air density could provide a more comprehensive understanding of projectile behavior.
4. **Advanced Modeling Techniques:** Employing more sophisticated modeling techniques, such as computational fluid dynamics, could enhance predictions of projectile trajectories and optimize parameters more effectively.
5. **Real-World Testing:** Conducting real-world experiments to validate the findings from simulations would provide valuable data on the practical applicability of the optimized parameters.

## 6. Conclusion

The optimization process successfully identified a maximum score of 95.63, demonstrating the effectiveness of moderate pitch angles and controlled velocities in maximizing projectile accuracy. The iterative refinement of hypotheses based on empirical data led to a focused exploration of parameter configurations, ultimately revealing the importance of stability and control in projectile motion. The findings not only contribute to the understanding of projectile dynamics but also lay the groundwork for future experiments in physics, emphasizing the relevance of systematic optimization in achieving desired outcomes. The insights gained from this study can inform both theoretical developments and practical applications in the field of projectile motion.
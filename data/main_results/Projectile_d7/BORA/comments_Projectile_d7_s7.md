# Projectile

## Experiment Overview

The goal of this experiment is to maximize the score, which reflects the accuracy of a projectile thrown from the origin (0, 0) toward a target located at (50, 0). The score is derived from the distance error between the projectile's landing position and the target, with higher scores indicating closer landings. 

To achieve this, we will optimize several parameters: pitch angle (pitch_deg), yaw angle (yaw_deg), initial velocity (v0), spin rate (spin_rpm), spin axis orientation (spin_axis_deg), release height (h0), and mass of the projectile. Each parameter has defined bounds, ensuring a systematic exploration of the parameter space: pitch_deg (-30, 90), yaw_deg (-180, 180), v0 (0, 50), spin_rpm (0, 3000), spin_axis_deg (-180, 180), h0 (0, 2), and mass (0.01, 10).

Bayesian Optimization (BO) will be employed to efficiently navigate this high-dimensional space, utilizing a probabilistic model to suggest parameter settings that are likely to yield higher scores. As the optimization progresses, I will provide insights and hypotheses to guide the exploration, especially when BO plateaus, by identifying conditions that may lead to improved performance. This iterative process aims to converge on the optimal parameter settings for maximizing the score.

## Initial Thoughts

In this initial sampling step, we aim to explore diverse regions of the parameter space to identify promising configurations for maximizing the score. The hypotheses consider various physical principles, such as the effects of angle, velocity, and spin on projectile motion. A low pitch angle combined with a high initial velocity is expected to produce a flatter trajectory, potentially allowing the projectile to cover more horizontal distance quickly. Releasing the projectile from a moderate height with reasonable spin may stabilize its flight and improve accuracy towards the target. Conversely, a high pitch angle with low velocity may lead to a high arc, allowing the projectile to drop closer to the target. A balanced combination of moderate pitch, yaw, and velocity may provide a good starting point for exploring the parameter space effectively. Finally, using extreme yaw angles may help in understanding how lateral adjustments affect the landing position, potentially revealing new insights into the projectile's trajectory. By strategically selecting points across the parameter bounds, we can gather valuable data to inform the Bayesian Optimization process and guide future explorations.
### Initial Hypotheses

#### Low Angle High Velocity

*Rationale:* A low pitch angle combined with a high initial velocity is expected to produce a flatter trajectory, potentially allowing the projectile to cover more horizontal distance quickly.

*Confidence:* medium

*Points:*

- {'pitch_deg': 10, 'yaw_deg': 0, 'v0': 45, 'spin_rpm': 1500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Optimal Height and Moderate Spin

*Rationale:* Releasing the projectile from a moderate height with a reasonable spin may stabilize its flight and improve accuracy towards the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 0, 'v0': 30, 'spin_rpm': 1000, 'spin_axis_deg': 90, 'h0': 1.5, 'mass': 0.5}

#### High Angle Low Velocity

*Rationale:* A high pitch angle with low velocity may lead to a high arc, allowing the projectile to drop closer to the target, especially if the target is at a fixed distance.

*Confidence:* low

*Points:*

- {'pitch_deg': 70, 'yaw_deg': 0, 'v0': 10, 'spin_rpm': 0, 'spin_axis_deg': 0, 'h0': 0.5, 'mass': 0.1}

#### Balanced Approach

*Rationale:* A balanced combination of moderate pitch, yaw, and velocity may provide a good starting point for exploring the parameter space effectively.

*Confidence:* high

*Points:*

- {'pitch_deg': 45, 'yaw_deg': 15, 'v0': 25, 'spin_rpm': 500, 'spin_axis_deg': 45, 'h0': 1, 'mass': 2}

#### Extreme Yaw for Lateral Adjustment

*Rationale:* Using extreme yaw angles may help in understanding how lateral adjustments affect the landing position, potentially revealing new insights into the projectile's trajectory.

*Confidence:* medium

*Points:*

- {'pitch_deg': 20, 'yaw_deg': -150, 'v0': 35, 'spin_rpm': 2000, 'spin_axis_deg': 180, 'h0': 0.8, 'mass': 0.75}

## Iteration 17

Upon reviewing the results from the first 16 iterations, the highest score achieved is 37.95 from iteration 10, which utilized a combination of moderate pitch (27.35°), slight yaw (0.87°), and a reasonable initial velocity (25.45 m/s). This indicates that a balanced approach with moderate angles and velocities is effective for maximizing the score. The data shows that extreme angles, particularly high pitch (70°) and extreme yaw values (e.g., -150°), have consistently resulted in low scores, suggesting these subspaces are detrimental. The promising subspace appears to be around moderate pitch angles (20° to 30°) and initial velocities (20 m/s to 30 m/s). Given these insights, I will refine the previous hypotheses, discarding those that performed poorly and proposing new ones that focus on the identified effective regions. The new hypotheses will aim to explore the effective parameter combinations further, particularly around the successful configurations observed in the data, to maximize the score towards the target.

### Updated Hypotheses

#### Moderate Pitch and Velocity

*Rationale:* Building on the successful configuration from iteration 10, this hypothesis focuses on a moderate pitch and velocity to maximize horizontal distance while maintaining accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 25, 'yaw_deg': 5, 'v0': 28, 'spin_rpm': 1000, 'spin_axis_deg': 45, 'h0': 1, 'mass': 1.5}

#### Slightly Higher Pitch with Moderate Velocity

*Rationale:* This hypothesis explores a slightly higher pitch angle while maintaining a moderate velocity, which may help in achieving a better arc towards the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 35, 'yaw_deg': 0, 'v0': 25, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1.2, 'mass': 1}

#### Low Pitch with Increased Velocity

*Rationale:* This hypothesis tests a low pitch angle with increased velocity, aiming for a flatter trajectory that could cover more horizontal distance quickly.

*Confidence:* medium

*Points:*

- {'pitch_deg': 15, 'yaw_deg': 0, 'v0': 35, 'spin_rpm': 1200, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Exploring Higher Yaw with Moderate Pitch

*Rationale:* This hypothesis aims to explore the effects of a moderate pitch angle combined with a higher yaw angle to assess lateral adjustments.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 30, 'v0': 25, 'spin_rpm': 1000, 'spin_axis_deg': 90, 'h0': 1, 'mass': 1.5}

#### Refined Low Angle Approach

*Rationale:* This hypothesis revisits the low angle approach with a focus on optimizing the initial velocity and spin to stabilize the projectile's flight.

*Confidence:* medium

*Points:*

- {'pitch_deg': 10, 'yaw_deg': 0, 'v0': 30, 'spin_rpm': 1500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

## Iteration 27

As we progress through the optimization iterations, the data reveals critical insights into the parameter space. The highest score achieved so far is 57.63 from iteration 18, which utilized a moderate pitch (35°) and a reasonable initial velocity (25 m/s). This suggests that a combination of moderate pitch angles and velocities is effective for maximizing the score. The promising subspace appears to be around pitch angles of 25° to 35° and initial velocities between 25 m/s and 30 m/s. Conversely, extreme angles, particularly high pitch (70°) and extreme yaw values (e.g., -150°), have consistently resulted in low scores, indicating these regions are detrimental. The data also shows that configurations with low pitch angles and high velocities have not performed well, suggesting that a flatter trajectory may not be beneficial in this context. Based on these findings, I will refine the previous hypotheses, discarding those that performed poorly and proposing new ones that focus on the identified effective regions. The new hypotheses will aim to explore the effective parameter combinations further, particularly around the successful configurations observed in the data, to maximize the score towards the target.

### Updated Hypotheses

#### Moderate Pitch and Velocity

*Rationale:* Building on the successful configuration from iteration 18, this hypothesis focuses on a moderate pitch and velocity to maximize horizontal distance while maintaining accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 0, 'v0': 28, 'spin_rpm': 1000, 'spin_axis_deg': 45, 'h0': 1, 'mass': 1.5}

#### Slightly Higher Pitch with Moderate Velocity

*Rationale:* This hypothesis explores a slightly higher pitch angle while maintaining a moderate velocity, which may help in achieving a better arc towards the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 35, 'yaw_deg': 0, 'v0': 27, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1.2, 'mass': 1}

#### Exploring Higher Yaw with Moderate Pitch

*Rationale:* This hypothesis aims to explore the effects of a moderate pitch angle combined with a higher yaw angle to assess lateral adjustments.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 15, 'v0': 26, 'spin_rpm': 1000, 'spin_axis_deg': 90, 'h0': 1, 'mass': 1.5}

#### Testing Lower Pitch with Moderate Velocity

*Rationale:* This hypothesis tests a lower pitch angle with a moderate velocity, aiming for a balance between distance and accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 20, 'yaw_deg': 0, 'v0': 25, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

## Iteration 35

Upon analyzing the results from the first 34 iterations, the highest score achieved is 76.76 from iteration 27, which utilized a moderate pitch (30°) and a reasonable initial velocity (28 m/s). This reinforces the effectiveness of moderate pitch angles (around 25° to 35°) and initial velocities (25 m/s to 30 m/s) for maximizing the score. The data indicates that configurations with extreme angles, particularly high pitch (70°) and extreme yaw values (e.g., -150°), consistently yield low scores, suggesting these regions are detrimental. Additionally, low pitch angles combined with high velocities have not performed well, indicating that a flatter trajectory may not be beneficial in this context. Based on these insights, I will refine the previous hypotheses, focusing on the identified effective regions while discarding those that performed poorly. The new hypotheses will aim to explore the effective parameter combinations further, particularly around the successful configurations observed in the data, to maximize the score towards the target. The promising subspace appears to be around pitch angles of 25° to 35° and initial velocities between 25 m/s and 30 m/s, while configurations with extreme angles and low pitch combined with high velocities should be avoided.

### Updated Hypotheses

#### Refined Moderate Pitch and Velocity

*Rationale:* Building on the successful configuration from iteration 27, this hypothesis focuses on a moderate pitch and velocity to maximize horizontal distance while maintaining accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 5, 'v0': 29, 'spin_rpm': 1000, 'spin_axis_deg': 45, 'h0': 1, 'mass': 1.5}

#### Higher Pitch with Moderate Velocity

*Rationale:* This hypothesis explores a slightly higher pitch angle while maintaining a moderate velocity, which may help in achieving a better arc towards the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 35, 'yaw_deg': 10, 'v0': 26, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1.2, 'mass': 1}

#### Moderate Pitch with Increased Yaw

*Rationale:* This hypothesis aims to explore the effects of a moderate pitch angle combined with a higher yaw angle to assess lateral adjustments while maintaining a reasonable score.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 15, 'v0': 27, 'spin_rpm': 1000, 'spin_axis_deg': 90, 'h0': 1, 'mass': 1.5}

#### Testing Lower Pitch with Moderate Velocity

*Rationale:* This hypothesis tests a lower pitch angle with a moderate velocity, aiming for a balance between distance and accuracy, while avoiding extremes.

*Confidence:* medium

*Points:*

- {'pitch_deg': 22, 'yaw_deg': 0, 'v0': 25, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Exploring Slightly Lower Pitch

*Rationale:* This hypothesis tests a slightly lower pitch angle to see if it can still achieve a reasonable score while maintaining a moderate velocity.

*Confidence:* medium

*Points:*

- {'pitch_deg': 25, 'yaw_deg': 5, 'v0': 26, 'spin_rpm': 900, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

## Iteration 47

As we reach iteration 46, the data reveals significant insights into the parameter space. The highest score achieved is 76.76 from iteration 27, which utilized a moderate pitch (30°) and a reasonable initial velocity (28 m/s). This reinforces the effectiveness of moderate pitch angles (around 25° to 35°) and initial velocities (25 m/s to 30 m/s) for maximizing the score. The promising subspace appears to be centered around these moderate pitch angles and velocities, while configurations with extreme angles, particularly high pitch (70°) and extreme yaw values (e.g., -150°), consistently yield low scores, indicating these regions are detrimental. Additionally, low pitch angles combined with high velocities have not performed well, suggesting that a flatter trajectory may not be beneficial in this context. Based on these findings, I will refine the previous hypotheses, focusing on the identified effective regions while discarding those that performed poorly. The new hypotheses will aim to explore the effective parameter combinations further, particularly around the successful configurations observed in the data, to maximize the score towards the target.

### Updated Hypotheses

#### Refined Moderate Pitch and Velocity

*Rationale:* Building on the successful configuration from iteration 27, this hypothesis focuses on a moderate pitch and velocity to maximize horizontal distance while maintaining accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 10, 'v0': 29, 'spin_rpm': 1000, 'spin_axis_deg': 45, 'h0': 1, 'mass': 1.5}

#### Higher Pitch with Moderate Velocity

*Rationale:* This hypothesis explores a slightly higher pitch angle while maintaining a moderate velocity, which may help in achieving a better arc towards the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 36, 'yaw_deg': 5, 'v0': 27, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1.2, 'mass': 1}

#### Moderate Pitch with Increased Yaw

*Rationale:* This hypothesis aims to explore the effects of a moderate pitch angle combined with a higher yaw angle to assess lateral adjustments while maintaining a reasonable score.

*Confidence:* medium

*Points:*

- {'pitch_deg': 31, 'yaw_deg': 20, 'v0': 27, 'spin_rpm': 1000, 'spin_axis_deg': 90, 'h0': 1, 'mass': 1.5}

#### Testing Lower Pitch with Moderate Velocity

*Rationale:* This hypothesis tests a lower pitch angle with a moderate velocity, aiming for a balance between distance and accuracy, while avoiding extremes.

*Confidence:* medium

*Points:*

- {'pitch_deg': 23, 'yaw_deg': 5, 'v0': 25, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Exploring Slightly Lower Pitch

*Rationale:* This hypothesis tests a slightly lower pitch angle to see if it can still achieve a reasonable score while maintaining a moderate velocity.

*Confidence:* medium

*Points:*

- {'pitch_deg': 26, 'yaw_deg': 10, 'v0': 26, 'spin_rpm': 900, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

## Iteration 61

As we reach iteration 60, the data reveals significant insights into the parameter space. The highest score achieved is 76.76 from iteration 27, which utilized a moderate pitch (30°) and a reasonable initial velocity (28 m/s). This reinforces the effectiveness of moderate pitch angles (around 25° to 35°) and initial velocities (25 m/s to 30 m/s) for maximizing the score. The promising subspace appears to be centered around these moderate pitch angles and velocities, while configurations with extreme angles, particularly high pitch (70°) and extreme yaw values (e.g., -150°), consistently yield low scores, indicating these regions are detrimental. Additionally, low pitch angles combined with high velocities have not performed well, suggesting that a flatter trajectory may not be beneficial in this context. Based on these findings, I will refine the previous hypotheses, focusing on the identified effective regions while discarding those that performed poorly. The new hypotheses will aim to explore the effective parameter combinations further, particularly around the successful configurations observed in the data, to maximize the score towards the target.

### Updated Hypotheses

#### Refined Moderate Pitch and Velocity

*Rationale:* Building on the successful configuration from iteration 27, this hypothesis focuses on a moderate pitch and velocity to maximize horizontal distance while maintaining accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 5, 'v0': 28, 'spin_rpm': 1000, 'spin_axis_deg': 45, 'h0': 1, 'mass': 1.5}

#### Higher Pitch with Moderate Velocity

*Rationale:* This hypothesis explores a slightly higher pitch angle while maintaining a moderate velocity, which may help in achieving a better arc towards the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 35, 'yaw_deg': 5, 'v0': 27, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1.2, 'mass': 1}

#### Moderate Pitch with Increased Yaw

*Rationale:* This hypothesis aims to explore the effects of a moderate pitch angle combined with a higher yaw angle to assess lateral adjustments while maintaining a reasonable score.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 20, 'v0': 27, 'spin_rpm': 1000, 'spin_axis_deg': 90, 'h0': 1, 'mass': 1.5}

#### Testing Lower Pitch with Moderate Velocity

*Rationale:* This hypothesis tests a lower pitch angle with a moderate velocity, aiming for a balance between distance and accuracy, while avoiding extremes.

*Confidence:* medium

*Points:*

- {'pitch_deg': 21, 'yaw_deg': 2, 'v0': 25, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Exploring Slightly Lower Pitch

*Rationale:* This hypothesis tests a slightly lower pitch angle to see if it can still achieve a reasonable score while maintaining a moderate velocity.

*Confidence:* medium

*Points:*

- {'pitch_deg': 27, 'yaw_deg': 8, 'v0': 26, 'spin_rpm': 900, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

## Iteration 74

As we reach iteration 73, the data provides valuable insights into the parameter space. The highest score achieved is 76.76 from iteration 27, which utilized a moderate pitch of 30° and an initial velocity of 28 m/s. This reinforces the effectiveness of moderate pitch angles (around 25° to 35°) and initial velocities (25 m/s to 30 m/s) for maximizing the score. The promising subspace appears to be centered around these moderate pitch angles and velocities, while configurations with extreme angles, particularly high pitch (70°) and extreme yaw values (e.g., -150°), consistently yield low scores, indicating these regions are detrimental. Additionally, low pitch angles combined with high velocities have not performed well, suggesting that a flatter trajectory may not be beneficial in this context. Based on these findings, I will refine the previous hypotheses, focusing on the identified effective regions while discarding those that performed poorly. The new hypotheses will aim to explore the effective parameter combinations further, particularly around the successful configurations observed in the data, to maximize the score towards the target.

### Updated Hypotheses

#### Refined Moderate Pitch and Velocity

*Rationale:* Building on the successful configuration from iteration 27, this hypothesis focuses on a moderate pitch and velocity to maximize horizontal distance while maintaining accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 8, 'v0': 28, 'spin_rpm': 1000, 'spin_axis_deg': 45, 'h0': 1, 'mass': 1.5}

#### Exploring Slightly Lower Pitch

*Rationale:* This hypothesis tests a slightly lower pitch angle to see if it can still achieve a reasonable score while maintaining a moderate velocity.

*Confidence:* medium

*Points:*

- {'pitch_deg': 28, 'yaw_deg': 5, 'v0': 26, 'spin_rpm': 900, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

## Iteration 83

As we reach iteration 82, the data provides significant insights into the parameter space. The highest score achieved is 76.76 from iteration 27, which utilized a moderate pitch of 30° and an initial velocity of 28 m/s. This reinforces the effectiveness of moderate pitch angles (around 25° to 35°) and initial velocities (25 m/s to 30 m/s) for maximizing the score. The promising subspace appears to be centered around these moderate pitch angles and velocities, while configurations with extreme angles, particularly high pitch (70°) and extreme yaw values (e.g., -150°), consistently yield low scores, indicating these regions are detrimental. Additionally, low pitch angles combined with high velocities have not performed well, suggesting that a flatter trajectory may not be beneficial in this context. Based on these findings, I will refine the previous hypotheses, focusing on the identified effective regions while discarding those that performed poorly. The new hypotheses will aim to explore the effective parameter combinations further, particularly around the successful configurations observed in the data, to maximize the score towards the target.

### Updated Hypotheses

#### Refined Moderate Pitch and Velocity

*Rationale:* Building on the successful configuration from iteration 27, this hypothesis focuses on a moderate pitch and velocity to maximize horizontal distance while maintaining accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 6, 'v0': 28, 'spin_rpm': 1000, 'spin_axis_deg': 45, 'h0': 1, 'mass': 1.5}

#### Higher Pitch with Moderate Velocity

*Rationale:* This hypothesis explores a slightly higher pitch angle while maintaining a moderate velocity, which may help in achieving a better arc towards the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 35, 'yaw_deg': 7, 'v0': 27, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1.2, 'mass': 1}

#### Moderate Pitch with Increased Yaw

*Rationale:* This hypothesis aims to explore the effects of a moderate pitch angle combined with a higher yaw angle to assess lateral adjustments while maintaining a reasonable score.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 16, 'v0': 27, 'spin_rpm': 1000, 'spin_axis_deg': 90, 'h0': 1, 'mass': 1.5}

#### Testing Lower Pitch with Moderate Velocity

*Rationale:* This hypothesis tests a lower pitch angle with a moderate velocity, aiming for a balance between distance and accuracy, while avoiding extremes.

*Confidence:* medium

*Points:*

- {'pitch_deg': 22, 'yaw_deg': 1, 'v0': 25, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Exploring Slightly Lower Pitch

*Rationale:* This hypothesis tests a slightly lower pitch angle to see if it can still achieve a reasonable score while maintaining a moderate velocity.

*Confidence:* medium

*Points:*

- {'pitch_deg': 28, 'yaw_deg': 6, 'v0': 26, 'spin_rpm': 900, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

## Iteration 96

As we reach iteration 95, the data provides critical insights into the parameter space. The highest score achieved is 76.76 from iteration 27, which utilized a moderate pitch of 30° and an initial velocity of 28 m/s. This reinforces the effectiveness of moderate pitch angles (around 25° to 35°) and initial velocities (25 m/s to 30 m/s) for maximizing the score. The promising subspace appears to be centered around these moderate pitch angles and velocities, while configurations with extreme angles, particularly high pitch (70°) and extreme yaw values (e.g., -150°), consistently yield low scores, indicating these regions are detrimental. Additionally, low pitch angles combined with high velocities have not performed well, suggesting that a flatter trajectory may not be beneficial in this context. Based on these findings, I will refine the previous hypotheses, focusing on the identified effective regions while discarding those that performed poorly. The new hypotheses will aim to explore the effective parameter combinations further, particularly around the successful configurations observed in the data, to maximize the score towards the target.

### Updated Hypotheses

#### Refined Moderate Pitch and Velocity

*Rationale:* Building on the successful configuration from iteration 27, this hypothesis focuses on a moderate pitch and velocity to maximize horizontal distance while maintaining accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 4, 'v0': 28, 'spin_rpm': 1000, 'spin_axis_deg': 45, 'h0': 1, 'mass': 1.5}

#### Higher Pitch with Moderate Velocity

*Rationale:* This hypothesis explores a slightly higher pitch angle while maintaining a moderate velocity, which may help in achieving a better arc towards the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 35, 'yaw_deg': 3, 'v0': 27, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1.2, 'mass': 1}

#### Moderate Pitch with Increased Yaw

*Rationale:* This hypothesis aims to explore the effects of a moderate pitch angle combined with a higher yaw angle to assess lateral adjustments while maintaining a reasonable score.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 18, 'v0': 27, 'spin_rpm': 1000, 'spin_axis_deg': 90, 'h0': 1, 'mass': 1.5}

#### Testing Lower Pitch with Moderate Velocity

*Rationale:* This hypothesis tests a lower pitch angle with a moderate velocity, aiming for a balance between distance and accuracy, while avoiding extremes.

*Confidence:* medium

*Points:*

- {'pitch_deg': 22, 'yaw_deg': 2, 'v0': 25, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Exploring Slightly Lower Pitch

*Rationale:* This hypothesis tests a slightly lower pitch angle to see if it can still achieve a reasonable score while maintaining a moderate velocity.

*Confidence:* medium

*Points:*

- {'pitch_deg': 28, 'yaw_deg': 7, 'v0': 26, 'spin_rpm': 900, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

## Final Conclusions

Throughout the optimization process, the hypotheses evolved significantly based on the experimental data collected from each iteration. Initially, the hypotheses were broad, exploring various combinations of pitch angles, yaw angles, initial velocities, and other parameters. However, as the iterations progressed, it became clear that certain configurations consistently yielded higher scores, particularly those with moderate pitch angles (around 25° to 35°) and initial velocities (25 m/s to 30 m/s).

The data revealed that extreme angles, especially high pitch and extreme yaw values, were detrimental to performance. Consequently, the hypotheses were refined to focus on the promising subspaces identified in earlier iterations. This led to a more targeted exploration of parameter combinations that had previously shown success, while discarding those that performed poorly.

By the end of the optimization, the hypotheses were more concentrated on configurations that balanced pitch and velocity effectively, with a notable emphasis on maintaining moderate values. This iterative learning process allowed for a systematic approach to refining the hypotheses, ultimately leading to the highest score of 76.76.

| Hypothesis Name                          | Initial Confidence | Final Confidence |
|------------------------------------------|--------------------|------------------|
| Low Angle High Velocity                  | Medium             | Low              |
| Optimal Height and Moderate Spin         | Medium             | Low              |
| High Angle Low Velocity                  | Low                 | Low              |
| Balanced Approach                        | High               | Medium           |
| Extreme Yaw for Lateral Adjustment       | Medium             | Low              |
| Refined Moderate Pitch and Velocity      | High               | High             |
| Higher Pitch with Moderate Velocity       | Medium             | Medium           |
| Moderate Pitch with Increased Yaw        | Medium             | Medium           |
| Testing Lower Pitch with Moderate Velocity| Medium             | Medium           |
| Exploring Slightly Lower Pitch           | Medium             | Medium           |
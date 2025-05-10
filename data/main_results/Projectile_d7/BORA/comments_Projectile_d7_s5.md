# Projectile

## Experiment Overview

The goal of this experiment is to maximize the score, which reflects the accuracy of a projectile thrown from the origin (0, 0) toward a target located at (50, 0). The score is derived from the distance error between the projectile's landing position and the target, with higher scores indicating closer landings. 

To achieve this, we will optimize several parameters: pitch_deg (release angle), yaw_deg (horizontal aiming angle), v0 (initial velocity), spin_rpm (spin rate), spin_axis_deg (orientation of the spin axis), h0 (release height), and mass of the projectile. Each parameter has defined bounds, ensuring a systematic exploration of the parameter space while adhering to physical constraints.

Bayesian Optimization (BO) will be employed to efficiently navigate this multi-dimensional space, leveraging a probabilistic model to predict the score based on current parameter settings. As BO iteratively samples points, it will identify regions of interest and suggest new parameter combinations. When the optimization process plateaus, I will provide insights to explore unexplored areas or adjust parameters strategically, aiming to uncover conditions that yield the highest scores. Ultimately, the experiment seeks to refine the projectile's launch parameters to achieve optimal accuracy in hitting the target.

## Initial Thoughts

In this initial sampling step, we aim to explore diverse regions of the parameter space to identify promising configurations for maximizing the score. The hypotheses are designed to cover a range of angles, velocities, and other parameters that could influence the projectile's trajectory. By sampling these points, we can gather valuable data on how different settings affect the distance error and, consequently, the score. The initial hypotheses reflect a balance between conservative and aggressive parameter choices, allowing us to assess both low and high potential outcomes. Notably, the maximum score of 100 is achievable when the projectile lands directly on the target, which requires careful tuning of parameters such as pitch, yaw, and initial velocity. The proposed configurations consider both low and high angles, as well as varying velocities and spins, to capture a wide array of potential trajectories. This approach will help us identify the optimal conditions for hitting the target accurately.
### Initial Hypotheses

#### Low Angle, High Velocity

*Rationale:* A low pitch angle combined with a high initial velocity may provide a flat trajectory that covers distance quickly, potentially reducing distance error.

*Confidence:* medium

*Points:*

- {'pitch_deg': 5, 'yaw_deg': 0, 'v0': 40, 'spin_rpm': 1500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Optimal Height and Moderate Spin

*Rationale:* Releasing the projectile from a moderate height with a balanced spin may stabilize its flight, improving accuracy toward the target.

*Confidence:* high

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 0, 'v0': 25, 'spin_rpm': 1000, 'spin_axis_deg': 90, 'h0': 1.5, 'mass': 0.5}

#### High Angle, Low Velocity

*Rationale:* A high pitch angle with a lower velocity may allow for a more controlled arc, potentially landing closer to the target despite the reduced speed.

*Confidence:* medium

*Points:*

- {'pitch_deg': 70, 'yaw_deg': 0, 'v0': 10, 'spin_rpm': 500, 'spin_axis_deg': 0, 'h0': 0.5, 'mass': 0.2}

#### Balanced Approach

*Rationale:* A balanced combination of moderate pitch, yaw, and velocity may yield a reliable trajectory that maximizes the chances of hitting the target.

*Confidence:* high

*Points:*

- {'pitch_deg': 45, 'yaw_deg': 10, 'v0': 30, 'spin_rpm': 800, 'spin_axis_deg': 45, 'h0': 1, 'mass': 0.8}

#### Aggressive Left Aim

*Rationale:* Aiming aggressively to the left with a high initial velocity may compensate for any lateral drift, potentially improving accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 10, 'yaw_deg': -45, 'v0': 45, 'spin_rpm': 2000, 'spin_axis_deg': 180, 'h0': 0.8, 'mass': 0.3}

## Iteration 14

As we progress through iteration 13 of the Bayesian Optimization, we observe that the highest score achieved so far is 65.50 from iteration 7, with parameters pitch_deg = 23.49, yaw_deg = 2.09, v0 = 28.96, spin_rpm = 810.82, spin_axis_deg = 40.74, h0 = 0.31, and mass = 7.24. This suggests that a moderate pitch angle and a slight rightward yaw may be beneficial for accuracy. The data indicates that extreme values in pitch and yaw, particularly those leading to high angles or aggressive lateral aiming, have resulted in low scores, indicating these subspaces are detrimental. Iterations 1, 3, 5, 6, 9, 10, 11, and 12 consistently yielded low scores, suggesting that either excessive spin, extreme angles, or inappropriate velocities negatively impact performance. Moving forward, we should focus on refining the parameters around the successful configurations while discarding those that consistently yield poor results. The next hypotheses will aim to explore variations around the successful parameters while also introducing new combinations to further investigate the parameter space. By concentrating on moderate pitch and yaw angles, along with controlled velocities and spins, we can maximize the chances of hitting the target accurately.

### Updated Hypotheses

#### Refined Moderate Pitch and Yaw

*Rationale:* Building on the successful parameters from iteration 7, this hypothesis maintains a moderate pitch and yaw while slightly increasing the initial velocity to explore its effect on score.

*Confidence:* high

*Points:*

- {'pitch_deg': 25, 'yaw_deg': 5, 'v0': 35, 'spin_rpm': 800, 'spin_axis_deg': 30, 'h0': 0.5, 'mass': 6}

#### Lower Spin with Moderate Velocity

*Rationale:* Reducing the spin while maintaining a moderate velocity may stabilize the projectile's flight, potentially improving accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 20, 'yaw_deg': 0, 'v0': 30, 'spin_rpm': 600, 'spin_axis_deg': 0, 'h0': 1, 'mass': 5}

#### Exploring Higher Pitch with Controlled Velocity

*Rationale:* Testing a higher pitch angle with a controlled velocity may allow for a more pronounced arc, which could help in landing closer to the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 40, 'yaw_deg': 0, 'v0': 20, 'spin_rpm': 700, 'spin_axis_deg': 0, 'h0': 1.5, 'mass': 0.8}

#### Aggressive Right Aim with Moderate Parameters

*Rationale:* Testing a slight aggressive right aim while keeping other parameters moderate may help in compensating for any lateral drift observed in previous iterations.

*Confidence:* medium

*Points:*

- {'pitch_deg': 15, 'yaw_deg': 15, 'v0': 28, 'spin_rpm': 900, 'spin_axis_deg': 45, 'h0': 0.75, 'mass': 1.5}

#### New Low Pitch Exploration

*Rationale:* Exploring a low pitch angle with a higher velocity may yield a flat trajectory that covers distance quickly, potentially improving score.

*Confidence:* medium

*Points:*

- {'pitch_deg': 5, 'yaw_deg': 0, 'v0': 45, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 2}

## Iteration 29

As we reach iteration 28 of the Bayesian Optimization, the highest score achieved so far is 65.50 from iteration 7, with parameters pitch_deg = 23.49, yaw_deg = 2.09, v0 = 28.96, spin_rpm = 810.82, spin_axis_deg = 40.74, h0 = 0.31, and mass = 7.24. The data indicates that configurations with extreme pitch angles (both high and low) and aggressive yaw settings have consistently resulted in low scores, suggesting these subspaces are detrimental. Specifically, iterations with pitch angles above 60° or below 10° and yaw angles beyond ±30° have not performed well. Conversely, the most promising subspace appears to be around moderate pitch angles (20° to 30°) and slight yaw adjustments (±10°), combined with controlled velocities (around 30 m/s). Moving forward, I will refine the previous hypotheses to focus on this successful region while discarding those that have consistently yielded poor results. The new hypotheses will explore variations around the successful parameters while introducing new combinations to further investigate the parameter space. This approach aims to maximize the chances of hitting the target accurately by concentrating on the identified effective subspaces.

### Updated Hypotheses

#### Refined Moderate Pitch and Yaw

*Rationale:* Building on the successful parameters from iteration 7, this hypothesis maintains a moderate pitch and yaw while slightly increasing the initial velocity to explore its effect on score.

*Confidence:* high

*Points:*

- {'pitch_deg': 25, 'yaw_deg': 5, 'v0': 36, 'spin_rpm': 800, 'spin_axis_deg': 30, 'h0': 0.5, 'mass': 6}

#### Lower Spin with Moderate Velocity

*Rationale:* Reducing the spin while maintaining a moderate velocity may stabilize the projectile's flight, potentially improving accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 22, 'yaw_deg': 0, 'v0': 30, 'spin_rpm': 500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 5}

#### Exploring Higher Pitch with Controlled Velocity

*Rationale:* Testing a higher pitch angle with a controlled velocity may allow for a more pronounced arc, which could help in landing closer to the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 35, 'yaw_deg': 0, 'v0': 25, 'spin_rpm': 700, 'spin_axis_deg': 0, 'h0': 1.5, 'mass': 0.8}

#### Aggressive Right Aim with Moderate Parameters

*Rationale:* Testing a slight aggressive right aim while keeping other parameters moderate may help in compensating for any lateral drift observed in previous iterations.

*Confidence:* medium

*Points:*

- {'pitch_deg': 18, 'yaw_deg': 10, 'v0': 28, 'spin_rpm': 900, 'spin_axis_deg': 45, 'h0': 0.75, 'mass': 1.5}

#### New Low Pitch Exploration

*Rationale:* Exploring a low pitch angle with a higher velocity may yield a flat trajectory that covers distance quickly, potentially improving score.

*Confidence:* low

*Points:*

- {'pitch_deg': 10, 'yaw_deg': 0, 'v0': 40, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 2}

## Iteration 45

As we reach iteration 44 of the Bayesian Optimization, the highest score achieved so far is 65.50 from iteration 7, indicating that we have yet to find a configuration that significantly improves upon this result. The data reveals that moderate pitch angles (around 20° to 30°) and slight yaw adjustments (within ±10°) are associated with higher scores, while extreme pitch angles (above 60° or below 10°) and aggressive yaw settings have consistently resulted in low scores. The most promising configurations also tend to have controlled velocities around 30 m/s. Notably, iterations with pitch angles above 60° or below 10° and yaw angles beyond ±30° have performed poorly, suggesting these subspaces are detrimental. Moving forward, I will refine the previous hypotheses to focus on this successful region while discarding those that have consistently yielded poor results. The new hypotheses will explore variations around the successful parameters while introducing new combinations to further investigate the parameter space. This approach aims to maximize the chances of hitting the target accurately by concentrating on the identified effective subspaces.

### Updated Hypotheses

#### Refined Moderate Pitch and Yaw

*Rationale:* Building on the successful parameters from iteration 7, this hypothesis maintains a moderate pitch and yaw while slightly increasing the initial velocity to explore its effect on score.

*Confidence:* high

*Points:*

- {'pitch_deg': 26, 'yaw_deg': 5, 'v0': 37, 'spin_rpm': 800, 'spin_axis_deg': 30, 'h0': 0.5, 'mass': 6}

#### Lower Spin with Moderate Velocity

*Rationale:* Reducing the spin while maintaining a moderate velocity may stabilize the projectile's flight, potentially improving accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 22, 'yaw_deg': 0, 'v0': 30, 'spin_rpm': 400, 'spin_axis_deg': 0, 'h0': 1, 'mass': 5}

#### Exploring Higher Pitch with Controlled Velocity

*Rationale:* Testing a higher pitch angle with a controlled velocity may allow for a more pronounced arc, which could help in landing closer to the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 35, 'yaw_deg': 0, 'v0': 25, 'spin_rpm': 600, 'spin_axis_deg': 0, 'h0': 1.5, 'mass': 0.8}

#### Aggressive Right Aim with Moderate Parameters

*Rationale:* Testing a slight aggressive right aim while keeping other parameters moderate may help in compensating for any lateral drift observed in previous iterations.

*Confidence:* medium

*Points:*

- {'pitch_deg': 18, 'yaw_deg': 8, 'v0': 28, 'spin_rpm': 800, 'spin_axis_deg': 45, 'h0': 0.75, 'mass': 1.5}

#### New Low Pitch Exploration

*Rationale:* Exploring a low pitch angle with a higher velocity may yield a flat trajectory that covers distance quickly, potentially improving score.

*Confidence:* low

*Points:*

- {'pitch_deg': 8, 'yaw_deg': 0, 'v0': 42, 'spin_rpm': 900, 'spin_axis_deg': 0, 'h0': 1, 'mass': 2}

## Iteration 58

As we continue to refine our hypotheses based on the latest data, we aim to explore new parameter configurations that have not been previously tested. The highest score achieved so far is 95.63, indicating that we are on the right track with moderate pitch angles and controlled velocities. The focus remains on optimizing the parameters around the successful regions identified in earlier iterations. By introducing new points for the hypotheses, we can further investigate the parameter space and potentially discover configurations that yield even higher scores. The goal is to maintain a balance between pitch, yaw, and velocity while avoiding previously explored configurations that have not performed well. This approach will help us maximize the chances of hitting the target accurately.

### Updated Hypotheses

#### Refined Moderate Pitch and Yaw

*Rationale:* Building on the successful parameters from iteration 49, this hypothesis maintains a moderate pitch and yaw while slightly increasing the initial velocity to explore its effect on score.

*Confidence:* high

*Points:*

- {'pitch_deg': 26, 'yaw_deg': 5, 'v0': 38, 'spin_rpm': 800, 'spin_axis_deg': 30, 'h0': 0.5, 'mass': 6}

#### Lower Spin with Moderate Velocity

*Rationale:* Reducing the spin while maintaining a moderate velocity may stabilize the projectile's flight, potentially improving accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 21, 'yaw_deg': 2, 'v0': 30, 'spin_rpm': 350, 'spin_axis_deg': 10, 'h0': 1, 'mass': 5}

#### Exploring Higher Pitch with Controlled Velocity

*Rationale:* Testing a higher pitch angle with a controlled velocity may allow for a more pronounced arc, which could help in landing closer to the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 36, 'yaw_deg': 1, 'v0': 24, 'spin_rpm': 650, 'spin_axis_deg': 5, 'h0': 1.5, 'mass': 0.9}

#### Aggressive Right Aim with Moderate Parameters

*Rationale:* Testing a slight aggressive right aim while keeping other parameters moderate may help in compensating for any lateral drift observed in previous iterations.

*Confidence:* medium

*Points:*

- {'pitch_deg': 19, 'yaw_deg': 9, 'v0': 29, 'spin_rpm': 750, 'spin_axis_deg': 40, 'h0': 0.8, 'mass': 1.6}

#### New Moderate Velocity Exploration

*Rationale:* Exploring a moderate pitch angle with a slightly higher velocity may yield a better trajectory that covers distance effectively.

*Confidence:* medium

*Points:*

- {'pitch_deg': 20, 'yaw_deg': 3, 'v0': 36, 'spin_rpm': 700, 'spin_axis_deg': 15, 'h0': 1, 'mass': 2}

## Iteration 73

As we reach iteration 72 of the Bayesian Optimization, we have observed that the highest score achieved so far is 95.63 from iteration 49. This indicates that we are effectively exploring the parameter space, particularly around moderate pitch angles (20° to 36°) and controlled velocities (around 30 m/s). The data suggests that configurations with extreme pitch angles (above 60° or below 10°) and aggressive yaw settings have consistently resulted in low scores, indicating these subspaces are detrimental. The most promising subspace appears to be around moderate pitch angles (20° to 30°) and slight yaw adjustments (within ±10°), combined with controlled velocities. Moving forward, I will refine the previous hypotheses to focus on this successful region while discarding those that have consistently yielded poor results. The new hypotheses will explore variations around the successful parameters while introducing new combinations to further investigate the parameter space. This approach aims to maximize the chances of hitting the target accurately by concentrating on the identified effective subspaces.

### Updated Hypotheses

#### Refined Moderate Pitch and Yaw

*Rationale:* Building on the successful parameters from iteration 49, this hypothesis maintains a moderate pitch and yaw while slightly increasing the initial velocity to explore its effect on score.

*Confidence:* high

*Points:*

- {'pitch_deg': 27, 'yaw_deg': 5, 'v0': 39, 'spin_rpm': 800, 'spin_axis_deg': 30, 'h0': 0.5, 'mass': 6}

#### Lower Spin with Moderate Velocity

*Rationale:* Reducing the spin while maintaining a moderate velocity may stabilize the projectile's flight, potentially improving accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 21, 'yaw_deg': 2, 'v0': 30, 'spin_rpm': 300, 'spin_axis_deg': 10, 'h0': 1, 'mass': 5}

#### Exploring Higher Pitch with Controlled Velocity

*Rationale:* Testing a higher pitch angle with a controlled velocity may allow for a more pronounced arc, which could help in landing closer to the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 36, 'yaw_deg': 0, 'v0': 24, 'spin_rpm': 600, 'spin_axis_deg': 0, 'h0': 1.5, 'mass': 0.9}

#### Aggressive Right Aim with Moderate Parameters

*Rationale:* Testing a slight aggressive right aim while keeping other parameters moderate may help in compensating for any lateral drift observed in previous iterations.

*Confidence:* medium

*Points:*

- {'pitch_deg': 19, 'yaw_deg': 8, 'v0': 29, 'spin_rpm': 700, 'spin_axis_deg': 40, 'h0': 0.8, 'mass': 1.6}

#### New Moderate Velocity Exploration

*Rationale:* Exploring a moderate pitch angle with a slightly higher velocity may yield a better trajectory that covers distance effectively.

*Confidence:* medium

*Points:*

- {'pitch_deg': 20, 'yaw_deg': 3, 'v0': 37, 'spin_rpm': 650, 'spin_axis_deg': 15, 'h0': 1, 'mass': 2}

#### Exploring Low Pitch with Controlled Velocity

*Rationale:* Testing a low pitch angle with a controlled velocity may yield a flat trajectory that covers distance quickly, potentially improving score.

*Confidence:* low

*Points:*

- {'pitch_deg': 9, 'yaw_deg': 0, 'v0': 40, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1, 'mass': 2}

## Iteration 90

As we reach iteration 89 of the Bayesian Optimization, the highest score achieved so far is 95.63 from iteration 49, indicating that we are effectively exploring the parameter space, particularly around moderate pitch angles (20° to 36°) and controlled velocities (around 30 m/s). The data suggests that configurations with extreme pitch angles (above 60° or below 10°) and aggressive yaw settings have consistently resulted in low scores, indicating these subspaces are detrimental. The most promising subspace appears to be around moderate pitch angles (20° to 30°) and slight yaw adjustments (within ±10°), combined with controlled velocities. Moving forward, I will refine the previous hypotheses to focus on this successful region while discarding those that have consistently yielded poor results. The new hypotheses will explore variations around the successful parameters while introducing new combinations to further investigate the parameter space. This approach aims to maximize the chances of hitting the target accurately by concentrating on the identified effective subspaces.

### Updated Hypotheses

#### Refined Moderate Pitch and Yaw

*Rationale:* Building on the successful parameters from iteration 49, this hypothesis maintains a moderate pitch and yaw while slightly increasing the initial velocity to explore its effect on score.

*Confidence:* high

*Points:*

- {'pitch_deg': 28, 'yaw_deg': 5, 'v0': 40, 'spin_rpm': 800, 'spin_axis_deg': 30, 'h0': 0.5, 'mass': 6}

#### Lower Spin with Moderate Velocity

*Rationale:* Reducing the spin while maintaining a moderate velocity may stabilize the projectile's flight, potentially improving accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 22, 'yaw_deg': 2, 'v0': 30, 'spin_rpm': 300, 'spin_axis_deg': 10, 'h0': 1, 'mass': 5}

#### Exploring Higher Pitch with Controlled Velocity

*Rationale:* Testing a higher pitch angle with a controlled velocity may allow for a more pronounced arc, which could help in landing closer to the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 36, 'yaw_deg': 0, 'v0': 25, 'spin_rpm': 600, 'spin_axis_deg': 0, 'h0': 1.5, 'mass': 0.9}

#### Aggressive Right Aim with Moderate Parameters

*Rationale:* Testing a slight aggressive right aim while keeping other parameters moderate may help in compensating for any lateral drift observed in previous iterations.

*Confidence:* medium

*Points:*

- {'pitch_deg': 20, 'yaw_deg': 8, 'v0': 30, 'spin_rpm': 700, 'spin_axis_deg': 40, 'h0': 0.8, 'mass': 1.6}

#### New Moderate Velocity Exploration

*Rationale:* Exploring a moderate pitch angle with a slightly higher velocity may yield a better trajectory that covers distance effectively.

*Confidence:* medium

*Points:*

- {'pitch_deg': 20, 'yaw_deg': 3, 'v0': 38, 'spin_rpm': 650, 'spin_axis_deg': 15, 'h0': 1, 'mass': 2}

#### Exploring Low Pitch with Controlled Velocity

*Rationale:* Testing a low pitch angle with a controlled velocity may yield a flat trajectory that covers distance quickly, potentially improving score.

*Confidence:* low

*Points:*

- {'pitch_deg': 8, 'yaw_deg': 0, 'v0': 42, 'spin_rpm': 750, 'spin_axis_deg': 0, 'h0': 1.2, 'mass': 2.5}

## Final Conclusions

Throughout the optimization process, the hypotheses evolved significantly based on the experimental data collected from each iteration. Initially, the hypotheses were broad, exploring a wide range of parameter combinations, including extreme values for pitch and yaw angles. However, as we gathered data, it became clear that configurations with moderate pitch angles (around 20° to 36°) and controlled velocities (approximately 30 m/s) yielded the highest scores, particularly the peak score of 95.63.

The insights gained from iterations indicated that extreme pitch angles and aggressive yaw settings consistently resulted in low scores, leading to a strategic shift in focus. Subsequent hypotheses were refined to concentrate on the successful regions identified in earlier iterations, emphasizing moderate parameters while systematically adjusting other variables like initial velocity and spin. This iterative learning process allowed us to discard less effective configurations and hone in on combinations that maximized the chances of hitting the target accurately.

The following table summarizes the evolution of confidence in the hypotheses throughout the optimization:

| Iteration | Hypothesis Name                          | Initial Confidence | Final Confidence |
|-----------|-----------------------------------------|--------------------|------------------|
| 1         | Low Angle, High Velocity                | Medium             | Low              |
| 2         | Optimal Height and Moderate Spin        | High                | Medium           |
| 3         | High Angle, Low Velocity                | Medium             | Low              |
| 4         | Balanced Approach                       | High                | Medium           |
| 5         | Aggressive Left Aim                     | Medium             | Low              |
| 6         | Refined Moderate Pitch and Yaw          | High                | High             |
| 7         | Lower Spin with Moderate Velocity       | Medium             | High             |
| 8         | Exploring Higher Pitch with Controlled Velocity | Medium      | Medium           |
| 9         | Aggressive Right Aim with Moderate Parameters | Medium        | Medium           |
| 10        | New Low Pitch Exploration               | Low                | Low              |

This table illustrates the transition from initial hypotheses to more focused and confident predictions based on empirical results, ultimately leading to a more effective optimization strategy.
# Projectile

## Experiment Overview

The goal of this experiment is to maximize the score, which reflects how closely a projectile lands to a target located at (50, 0) after being thrown from the origin (0, 0). The score is derived from the distance error between the landing position and the target, with higher scores indicating better performance. 

To achieve this, we will optimize several parameters: pitch_deg (release angle), yaw_deg (horizontal aiming angle), v0 (initial velocity), spin_rpm (spin rate), spin_axis_deg (orientation of the spin axis), h0 (release height), and mass of the projectile. Each parameter has defined bounds, ensuring that the exploration remains within realistic and physically meaningful limits.

Bayesian Optimization (BO) will be employed to systematically explore this multi-dimensional parameter space. BO will utilize a probabilistic model to predict the score based on previous trials, allowing it to suggest new parameter settings that are likely to yield higher scores. When the optimization process plateaus, I will provide insights and hypotheses to guide further exploration, such as adjusting parameters that have shown promise or exploring untested regions of the parameter space. The intended outcome is to identify the optimal parameter settings that maximize the score, ultimately achieving a successful throw that lands closest to the target.

## Initial Thoughts

In this initial sampling step, we aim to explore diverse regions of the parameter space to gather valuable data for Bayesian Optimization. The hypotheses are designed to cover a range of angles, velocities, and other parameters that could influence the projectile's trajectory. A moderate launch angle around 30 degrees is often optimal for maximizing range in projectile motion, balancing vertical and horizontal components. Additionally, a low pitch angle combined with high initial velocity may allow the projectile to travel fast and cover more horizontal distance quickly. Launching vertically with significant spin may stabilize the projectile and allow it to descend closer to the target. Aiming slightly left with a moderate height may help in compensating for any lateral drift due to wind or spin effects. Finally, a balanced approach with moderate parameters across the board may yield a reliable score, allowing for a comprehensive understanding of interactions. By strategically selecting these points, we can identify promising areas for further exploration and refine our understanding of how each parameter affects the score.
### Initial Hypotheses

#### Moderate Launch Angle

*Rationale:* A moderate pitch angle of around 30 degrees is often optimal for maximizing range in projectile motion, balancing vertical and horizontal components.

*Confidence:* high

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 0, 'v0': 25, 'spin_rpm': 1500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### High Velocity, Low Angle

*Rationale:* A low pitch angle combined with high initial velocity may allow the projectile to travel fast and cover more horizontal distance quickly.

*Confidence:* medium

*Points:*

- {'pitch_deg': 10, 'yaw_deg': 0, 'v0': 45, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 0.5, 'mass': 0.5}

#### Vertical Launch with Spin

*Rationale:* Launching vertically with significant spin may stabilize the projectile and allow it to descend closer to the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 80, 'yaw_deg': 0, 'v0': 20, 'spin_rpm': 2500, 'spin_axis_deg': 90, 'h0': 2, 'mass': 0.1}

#### Leftward Aim with Moderate Height

*Rationale:* Aiming slightly left with a moderate height may help in compensating for any lateral drift due to wind or spin effects.

*Confidence:* medium

*Points:*

- {'pitch_deg': 45, 'yaw_deg': -15, 'v0': 30, 'spin_rpm': 500, 'spin_axis_deg': 0, 'h0': 1.5, 'mass': 2}

#### Balanced Approach

*Rationale:* A balanced approach with moderate parameters across the board may yield a reliable score, allowing for a comprehensive understanding of interactions.

*Confidence:* high

*Points:*

- {'pitch_deg': 40, 'yaw_deg': 5, 'v0': 35, 'spin_rpm': 1200, 'spin_axis_deg': 45, 'h0': 1, 'mass': 1.5}

## Iteration 12

As we progress through iteration 11 of the Bayesian Optimization, we observe that the highest score achieved so far is 49, from the hypothesis with pitch_deg 40, yaw_deg 5, v0 35, spin_rpm 1200, spin_axis_deg 45, h0 1, and mass 1.5. This suggests that moderate pitch and yaw angles, combined with a balanced initial velocity and spin, are promising. Conversely, several configurations with extreme angles (e.g., pitch_deg 80, yaw_deg -138.04) and high spin rates have resulted in very low scores, indicating that these regions of the parameter space are detrimental. The data suggests that the subspace around pitch angles between 30 and 45 degrees, yaw angles close to 0, and moderate velocities (around 30-35 m/s) may yield better results. We will discard hypotheses that consistently performed poorly, such as those with extreme yaw angles and high spin rates, and propose new hypotheses focusing on the promising regions identified. The next hypotheses will aim to refine the parameters based on the successful configurations observed, particularly emphasizing moderate pitch and yaw angles while exploring slight variations in velocity and spin to maximize the score.

### Updated Hypotheses

#### Refined Moderate Launch Angle

*Rationale:* Building on the previous successful configuration, we will maintain a moderate pitch angle and adjust yaw slightly to explore its effect.

*Confidence:* high

*Points:*

- {'pitch_deg': 35, 'yaw_deg': 2, 'v0': 34, 'spin_rpm': 1200, 'spin_axis_deg': 30, 'h0': 1, 'mass': 1.5}

#### Balanced Approach with Higher Velocity

*Rationale:* Increasing the initial velocity while keeping other parameters balanced may help achieve a better score.

*Confidence:* medium

*Points:*

- {'pitch_deg': 40, 'yaw_deg': 0, 'v0': 40, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Slightly Elevated Launch

*Rationale:* Testing a slightly higher launch angle with moderate velocity may help in achieving a better trajectory.

*Confidence:* medium

*Points:*

- {'pitch_deg': 45, 'yaw_deg': 0, 'v0': 30, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1.5, 'mass': 1.2}

#### Low Angle with Increased Spin

*Rationale:* Exploring a low pitch angle with increased spin may stabilize the projectile and improve landing accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 15, 'yaw_deg': 0, 'v0': 35, 'spin_rpm': 2000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 0.8}

#### Exploring Higher Yaw with Moderate Pitch

*Rationale:* Testing a higher yaw angle while keeping a moderate pitch may help in compensating for lateral drift.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 10, 'v0': 32, 'spin_rpm': 1200, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1.5}

## Iteration 23

As we reach iteration 22 of the Bayesian Optimization, we have gathered valuable insights from the experimental data. The highest score achieved so far is 90.53 from the configuration with pitch_deg 18.48, yaw_deg 2.03, v0 37.36, spin_rpm 1996.69, spin_axis_deg 13.21, h0 1.00, and mass 0.30. This suggests that lower pitch angles combined with slight yaw adjustments can yield better results, likely due to a more favorable trajectory. The subspace around pitch angles between 15 and 30 degrees, with yaw angles close to 0 or slightly positive, appears to maximize the score. Conversely, configurations with extreme yaw angles (e.g., yaw_deg -138.04) and high spin rates have consistently resulted in very low scores, indicating these regions are detrimental.     Moving forward, I will refine the previous hypotheses by focusing on the promising regions identified, particularly lower pitch angles and moderate velocities. I will discard hypotheses that have performed poorly, such as those with extreme yaw angles and high spin rates. New hypotheses will explore slight variations in pitch and yaw while maintaining moderate velocities and spins to maximize the score. The next hypotheses will aim to further explore the successful configurations while ensuring we remain within the identified optimal subspaces.

### Updated Hypotheses

#### Low Pitch with Moderate Velocity

*Rationale:* Exploring lower pitch angles with moderate velocity may yield a favorable trajectory, as indicated by previous successful configurations.

*Confidence:* high

*Points:*

- {'pitch_deg': 20, 'yaw_deg': 2, 'v0': 35, 'spin_rpm': 1200, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Slightly Elevated Launch with Low Spin

*Rationale:* Testing a slightly elevated launch angle with low spin may help in achieving a better trajectory while maintaining stability.

*Confidence:* medium

*Points:*

- {'pitch_deg': 25, 'yaw_deg': 0, 'v0': 30, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1.5, 'mass': 1.2}

#### Moderate Pitch with Increased Yaw

*Rationale:* Exploring a moderate pitch angle with increased yaw may help in compensating for lateral drift while maintaining a favorable trajectory.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 5, 'v0': 32, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1.5}

#### Low Angle with High Stability

*Rationale:* Testing a low pitch angle with increased stability through lower spin may improve landing accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 15, 'yaw_deg': 0, 'v0': 30, 'spin_rpm': 500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 0.8}

#### Exploring Higher Velocity with Low Pitch

*Rationale:* Increasing the initial velocity while keeping a low pitch angle may help achieve a better score, as higher speeds can improve distance.

*Confidence:* medium

*Points:*

- {'pitch_deg': 18, 'yaw_deg': 0, 'v0': 40, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

## Iteration 36

As we reach iteration 35 of the Bayesian Optimization, we have gathered significant insights from the experimental data. The highest score achieved so far is 90.53, indicating that lower pitch angles (around 18-20 degrees) combined with slight yaw adjustments (close to 0 or slightly positive) and moderate velocities (around 35-40 m/s) yield the best results. The data suggests that configurations with pitch angles between 15 and 25 degrees and yaw angles close to 0 are particularly promising. Conversely, configurations with extreme yaw angles, high spin rates, and very high or very low pitch angles have consistently resulted in low scores, indicating these regions are detrimental. Moving forward, I will refine the previous hypotheses by focusing on the successful regions identified, particularly lower pitch angles and moderate velocities, while discarding hypotheses that have performed poorly. New hypotheses will explore slight variations in pitch and yaw while maintaining moderate velocities and spins to maximize the score. The promising subspaces identified include pitch angles around 18-20 degrees, yaw angles between 0 and 5 degrees, and velocities around 35-40 m/s. We will continue to explore these regions to further optimize the projectile's trajectory.

### Updated Hypotheses

#### Optimized Low Pitch with Moderate Velocity

*Rationale:* Exploring lower pitch angles with moderate velocity has shown to yield favorable trajectories, as indicated by previous successful configurations.

*Confidence:* high

*Points:*

- {'pitch_deg': 19, 'yaw_deg': 1, 'v0': 36, 'spin_rpm': 1200, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Slightly Elevated Launch with Low Spin

*Rationale:* Testing a slightly elevated launch angle with low spin may help in achieving a better trajectory while maintaining stability.

*Confidence:* medium

*Points:*

- {'pitch_deg': 22, 'yaw_deg': 0, 'v0': 30, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1.5, 'mass': 1.2}

#### Moderate Pitch with Increased Yaw

*Rationale:* Exploring a moderate pitch angle with increased yaw may help in compensating for lateral drift while maintaining a favorable trajectory.

*Confidence:* medium

*Points:*

- {'pitch_deg': 25, 'yaw_deg': 3, 'v0': 32, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1.5}

#### Low Angle with High Stability

*Rationale:* Testing a low pitch angle with increased stability through lower spin may improve landing accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 15, 'yaw_deg': 2, 'v0': 28, 'spin_rpm': 600, 'spin_axis_deg': 0, 'h0': 1.2, 'mass': 0.9}

#### Exploring Higher Velocity with Low Pitch

*Rationale:* Increasing the initial velocity while keeping a low pitch angle may help achieve a better score, as higher speeds can improve distance.

*Confidence:* medium

*Points:*

- {'pitch_deg': 18, 'yaw_deg': 1, 'v0': 42, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

## Iteration 51

As we reach iteration 50 of the Bayesian Optimization, we have gathered substantial insights from the experimental data. The highest score achieved so far is 90.53, indicating that lower pitch angles (around 18-20 degrees) combined with slight yaw adjustments (close to 0 or slightly positive) and moderate velocities (around 35-40 m/s) yield the best results. The data suggests that configurations with pitch angles between 15 and 25 degrees and yaw angles close to 0 are particularly promising. Conversely, configurations with extreme yaw angles, high spin rates, and very high or very low pitch angles have consistently resulted in low scores, indicating these regions are detrimental. Moving forward, I will refine the previous hypotheses by focusing on the successful regions identified, particularly lower pitch angles and moderate velocities, while discarding hypotheses that have performed poorly. New hypotheses will explore slight variations in pitch and yaw while maintaining moderate velocities and spins to maximize the score. The promising subspaces identified include pitch angles around 18-20 degrees, yaw angles between 0 and 5 degrees, and velocities around 35-40 m/s. We will continue to explore these regions to further optimize the projectile's trajectory.

### Updated Hypotheses

#### Optimized Low Pitch with Moderate Velocity

*Rationale:* Exploring lower pitch angles with moderate velocity has shown to yield favorable trajectories, as indicated by previous successful configurations.

*Confidence:* high

*Points:*

- {'pitch_deg': 19, 'yaw_deg': 2, 'v0': 36, 'spin_rpm': 1200, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Slightly Elevated Launch with Low Spin

*Rationale:* Testing a slightly elevated launch angle with low spin may help in achieving a better trajectory while maintaining stability.

*Confidence:* medium

*Points:*

- {'pitch_deg': 23, 'yaw_deg': 1, 'v0': 30, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1.5, 'mass': 1.2}

#### Moderate Pitch with Increased Yaw

*Rationale:* Exploring a moderate pitch angle with increased yaw may help in compensating for lateral drift while maintaining a favorable trajectory.

*Confidence:* medium

*Points:*

- {'pitch_deg': 26, 'yaw_deg': 4, 'v0': 32, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1.5}

#### Low Angle with High Stability

*Rationale:* Testing a low pitch angle with increased stability through lower spin may improve landing accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 15, 'yaw_deg': 1, 'v0': 30, 'spin_rpm': 600, 'spin_axis_deg': 0, 'h0': 1, 'mass': 0.9}

#### Exploring Higher Velocity with Low Pitch

*Rationale:* Increasing the initial velocity while keeping a low pitch angle may help achieve a better score, as higher speeds can improve distance.

*Confidence:* medium

*Points:*

- {'pitch_deg': 18, 'yaw_deg': 1, 'v0': 40, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Refined Low Pitch with Slightly Higher Yaw

*Rationale:* Testing a low pitch angle with a slight increase in yaw may help in fine-tuning the trajectory for better accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 20, 'yaw_deg': 4, 'v0': 35, 'spin_rpm': 900, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

## Iteration 66

As we reach iteration 65 of the Bayesian Optimization, we have gathered substantial insights from the experimental data. The highest score achieved so far is 90.53, from the configuration with pitch_deg 18.48, yaw_deg 2.03, v0 37.36, spin_rpm 1996.69, spin_axis_deg 13.21, h0 1.00, and mass 0.30. This indicates that lower pitch angles (around 18-20 degrees) combined with slight yaw adjustments (close to 0 or slightly positive) and moderate velocities (around 35-40 m/s) yield the best results. The data suggests that configurations with pitch angles between 15 and 25 degrees and yaw angles close to 0 are particularly promising. Conversely, configurations with extreme yaw angles, high spin rates, and very high or very low pitch angles have consistently resulted in low scores, indicating these regions are detrimental. Moving forward, I will refine the previous hypotheses by focusing on the successful regions identified, particularly lower pitch angles and moderate velocities, while discarding hypotheses that have performed poorly. New hypotheses will explore slight variations in pitch and yaw while maintaining moderate velocities and spins to maximize the score. The promising subspaces identified include pitch angles around 18-20 degrees, yaw angles between 0 and 5 degrees, and velocities around 35-40 m/s. We will continue to explore these regions to further optimize the projectile's trajectory.

### Updated Hypotheses

#### Optimized Low Pitch with Moderate Velocity

*Rationale:* Exploring lower pitch angles with moderate velocity has shown to yield favorable trajectories, as indicated by previous successful configurations.

*Confidence:* high

*Points:*

- {'pitch_deg': 19, 'yaw_deg': 3, 'v0': 36, 'spin_rpm': 1200, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Refined Low Pitch with Slightly Higher Yaw

*Rationale:* Testing a low pitch angle with a slight increase in yaw may help in fine-tuning the trajectory for better accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 20, 'yaw_deg': 3, 'v0': 35, 'spin_rpm': 900, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Slightly Elevated Launch with Low Spin

*Rationale:* Testing a slightly elevated launch angle with low spin may help in achieving a better trajectory while maintaining stability.

*Confidence:* medium

*Points:*

- {'pitch_deg': 22, 'yaw_deg': 1, 'v0': 30, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1.5, 'mass': 1.2}

#### Moderate Pitch with Increased Yaw

*Rationale:* Exploring a moderate pitch angle with increased yaw may help in compensating for lateral drift while maintaining a favorable trajectory.

*Confidence:* medium

*Points:*

- {'pitch_deg': 25, 'yaw_deg': 4, 'v0': 32, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1.5}

#### Low Angle with High Stability

*Rationale:* Testing a low pitch angle with increased stability through lower spin may improve landing accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 16, 'yaw_deg': 2, 'v0': 30, 'spin_rpm': 600, 'spin_axis_deg': 0, 'h0': 1, 'mass': 0.9}

#### Exploring Higher Velocity with Low Pitch

*Rationale:* Increasing the initial velocity while keeping a low pitch angle may help achieve a better score, as higher speeds can improve distance.

*Confidence:* medium

*Points:*

- {'pitch_deg': 18, 'yaw_deg': 2, 'v0': 40, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

## Iteration 80

As we reach iteration 79 of the Bayesian Optimization, we have gathered substantial insights from the experimental data. The highest score achieved so far is 90.53, from the configuration with pitch_deg 18.48, yaw_deg 2.03, v0 37.36, spin_rpm 1996.69, spin_axis_deg 13.21, h0 1.00, and mass 0.30. This indicates that lower pitch angles (around 18-20 degrees) combined with slight yaw adjustments (close to 0 or slightly positive) and moderate velocities (around 35-40 m/s) yield the best results. The data suggests that configurations with pitch angles between 15 and 25 degrees and yaw angles close to 0 are particularly promising. Conversely, configurations with extreme yaw angles, high spin rates, and very high or very low pitch angles have consistently resulted in low scores, indicating these regions are detrimental. Moving forward, I will refine the previous hypotheses by focusing on the successful regions identified, particularly lower pitch angles and moderate velocities, while discarding hypotheses that have performed poorly. New hypotheses will explore slight variations in pitch and yaw while maintaining moderate velocities and spins to maximize the score. The promising subspaces identified include pitch angles around 18-20 degrees, yaw angles between 0 and 5 degrees, and velocities around 35-40 m/s. We will continue to explore these regions to further optimize the projectile's trajectory.

### Updated Hypotheses

#### Optimized Low Pitch with Moderate Velocity

*Rationale:* Exploring lower pitch angles with moderate velocity has shown to yield favorable trajectories, as indicated by previous successful configurations.

*Confidence:* high

*Points:*

- {'pitch_deg': 19, 'yaw_deg': 4, 'v0': 36, 'spin_rpm': 1200, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Refined Low Pitch with Slightly Higher Yaw

*Rationale:* Testing a low pitch angle with a slight increase in yaw may help in fine-tuning the trajectory for better accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 21, 'yaw_deg': 5, 'v0': 35, 'spin_rpm': 900, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Slightly Elevated Launch with Low Spin

*Rationale:* Testing a slightly elevated launch angle with low spin may help in achieving a better trajectory while maintaining stability.

*Confidence:* medium

*Points:*

- {'pitch_deg': 23, 'yaw_deg': 2, 'v0': 30, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1.5, 'mass': 1.2}

#### Moderate Pitch with Increased Yaw

*Rationale:* Exploring a moderate pitch angle with increased yaw may help in compensating for lateral drift while maintaining a favorable trajectory.

*Confidence:* medium

*Points:*

- {'pitch_deg': 26, 'yaw_deg': 5, 'v0': 32, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1.5}

#### Low Angle with High Stability

*Rationale:* Testing a low pitch angle with increased stability through lower spin may improve landing accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 15, 'yaw_deg': 3, 'v0': 30, 'spin_rpm': 600, 'spin_axis_deg': 0, 'h0': 1, 'mass': 0.9}

#### Exploring Higher Velocity with Low Pitch

*Rationale:* Increasing the initial velocity while keeping a low pitch angle may help achieve a better score, as higher speeds can improve distance.

*Confidence:* medium

*Points:*

- {'pitch_deg': 18, 'yaw_deg': 3, 'v0': 41, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

## Iteration 95

As we reach iteration 94 of the Bayesian Optimization, we have gathered substantial insights from the experimental data. The highest score achieved so far is 90.53, from the configuration with pitch_deg 18.48, yaw_deg 2.03, v0 37.36, spin_rpm 1996.69, spin_axis_deg 13.21, h0 1.00, and mass 0.30. This indicates that lower pitch angles (around 18-20 degrees) combined with slight yaw adjustments (close to 0 or slightly positive) and moderate velocities (around 35-40 m/s) yield the best results. The data suggests that configurations with pitch angles between 15 and 25 degrees and yaw angles close to 0 are particularly promising. Conversely, configurations with extreme yaw angles, high spin rates, and very high or very low pitch angles have consistently resulted in low scores, indicating these regions are detrimental. Moving forward, I will refine the previous hypotheses by focusing on the successful regions identified, particularly lower pitch angles and moderate velocities, while discarding hypotheses that have performed poorly. New hypotheses will explore slight variations in pitch and yaw while maintaining moderate velocities and spins to maximize the score. The promising subspaces identified include pitch angles around 18-20 degrees, yaw angles between 0 and 5 degrees, and velocities around 35-40 m/s. We will continue to explore these regions to further optimize the projectile's trajectory.

### Updated Hypotheses

#### Refined Low Pitch with Slightly Higher Yaw

*Rationale:* Testing a low pitch angle with a slight increase in yaw may help in fine-tuning the trajectory for better accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 20, 'yaw_deg': 5, 'v0': 35, 'spin_rpm': 900, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Slightly Elevated Launch with Low Spin

*Rationale:* Testing a slightly elevated launch angle with low spin may help in achieving a better trajectory while maintaining stability.

*Confidence:* medium

*Points:*

- {'pitch_deg': 22, 'yaw_deg': 2, 'v0': 31, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1.5, 'mass': 1.2}

#### Moderate Pitch with Increased Yaw

*Rationale:* Exploring a moderate pitch angle with increased yaw may help in compensating for lateral drift while maintaining a favorable trajectory.

*Confidence:* medium

*Points:*

- {'pitch_deg': 25, 'yaw_deg': 4, 'v0': 33, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1.5}

#### Low Angle with High Stability

*Rationale:* Testing a low pitch angle with increased stability through lower spin may improve landing accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 15, 'yaw_deg': 3, 'v0': 29, 'spin_rpm': 600, 'spin_axis_deg': 0, 'h0': 1, 'mass': 0.9}

#### Exploring Higher Velocity with Low Pitch

*Rationale:* Increasing the initial velocity while keeping a low pitch angle may help achieve a better score, as higher speeds can improve distance.

*Confidence:* medium

*Points:*

- {'pitch_deg': 18, 'yaw_deg': 4, 'v0': 41, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

## Final Conclusions

Throughout the optimization process, the hypotheses evolved significantly based on the experimental data collected from each iteration. Initially, the hypotheses explored a wide range of parameter settings, including extreme angles and velocities. However, as we gathered data, it became clear that lower pitch angles (around 18-20 degrees) combined with slight yaw adjustments (close to 0 or slightly positive) and moderate velocities (35-40 m/s) yielded the best results, with the highest score reaching 90.53.

The insights gained from the experiments led to a more focused approach, discarding configurations that consistently performed poorly, such as those with extreme yaw angles and high spin rates. The hypotheses were refined to emphasize lower pitch angles and moderate velocities, while exploring slight variations in yaw and spin. This iterative process allowed us to hone in on the most promising regions of the parameter space, ultimately leading to a more effective optimization strategy.

The following table summarizes the evolution of confidence in the hypotheses throughout the optimization:

| Iteration | Hypothesis Name                               | Confidence Level |
|-----------|-----------------------------------------------|------------------|
| 1         | Moderate Launch Angle                         | High             |
| 12        | Refined Moderate Launch Angle                 | High             |
| 23        | Low Pitch with Moderate Velocity              | High             |
| 36        | Optimized Low Pitch with Moderate Velocity    | High             |
| 51        | Refined Low Pitch with Slightly Higher Yaw   | Medium           |
| 66        | Optimized Low Pitch with Moderate Velocity    | High             |
| 80        | Refined Low Pitch with Slightly Higher Yaw   | Medium           |
| 95        | Refined Low Pitch with Slightly Higher Yaw   | Medium           |
| Final     | Optimized Low Pitch with Moderate Velocity    | High             |
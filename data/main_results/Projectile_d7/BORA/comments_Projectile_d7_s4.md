# Projectile

## Experiment Overview

The goal of this experiment is to maximize the score, which reflects the accuracy of a projectile thrown from the origin (0, 0) toward a target located at (50, 0). The score is derived from the distance error between the projectile's landing position and the target, with higher scores indicating closer landings. 

To achieve this, we will optimize several parameters: pitch_deg (release angle), yaw_deg (horizontal aiming angle), v0 (initial velocity), spin_rpm (spin rate), spin_axis_deg (orientation of the spin axis), h0 (release height), and mass of the projectile. Each parameter has defined bounds, ensuring a systematic exploration of the parameter space while adhering to physical constraints.

Bayesian Optimization (BO) will be employed to efficiently navigate this multi-dimensional space, leveraging a probabilistic model to predict the score based on current parameter settings. As BO iteratively samples points, it will identify regions of interest and suggest new parameter combinations. When the optimization process plateaus, I will provide insights to explore unexplored areas or adjust the search strategy, focusing on conditions that maximize the score. The intended outcome is to identify the optimal parameter settings that yield the highest score, effectively hitting the target.

## Initial Thoughts

In this initial sampling step, we aim to explore diverse regions of the parameter space to gather valuable data for Bayesian Optimization. The hypotheses are designed to cover a range of angles, velocities, and other parameters that could influence the projectile's trajectory. By strategically selecting points, we can identify promising areas that may lead to higher scores. The initial hypotheses reflect a balance between high angles for potential height and lower angles for distance, as well as varying velocities and spins to understand their effects on landing accuracy. Notably, the maximum score of 100 is achievable when the projectile lands directly on the target at (50, 0). The proposed points consider both high and low launch angles, moderate to high velocities, and the introduction of spin to stabilize the flight path. This comprehensive approach will help us identify optimal parameter settings that maximize the score effectively.
### Initial Hypotheses

#### High Angle Launch

*Rationale:* Launching at a high angle may maximize vertical distance, allowing the projectile to cover more horizontal distance before descending.

*Confidence:* medium

*Points:*

- {'pitch_deg': 80, 'yaw_deg': 0, 'v0': 30, 'spin_rpm': 1500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Moderate Velocity with Low Angle

*Rationale:* A lower launch angle combined with moderate velocity may provide a good balance for reaching the target without overshooting.

*Confidence:* high

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 5, 'v0': 25, 'spin_rpm': 1000, 'spin_axis_deg': 10, 'h0': 0.5, 'mass': 0.5}

#### Straight Shot with High Velocity

*Rationale:* Aiming straight with high velocity could lead to a direct hit on the target, minimizing distance error.

*Confidence:* high

*Points:*

- {'pitch_deg': 0, 'yaw_deg': 0, 'v0': 45, 'spin_rpm': 0, 'spin_axis_deg': 0, 'h0': 0, 'mass': 2}

#### Spin for Stability

*Rationale:* Introducing spin may stabilize the projectile's flight, potentially improving accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 45, 'yaw_deg': -10, 'v0': 35, 'spin_rpm': 2000, 'spin_axis_deg': 90, 'h0': 1.5, 'mass': 0.8}

#### Low Launch Height

*Rationale:* A lower launch height may reduce the time in the air, allowing for a quicker descent towards the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 15, 'yaw_deg': 10, 'v0': 20, 'spin_rpm': 500, 'spin_axis_deg': -30, 'h0': 0.2, 'mass': 0.3}

## Iteration 12

Analyzing the results from the first 11 iterations reveals that the optimization process is still developing, with scores ranging from 0.00 to 29.08. The highest score achieved was 29.08, obtained with a moderate pitch angle of 30° and a low initial velocity of 25 m/s. This suggests that a balance between angle and speed is crucial for accuracy. The data indicates that extreme angles (both high and low) and certain yaw angles, particularly those leading to negative values, have not yielded favorable results, as seen in iterations 1, 3, 4, 5, 6, 7, 8, 9, and 10, which produced low scores. The subspaces that seem to maximize the score are those with moderate pitch angles (around 30°) and controlled velocities, while detrimental subspaces include extreme yaw angles and high spin rates that may destabilize the projectile. Moving forward, I will refine the previous hypotheses, discarding those that consistently performed poorly and proposing new ones based on the observed data trends. The focus will be on maintaining moderate angles and velocities while exploring slight variations in spin and height to improve accuracy.

### Updated Hypotheses

#### Moderate Angle and Velocity

*Rationale:* Building on the successful parameters from iteration 2, this hypothesis aims to maintain a moderate pitch and velocity for optimal accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 35, 'yaw_deg': 0, 'v0': 28, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 0.5, 'mass': 0.5}

#### Low Angle with Increased Velocity

*Rationale:* Exploring a slightly lower angle with increased velocity may help in achieving a better trajectory towards the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 20, 'yaw_deg': 5, 'v0': 32, 'spin_rpm': 1500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 0.7}

#### Controlled Spin for Stability

*Rationale:* Introducing a moderate spin rate may stabilize the projectile's flight, potentially improving accuracy without excessive deviation.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': -5, 'v0': 30, 'spin_rpm': 1200, 'spin_axis_deg': 0, 'h0': 1, 'mass': 0.6}

#### Higher Launch Height

*Rationale:* Testing a higher launch height with a moderate angle may allow for a better arc and improved landing accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 40, 'yaw_deg': 0, 'v0': 25, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1.5, 'mass': 0.5}

#### Exploring Negative Yaw

*Rationale:* While previous attempts with extreme yaw angles were unsuccessful, a controlled negative yaw may help in fine-tuning the trajectory.

*Confidence:* low

*Points:*

- {'pitch_deg': 25, 'yaw_deg': -10, 'v0': 30, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 0.5, 'mass': 0.4}

## Iteration 22

As we continue to analyze the optimization process, it is clear that the exploration of the parameter space is yielding valuable insights. The highest score achieved remains at 45.92, indicating that we are honing in on effective parameter combinations. The data suggests that maintaining moderate pitch angles (around 30° to 40°) and controlled velocities (around 25 m/s) are key to maximizing accuracy. The subspaces that have shown promise include moderate pitch angles with low to moderate velocities, while extreme angles and high spin rates have consistently resulted in low scores. Moving forward, I will refine the hypotheses to ensure they explore new points that have not been previously tested, focusing on combinations that balance angle, velocity, and spin for improved accuracy.

### Updated Hypotheses

#### Moderate Pitch and Velocity

*Rationale:* Building on the successful parameters from previous iterations, this hypothesis aims to maintain a moderate pitch and velocity for optimal accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 36, 'yaw_deg': 2, 'v0': 27, 'spin_rpm': 900, 'spin_axis_deg': 0, 'h0': 0.6, 'mass': 0.5}

#### Optimal Angle with Low Velocity

*Rationale:* Exploring a slightly lower angle with a reduced velocity may help in achieving a better trajectory towards the target without overshooting.

*Confidence:* medium

*Points:*

- {'pitch_deg': 24, 'yaw_deg': 3, 'v0': 19, 'spin_rpm': 850, 'spin_axis_deg': 0, 'h0': 1.2, 'mass': 0.6}

#### Controlled Spin for Stability

*Rationale:* Introducing a moderate spin rate may stabilize the projectile's flight, potentially improving accuracy without excessive deviation.

*Confidence:* medium

*Points:*

- {'pitch_deg': 31, 'yaw_deg': -4, 'v0': 29, 'spin_rpm': 1100, 'spin_axis_deg': 0, 'h0': 1, 'mass': 0.7}

#### Higher Launch Height with Moderate Angle

*Rationale:* Testing a higher launch height with a moderate angle may allow for a better arc and improved landing accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 42, 'yaw_deg': 1, 'v0': 26, 'spin_rpm': 750, 'spin_axis_deg': 0, 'h0': 1.8, 'mass': 0.5}

#### Exploring Slightly Negative Yaw

*Rationale:* While previous attempts with extreme yaw angles were unsuccessful, a controlled negative yaw may help in fine-tuning the trajectory.

*Confidence:* low

*Points:*

- {'pitch_deg': 29, 'yaw_deg': -6, 'v0': 28, 'spin_rpm': 950, 'spin_axis_deg': 0, 'h0': 0.7, 'mass': 0.4}

## Iteration 35

As we analyze the results from the first 34 iterations, we are making significant progress in identifying effective parameter combinations. The highest score achieved so far is 45.92, obtained with a pitch angle of 40°, a yaw angle of 0°, and an initial velocity of 25 m/s. This indicates that moderate pitch angles (around 30° to 42°) and controlled velocities (around 25 m/s) are key to maximizing accuracy. The subspaces that have shown promise include moderate pitch angles with low to moderate velocities, while extreme angles (both high and low) and high spin rates have consistently resulted in low scores. Notably, attempts with negative yaw angles have not yielded favorable results, suggesting they may destabilize the projectile. Moving forward, I will refine the hypotheses to focus on combinations that balance angle, velocity, and spin for improved accuracy, while discarding those that have consistently performed poorly. The next steps will involve exploring slightly higher pitch angles and controlled velocities, as well as testing different launch heights to optimize the trajectory towards the target.

### Updated Hypotheses

#### Moderate Pitch and Velocity

*Rationale:* Building on the successful parameters from previous iterations, this hypothesis aims to maintain a moderate pitch and velocity for optimal accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 38, 'yaw_deg': 0, 'v0': 26, 'spin_rpm': 900, 'spin_axis_deg': 0, 'h0': 0.6, 'mass': 0.5}

#### Optimal Angle with Controlled Velocity

*Rationale:* Exploring a slightly higher angle with a controlled velocity may help in achieving a better trajectory towards the target without overshooting.

*Confidence:* medium

*Points:*

- {'pitch_deg': 41, 'yaw_deg': 1, 'v0': 24, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1.2, 'mass': 0.6}

#### Higher Launch Height with Moderate Angle

*Rationale:* Testing a higher launch height with a moderate angle may allow for a better arc and improved landing accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 42, 'yaw_deg': 0, 'v0': 25, 'spin_rpm': 750, 'spin_axis_deg': 0, 'h0': 1.8, 'mass': 0.5}

#### Exploring Slightly Positive Yaw

*Rationale:* While previous attempts with extreme yaw angles were unsuccessful, a controlled positive yaw may help in fine-tuning the trajectory.

*Confidence:* low

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 5, 'v0': 28, 'spin_rpm': 950, 'spin_axis_deg': 0, 'h0': 0.7, 'mass': 0.4}

#### Controlled Spin for Stability

*Rationale:* Introducing a moderate spin rate may stabilize the projectile's flight, potentially improving accuracy without excessive deviation.

*Confidence:* medium

*Points:*

- {'pitch_deg': 35, 'yaw_deg': -2, 'v0': 27, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 0.5}

## Iteration 47

As we analyze the results from the first 46 iterations, we observe that the optimization process is yielding valuable insights into effective parameter combinations. The highest score achieved is 50.20, obtained with a pitch angle of 41°, a yaw angle of 1°, and an initial velocity of 24 m/s. This indicates that moderate pitch angles (around 30° to 42°) and controlled velocities (around 24 to 28 m/s) are key to maximizing accuracy. The subspaces that have shown promise include moderate pitch angles with low to moderate velocities, particularly around 25 m/s, while extreme angles (both high and low) and high spin rates have consistently resulted in low scores. Notably, attempts with negative yaw angles have not yielded favorable results, suggesting they may destabilize the projectile. Moving forward, I will refine the hypotheses to focus on combinations that balance angle, velocity, and spin for improved accuracy, while discarding those that have consistently performed poorly. The next steps will involve exploring slightly higher pitch angles and controlled velocities, as well as testing different launch heights to optimize the trajectory towards the target. Additionally, I will emphasize the importance of maintaining a moderate spin rate to enhance stability without causing excessive deviation.

### Updated Hypotheses

#### Moderate Pitch and Velocity

*Rationale:* Building on the successful parameters from previous iterations, this hypothesis aims to maintain a moderate pitch and velocity for optimal accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 39, 'yaw_deg': 0, 'v0': 26, 'spin_rpm': 900, 'spin_axis_deg': 0, 'h0': 0.6, 'mass': 0.5}

#### Optimal Angle with Controlled Velocity

*Rationale:* Exploring a slightly higher angle with a controlled velocity may help in achieving a better trajectory towards the target without overshooting.

*Confidence:* medium

*Points:*

- {'pitch_deg': 42, 'yaw_deg': 1, 'v0': 25, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1.2, 'mass': 0.6}

#### Higher Launch Height with Moderate Angle

*Rationale:* Testing a higher launch height with a moderate angle may allow for a better arc and improved landing accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 43, 'yaw_deg': 0, 'v0': 24, 'spin_rpm': 750, 'spin_axis_deg': 0, 'h0': 1.8, 'mass': 0.5}

#### Exploring Slightly Positive Yaw

*Rationale:* While previous attempts with extreme yaw angles were unsuccessful, a controlled positive yaw may help in fine-tuning the trajectory.

*Confidence:* low

*Points:*

- {'pitch_deg': 31, 'yaw_deg': 5, 'v0': 28, 'spin_rpm': 950, 'spin_axis_deg': 0, 'h0': 0.7, 'mass': 0.4}

#### Controlled Spin for Stability

*Rationale:* Introducing a moderate spin rate may stabilize the projectile's flight, potentially improving accuracy without excessive deviation.

*Confidence:* medium

*Points:*

- {'pitch_deg': 36, 'yaw_deg': -2, 'v0': 27, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 0.5}

## Iteration 60

As we analyze the results from the first 59 iterations, we observe significant progress in identifying effective parameter combinations. The highest score achieved is 50.20, obtained with a pitch angle of 41°, a yaw angle of 1°, and an initial velocity of 24 m/s. This indicates that moderate pitch angles (around 30° to 42°) and controlled velocities (around 24 to 28 m/s) are key to maximizing accuracy. The subspaces that have shown promise include moderate pitch angles with low to moderate velocities, particularly around 25 m/s. Conversely, extreme angles (both high and low) and high spin rates have consistently resulted in low scores, indicating they destabilize the projectile. Negative yaw angles have also proven detrimental, suggesting they lead to erratic trajectories. Moving forward, I will refine the hypotheses to focus on combinations that balance angle, velocity, and spin for improved accuracy, while discarding those that have consistently performed poorly. I will also explore slightly higher pitch angles and controlled velocities, as well as testing different launch heights to optimize the trajectory towards the target. The next steps will involve maintaining moderate spin rates to enhance stability without causing excessive deviation.

### Updated Hypotheses

#### Moderate Pitch and Velocity

*Rationale:* Building on the successful parameters from previous iterations, this hypothesis aims to maintain a moderate pitch and velocity for optimal accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 40, 'yaw_deg': 0, 'v0': 25, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1.0, 'mass': 0.5}

#### Higher Launch Height with Controlled Velocity

*Rationale:* Testing a higher launch height with a moderate angle may allow for a better arc and improved landing accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 42, 'yaw_deg': 1, 'v0': 24, 'spin_rpm': 750, 'spin_axis_deg': 0, 'h0': 1.8, 'mass': 0.5}

#### Exploring Slightly Positive Yaw

*Rationale:* While previous attempts with extreme yaw angles were unsuccessful, a controlled positive yaw may help in fine-tuning the trajectory.

*Confidence:* low

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 3, 'v0': 26, 'spin_rpm': 900, 'spin_axis_deg': 0, 'h0': 0.7, 'mass': 0.4}

#### Controlled Spin for Stability

*Rationale:* Introducing a moderate spin rate may stabilize the projectile's flight, potentially improving accuracy without excessive deviation.

*Confidence:* medium

*Points:*

- {'pitch_deg': 35, 'yaw_deg': -1, 'v0': 27, 'spin_rpm': 850, 'spin_axis_deg': 0, 'h0': 1.0, 'mass': 0.5}

#### Lower Launch Height with Moderate Angle

*Rationale:* Testing a lower launch height with a moderate angle may help in achieving a better trajectory towards the target without overshooting.

*Confidence:* medium

*Points:*

- {'pitch_deg': 38, 'yaw_deg': 0, 'v0': 26, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 0.5, 'mass': 0.5}

## Iteration 72

As we analyze the results from the first 71 iterations, we observe significant progress in identifying effective parameter combinations. The highest score achieved is 80.26, obtained with a pitch angle of 30° and a yaw angle of 3° at an initial velocity of 26 m/s. This indicates that maintaining moderate pitch angles (around 30° to 42°) and controlled velocities (around 24 to 28 m/s) are key to maximizing accuracy. The subspaces that have shown promise include moderate pitch angles with low to moderate velocities, particularly around 25 m/s. Conversely, extreme angles (both high and low) and high spin rates have consistently resulted in low scores, indicating they destabilize the projectile. Negative yaw angles have also proven detrimental, suggesting they lead to erratic trajectories. Moving forward, I will refine the hypotheses to focus on combinations that balance angle, velocity, and spin for improved accuracy, while discarding those that have consistently performed poorly. I will also explore slightly higher pitch angles and controlled velocities, as well as testing different launch heights to optimize the trajectory towards the target. The next steps will involve maintaining moderate spin rates to enhance stability without causing excessive deviation.

### Updated Hypotheses

#### Moderate Pitch and Velocity

*Rationale:* Building on the successful parameters from previous iterations, this hypothesis aims to maintain a moderate pitch and velocity for optimal accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 39, 'yaw_deg': 0, 'v0': 26, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1.0, 'mass': 0.5}

#### Higher Launch Height with Controlled Velocity

*Rationale:* Testing a higher launch height with a moderate angle may allow for a better arc and improved landing accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 42, 'yaw_deg': 1, 'v0': 23, 'spin_rpm': 750, 'spin_axis_deg': 0, 'h0': 1.9, 'mass': 0.5}

#### Exploring Slightly Positive Yaw

*Rationale:* While previous attempts with extreme yaw angles were unsuccessful, a controlled positive yaw may help in fine-tuning the trajectory.

*Confidence:* low

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 4, 'v0': 27, 'spin_rpm': 900, 'spin_axis_deg': 0, 'h0': 0.8, 'mass': 0.4}

#### Controlled Spin for Stability

*Rationale:* Introducing a moderate spin rate may stabilize the projectile's flight, potentially improving accuracy without excessive deviation.

*Confidence:* medium

*Points:*

- {'pitch_deg': 35, 'yaw_deg': 2, 'v0': 28, 'spin_rpm': 850, 'spin_axis_deg': 0, 'h0': 1.2, 'mass': 0.5}

#### Lower Launch Height with Moderate Angle

*Rationale:* Testing a lower launch height with a moderate angle may help in achieving a better trajectory towards the target without overshooting.

*Confidence:* medium

*Points:*

- {'pitch_deg': 38, 'yaw_deg': 1, 'v0': 25, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 0.6, 'mass': 0.5}

## Iteration 86

As we analyze the results from the first 85 iterations, we observe significant progress in identifying effective parameter combinations. The highest score achieved is 80.26, obtained with a pitch angle of 30° and a yaw angle of 3° at an initial velocity of 26 m/s. This indicates that maintaining moderate pitch angles (around 30° to 42°) and controlled velocities (around 24 to 28 m/s) are key to maximizing accuracy. The subspaces that have shown promise include moderate pitch angles with low to moderate velocities, particularly around 25 m/s. Conversely, extreme angles (both high and low) and high spin rates have consistently resulted in low scores, indicating they destabilize the projectile. Negative yaw angles have also proven detrimental, suggesting they lead to erratic trajectories. Moving forward, I will refine the hypotheses to focus on combinations that balance angle, velocity, and spin for improved accuracy, while discarding those that have consistently performed poorly. I will also explore slightly higher pitch angles and controlled velocities, as well as testing different launch heights to optimize the trajectory towards the target. The next steps will involve maintaining moderate spin rates to enhance stability without causing excessive deviation.

### Updated Hypotheses

#### Moderate Pitch and Velocity

*Rationale:* Building on the successful parameters from previous iterations, this hypothesis aims to maintain a moderate pitch and velocity for optimal accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 39, 'yaw_deg': 1, 'v0': 26, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1.0, 'mass': 0.5}

#### Higher Launch Height with Controlled Velocity

*Rationale:* Testing a higher launch height with a moderate angle may allow for a better arc and improved landing accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 42, 'yaw_deg': 1, 'v0': 24, 'spin_rpm': 750, 'spin_axis_deg': 0, 'h0': 1.9, 'mass': 0.5}

#### Exploring Slightly Positive Yaw

*Rationale:* While previous attempts with extreme yaw angles were unsuccessful, a controlled positive yaw may help in fine-tuning the trajectory.

*Confidence:* low

*Points:*

- {'pitch_deg': 31, 'yaw_deg': 4, 'v0': 27, 'spin_rpm': 900, 'spin_axis_deg': 0, 'h0': 0.8, 'mass': 0.4}

#### Controlled Spin for Stability

*Rationale:* Introducing a moderate spin rate may stabilize the projectile's flight, potentially improving accuracy without excessive deviation.

*Confidence:* medium

*Points:*

- {'pitch_deg': 36, 'yaw_deg': 2, 'v0': 28, 'spin_rpm': 850, 'spin_axis_deg': 0, 'h0': 1.2, 'mass': 0.5}

#### Lower Launch Height with Moderate Angle

*Rationale:* Testing a lower launch height with a moderate angle may help in achieving a better trajectory towards the target without overshooting.

*Confidence:* medium

*Points:*

- {'pitch_deg': 38, 'yaw_deg': 1, 'v0': 26, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 0.5, 'mass': 0.5}

## Iteration 101

As we analyze the results from the first 100 iterations, we observe significant progress in identifying effective parameter combinations. The highest score achieved is 80.26, obtained with a pitch angle of 30° and a yaw angle of 3° at an initial velocity of 26 m/s. This indicates that maintaining moderate pitch angles (around 30° to 42°) and controlled velocities (around 24 to 28 m/s) are key to maximizing accuracy. The subspaces that have shown promise include moderate pitch angles with low to moderate velocities, particularly around 25 m/s. Conversely, extreme angles (both high and low) and high spin rates have consistently resulted in low scores, indicating they destabilize the projectile. Negative yaw angles have also proven detrimental, suggesting they lead to erratic trajectories. Moving forward, I will refine the hypotheses to focus on combinations that balance angle, velocity, and spin for improved accuracy, while discarding those that have consistently performed poorly. I will also explore slightly higher pitch angles and controlled velocities, as well as testing different launch heights to optimize the trajectory towards the target. The next steps will involve maintaining moderate spin rates to enhance stability without causing excessive deviation.

### Updated Hypotheses

#### Moderate Pitch and Velocity

*Rationale:* Building on the successful parameters from previous iterations, this hypothesis aims to maintain a moderate pitch and velocity for optimal accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 39, 'yaw_deg': 2, 'v0': 27, 'spin_rpm': 850, 'spin_axis_deg': 0, 'h0': 1.1, 'mass': 0.5}

## Final Conclusions

Throughout the optimization process, the hypotheses evolved significantly based on the experimental data collected from each iteration. Initially, the hypotheses were broad, exploring a wide range of angles, velocities, and spins. However, as the iterations progressed, it became clear that certain parameter combinations consistently yielded better scores, particularly those involving moderate pitch angles (around 30° to 42°) and controlled velocities (24 to 28 m/s). 

The initial hypotheses that included extreme angles or high spin rates were largely discarded due to their poor performance, which indicated they destabilized the projectile's trajectory. Instead, the focus shifted towards refining hypotheses that maintained moderate parameters, emphasizing stability and accuracy. 

Additionally, the exploration of yaw angles was adjusted; while initial attempts with extreme yaw angles were unsuccessful, later hypotheses incorporated slight adjustments to yaw, aiming for fine-tuning rather than drastic changes. 

Overall, the hypotheses became more targeted and data-driven, concentrating on combinations that had shown promise in previous iterations. This iterative refinement led to a significant increase in the highest score achieved, culminating in a peak score of 80.26.

| Hypothesis Name                     | Initial Confidence | Final Confidence |
|-------------------------------------|--------------------|------------------|
| High Angle Launch                   | Medium             | Low              |
| Moderate Velocity with Low Angle    | High               | Medium           |
| Controlled Spin for Stability       | Medium             | Medium           |
| Higher Launch Height                | Medium             | Medium           |
| Exploring Negative Yaw              | Low                | Low              |
| Moderate Pitch and Velocity         | High               | High             |
| Optimal Angle with Controlled Velocity| Medium           | Medium           |
| Higher Launch Height with Moderate Angle| Medium         | Medium           |
| Exploring Slightly Positive Yaw     | Low                | Low              |
| Controlled Spin for Stability       | Medium             | Medium           |
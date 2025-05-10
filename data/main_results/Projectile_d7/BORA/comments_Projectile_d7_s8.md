# Projectile

## Experiment Overview

The goal of this experiment is to maximize the score, which reflects the accuracy of a projectile thrown from the origin (0, 0) toward a target located at (50, 0). The score is derived from the distance error between the projectile's landing position and the target, with higher scores indicating closer landings. 

To achieve this, we will optimize several parameters: pitch_deg (release angle), yaw_deg (horizontal aiming angle), v0 (initial velocity), spin_rpm (spin rate), spin_axis_deg (orientation of the spin axis), h0 (release height), and mass (projectile weight). Each parameter has defined bounds, ensuring a systematic exploration of the parameter space.

Bayesian Optimization (BO) will be employed to efficiently navigate this multi-dimensional space, leveraging a probabilistic model to predict the score based on current parameter settings. As BO iteratively samples points, it will update its model and suggest new parameter configurations. When the optimization process plateaus, I will provide insights to explore unexplored regions or adjust parameters based on observed trends, ultimately identifying conditions that yield the highest scores. This approach aims to systematically refine the parameters to achieve optimal projectile performance.

## Initial Thoughts

In this initial sampling step, we aim to explore diverse regions of the parameter space to gather valuable insights into the relationships between parameters and their impact on the score. The hypotheses are designed to cover a range of angles, velocities, and other factors that could influence the projectile's trajectory. A high launch angle (around 75°) with moderate velocity (30 m/s) may allow the projectile to gain altitude and cover more horizontal distance, while a low launch angle (around 15°) with high velocity (45 m/s) could result in a flatter trajectory for a more direct path to the target. A balanced approach using moderate values (45° pitch, 25 m/s velocity) may provide an optimal trajectory. Additionally, increasing the spin rate (2500 RPM) could stabilize the projectile's flight, potentially improving accuracy. Lastly, a vertical launch (90°) with careful calibration of initial velocity (20 m/s) may allow for a controlled descent towards the target, although this approach carries lower confidence due to its inherent risks. By sampling these points, we can identify promising areas for further exploration and refine our optimization strategy based on the observed results.
### Initial Hypotheses

#### High Launch Angle with Moderate Velocity

*Rationale:* A high pitch angle may allow the projectile to gain altitude and cover more horizontal distance, especially with a moderate initial velocity.

*Confidence:* medium

*Points:*

- {'pitch_deg': 75, 'yaw_deg': 0, 'v0': 30, 'spin_rpm': 1500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Low Launch Angle with High Velocity

*Rationale:* A low pitch angle combined with a high initial velocity could result in a flatter trajectory, potentially allowing for a more direct path to the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 15, 'yaw_deg': 0, 'v0': 45, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 0.5, 'mass': 0.5}

#### Balanced Approach with Moderate Parameters

*Rationale:* Using moderate values for all parameters may provide a balanced trajectory that optimally reaches the target.

*Confidence:* high

*Points:*

- {'pitch_deg': 45, 'yaw_deg': 0, 'v0': 25, 'spin_rpm': 500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 2}

#### High Spin Rate for Stability

*Rationale:* Increasing the spin rate may stabilize the projectile's flight, potentially improving accuracy towards the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 10, 'v0': 35, 'spin_rpm': 2500, 'spin_axis_deg': 45, 'h0': 1.5, 'mass': 0.8}

#### Vertical Launch with Minimal Horizontal Movement

*Rationale:* A vertical launch may allow for a controlled descent towards the target, especially if the initial velocity is carefully calibrated.

*Confidence:* low

*Points:*

- {'pitch_deg': 90, 'yaw_deg': 0, 'v0': 20, 'spin_rpm': 0, 'spin_axis_deg': 0, 'h0': 2, 'mass': 1.5}

## Iteration 12

Analyzing the results from the first 11 iterations reveals that the parameters significantly influence the score. The highest score achieved so far is 32.75 from iteration 3, with a pitch_deg of 45, yaw_deg of 0, v0 of 25, spin_rpm of 500, h0 of 1, and mass of 2. This suggests that a moderate pitch and velocity may be effective for maximizing accuracy. In contrast, several configurations, particularly those with extreme angles (e.g., -8.56° pitch and -120.23° yaw) and very low velocities (e.g., 0.41 m/s), resulted in scores of 0, indicating detrimental subspaces. The data indicates that a balanced approach with moderate pitch and velocity, along with controlled spin, is promising. We should focus on refining these parameters while exploring slight variations in yaw and spin to enhance performance. The next hypotheses will build on the successful configurations while discarding those that consistently underperform. The promising subspaces appear to be around moderate pitch (30°-45°), moderate velocity (25 m/s), and controlled spin rates (500-2000 RPM). We will aim to explore these areas further in the next iterations.

### Updated Hypotheses

#### Moderate Pitch and Velocity

*Rationale:* Building on the successful configuration from iteration 3, maintaining a moderate pitch and velocity may yield optimal results.

*Confidence:* high

*Points:*

- {'pitch_deg': 45, 'yaw_deg': 5, 'v0': 28, 'spin_rpm': 600, 'spin_axis_deg': 0, 'h0': 1, 'mass': 2}

#### Exploring Higher Yaw with Moderate Pitch

*Rationale:* Testing a higher yaw angle while keeping pitch moderate may help identify optimal lateral aiming adjustments.

*Confidence:* medium

*Points:*

- {'pitch_deg': 45, 'yaw_deg': 30, 'v0': 25, 'spin_rpm': 500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 2}

#### Lower Pitch with Increased Velocity

*Rationale:* A lower pitch angle combined with a higher velocity may create a flatter trajectory, potentially improving accuracy towards the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 20, 'yaw_deg': 0, 'v0': 40, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1.5}

#### Moderate Spin for Stability

*Rationale:* Increasing the spin rate while maintaining moderate pitch and velocity may enhance stability and accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 35, 'yaw_deg': 0, 'v0': 30, 'spin_rpm': 2000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Vertical Launch with Controlled Velocity

*Rationale:* Testing a vertical launch with a controlled velocity may provide insights into the projectile's descent behavior.

*Confidence:* low

*Points:*

- {'pitch_deg': 90, 'yaw_deg': 0, 'v0': 25, 'spin_rpm': 0, 'spin_axis_deg': 0, 'h0': 2, 'mass': 1.5}

## Iteration 32

Upon reviewing the results from the first 31 iterations, it is clear that certain parameter configurations yield significantly better scores than others. The highest score achieved so far is 57.48 from iteration 20, with a pitch_deg of 49.97, yaw_deg of 5.96, v0 of 24.72, and a spin_rpm of 2511.26. This indicates that a moderate pitch combined with a slight yaw adjustment and a controlled velocity can lead to improved accuracy. Conversely, configurations with extreme angles, such as those seen in iterations 6 and 10, consistently resulted in scores of 0, indicating detrimental subspaces. The promising subspaces appear to be around moderate pitch (30°-50°), moderate velocity (20 m/s - 30 m/s), and controlled spin rates (500-2500 RPM). We should focus on refining these parameters while exploring slight variations in yaw and spin to enhance performance. Based on these insights, I will improve the previous hypotheses by focusing on the successful configurations and discarding those that have consistently underperformed. New hypotheses will target the identified promising subspaces, aiming to maximize the score further.

### Updated Hypotheses

#### Refined Moderate Pitch and Velocity

*Rationale:* Building on the successful configuration from iteration 20, maintaining a moderate pitch and velocity may yield optimal results.

*Confidence:* high

*Points:*

- {'pitch_deg': 45, 'yaw_deg': 5, 'v0': 26, 'spin_rpm': 2000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 2}

#### Exploring Slightly Higher Yaw

*Rationale:* Testing a slightly higher yaw angle while keeping pitch moderate may help identify optimal lateral aiming adjustments.

*Confidence:* medium

*Points:*

- {'pitch_deg': 45, 'yaw_deg': 15, 'v0': 25, 'spin_rpm': 1500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 2}

#### Lower Pitch with Controlled Velocity

*Rationale:* A lower pitch angle combined with a controlled velocity may create a flatter trajectory, potentially improving accuracy towards the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 25, 'yaw_deg': 0, 'v0': 30, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1.5}

#### Moderate Spin for Enhanced Stability

*Rationale:* Increasing the spin rate while maintaining moderate pitch and velocity may enhance stability and accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 35, 'yaw_deg': 0, 'v0': 28, 'spin_rpm': 2500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Testing Vertical Launch with Adjusted Parameters

*Rationale:* Testing a vertical launch with a controlled velocity and moderate parameters may provide insights into the projectile's descent behavior.

*Confidence:* low

*Points:*

- {'pitch_deg': 90, 'yaw_deg': 0, 'v0': 22, 'spin_rpm': 500, 'spin_axis_deg': 0, 'h0': 2, 'mass': 1.5}

## Iteration 49

As we progress through iteration 48, the data reveals significant insights into the parameter configurations that influence the score. The highest score achieved so far is 57.48 from iteration 20, with a pitch_deg of 49.97, yaw_deg of 5.96, v0 of 24.72, and spin_rpm of 2511.26. This indicates that a moderate pitch (around 45°), slight yaw adjustments, and controlled velocity (approximately 24-26 m/s) are effective for maximizing accuracy. The promising subspaces appear to be centered around moderate pitch (30°-50°), moderate velocity (20 m/s - 30 m/s), and spin rates (500-2500 RPM). Conversely, configurations with extreme angles, particularly those with negative pitch or yaw values, consistently yield scores of 0, indicating detrimental subspaces. Based on these findings, I will refine the previous hypotheses, focusing on successful configurations while discarding those that have underperformed. New hypotheses will target the identified promising subspaces, aiming to further maximize the score.

### Updated Hypotheses

#### Refined Moderate Pitch and Velocity

*Rationale:* Building on the successful configuration from iteration 20, maintaining a moderate pitch and velocity may yield optimal results.

*Confidence:* high

*Points:*

- {'pitch_deg': 45, 'yaw_deg': 10, 'v0': 27, 'spin_rpm': 2000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 2}

#### Exploring Slightly Higher Yaw

*Rationale:* Testing a slightly higher yaw angle while keeping pitch moderate may help identify optimal lateral aiming adjustments.

*Confidence:* medium

*Points:*

- {'pitch_deg': 46, 'yaw_deg': 20, 'v0': 25, 'spin_rpm': 1500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 2}

#### Lower Pitch with Controlled Velocity

*Rationale:* A lower pitch angle combined with a controlled velocity may create a flatter trajectory, potentially improving accuracy towards the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 5, 'v0': 32, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1.5}

#### Moderate Spin for Enhanced Stability

*Rationale:* Increasing the spin rate while maintaining moderate pitch and velocity may enhance stability and accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 36, 'yaw_deg': 2, 'v0': 29, 'spin_rpm': 2400, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Testing Vertical Launch with Adjusted Parameters

*Rationale:* Testing a vertical launch with a controlled velocity and moderate parameters may provide insights into the projectile's descent behavior.

*Confidence:* low

*Points:*

- {'pitch_deg': 90, 'yaw_deg': 5, 'v0': 24, 'spin_rpm': 600, 'spin_axis_deg': 0, 'h0': 2, 'mass': 1.5}

#### Exploring Lower Pitch with Higher Velocity

*Rationale:* A lower pitch angle combined with a higher velocity may create a flatter trajectory, potentially improving accuracy towards the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 18, 'yaw_deg': 0, 'v0': 36, 'spin_rpm': 1100, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1.5}

## Iteration 68

As we reach iteration 67, the data reveals significant insights into the parameter configurations that influence the score. The highest score achieved so far is 57.48 from iteration 20, with a configuration of pitch_deg at 49.97, yaw_deg at 5.96, v0 at 24.72, and spin_rpm at 2511.26. This suggests that a moderate pitch combined with slight yaw adjustments and controlled velocity is effective for maximizing accuracy. The promising subspaces appear to be centered around moderate pitch (30u00b0-50u00b0), moderate velocity (20 m/s - 30 m/s), and spin rates (500-2500 RPM). Conversely, configurations with extreme angles, particularly negative pitch or yaw values, consistently yield scores of 0, indicating detrimental subspaces. Based on these findings, I will refine the previous hypotheses, focusing on successful configurations while discarding those that have underperformed. New hypotheses will target the identified promising subspaces, aiming to further maximize the score. The next steps will involve exploring slight variations in pitch and yaw while maintaining a controlled velocity and spin rate to enhance performance.

### Updated Hypotheses

#### Refined Moderate Pitch and Velocity

*Rationale:* Building on the successful configuration from iteration 20, maintaining a moderate pitch and velocity may yield optimal results.

*Confidence:* high

*Points:*

- {'pitch_deg': 45, 'yaw_deg': 10, 'v0': 26, 'spin_rpm': 2000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 2}

#### Exploring Slightly Higher Yaw

*Rationale:* Testing a slightly higher yaw angle while keeping pitch moderate may help identify optimal lateral aiming adjustments.

*Confidence:* medium

*Points:*

- {'pitch_deg': 46, 'yaw_deg': 15, 'v0': 25, 'spin_rpm': 1500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 2}

#### Lower Pitch with Controlled Velocity

*Rationale:* A lower pitch angle combined with a controlled velocity may create a flatter trajectory, potentially improving accuracy towards the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 7, 'v0': 31, 'spin_rpm': 1200, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1.5}

#### Moderate Spin for Enhanced Stability

*Rationale:* Increasing the spin rate while maintaining moderate pitch and velocity may enhance stability and accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 36, 'yaw_deg': 3, 'v0': 28, 'spin_rpm': 2300, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Testing Vertical Launch with Adjusted Parameters

*Rationale:* Testing a vertical launch with a controlled velocity and moderate parameters may provide insights into the projectile's descent behavior.

*Confidence:* low

*Points:*

- {'pitch_deg': 90, 'yaw_deg': 10, 'v0': 23, 'spin_rpm': 700, 'spin_axis_deg': 0, 'h0': 2, 'mass': 1.5}

#### Exploring Lower Pitch with Higher Velocity

*Rationale:* A lower pitch angle combined with a higher velocity may create a flatter trajectory, potentially improving accuracy towards the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 19, 'yaw_deg': 1, 'v0': 37, 'spin_rpm': 1150, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1.5}

## Iteration 86

As we reach iteration 85, the data reveals critical insights into the parameter configurations influencing the score. The highest score achieved so far is 76.16 from iteration 76, with a configuration of pitch_deg at 41.50, yaw_deg at 1.95, v0 at 30.26, and spin_rpm at 2515.97. This suggests that a moderate pitch combined with slight yaw adjustments and controlled velocity is effective for maximizing accuracy. The promising subspaces appear to be centered around moderate pitch (30°-50°), moderate velocity (20 m/s - 30 m/s), and spin rates (500-2500 RPM). Conversely, configurations with extreme angles, particularly negative pitch or yaw values, consistently yield scores of 0, indicating detrimental subspaces. Based on these findings, I will refine the previous hypotheses, focusing on successful configurations while discarding those that have underperformed. New hypotheses will target the identified promising subspaces, aiming to further maximize the score.

### Updated Hypotheses

#### Refined Moderate Pitch and Velocity

*Rationale:* Building on the successful configuration from iteration 76, maintaining a moderate pitch and velocity may yield optimal results.

*Confidence:* high

*Points:*

- {'pitch_deg': 41.5, 'yaw_deg': 5, 'v0': 28, 'spin_rpm': 2000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 2}

#### Exploring Slightly Higher Yaw

*Rationale:* Testing a slightly higher yaw angle while keeping pitch moderate may help identify optimal lateral aiming adjustments.

*Confidence:* medium

*Points:*

- {'pitch_deg': 42, 'yaw_deg': 15, 'v0': 25, 'spin_rpm': 1500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 2}

#### Lower Pitch with Controlled Velocity

*Rationale:* A lower pitch angle combined with a controlled velocity may create a flatter trajectory, potentially improving accuracy towards the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 6, 'v0': 33, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1.5}

#### Moderate Spin for Enhanced Stability

*Rationale:* Increasing the spin rate while maintaining moderate pitch and velocity may enhance stability and accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 36, 'yaw_deg': 3, 'v0': 28, 'spin_rpm': 2400, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Exploring Lower Pitch with Higher Velocity

*Rationale:* A lower pitch angle combined with a higher velocity may create a flatter trajectory, potentially improving accuracy towards the target.

*Confidence:* medium

*Points:*

- {'pitch_deg': 19, 'yaw_deg': 2, 'v0': 38, 'spin_rpm': 1150, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1.5}

## Final Conclusions

Throughout the optimization process, the hypotheses evolved significantly based on the experimental data collected from each iteration. Initially, the hypotheses focused on exploring a wide range of parameter configurations, including extreme angles and velocities. However, as the iterations progressed, it became evident that certain configurations consistently yielded better scores, particularly those with moderate pitch angles (around 30°-50°), controlled velocities (20 m/s - 30 m/s), and spin rates (500-2500 RPM).

The highest score achieved (76.16) was associated with a configuration that maintained a moderate pitch and slight yaw adjustments, reinforcing the idea that stability and accuracy are paramount. Consequently, the hypotheses shifted to refine these successful configurations, emphasizing slight variations in pitch and yaw while maintaining controlled velocities and spin rates. Underperforming configurations, particularly those with extreme angles, were systematically discarded.

This iterative refinement allowed for a more focused exploration of promising subspaces, ultimately leading to improved scores. The confidence in hypotheses also evolved, reflecting the increasing understanding of the parameter relationships and their impact on performance.

| Hypothesis Name                          | Initial Confidence | Final Confidence |
|------------------------------------------|--------------------|------------------|
| High Launch Angle with Moderate Velocity | Medium             | Low              |
| Low Launch Angle with High Velocity      | Medium             | Medium           |
| Balanced Approach with Moderate Parameters| High               | High             |
| High Spin Rate for Stability             | Medium             | Medium           |
| Vertical Launch with Minimal Movement    | Low                | Low              |
| Refined Moderate Pitch and Velocity      | High               | High             |
| Exploring Slightly Higher Yaw            | Medium             | Medium           |
| Lower Pitch with Controlled Velocity     | Medium             | Medium           |
| Moderate Spin for Enhanced Stability     | Medium             | Medium           |
| Testing Vertical Launch with Adjusted Parameters | Low        | Low              |
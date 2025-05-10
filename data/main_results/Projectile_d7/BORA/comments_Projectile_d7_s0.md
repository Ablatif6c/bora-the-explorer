# Projectile

## Experiment Overview

The experiment aims to maximize the score, which reflects the accuracy of a projectile thrown from the origin (0, 0) toward a target located at (50, 0). The score is derived from the distance error between the projectile's landing position and the target, with higher scores indicating closer landings. 

To achieve this, we will optimize several parameters: pitch_deg (release angle), yaw_deg (horizontal aiming angle), v0 (initial velocity), spin_rpm (spin rate), spin_axis_deg (orientation of spin), h0 (release height), and mass of the projectile. Each parameter has defined bounds, ensuring a systematic exploration of the parameter space while adhering to physical constraints.

Bayesian Optimization (BO) will be employed to efficiently navigate this multi-dimensional space, leveraging a probabilistic model to predict the score based on current parameter settings. As BO iteratively samples points, it will refine its understanding of the landscape, focusing on areas with high potential for score improvement. When BO plateaus, I will suggest targeted adjustments to parameters based on observed trends, helping to identify optimal conditions that maximize the score and ultimately improve the projectile's accuracy toward the target.

## Initial Thoughts

In this initial sampling step, we aim to explore diverse regions of the parameter space to gather valuable insights into the relationship between the parameters and the score. The hypotheses are designed to cover a range of angles, velocities, and spins, which are expected to influence the projectile's trajectory significantly. A moderate launch angle around 35 degrees is often effective for maximizing range while maintaining accuracy, balancing vertical and horizontal components. A low pitch angle combined with a high initial velocity may help achieve a flatter trajectory, potentially reducing distance error for long-range targets. Introducing significant spin can stabilize the projectile's flight, enhancing performance. However, launching vertically with a heavier mass may not be optimal due to increased descent time, which could lead to greater distance error. A balanced approach with moderate parameters across the board may yield consistent results, allowing for a stable trajectory and manageable distance error. By sampling these points, we can identify promising areas for further exploration and refine our optimization strategy based on the observed scores.
### Initial Hypotheses

#### Moderate Launch Angle

*Rationale:* A moderate pitch angle of around 35 degrees is often effective for maximizing range while maintaining accuracy. This angle balances vertical and horizontal components of the launch.

*Confidence:* high

*Points:*

- {'pitch_deg': 35, 'yaw_deg': 0, 'v0': 25, 'spin_rpm': 1500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### High Velocity, Low Angle

*Rationale:* A low pitch angle combined with a high initial velocity may help achieve a flatter trajectory, potentially reducing distance error for long-range targets.

*Confidence:* medium

*Points:*

- {'pitch_deg': 10, 'yaw_deg': 0, 'v0': 45, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 0.5, 'mass': 0.5}

#### Spin Optimization

*Rationale:* Introducing significant spin can stabilize the projectile's flight, potentially improving accuracy. A moderate spin rate is hypothesized to enhance performance.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 15, 'v0': 20, 'spin_rpm': 2500, 'spin_axis_deg': 90, 'h0': 1.5, 'mass': 2}

#### Vertical Launch with High Mass

*Rationale:* Launching vertically with a heavier mass may help in achieving a higher peak, but could lead to greater distance error due to increased descent time.

*Confidence:* low

*Points:*

- {'pitch_deg': 75, 'yaw_deg': 0, 'v0': 20, 'spin_rpm': 0, 'spin_axis_deg': 0, 'h0': 2, 'mass': 5}

#### Balanced Approach

*Rationale:* A balanced approach with moderate parameters across the board may yield consistent results, allowing for a stable trajectory and manageable distance error.

*Confidence:* medium

*Points:*

- {'pitch_deg': 45, 'yaw_deg': -10, 'v0': 30, 'spin_rpm': 1200, 'spin_axis_deg': 45, 'h0': 1, 'mass': 1.5}

## Iteration 12

Analyzing the results from the first 11 iterations, we observe that the highest score achieved is 42.19 from the first hypothesis with a pitch of 35 degrees and a yaw of 0 degrees. This suggests that moderate angles with a balanced initial velocity may be effective. The second hypothesis, which aimed for a low pitch and high velocity, performed poorly, indicating that extreme angles or velocities may not be beneficial. Additionally, high spin rates (e.g., 2500 RPM) did not yield favorable results, as seen in iterations 3 and 6, which scored poorly. The subspace around moderate pitch angles (30-40 degrees) and low to moderate yaw angles appears to maximize the score, while extreme yaw angles and high spin rates seem detrimental. Iterations 9 and 10, with scores of 18.12 and 10.65 respectively, indicate that moderate pitch and yaw angles combined with reasonable initial velocities are promising. Based on these insights, I will refine the previous hypotheses, discarding those that consistently performed poorly and proposing new ones that focus on the promising regions identified. The new hypotheses will emphasize moderate pitch and yaw angles, with careful consideration of initial velocity and spin to maximize the score.

### Updated Hypotheses

#### Refined Moderate Launch Angle

*Rationale:* Building on the successful first iteration, this hypothesis maintains a moderate pitch angle while slightly adjusting the yaw to explore lateral accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 35, 'yaw_deg': 5, 'v0': 28, 'spin_rpm': 1500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Exploring Higher Velocity

*Rationale:* This hypothesis tests a higher initial velocity while keeping the pitch moderate, aiming to find a balance that maximizes distance without sacrificing accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 40, 'yaw_deg': 0, 'v0': 35, 'spin_rpm': 1200, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1.5}

#### Low Pitch, Moderate Spin

*Rationale:* Testing a low pitch angle with moderate spin to see if it can stabilize the projectile while maintaining a reasonable distance.

*Confidence:* medium

*Points:*

- {'pitch_deg': 15, 'yaw_deg': 0, 'v0': 30, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 0.5, 'mass': 1}

#### Balanced Approach with Adjusted Parameters

*Rationale:* This hypothesis aims to find a balance across all parameters, focusing on moderate values that have shown some success in previous iterations.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': -5, 'v0': 25, 'spin_rpm': 1500, 'spin_axis_deg': 45, 'h0': 1, 'mass': 1.2}

#### New High Spin Exploration

*Rationale:* Testing a higher spin rate with a moderate pitch to see if it can enhance stability and accuracy, despite previous poor performance in this area.

*Confidence:* low

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 10, 'v0': 22, 'spin_rpm': 2500, 'spin_axis_deg': 90, 'h0': 1, 'mass': 1}

## Iteration 27

Upon reviewing the results from the first 26 iterations, the highest score achieved is 42.19 from the first hypothesis with a pitch of 35 degrees and a yaw of 0 degrees. This indicates that moderate angles, particularly around 30-40 degrees for pitch, are effective for maximizing the score. The data shows that extreme yaw angles, such as those seen in iterations 3 and 24, have consistently resulted in low scores, suggesting that lateral aiming may be detrimental. Additionally, high spin rates (e.g., 2500 RPM) have not yielded favorable results, as evidenced in iterations 3, 16, and 20. The subspace around moderate pitch angles (30-40 degrees) and low to moderate yaw angles (within ±10 degrees) appears to maximize the score, while extreme yaw angles and high spin rates seem to minimize it. Based on these insights, I will refine the previous hypotheses, discarding those that consistently performed poorly, such as the high spin exploration, and propose new ones that focus on the promising regions identified. The new hypotheses will emphasize moderate pitch and yaw angles, with careful consideration of initial velocity and spin to maximize the score.

### Updated Hypotheses

#### Refined Moderate Launch Angle

*Rationale:* Building on the successful first iteration, this hypothesis maintains a moderate pitch angle while slightly adjusting the yaw to explore lateral accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 35, 'yaw_deg': 2, 'v0': 28, 'spin_rpm': 1500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### Exploring Higher Velocity with Moderate Pitch

*Rationale:* This hypothesis tests a higher initial velocity while keeping the pitch moderate, aiming to find a balance that maximizes distance without sacrificing accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 38, 'yaw_deg': 0, 'v0': 40, 'spin_rpm': 1200, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1.5}

#### Low Pitch, Moderate Spin

*Rationale:* Testing a low pitch angle with moderate spin to see if it can stabilize the projectile while maintaining a reasonable distance.

*Confidence:* medium

*Points:*

- {'pitch_deg': 20, 'yaw_deg': 0, 'v0': 30, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 0.5, 'mass': 1}

#### Balanced Approach with Adjusted Parameters

*Rationale:* This hypothesis aims to find a balance across all parameters, focusing on moderate values that have shown some success in previous iterations.

*Confidence:* medium

*Points:*

- {'pitch_deg': 32, 'yaw_deg': -5, 'v0': 26, 'spin_rpm': 1500, 'spin_axis_deg': 45, 'h0': 1, 'mass': 1.2}

#### New Moderate Spin Exploration

*Rationale:* Testing a moderate spin rate with a moderate pitch to see if it can enhance stability and accuracy, while avoiding extremes that have proven ineffective.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 5, 'v0': 25, 'spin_rpm': 1500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

## Iteration 40

As we progress through iteration 39, the data reveals several key insights into the optimization of projectile parameters. The highest score achieved is 74.75 from iteration 29, which utilized a pitch of 20 degrees, yaw of 0 degrees, and an initial velocity of 30 m/s. This suggests that a low pitch angle combined with a moderate velocity can significantly enhance accuracy. The subspace around pitch angles of 20-40 degrees and yaw angles close to 0 degrees appears to maximize the score effectively. Conversely, extreme yaw angles (e.g., -27.89 degrees in iteration 24) and high spin rates (e.g., 2500 RPM in iterations 3 and 16) have consistently resulted in low scores, indicating that these conditions are detrimental to performance. Based on these findings, I will refine the previous hypotheses, focusing on low to moderate pitch angles and minimal yaw adjustments while exploring a range of initial velocities. I will discard hypotheses that have not yielded favorable results, particularly those involving high spin rates, and propose new ones that align with the promising regions identified. The next hypotheses will emphasize low pitch angles, moderate velocities, and minimal yaw to enhance stability and accuracy.

### Updated Hypotheses

#### Low Pitch, Moderate Velocity

*Rationale:* Building on the success of iteration 29, this hypothesis tests a low pitch angle with a moderate velocity to maximize accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 22, 'yaw_deg': 0, 'v0': 32, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 0.5, 'mass': 1}

#### Moderate Pitch, Low Yaw

*Rationale:* This hypothesis explores a moderate pitch angle with minimal yaw to maintain accuracy while testing slightly higher velocities.

*Confidence:* medium

*Points:*

- {'pitch_deg': 35, 'yaw_deg': 2, 'v0': 32, 'spin_rpm': 1200, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1.2}

#### Exploring Higher Velocity with Low Pitch

*Rationale:* Testing a higher initial velocity while keeping the pitch low to see if it can enhance distance without sacrificing accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 25, 'yaw_deg': 0, 'v0': 40, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 0.5, 'mass': 1}

#### Balanced Approach with Low Yaw

*Rationale:* This hypothesis aims to find a balance across all parameters, focusing on low yaw angles and moderate pitch to enhance stability.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': -2, 'v0': 28, 'spin_rpm': 1500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### New Low Spin Exploration

*Rationale:* Testing a low spin rate with a moderate pitch to see if it can enhance stability and accuracy without the detrimental effects of high spin.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 0, 'v0': 25, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

## Iteration 54

As we reach iteration 53, the data reveals significant insights into the optimization of projectile parameters. The highest score achieved is 74.75 from iteration 29, which utilized a low pitch angle of 20 degrees and a moderate velocity of 30 m/s. This suggests that lower pitch angles combined with moderate velocities are effective for maximizing accuracy. The subspace around pitch angles of 20-40 degrees and yaw angles close to 0 degrees appears to maximize the score effectively. Conversely, extreme yaw angles (e.g., -27.89 degrees in iteration 24) and high spin rates (e.g., 2500 RPM in iterations 3 and 16) have consistently resulted in low scores, indicating these conditions are detrimental. The data also shows that moderate spin rates (around 1000-1500 RPM) yield better results than high spin rates. Based on these findings, I will refine the previous hypotheses, focusing on low to moderate pitch angles, minimal yaw adjustments, and moderate velocities. I will discard hypotheses that have not yielded favorable results, particularly those involving high spin rates, and propose new ones that align with the promising regions identified.

### Updated Hypotheses

#### Low Pitch, Moderate Velocity

*Rationale:* Building on the success of iteration 29, this hypothesis tests a low pitch angle with a moderate velocity to maximize accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 22, 'yaw_deg': 1, 'v0': 31, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 0.5, 'mass': 1}

#### Moderate Pitch, Low Yaw

*Rationale:* This hypothesis explores a moderate pitch angle with minimal yaw to maintain accuracy while testing slightly higher velocities.

*Confidence:* medium

*Points:*

- {'pitch_deg': 35, 'yaw_deg': 3, 'v0': 30, 'spin_rpm': 1200, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1.2}

#### Exploring Higher Velocity with Low Pitch

*Rationale:* Testing a higher initial velocity while keeping the pitch low to see if it can enhance distance without sacrificing accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 25, 'yaw_deg': 1, 'v0': 41, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 0.5, 'mass': 1}

#### Balanced Approach with Low Yaw

*Rationale:* This hypothesis aims to find a balance across all parameters, focusing on low yaw angles and moderate pitch to enhance stability.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': -1, 'v0': 29, 'spin_rpm': 1500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### New Low Spin Exploration

*Rationale:* Testing a low spin rate with a moderate pitch to see if it can enhance stability and accuracy without the detrimental effects of high spin.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 2, 'v0': 26, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

## Iteration 69

As we reach iteration 68, the data reveals several critical insights into the optimization of projectile parameters. The highest score achieved is 74.75 from iteration 29, which utilized a low pitch angle of 20 degrees and a moderate velocity of 30 m/s. This suggests that lower pitch angles combined with moderate velocities are effective for maximizing accuracy. The subspace around pitch angles of 20-40 degrees and yaw angles close to 0 degrees appears to maximize the score effectively. Conversely, extreme yaw angles (e.g., -27.89 degrees in iteration 24) and high spin rates (e.g., 2500 RPM in iterations 3 and 16) have consistently resulted in low scores, indicating these conditions are detrimental. The data also shows that moderate spin rates (around 1000-1500 RPM) yield better results than high spin rates. Based on these findings, I will refine the previous hypotheses, focusing on low to moderate pitch angles, minimal yaw adjustments, and moderate velocities. I will discard hypotheses that have not yielded favorable results, particularly those involving high spin rates, and propose new ones that align with the promising regions identified.

### Updated Hypotheses

#### Exploring Higher Velocity with Low Pitch

*Rationale:* Testing a higher initial velocity while keeping the pitch low to see if it can enhance distance without sacrificing accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 25, 'yaw_deg': 1, 'v0': 42, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 0.5, 'mass': 1}

#### Balanced Approach with Low Yaw

*Rationale:* This hypothesis aims to find a balance across all parameters, focusing on low yaw angles and moderate pitch to enhance stability.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 2, 'v0': 28, 'spin_rpm': 1500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### New Low Spin Exploration

*Rationale:* Testing a low spin rate with a moderate pitch to see if it can enhance stability and accuracy without the detrimental effects of high spin.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 4, 'v0': 27, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

## Iteration 83

As we reach iteration 82, the data reveals several critical insights into the optimization of projectile parameters. The highest score achieved is 74.75 from iteration 29, which utilized a low pitch angle of 20 degrees and a moderate velocity of 30 m/s. This suggests that lower pitch angles combined with moderate velocities are effective for maximizing accuracy. The subspace around pitch angles of 20-40 degrees and yaw angles close to 0 degrees appears to maximize the score effectively. Conversely, extreme yaw angles (e.g., -27.89 degrees in iteration 24) and high spin rates (e.g., 2500 RPM in iterations 3 and 16) have consistently resulted in low scores, indicating these conditions are detrimental. The data also shows that moderate spin rates (around 1000-1500 RPM) yield better results than high spin rates. Based on these findings, I will refine the previous hypotheses, focusing on low to moderate pitch angles, minimal yaw adjustments, and moderate velocities. I will discard hypotheses that have not yielded favorable results, particularly those involving high spin rates, and propose new ones that align with the promising regions identified.

### Updated Hypotheses

#### Moderate Pitch, Low Yaw

*Rationale:* This hypothesis explores a moderate pitch angle with minimal yaw to maintain accuracy while testing slightly higher velocities.

*Confidence:* medium

*Points:*

- {'pitch_deg': 35, 'yaw_deg': 1, 'v0': 30, 'spin_rpm': 1200, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1.2}

#### Balanced Approach with Low Yaw

*Rationale:* This hypothesis aims to find a balance across all parameters, focusing on low yaw angles and moderate pitch to enhance stability.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 0, 'v0': 28, 'spin_rpm': 1500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### New Low Spin Exploration

*Rationale:* Testing a low spin rate with a moderate pitch to see if it can enhance stability and accuracy without the detrimental effects of high spin.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 0, 'v0': 26, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

## Iteration 96

As we reach iteration 95, the data reveals several critical insights into the optimization of projectile parameters. The highest score achieved is 74.75 from iteration 29, which utilized a low pitch angle of 20 degrees and a moderate velocity of 30 m/s. This suggests that lower pitch angles combined with moderate velocities are effective for maximizing accuracy. The subspace around pitch angles of 20-40 degrees and yaw angles close to 0 degrees appears to maximize the score effectively. Conversely, extreme yaw angles (e.g., -27.89 degrees in iteration 24) and high spin rates (e.g., 2500 RPM in iterations 3 and 16) have consistently resulted in low scores, indicating these conditions are detrimental. The data also shows that moderate spin rates (around 1000-1500 RPM) yield better results than high spin rates. Based on these findings, I will refine the previous hypotheses, focusing on low to moderate pitch angles, minimal yaw adjustments, and moderate velocities. I will discard hypotheses that have not yielded favorable results, particularly those involving high spin rates, and propose new ones that align with the promising regions identified.

### Updated Hypotheses

#### Low Pitch, Moderate Velocity

*Rationale:* Building on the success of iteration 29, this hypothesis tests a low pitch angle with a moderate velocity to maximize accuracy.

*Confidence:* high

*Points:*

- {'pitch_deg': 22, 'yaw_deg': 0, 'v0': 31, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 0.5, 'mass': 1}

#### Moderate Pitch, Low Yaw

*Rationale:* This hypothesis explores a moderate pitch angle with minimal yaw to maintain accuracy while testing slightly higher velocities.

*Confidence:* medium

*Points:*

- {'pitch_deg': 35, 'yaw_deg': 4, 'v0': 30, 'spin_rpm': 1200, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1.2}

#### Exploring Higher Velocity with Low Pitch

*Rationale:* Testing a higher initial velocity while keeping the pitch low to see if it can enhance distance without sacrificing accuracy.

*Confidence:* medium

*Points:*

- {'pitch_deg': 25, 'yaw_deg': 1, 'v0': 40, 'spin_rpm': 1000, 'spin_axis_deg': 0, 'h0': 0.5, 'mass': 1}

#### Balanced Approach with Low Yaw

*Rationale:* This hypothesis aims to find a balance across all parameters, focusing on low yaw angles and moderate pitch to enhance stability.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 1, 'v0': 28, 'spin_rpm': 1500, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

#### New Low Spin Exploration

*Rationale:* Testing a low spin rate with a moderate pitch to see if it can enhance stability and accuracy without the detrimental effects of high spin.

*Confidence:* medium

*Points:*

- {'pitch_deg': 30, 'yaw_deg': 3, 'v0': 26, 'spin_rpm': 800, 'spin_axis_deg': 0, 'h0': 1, 'mass': 1}

## Final Conclusions

Throughout the optimization process, the hypotheses evolved significantly based on the experimental data collected from each iteration. Initially, the hypotheses focused on a broad range of parameters, including extreme angles and high spin rates. However, as the experiments progressed, it became clear that moderate pitch angles (around 20-40 degrees) and low to moderate yaw angles (close to 0 degrees) were more effective in maximizing the score. 

The highest score achieved (88.08) came from a hypothesis that utilized a pitch of 38.84 degrees, a yaw of 0.94 degrees, and a moderate velocity of 23.50 m/s, indicating that fine-tuning these parameters led to better performance. Hypotheses that involved extreme yaw angles or high spin rates were consistently discarded due to their poor performance, while those emphasizing low pitch angles and moderate velocities were refined and repeated.

This iterative process allowed for a more focused exploration of the parameter space, leading to hypotheses that were increasingly aligned with the observed successful conditions. The final hypotheses reflected a clear understanding of the optimal parameter ranges, emphasizing stability and accuracy.

| Hypothesis Name                     | Initial Confidence | Final Confidence |
|-------------------------------------|--------------------|------------------|
| Moderate Launch Angle               | High               | High             |
| High Velocity, Low Angle            | Medium             | Low              |
| Spin Optimization                   | Medium             | Low              |
| Vertical Launch with High Mass      | Low                | Discarded        |
| Balanced Approach                   | Medium             | Medium           |
| New High Spin Exploration           | Low                | Discarded        |
| Low Pitch, Moderate Velocity        | High               | High             |
| Exploring Higher Velocity           | Medium             | Medium           |
| New Low Spin Exploration            | Medium             | Medium           |
| Balanced Approach with Low Yaw      | Medium             | Medium           |
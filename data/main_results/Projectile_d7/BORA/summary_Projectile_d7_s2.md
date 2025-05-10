# BORA for Score Maximization 

## 1. Executive Summary

The optimization process aimed at maximizing the score for a projectile's landing accuracy yielded a maximum score of 90.53. The most effective parameters identified included a pitch angle of approximately 18.48 degrees, a yaw angle of 2.03 degrees, an initial velocity of 37.36 m/s, and a moderate spin rate. These findings highlight the importance of lower pitch angles and slight yaw adjustments in achieving optimal projectile trajectories, aligning with classical physics principles regarding projectile motion.

## 2. Optimization Overview

**Objective:**  
The primary goal of the optimization process was to identify the optimal parameter settings that would maximize the score, which reflects the accuracy of a projectile landing near a target located at (50, 0).

**Initial Hypotheses:**  
The initial hypotheses proposed a diverse range of parameter settings, including extreme angles and velocities. For example, one hypothesis suggested a moderate launch angle of 30 degrees, while another explored a high velocity with a low pitch angle. The rationale behind these hypotheses was based on classical projectile motion principles, where varying angles and velocities can significantly impact the trajectory and landing accuracy. The initial assumptions included the belief that both high velocities and optimal angles would contribute to maximizing the score.

## 3. Progress Summary

**Key Milestones:**

| Iteration | Hypothesis Name                               | Confidence Level | Key Findings                                                                 |
|-----------|-----------------------------------------------|------------------|------------------------------------------------------------------------------|
| 1         | Moderate Launch Angle                         | High             | Initial exploration of moderate angles yielded low scores.                  |
| 12        | Refined Moderate Launch Angle                 | High             | Moderate pitch and yaw angles began to show promise, with scores improving. |
| 23        | Low Pitch with Moderate Velocity              | High             | Lower pitch angles (15-25 degrees) started to yield better results.         |
| 36        | Optimized Low Pitch with Moderate Velocity    | High             | Continued refinement led to a focus on lower pitch angles and moderate speeds. |
| 51        | Refined Low Pitch with Slightly Higher Yaw   | Medium           | Slight adjustments in yaw were tested, confirming the importance of fine-tuning. |
| 66        | Optimized Low Pitch with Moderate Velocity    | High             | Consistent results reinforced the effectiveness of lower pitch angles.      |
| 80        | Refined Low Pitch with Slightly Higher Yaw   | Medium           | Further exploration of yaw adjustments continued to yield promising results.  |
| 95        | Refined Low Pitch with Slightly Higher Yaw   | Medium           | Final adjustments confirmed the optimal parameter settings.                  |

**Major Parameter Adjustments:**  
Throughout the optimization process, significant shifts occurred in the parameter subspaces. Initially, hypotheses explored a wide range of pitch angles, including extremes. However, as data was collected, the focus shifted towards lower pitch angles (around 18-20 degrees) and slight yaw adjustments (0-5 degrees). This change was driven by the observed correlation between these parameters and improved scores, aligning with the physics of projectile motion, where lower angles can enhance horizontal distance while maintaining stability.

## 4. Results and Key Insights

The best-performing configuration was identified as having a pitch angle of 18.48 degrees, a yaw angle of 2.03 degrees, an initial velocity of 37.36 m/s, a spin rate of 1996.69 RPM, a spin axis of 13.21 degrees, a height of 1.00 m, and a mass of 0.30 kg, resulting in a score of 90.53. Conversely, the worst-performing configurations often involved extreme yaw angles or high spin rates, which consistently resulted in low scores, indicating detrimental effects on trajectory stability.

These results align with known physics behaviors, where lower launch angles tend to maximize range while maintaining a stable flight path. The unexpected finding was the significant impact of slight yaw adjustments, which proved crucial in compensating for lateral drift and enhancing accuracy. The analysis of different parameter sets revealed that combinations emphasizing lower pitch angles and moderate velocities consistently outperformed others, reinforcing the importance of these parameters in projectile motion.

## 5. Recommendations for Future Experiments

Future experiments should explore the effects of varying environmental conditions, such as wind resistance and air density, on projectile performance. Additionally, investigating the impact of different projectile shapes and materials could yield insights into optimizing landing accuracy further. It may also be beneficial to explore a wider range of spin rates and their effects on stability and trajectory. Enhancing the optimization process could involve integrating real-time feedback mechanisms to adjust parameters dynamically during trials, potentially leading to even higher scores.

## 6. Conclusion

The optimization process successfully identified the optimal parameters for maximizing the projectile's landing accuracy, demonstrating the effectiveness of Bayesian Optimization in exploring complex parameter spaces. The evolution of hypotheses throughout the experiment highlighted the importance of data-driven decision-making, leading to refined configurations that aligned with classical physics principles. The findings not only contribute to the understanding of projectile motion but also provide a foundation for future experiments in this domain, emphasizing the relevance of these insights for advancing both practical applications and theoretical developments in physics.
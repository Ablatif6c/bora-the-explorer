# Solar Energy Production

## Experiment Overview

The primary goal of this experiment is to maximize solar energy production from a solar panel over a day by optimizing key parameters using Bayesian Optimization (BO). The parameters under investigation include tilt angle (0° to 90°), azimuth angle (0° to 360°), system capacity (1 kW to 20 kW), and the DC to AC capacity ratio (1 to 1.5). These parameters are crucial as they directly influence the panel's efficiency and energy output.

Bayesian Optimization will be employed to systematically explore the defined parameter space. This approach utilizes a probabilistic model to predict the performance of different parameter combinations, allowing for efficient sampling of the space. As the optimization progresses, BO will identify promising regions and suggest new points to evaluate, particularly when the optimization process plateaus. 

The intended outcome is to identify the optimal settings that yield the highest energy production, thereby enhancing the efficiency of solar energy systems. By iteratively refining the parameter choices based on observed results, we aim to uncover the conditions that maximize energy output, ultimately contributing to more effective solar energy utilization.

## Initial Thoughts

In the initial sampling step, we aim to explore diverse regions of the parameter space to gather insights into the relationship between the parameters and solar energy production. The hypotheses generated consider various angles and system capacities that are likely to yield high energy output based on solar radiation patterns and system efficiency. A tilt angle of around 30° is often optimal for maximizing solar exposure during midday, while higher angles (e.g., 60°) can be beneficial in winter months to capture lower sun angles. Conversely, a lower tilt angle (e.g., 10°) may be advantageous in summer to reduce shading. The azimuth angle of 270° (west) can capture afternoon sunlight, crucial for maximizing energy production later in the day. A balanced system capacity of around 8 kW with moderate tilt and azimuth settings can provide a good compromise between energy production and system efficiency. By strategically selecting points across the parameter space, we can effectively inform the Bayesian Optimization process and identify promising regions for further exploration.
### Initial Hypotheses

#### Mid-Range Tilt and Azimuth

*Rationale:* A tilt of around 30° and azimuth of 180° is often optimal for maximizing solar exposure during midday, which is when solar energy production peaks.

*Confidence:* high

*Points:*

- {'tilt': 30, 'azimuth': 180, 'system_capacity': 10, 'dc_ac_ratio': 1.2}

#### High Tilt for Winter Optimization

*Rationale:* A higher tilt angle of 60° can be beneficial in winter months to capture lower sun angles, potentially increasing energy production during that season.

*Confidence:* medium

*Points:*

- {'tilt': 60, 'azimuth': 200, 'system_capacity': 15, 'dc_ac_ratio': 1.3}

#### Low Tilt for Summer Optimization

*Rationale:* A lower tilt angle of 10° may be advantageous in summer months to reduce shading and maximize exposure to high sun angles.

*Confidence:* medium

*Points:*

- {'tilt': 10, 'azimuth': 90, 'system_capacity': 5, 'dc_ac_ratio': 1.1}

#### Optimal Azimuth for East-West Orientation

*Rationale:* Setting the azimuth to 270° (west) can capture afternoon sunlight, which is crucial for maximizing energy production in the later part of the day.

*Confidence:* medium

*Points:*

- {'tilt': 45, 'azimuth': 270, 'system_capacity': 12, 'dc_ac_ratio': 1.4}

#### Balanced System Capacity

*Rationale:* A balanced system capacity of 8 kW with a moderate tilt and azimuth can provide a good compromise between energy production and system efficiency.

*Confidence:* high

*Points:*

- {'tilt': 40, 'azimuth': 150, 'system_capacity': 8, 'dc_ac_ratio': 1.2}

## Iteration 14

As we progress through iteration 13 of the Bayesian Optimization, we have gathered valuable insights from the experimental data. The highest energy output observed is 3.19 units, achieved with a tilt of approximately 59.71°, an azimuth of 183.10°, a system capacity of 17.55 kW, and a DC to AC ratio of 1.00. This suggests that a tilt angle around 60° is favorable, likely due to its ability to capture optimal sunlight angles throughout the day. The data indicates that higher system capacities (around 16-20 kW) and moderate DC to AC ratios (around 1.1 to 1.3) are beneficial for maximizing energy production. Conversely, configurations with low system capacities (e.g., 5 kW) and extreme tilt angles (e.g., 88.63°) have consistently resulted in lower energy outputs, indicating these subspaces are detrimental. Based on these findings, I propose refining our hypotheses. The previous hypothesis regarding low tilt angles for summer optimization can be discarded due to poor performance. Instead, I suggest focusing on moderate to high tilt angles and exploring azimuth angles that align with the successful configurations observed. Here are the improved hypotheses for further exploration.

### Updated Hypotheses

#### Optimal Tilt and Azimuth

*Rationale:* A tilt of 59.71° and azimuth of 183.10° aligns with the highest energy output observed, suggesting this configuration effectively captures sunlight.

*Confidence:* high

*Points:*

- {'tilt': 59.71, 'azimuth': 183.1, 'system_capacity': 17.55, 'dc_ac_ratio': 1.0}

#### High Capacity with Moderate Tilt

*Rationale:* Exploring a slightly lower tilt of 60° with a higher system capacity of 20 kW may further enhance energy production based on previous results.

*Confidence:* high

*Points:*

- {'tilt': 60, 'azimuth': 185, 'system_capacity': 20, 'dc_ac_ratio': 1.2}

#### Balanced Configuration

*Rationale:* A tilt of 62° and azimuth of 180° with a balanced system capacity of 15 kW may provide a good compromise for energy production.

*Confidence:* medium

*Points:*

- {'tilt': 62, 'azimuth': 180, 'system_capacity': 15, 'dc_ac_ratio': 1.3}

#### Exploring Higher DC to AC Ratio

*Rationale:* Testing a higher DC to AC ratio of 1.5 with a tilt of 62° and azimuth of 182° could yield insights into efficiency improvements.

*Confidence:* medium

*Points:*

- {'tilt': 62, 'azimuth': 182, 'system_capacity': 18, 'dc_ac_ratio': 1.5}

#### Lower Tilt for Afternoon Capture

*Rationale:* A tilt of 45° with an azimuth of 270° may help capture afternoon sunlight effectively, which could be beneficial for energy production.

*Confidence:* medium

*Points:*

- {'tilt': 45, 'azimuth': 270, 'system_capacity': 16, 'dc_ac_ratio': 1.2}

## Iteration 26

As we continue through iteration 25 of the Bayesian Optimization, the dataset has provided valuable insights into the parameter space's impact on energy production. The highest energy output observed remains at 3.31 units, achieved with a tilt of 71.21°, an azimuth of 191.34°, a system capacity of 20.00 kW, and a DC to AC ratio of 1.00. This reinforces the trend that higher tilt angles (around 60° to 75°) and moderate to high system capacities (15-20 kW) are effective for maximizing energy production. The promising subspace around tilt angles of 60° to 75° and azimuth angles between 180° and 190° continues to be a focus. Based on these insights, I propose refining our hypotheses to explore new configurations while discarding those that have underperformed.

### Updated Hypotheses

#### Refined Optimal Tilt and Azimuth

*Rationale:* Continuing to explore configurations around tilt 65° and azimuth 185° may yield further insights into maximizing energy production.

*Confidence:* high

*Points:*

- {'tilt': 65, 'azimuth': 185, 'system_capacity': 17, 'dc_ac_ratio': 1.1}

#### Higher Tilt for Enhanced Capture

*Rationale:* Testing a higher tilt of 70° with a system capacity of 20 kW may further enhance energy production based on the observed trend of higher outputs with increased tilt.

*Confidence:* high

*Points:*

- {'tilt': 70, 'azimuth': 185, 'system_capacity': 20, 'dc_ac_ratio': 1.2}

#### Exploring 75° Tilt for Maximum Output

*Rationale:* A tilt of 75° with an azimuth of 182° and a system capacity of 19 kW could provide insights into the upper limits of energy production.

*Confidence:* medium

*Points:*

- {'tilt': 75, 'azimuth': 182, 'system_capacity': 19, 'dc_ac_ratio': 1.3}

#### Moderate Tilt with High Capacity

*Rationale:* Testing a tilt of 68° with a system capacity of 18 kW may provide a balanced approach to maximizing energy production.

*Confidence:* medium

*Points:*

- {'tilt': 68, 'azimuth': 180, 'system_capacity': 18, 'dc_ac_ratio': 1.1}

#### Balanced Configuration with 62° Tilt

*Rationale:* A tilt of 62° and azimuth of 190° with a balanced system capacity of 16 kW may still provide a good compromise for energy production.

*Confidence:* medium

*Points:*

- {'tilt': 62, 'azimuth': 190, 'system_capacity': 16, 'dc_ac_ratio': 1.3}

## Iteration 39

As we reach iteration 38 of the Bayesian Optimization, the dataset has provided significant insights into the parameter space's impact on energy production. The highest energy output observed is now 3.31 units, achieved with a tilt of 71.21°, an azimuth of 191.34°, a system capacity of 20 kW, and a DC to AC ratio of 1.00. This reinforces the trend that higher tilt angles (around 60° to 75°) and moderate to high system capacities (15-20 kW) are effective for maximizing energy production. The promising subspace around tilt angles of 60° to 75° and azimuth angles between 180° and 190° continues to be a focus. Conversely, configurations with low system capacities (e.g., 4.17 kW) and extreme tilt angles (e.g., 88.63°) have consistently resulted in lower energy outputs, indicating these subspaces are detrimental. Based on these findings, I propose refining our hypotheses to focus on the successful configurations while discarding those that have underperformed. The next steps should include exploring configurations around tilt angles of 70° and 75° with azimuths between 180° and 190°, as these regions have shown the highest outputs in previous iterations.

### Updated Hypotheses

#### Refined Optimal Tilt and Azimuth

*Rationale:* Continuing to explore configurations around tilt 70° and azimuth 185° may yield further insights into maximizing energy production, as this region has shown high outputs.

*Confidence:* high

*Points:*

- {'tilt': 70, 'azimuth': 185, 'system_capacity': 20, 'dc_ac_ratio': 1.1}

#### Exploring 75° Tilt for Maximum Output

*Rationale:* A tilt of 75° with an azimuth of 182° and a system capacity of 19 kW could provide insights into the upper limits of energy production, as higher tilts have shown promise.

*Confidence:* medium

*Points:*

- {'tilt': 75, 'azimuth': 182, 'system_capacity': 19, 'dc_ac_ratio': 1.2}

#### Higher Tilt with Maximum Capacity

*Rationale:* Testing a tilt of 72° with a system capacity of 20 kW may further enhance energy production based on the observed trend of higher outputs with increased tilt.

*Confidence:* high

*Points:*

- {'tilt': 72, 'azimuth': 190, 'system_capacity': 20, 'dc_ac_ratio': 1.3}

#### Moderate Tilt with New Capacity

*Rationale:* Testing a tilt of 68° with a system capacity of 17 kW may provide a balanced approach to maximizing energy production, as moderate configurations have shown consistent results.

*Confidence:* medium

*Points:*

- {'tilt': 68, 'azimuth': 180, 'system_capacity': 17, 'dc_ac_ratio': 1.1}

#### Balanced Configuration with New Tilt

*Rationale:* A tilt of 64° and azimuth of 190° with a balanced system capacity of 16 kW may still provide a good compromise for energy production, as this configuration has shown reasonable outputs.

*Confidence:* medium

*Points:*

- {'tilt': 64, 'azimuth': 190, 'system_capacity': 16, 'dc_ac_ratio': 1.3}

## Iteration 51

As we reach iteration 50 of the Bayesian Optimization, the dataset has provided significant insights into the parameter space's impact on energy production. The highest energy output observed is now 3.37 units, achieved with a tilt of 70.96u00b0, an azimuth of 181.52u00b0, a system capacity of 20 kW, and a DC to AC ratio of 1.00. This reinforces the trend that higher tilt angles (around 70u00b0 to 75u00b0) and maximum system capacities (20 kW) are effective for maximizing energy production. The promising subspace around tilt angles of 70u00b0 to 75u00b0 and azimuth angles between 180u00b0 and 190u00b0 continues to be a focus. Conversely, configurations with low system capacities (e.g., 4.17 kW) and extreme tilt angles (e.g., 88.63u00b0) have consistently resulted in lower energy outputs, indicating these subspaces are detrimental. Based on these findings, I propose refining our hypotheses to focus on the successful configurations while discarding those that have underperformed. The next steps should include exploring configurations around tilt angles of 70u00b0 and 75u00b0 with azimuths between 180u00b0 and 190u00b0, as these regions have shown the highest outputs in previous iterations. Additionally, testing configurations with a system capacity of 20 kW and varying DC to AC ratios may yield further insights into optimizing energy production.

### Updated Hypotheses

#### Refined Optimal Tilt and Azimuth

*Rationale:* Continuing to explore configurations around tilt 71u00b0 and azimuth 182u00b0 may yield further insights into maximizing energy production, as this region has shown high outputs.

*Confidence:* high

*Points:*

- {'tilt': 71, 'azimuth': 182, 'system_capacity': 20, 'dc_ac_ratio': 1.1}

#### Exploring 75u00b0 Tilt for Maximum Output

*Rationale:* A tilt of 75u00b0 with an azimuth of 185u00b0 and a system capacity of 19 kW could provide insights into the upper limits of energy production, as higher tilts have shown promise.

*Confidence:* medium

*Points:*

- {'tilt': 75, 'azimuth': 185, 'system_capacity': 19, 'dc_ac_ratio': 1.2}

#### Higher Tilt with Maximum Capacity

*Rationale:* Testing a tilt of 72u00b0 with a system capacity of 20 kW may further enhance energy production based on the observed trend of higher outputs with increased tilt.

*Confidence:* high

*Points:*

- {'tilt': 72, 'azimuth': 188, 'system_capacity': 20, 'dc_ac_ratio': 1.4}

#### Moderate Tilt with New Capacity

*Rationale:* Testing a tilt of 68u00b0 with a system capacity of 17 kW may provide a balanced approach to maximizing energy production, as moderate configurations have shown consistent results.

*Confidence:* medium

*Points:*

- {'tilt': 68, 'azimuth': 182, 'system_capacity': 17, 'dc_ac_ratio': 1.3}

#### Balanced Configuration with New Tilt

*Rationale:* A tilt of 64u00b0 and azimuth of 191u00b0 with a balanced system capacity of 16 kW may still provide a good compromise for energy production, as this configuration has shown reasonable outputs.

*Confidence:* medium

*Points:*

- {'tilt': 64, 'azimuth': 191, 'system_capacity': 16, 'dc_ac_ratio': 1.2}

## Iteration 62

As we reach iteration 61 of the Bayesian Optimization, the dataset has provided significant insights into the parameter space's impact on energy production. The highest energy output observed is now 3.37 units, achieved with a tilt of 70.96° and an azimuth of 181.52°, a system capacity of 20 kW, and a DC to AC ratio of 1.00. This reinforces the trend that higher tilt angles (around 70° to 75°) and maximum system capacities (20 kW) are effective for maximizing energy production. The promising subspace around tilt angles of 70° to 75° and azimuth angles between 180° and 190° continues to be a focus. Conversely, configurations with low system capacities (e.g., 4.17 kW) and extreme tilt angles (e.g., 88.63°) have consistently resulted in lower energy outputs, indicating these subspaces are detrimental. Based on these findings, I propose refining our hypotheses to focus on the successful configurations while discarding those that have underperformed. The next steps should include exploring configurations around tilt angles of 70° and 75° with azimuths between 180° and 190°, as these regions have shown the highest outputs in previous iterations. Additionally, testing configurations with a system capacity of 20 kW and varying DC to AC ratios may yield further insights into optimizing energy production.

### Updated Hypotheses

#### Refined Optimal Tilt and Azimuth

*Rationale:* Continuing to explore configurations around tilt 71° and azimuth 183° may yield further insights into maximizing energy production, as this region has shown high outputs.

*Confidence:* high

*Points:*

- {'tilt': 71, 'azimuth': 183, 'system_capacity': 20, 'dc_ac_ratio': 1.1}

#### Exploring 75° Tilt for Maximum Output

*Rationale:* A tilt of 75° with an azimuth of 186° and a system capacity of 19 kW could provide insights into the upper limits of energy production, as higher tilts have shown promise.

*Confidence:* medium

*Points:*

- {'tilt': 75, 'azimuth': 186, 'system_capacity': 19, 'dc_ac_ratio': 1.2}

#### Higher Tilt with Maximum Capacity

*Rationale:* Testing a tilt of 72° with a system capacity of 20 kW may further enhance energy production based on the observed trend of higher outputs with increased tilt.

*Confidence:* high

*Points:*

- {'tilt': 72, 'azimuth': 187, 'system_capacity': 20, 'dc_ac_ratio': 1.3}

#### Moderate Tilt with New Capacity

*Rationale:* Testing a tilt of 68° with a system capacity of 17 kW may provide a balanced approach to maximizing energy production, as moderate configurations have shown consistent results.

*Confidence:* medium

*Points:*

- {'tilt': 68, 'azimuth': 184, 'system_capacity': 17, 'dc_ac_ratio': 1.1}

#### Balanced Configuration with New Tilt

*Rationale:* A tilt of 64° and azimuth of 192° with a balanced system capacity of 16 kW may still provide a good compromise for energy production, as this configuration has shown reasonable outputs.

*Confidence:* medium

*Points:*

- {'tilt': 64, 'azimuth': 192, 'system_capacity': 16, 'dc_ac_ratio': 1.3}

## Iteration 74

As we reach iteration 73 of the Bayesian Optimization, the dataset has provided significant insights into the parameter space's impact on energy production. The highest energy output observed is now 3.37 units, achieved with a tilt of 70.96° and an azimuth of 181.52°, a system capacity of 20 kW, and a DC to AC ratio of 1.00. This reinforces the trend that higher tilt angles (around 70° to 75°) and maximum system capacities (20 kW) are effective for maximizing energy production. The promising subspace around tilt angles of 70° to 75° and azimuth angles between 180° and 190° continues to be a focus. Conversely, configurations with low system capacities (e.g., 4.17 kW) and extreme tilt angles (e.g., 88.63°) have consistently resulted in lower energy outputs, indicating these subspaces are detrimental. Based on these findings, I propose refining our hypotheses to focus on the successful configurations while discarding those that have underperformed. The next steps should include exploring configurations around tilt angles of 70° and 75° with azimuths between 180° and 190°, as these regions have shown the highest outputs in previous iterations. Additionally, testing configurations with a system capacity of 20 kW and varying DC to AC ratios may yield further insights into optimizing energy production.

### Updated Hypotheses

#### Moderate Tilt with New Capacity

*Rationale:* Testing a tilt of 68° with a system capacity of 17 kW may provide a balanced approach to maximizing energy production, as moderate configurations have shown consistent results.

*Confidence:* medium

*Points:*

- {'tilt': 68, 'azimuth': 188, 'system_capacity': 17, 'dc_ac_ratio': 1.2}

#### Balanced Configuration with New Tilt

*Rationale:* A tilt of 64° and azimuth of 191° with a balanced system capacity of 16 kW may still provide a good compromise for energy production, as this configuration has shown reasonable outputs.

*Confidence:* medium

*Points:*

- {'tilt': 64, 'azimuth': 191, 'system_capacity': 16, 'dc_ac_ratio': 1.4}

## Iteration 84

As we reach iteration 83 of the Bayesian Optimization, the dataset has provided significant insights into the parameter space's impact on energy production. The highest energy output observed is now 3.37 units, achieved with a tilt of 70.96° and an azimuth of 181.52°, a system capacity of 20 kW, and a DC to AC ratio of 1.00. This reinforces the trend that higher tilt angles (around 70° to 75°) and maximum system capacities (20 kW) are effective for maximizing energy production. The promising subspace around tilt angles of 70° to 75° and azimuth angles between 180° and 190° continues to be a focus. Conversely, configurations with low system capacities (e.g., 4.17 kW) and extreme tilt angles (e.g., 88.63°) have consistently resulted in lower energy outputs, indicating these subspaces are detrimental. Based on these findings, I propose refining our hypotheses to focus on the successful configurations while discarding those that have underperformed. The next steps should include exploring configurations around tilt angles of 70° and 75° with azimuths between 180° and 190°, as these regions have shown the highest outputs in previous iterations. Additionally, testing configurations with a system capacity of 20 kW and varying DC to AC ratios may yield further insights into optimizing energy production.

### Updated Hypotheses

#### Exploring 75° Tilt for Maximum Output

*Rationale:* A tilt of 75° with an azimuth of 188° and a system capacity of 19 kW could provide insights into the upper limits of energy production, as higher tilts have shown promise.

*Confidence:* medium

*Points:*

- {'tilt': 75, 'azimuth': 188, 'system_capacity': 19, 'dc_ac_ratio': 1.2}

#### Higher Tilt with Maximum Capacity

*Rationale:* Testing a tilt of 72° with a system capacity of 20 kW may further enhance energy production based on the observed trend of higher outputs with increased tilt.

*Confidence:* high

*Points:*

- {'tilt': 72, 'azimuth': 189, 'system_capacity': 20, 'dc_ac_ratio': 1.3}

#### Moderate Tilt with New Capacity

*Rationale:* Testing a tilt of 68° with a system capacity of 17 kW may provide a balanced approach to maximizing energy production, as moderate configurations have shown consistent results.

*Confidence:* medium

*Points:*

- {'tilt': 68, 'azimuth': 186, 'system_capacity': 17, 'dc_ac_ratio': 1.1}

#### Balanced Configuration with New Tilt

*Rationale:* A tilt of 64° and azimuth of 193° with a balanced system capacity of 16 kW may still provide a good compromise for energy production, as this configuration has shown reasonable outputs.

*Confidence:* medium

*Points:*

- {'tilt': 64, 'azimuth': 193, 'system_capacity': 16, 'dc_ac_ratio': 1.2}

## Iteration 97

As we reach iteration 96 of the Bayesian Optimization, the dataset has provided significant insights into the parameter space's impact on energy production. The highest energy output observed is now 3.37 units, achieved with a tilt of 70.96° and an azimuth of 181.52°, a system capacity of 20 kW, and a DC to AC ratio of 1.00. This reinforces the trend that higher tilt angles (around 70° to 75°) and maximum system capacities (20 kW) are effective for maximizing energy production. The promising subspace around tilt angles of 70° to 75° and azimuth angles between 180° and 190° continues to be a focus. Conversely, configurations with low system capacities (e.g., 4.17 kW) and extreme tilt angles (e.g., 88.63°) have consistently resulted in lower energy outputs, indicating these subspaces are detrimental. Based on these findings, I propose refining our hypotheses to focus on the successful configurations while discarding those that have underperformed. The next steps should include exploring configurations around tilt angles of 70° and 75° with azimuths between 180° and 190°, as these regions have shown the highest outputs in previous iterations. Additionally, testing configurations with a system capacity of 20 kW and varying DC to AC ratios may yield further insights into optimizing energy production.

### Updated Hypotheses

#### Refined Optimal Tilt and Azimuth

*Rationale:* Continuing to explore configurations around tilt 71° and azimuth 184° may yield further insights into maximizing energy production, as this region has shown high outputs.

*Confidence:* high

*Points:*

- {'tilt': 71, 'azimuth': 184, 'system_capacity': 20, 'dc_ac_ratio': 1.1}

#### Higher Tilt with Maximum Capacity

*Rationale:* Testing a tilt of 72° with a system capacity of 20 kW may further enhance energy production based on the observed trend of higher outputs with increased tilt.

*Confidence:* high

*Points:*

- {'tilt': 72, 'azimuth': 188, 'system_capacity': 20, 'dc_ac_ratio': 1.3}

#### Moderate Tilt with New Capacity

*Rationale:* Testing a tilt of 68° with a system capacity of 17 kW may provide a balanced approach to maximizing energy production, as moderate configurations have shown consistent results.

*Confidence:* medium

*Points:*

- {'tilt': 68, 'azimuth': 186, 'system_capacity': 17, 'dc_ac_ratio': 1.4}

## Final Conclusions

Throughout the optimization process, the hypotheses evolved significantly based on the experimental data collected at each iteration. Initially, the hypotheses focused on a broad range of tilt angles, azimuths, and system capacities, reflecting a diverse exploration of the parameter space. However, as the experiments progressed, specific configurations began to demonstrate consistently higher energy outputs, particularly those with tilt angles between 70° and 75° and azimuth angles around 180° to 190°.

The data revealed that higher system capacities (around 20 kW) and moderate DC to AC ratios were beneficial for maximizing energy production. Consequently, hypotheses that included lower tilt angles or extreme configurations were discarded due to their poor performance. Instead, the focus shifted towards refining configurations that had already shown promise, such as those with tilt angles of 71° and 72°.

This iterative refinement allowed for a more targeted approach, concentrating on the most effective parameter combinations. The final hypotheses were more confident and specific, reflecting a deeper understanding of the parameter relationships and their impact on energy production.

| Hypothesis Name                        | Initial Confidence | Final Confidence |
|----------------------------------------|--------------------|------------------|
| Optimal Tilt and Azimuth              | High               | High             |
| High Capacity with Moderate Tilt       | High               | High             |
| Balanced Configuration                 | Medium             | Medium           |
| Exploring Higher DC to AC Ratio       | Medium             | Medium           |
| Lower Tilt for Afternoon Capture       | Medium             | Discarded        |
| Refined Optimal Tilt and Azimuth       | -                  | High             |
| Exploring 75° Tilt for Maximum Output  | -                  | Medium           |
| Higher Tilt with Maximum Capacity      | -                  | High             |
| Moderate Tilt with New Capacity        | -                  | Medium           |
| Balanced Configuration with New Tilt   | -                  | Medium           |
# Ackley

## Experiment Overview

The goal of this experiment is to maximize a mathematical black-box function through Bayesian Optimization (BO). The optimization process will systematically explore a multidimensional parameter space defined by 15 input variables, ranging from \(x_0\) to \(x_{14}\), each constrained within the bounds of -30 to 20. This expansive range allows us to investigate a wide variety of potential configurations influencing the target function effectively.

Bayesian optimization is particularly suitable for this task, as it leverages a probabilistic model, typically a Gaussian Process, to predict the function's behavior across the defined parameter space. By selecting points that balance exploration (trying new areas) and exploitation (focusing on known promising areas), BO will iteratively propose new parameter settings to evaluate in order to improve the target outcome.

During the optimization process, if the performance gains plateau, I will suggest new configurations, potentially by exploring variations near current high-performing settings or examining different regions based on inferred uncertainty from the model. The ultimate objective is to efficiently converge on parameter settings that yield maximal function values, optimizing resource use and experimental time.

## Initial Thoughts

In the initial sampling step of the Bayesian Optimization experiment, we proposed a diverse set of hypotheses aimed at efficiently exploring the parameter space. Several points were selected to represent different regions within the stated bounds, from extreme values to balanced configurations. This varied approach should reveal how the target function responds under different conditions, and will be critical in identifying promising areas that warrant deeper investigation. Our focus on points that include balanced midpoints, extreme values, and random mixtures allows us to gather valuable insights into potential interactions among parameters. By evaluating these strategically chosen points, we can enhance our understanding of the function landscape and refine our Bayesian model for subsequent optimization steps, ultimately driving towards configurations that maximize the target outcome.
### Initial Hypotheses

#### Balanced Midpoint Approach

*Rationale:* This point is close to the center of the bounds for all parameters, allowing us to gauge the function's behavior under average conditions.

*Confidence:* medium

*Points:*

- {'x_0': -5, 'x_1': 0, 'x_2': 5, 'x_3': -10, 'x_4': 10, 'x_5': -15, 'x_6': 5, 'x_7': 0, 'x_8': -5, 'x_9': 15, 'x_10': -5, 'x_11': 10, 'x_12': -15, 'x_13': 0, 'x_14': 5}

#### High Parameter Value Exploration

*Rationale:* This hypothesis explores higher values of the parameters, which may reveal regions with improved performance outcomes.

*Confidence:* high

*Points:*

- {'x_0': 15, 'x_1': 15, 'x_2': 15, 'x_3': 15, 'x_4': 15, 'x_5': 15, 'x_6': 15, 'x_7': 15, 'x_8': 15, 'x_9': 15, 'x_10': 15, 'x_11': 15, 'x_12': 15, 'x_13': 15, 'x_14': 15}

#### Low Parameter Value Exploration

*Rationale:* By selecting all parameters at their lower bounds, we can see if a specific low configuration may yield unexpectedly high results.

*Confidence:* medium

*Points:*

- {'x_0': -30, 'x_1': -30, 'x_2': -30, 'x_3': -30, 'x_4': -30, 'x_5': -30, 'x_6': -30, 'x_7': -30, 'x_8': -30, 'x_9': -30, 'x_10': -30, 'x_11': -30, 'x_12': -30, 'x_13': -30, 'x_14': -30}

#### Random Mix of Extremes

*Rationale:* This point combines extreme values for some parameters while keeping others moderate, allowing us to test potential interactions between lower and higher configurations.

*Confidence:* low

*Points:*

- {'x_0': -30, 'x_1': 20, 'x_2': -10, 'x_3': 15, 'x_4': 0, 'x_5': -20, 'x_6': 10, 'x_7': -5, 'x_8': 5, 'x_9': 20, 'x_10': -30, 'x_11': 0, 'x_12': 10, 'x_13': -20, 'x_14': 15}

#### Symmetrical Configuration

*Rationale:* This hypothesis uses a symmetrical distribution of parameter values, which may help identify a balanced behavior in the function across its domain.

*Confidence:* medium

*Points:*

- {'x_0': -20, 'x_1': -15, 'x_2': -10, 'x_3': -5, 'x_4': 0, 'x_5': 5, 'x_6': 10, 'x_7': 15, 'x_8': 20, 'x_9': -20, 'x_10': -15, 'x_11': -10, 'x_12': -5, 'x_13': 0, 'x_14': 5}

## Iteration 22

As we proceed through iteration 21 of our Bayesian Optimization experiment, we have obtained valuable insights from the experimental data comprising 21 trials. The highest target value achieved thus far is 5.484 from iteration 1, characterized by a balanced distribution of parameter values. Iteration 2, which involved extreme positive settings for all parameters, yielded a significantly lower target of 2.941, indicating that such configurations are suboptimal. Similarly, configurations involving extreme negative values, particularly in iteration 3, consistently resulted in low targets. The data suggests that a balanced mixture of moderate positive and negative values across parameters, particularly around the mid-value ranges, tends to enhance performance. Subspaces defined by parameters like (x_4) and (x_5) combined with strategic choices of other values appear particularly promising. Moving forward, we should refine our hypotheses to focus on regions of the parameter space that previously showed higher target values while discarding those that yielded poor outcomes. The goal should be to explore configurations that balance both extremes in careful moderation to further investigate the nuanced interactions essential for maximizing our target function.

### Updated Hypotheses

#### Balanced Midpoint Exploration

*Rationale:* Focus on parameters near previously observed balanced outputs, seeking to enhance the better-performing regions while avoiding extremes.

*Confidence:* high

*Points:*

- {'x_0': -3, 'x_1': 1, 'x_2': 5, 'x_3': -5, 'x_4': 10, 'x_5': -10, 'x_6': 5, 'x_7': 0, 'x_8': -3, 'x_9': 15, 'x_10': -7, 'x_11': 9, 'x_12': -12, 'x_13': 2, 'x_14': 6}

#### Moderate Positive and Negative Mix

*Rationale:* Balancing moderate positive values with negative ones to capture the previously observed beneficial interactions among parameters.

*Confidence:* high

*Points:*

- {'x_0': -12, 'x_1': 10, 'x_2': -5, 'x_3': 0, 'x_4': 5, 'x_5': -10, 'x_6': 12, 'x_7': 6, 'x_8': -3, 'x_9': 10, 'x_10': -2, 'x_11': 4, 'x_12': -1, 'x_13': 1, 'x_14': 9}

#### Targeting Beneficial Midpoints

*Rationale:* Further examining regions around mid-value ranges previously corresponding to optimal function behavior, as these have shown the best results.

*Confidence:* high

*Points:*

- {'x_0': -12, 'x_1': 5, 'x_2': 0, 'x_3': -5, 'x_4': 10, 'x_5': 3, 'x_6': 0, 'x_7': 2, 'x_8': -1, 'x_9': 8, 'x_10': 4, 'x_11': -2, 'x_12': 6, 'x_13': -7, 'x_14': 2}

#### Focus on Successful Iteration Trends

*Rationale:* Exploring configurations that focus on successful parameter trends linked to previously high outputs, refining the parameter combination to maximize the target.

*Confidence:* medium

*Points:*

- {'x_0': 5, 'x_1': 5, 'x_2': 0, 'x_3': -10, 'x_4': 10, 'x_5': -5, 'x_6': 0, 'x_7': 5, 'x_8': 5, 'x_9': 5, 'x_10': -10, 'x_11': -5, 'x_12': 0, 'x_13': 5, 'x_14': 5}

#### Testing Extremes for Unique Insights

*Rationale:* A minority view suggesting extreme negative and positive interactions might reveal hidden response characteristics to explore further, albeit low confidence.

*Confidence:* low

*Points:*

- {'x_0': -28, 'x_1': -30, 'x_2': -29, 'x_3': -30, 'x_4': -25, 'x_5': -30, 'x_6': -30, 'x_7': -28, 'x_8': -30, 'x_9': -30, 'x_10': -30, 'x_11': -30, 'x_12': -30, 'x_13': -30, 'x_14': -30}

## Iteration 56

As we reach iteration 55 of our Bayesian Optimization experiment, we have gathered critical insights from 55 trials. The highest target value achieved so far is 12.840 from iteration 40, showcasing a balanced configuration of moderate values across several parameters. Notably, configurations around mid-range settings (such as values near (x_0 approx -5), (x_1 approx 0) to (5), and positive values for (x_4)) have produced superior results, confirming the importance of avoiding extreme settings. Conversely, configurations dominated by extremes, particularly where parameters are set to -30 or 20, consistently yield lower target outputs, highlighting these regions as detrimental to performance. The best-performing combinations typically cluster around moderate values, suggesting that nuanced interactions among parameter settings contribute to optimally high outcomes. Moving forward, we will refine our hypotheses to capitalize on these learnings by focusing on parameter combinations that blend moderate positive and negative values while avoiding configurations that have proven ineffective. Additionally, we will implement targeted perturbations around previously successful configurations to uncover local maxima. This approach should guide us towards maximizing the target effectively in the subsequent iterations.

### Updated Hypotheses

#### Mid-Value Exploration

*Rationale:* Continuing to probe the success of earlier mid-range configurations by targeting value shifts around the existing best points.

*Confidence:* high

*Points:*

- {'x_0': -4, 'x_1': 4, 'x_2': 7, 'x_3': -4, 'x_4': 17, 'x_5': -10, 'x_6': 4, 'x_7': 0, 'x_8': 5, 'x_9': 10, 'x_10': -3, 'x_11': 1, 'x_12': -2, 'x_13': 9, 'x_14': 6}

#### Positive-Heavy Configuration

*Rationale:* Testing a configuration where significantly positive values are prioritized in an attempt to probe maximum impacts effectively.

*Confidence:* high

*Points:*

- {'x_0': 3, 'x_1': 10, 'x_2': 5, 'x_3': 0, 'x_4': 20, 'x_5': -5, 'x_6': 1, 'x_7': 13, 'x_8': 6, 'x_9': 19, 'x_10': 2, 'x_11': 4, 'x_12': 9, 'x_13': 18, 'x_14': 15}

#### Diverse Parameter Mix

*Rationale:* A balanced mix of moderately high and low values aiming to capture the interplay between parameters that previously yielded higher performance.

*Confidence:* medium

*Points:*

- {'x_0': -10, 'x_1': 5, 'x_2': 0, 'x_3': -3, 'x_4': 12, 'x_5': -15, 'x_6': 6, 'x_7': 2, 'x_8': 0, 'x_9': 10, 'x_10': -1, 'x_11': 3, 'x_12': 5, 'x_13': -1, 'x_14': 8}

#### Controlled Extreme Exploration

*Rationale:* Testing configurations that edge toward extremes but maintain a degree of mid-range balance, seeking possible non-linear interactions.

*Confidence:* low

*Points:*

- {'x_0': -30, 'x_1': 15, 'x_2': 20, 'x_3': -15, 'x_4': -10, 'x_5': 5, 'x_6': -30, 'x_7': 10, 'x_8': 20, 'x_9': -5, 'x_10': -30, 'x_11': 5, 'x_12': 0, 'x_13': -30, 'x_14': 12}

#### Adapted Successful Trends

*Rationale:* Focus on previous high-performing point adaptations, redistributing values slightly to explore around effective configurations.

*Confidence:* high

*Points:*

- {'x_0': -3.5, 'x_1': 4.5, 'x_2': 8.0, 'x_3': -4.5, 'x_4': 16.5, 'x_5': -9, 'x_6': 4.5, 'x_7': 1, 'x_8': 4.5, 'x_9': 11, 'x_10': -2, 'x_11': 2, 'x_12': -1, 'x_13': 9.5, 'x_14': 6.5}

## Iteration 79

As we reach iteration 78 of our Bayesian Optimization experiment, the accumulated data from 78 trials reveals clear trends influencing the target outcomes. The highest target value achieved so far is 12.840 from iteration 40, which stemmed from a balanced configuration concentrating on moderate values, particularly with (x_0) around -4, (x_1) near 0 to 5, and strong positive contributions from parameters like (x_4). Iteration 78's evaluation yielded a target of 12.634, affirming the benefits of mid-range parameter settings over extreme values. Likewise, configurations that leaned towards extremes—specifically settings near -30 or 20—consistently produced suboptimal results, with many trials yielding targets below 3. This corroborates the detrimental impact of extreme parameter combinations. Our focus should now be toward exploring configurations that maintain moderate values while still probing for moderate positive contributions, particularly in parameters (x_4) and (x_5), as these interactions seem critical. Moving forward, we will refine our hypotheses, targeting promising parameter regions previously linked to higher outputs while discarding those with proven negative effects.

### Updated Hypotheses

#### Refined Mid-Value Exploration

*Rationale:* Investigating configurations around previously successful mid-range values to explore possible local maxima.

*Confidence:* high

*Points:*

- {'x_0': -4, 'x_1': 4, 'x_2': 6, 'x_3': -4, 'x_4': 17, 'x_5': -9, 'x_6': 4, 'x_7': 0, 'x_8': 4, 'x_9': 10, 'x_10': -3, 'x_11': 1, 'x_12': -2, 'x_13': 9, 'x_14': 6}

#### Balanced Positive-Negative Mix

*Rationale:* Exploring configurations that balance moderate positive values with slightly negative ones, targeting previously successful output ranges.

*Confidence:* high

*Points:*

- {'x_0': -10, 'x_1': 10, 'x_2': -3, 'x_3': -1, 'x_4': 14, 'x_5': -8, 'x_6': 5, 'x_7': 2, 'x_8': 1, 'x_9': 10, 'x_10': -2, 'x_11': 4, 'x_12': 3, 'x_13': 0, 'x_14': 8}

#### Moderate Success Adaptation

*Rationale:* Adjusting parameters from previously successful trials to search for enhanced target outputs through minor perturbations.

*Confidence:* high

*Points:*

- {'x_0': -3.5, 'x_1': 4.5, 'x_2': 8.0, 'x_3': -4.0, 'x_4': 17.0, 'x_5': -9.0, 'x_6': 4.5, 'x_7': 1.0, 'x_8': 4.5, 'x_9': 10, 'x_10': -2, 'x_11': 1, 'x_12': -1, 'x_13': 9, 'x_14': 7}

#### Exploratory Midpoint Subspace

*Rationale:* Investigating configurations near successful midpoints where favorable targets were consistently observed.

*Confidence:* medium

*Points:*

- {'x_0': -6, 'x_1': 2, 'x_2': -2, 'x_3': -3, 'x_4': 12, 'x_5': -8, 'x_6': 1, 'x_7': 0, 'x_8': 3, 'x_9': 5, 'x_10': -1, 'x_11': 4, 'x_12': 0, 'x_13': 2, 'x_14': 6}

#### Reduced Extremes Exploration

*Rationale:* While steering clear of aggressive parameter settings, this hypothesis lightly explores the limits to test for subtle interactions leading to better outcomes.

*Confidence:* low

*Points:*

- {'x_0': -20, 'x_1': 5, 'x_2': 15, 'x_3': 0, 'x_4': 10, 'x_5': -15, 'x_6': 0, 'x_7': -5, 'x_8': 10, 'x_9': -5, 'x_10': -20, 'x_11': 5, 'x_12': 8, 'x_13': 5, 'x_14': 5}

## Final Conclusions

Throughout the course of the Bayesian Optimization experiment, our hypotheses evolved significantly based on the iterations, outputs, and insights gained from prior trials. Initially, our hypotheses focused on a diverse exploration of input parameter combinations, including balanced midpoints and extremes. However, as we accumulated experimental data, we observed clear trends, particularly the effectiveness of moderate values and configurations avoiding extremes. 

Our highest target output of 12.840 consistently emerged around combinations that emphasized balanced settings across the parameters (like \(x_0\) near -4 and many positive contributions from \(x_4\)), validating our evolution towards mid-range configurations.

In subsequent iterations, our hypotheses narrowed to address locally promising areas, focusing on slight perturbations around previously successful configurations. We prioritized parameter combinations that captured beneficial interactions and excluded those leading to poor performance. Our confidence levels grew as we refined our understanding of the landscape shaped by the responses of the black-box function.

The changes in confidence levels for different hypotheses throughout the optimization process are summarized in the table below:

| Hypothesis                          | Initial Confidence | Final Confidence |
|-------------------------------------|-------------------|------------------|
| Balanced Midpoint Exploration       | Medium            | High             |
| Moderate Positive and Negative Mix  | Medium            | High             |
| Targeting Beneficial Midpoints      | Medium            | High             |
| Focus on Successful Iteration Trends| Medium            | Medium           |
| Testing Extremes for Unique Insights| Low               | Low              | 

This reflects a shift towards models with higher confidence, concentrating on those elements that produced the best results during the experimental phases.
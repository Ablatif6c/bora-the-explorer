# Ackley

## Experiment Overview

The primary goal of this experiment is to maximize a mathematical black-box function through the systematic exploration of an extensive parameter space using Bayesian Optimization (BO). The function is defined by 15 input variables (x_0 to x_14), each constrained within the bounds of (-30, 20). BO will serve as an efficient search mechanism to navigate this multi-dimensional space, leveraging the probabilistic modeling of the function to make informed decisions about where to sample next.

As the optimization progresses, BO will use a surrogate model (likely a Gaussian Process or similar) to approximate the target function and calculate an acquisition function, which indicates where the parameters may yield the highest expected improvement. When BO plateaus—indicating diminished returns from the current sampling strategy—I will provide recommendations for alternatives, such as refining the exploration-exploitation balance, adjusting hyperparameters of the surrogate model, or suggesting specific points in the parameter space based on observed behaviors.

The intended outcome is to identify the optimal settings of the input variables that produce the highest value of the target function, thereby efficiently converging on the global optima within the defined constraints. This approach harnesses the strengths of Bayesian optimization to mitigate the number of function evaluations needed in this challenging black-box setting.

## Initial Thoughts

In this initial sampling step, we have generated hypotheses that collectively explore a diverse range of the parameter space to maximize the target function. The proposed points span extremes in the parameter bounds, central values, and combinations thereof, providing a comprehensive evaluation of the black-box function's behavior. Notably, exploring lower bounds offers insights into how negative inputs affect performance, while central values may reveal stability characteristics of the function. Furthermore, testing upper bounds seeks to uncover if the function responds favorably to higher parameter values. The diagonal spread and localized clusters help assess interactions among parameters and the potential presence of local maxima. By addressing different regions and hypothesizing about relationships within this high-dimensional space, we aim to systematically identify conditions that maximize the target function as we progress through the optimization process.
### Initial Hypotheses

#### Explorative Negative Cluster

*Rationale:* Exploring the lower bound of the parameter space may reveal extreme conditions under which the target function behaves favorably.

*Confidence:* medium

*Points:*

- {'x_0': -30, 'x_1': -30, 'x_2': -30, 'x_3': -30, 'x_4': -30, 'x_5': -30, 'x_6': -30, 'x_7': -30, 'x_8': -30, 'x_9': -30, 'x_10': -30, 'x_11': -30, 'x_12': -30, 'x_13': -30, 'x_14': -30}

#### Central Exploration

*Rationale:* Sampling near the center of the parameter space may yield insights into the function behavior, potentially identifying stable regions for improvement.

*Confidence:* high

*Points:*

- {'x_0': -5, 'x_1': 0, 'x_2': 5, 'x_3': 10, 'x_4': 5, 'x_5': 0, 'x_6': -5, 'x_7': -10, 'x_8': 15, 'x_9': -5, 'x_10': 0, 'x_11': 0, 'x_12': -2, 'x_13': 3, 'x_14': 6}

#### Positive Extremes

*Rationale:* Investigating the upper limits of the parameter space could unveil how the function responds to higher values.

*Confidence:* medium

*Points:*

- {'x_0': 20, 'x_1': 15, 'x_2': 10, 'x_3': 20, 'x_4': 18, 'x_5': 12, 'x_6': 15, 'x_7': 10, 'x_8': 20, 'x_9': 20, 'x_10': 15, 'x_11': 20, 'x_12': 18, 'x_13': 19, 'x_14': 20}

#### Diagonal Spread

*Rationale:* Employing a diagonal strategy from low negative to positive values may help to reveal interactions among parameters.

*Confidence:* low

*Points:*

- {'x_0': -30, 'x_1': -15, 'x_2': 0, 'x_3': 5, 'x_4': 10, 'x_5': 15, 'x_6': 20, 'x_7': 5, 'x_8': -10, 'x_9': -5, 'x_10': 0, 'x_11': -15, 'x_12': -20, 'x_13': 10, 'x_14': 15}

#### Local Peaks

*Rationale:* Identifying localized clusters through this hypothesis may help in uncovering potential local maxima in the target function.

*Confidence:* medium

*Points:*

- {'x_0': -15, 'x_1': -10, 'x_2': 5, 'x_3': 10, 'x_4': 0, 'x_5': 15, 'x_6': 10, 'x_7': -5, 'x_8': -10, 'x_9': 5, 'x_10': 2, 'x_11': -8, 'x_12': 3, 'x_13': 0, 'x_14': -10}

## Iteration 91

As we continue to analyze the results from the Bayesian Optimization experiments, it's becoming evident that the balance between parameter values is crucial in determining the outcome of the target function. The highest target achieved thus far remains at 16.372, and we see that a combination of moderate positive parameters is central to achieving improved results. The regions showing promise are those with mixed moderate and positive values. In particular, iterations with multiple parameters at -30 have consistently resulted in lower target values, further emphasizing the importance of avoiding extreme negativity. Therefore, our revised hypotheses will continue to leverage these insights, focusing on stable configurations that have previously yielded success, while also avoiding previously ineffective configurations. By emphasizing combinations of parameters closer to the center or positive values, we aim to discover optimal configurations for maximizing the target function.

### Updated Hypotheses

#### Optimized Central Values

*Rationale:* Exploring values centered around previously successful points could capitalize on observed performance trends.

*Confidence:* high

*Points:*

- {'x_0': 1, 'x_1': 2, 'x_2': -1, 'x_3': 1, 'x_4': 0, 'x_5': 1, 'x_6': 1, 'x_7': 0, 'x_8': 1, 'x_9': 1, 'x_10': -1, 'x_11': 0, 'x_12': 1, 'x_13': 0, 'x_14': 1}

#### Micro-Variation Exploration

*Rationale:* Fine-tuning around the highest observed target to capture variations might yield further improvements.

*Confidence:* medium

*Points:*

- {'x_0': 1.2, 'x_1': 0.5, 'x_2': -0.5, 'x_3': 0.5, 'x_4': 1, 'x_5': 1, 'x_6': 1, 'x_7': -0.3, 'x_8': 1.5, 'x_9': 0.7, 'x_10': -0.6, 'x_11': 1, 'x_12': 0, 'x_13': -0.5, 'x_14': 1}

#### Balanced Positive Exploration

*Rationale:* By focusing on combinations of slight positive values, this hypothesis seeks to reveal peaks in the target function more effectively.

*Confidence:* medium

*Points:*

- {'x_0': 3, 'x_1': 3, 'x_2': 1, 'x_3': 2, 'x_4': 0, 'x_5': 2, 'x_6': 0, 'x_7': -1, 'x_8': 2, 'x_9': 0, 'x_10': 0, 'x_11': -1, 'x_12': 2, 'x_13': 1, 'x_14': 1}

#### Extreme Negative Test

*Rationale:* Validating the effects of extreme negative parameters could help clarify their impact on the function's performance.

*Confidence:* low

*Points:*

- {'x_0': -25, 'x_1': -20, 'x_2': -22, 'x_3': -18, 'x_4': -15, 'x_5': -12, 'x_6': -10, 'x_7': -5, 'x_8': -3, 'x_9': -1, 'x_10': -4, 'x_11': -8, 'x_12': -6, 'x_13': -7, 'x_14': -9}

#### High Positive Variation

*Rationale:* Testing combinations with high positive values could reveal potential unexplored peaks in the target space.

*Confidence:* medium

*Points:*

- {'x_0': 20, 'x_1': 15, 'x_2': 20, 'x_3': 15, 'x_4': 18, 'x_5': 20, 'x_6': 20, 'x_7': 15, 'x_8': 20, 'x_9': 20, 'x_10': 15, 'x_11': 20, 'x_12': 20, 'x_13': 18, 'x_14': 20}

## Final Conclusions

As the Bayesian Optimization experiments progressed, our hypotheses evolved substantially based on the experimental data collected, especially the observed target values. Initially, our hypotheses focused broadly on different regions of the parameter space—ranging from extreme negative values to balanced configurations near the center. As we gathered insights from the initial iterations, it became clear that configurations with a balance of moderate positive values consistently achieved higher target scores.

With the highest observed target remaining at 16.372, we shifted our focus towards fine-tuning parameter clusters where positive values were predominant while avoiding extreme negativity. This adjustment reflected a strategic pivot to explore more stable configurations that had previously demonstrated better performance. The introduction of micro-variations around successful points aimed to capture local peaks and enhance optimal configurations.

While exploring configurations with extreme negatives was initially considered, the subsequent results indicated that these values often led to considerably lower targets, prompting a reduction in confidence for those hypotheses.

In summary, the hypotheses transitioned from wide-ranging exploratory points to targeted refinements focusing on stable configurations, based on familiarity with the function's response to varying parameters. 

| Hypothesis Name               | Initial Confidence | Final Confidence |
|-------------------------------|-------------------|------------------|
| Optimized Central Values      | High              | High             |
| Micro-Variation Exploration    | Medium            | Medium           |
| Balanced Positive Exploration  | Medium            | High             |
| Extreme Negative Test         | Low               | Low              |
| High Positive Variation        | Medium            | Low              |
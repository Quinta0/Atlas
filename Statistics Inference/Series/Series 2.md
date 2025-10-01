# Ex 1
**Given data:** 4, 4, 7, 6, 6, 11, 1, 6, 3, 3 ($n = 10$ observations)
**True parameter:** $\lambda = 5$

### Part 1: Estimate the expected value of X

**Process:** For a Poisson distribution, E[X] = λ. We use the sample mean as an unbiased estimator.

**Solution:**
$$\bar{x}_n = \frac{1}{n}\sum_{i=1}^{n} x_i = \frac{4+4+7+6+6+11+1+6+3+3}{10} = \frac{51}{10} = 5.1$$
**Estimated $E[X] = 5.1$**

### Part 2: Estimate the variance using the unbiased estimator

**Process:** For Poisson distribution, $\text{Var}(X) = \lambda$. We use the corrected sample variance with $(n-1)$ denominator.

**Solution:**
First, calculate deviations from the mean:
- $(4-5.1)^2 = 1.21$
- $(4-5.1)^2 = 1.21$  
- $(7-5.1)^2 = 3.61$
- $(6-5.1)^2 = 0.81$
- $(6-5.1)^2 = 0.81$
- $(11-5.1)^2 = 34.81$
- $(1-5.1)^2 = 16.81$
- $(6-5.1)^2 = 0.81$
- $(3-5.1)^2 = 4.41$
- $(3-5.1)^2 = 4.41$

$$S_n^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2 = \frac{1}{9} \times 68.9 = 7.66$$

**Estimated $\text{Var}(X) = 7.66$**

**Theory behind this:** $S_n^2 = \frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar{X}_n)^2$ is an unbiased estimator of $\text{Var}(X)$, while the version with denominator $n$ is biased. The $(n-1)$ correction accounts for the loss of one degree of freedom when estimating the mean.
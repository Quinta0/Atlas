Consider the binomial distribution of the number $k$ of successes in $n$ independent trials:

$$\sum_{i=1}^{n} X_i \sim \text{Binomial}(n, p)$$

The log-likelihood function is:

$$\log L(p) = \log \binom{n}{k} + k \log(p) + (n-k) \log(1-p)$$

## Part 1: Plot Log L(p)
Given $n=100$ and $k=10$ 
![[image-1.png]]

## Part 2: Compute the MLE

**Given:** $\sum_{i=1}^{n} x_i = 15$ with $n = 100$ trials

### Finding the MLE

To find the maximum likelihood estimator, we take the derivative of the log-likelihood with respect to $p$ and set it equal to zero:

$$\frac{d}{dp} \log L(p) = \frac{k}{p} - \frac{n-k}{1-p} = 0$$

Solving for $p$:

$$\frac{k}{p} = \frac{n-k}{1-p}$$

$$k(1-p) = p(n-k)$$

$$k - kp = pn - pk$$

$$k = pn$$

$$\hat{p}_{MLE} = \frac{k}{n}$$
![[image-2.png]]
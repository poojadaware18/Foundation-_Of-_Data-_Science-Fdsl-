import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
import pandas as pd

# 1. Load data
df = pd.read_csv('marketing_campaign_dataset.csv')
data = df['Conversion_Rate']   # already a fraction (0-1), so no /100

# 2. Define parameters
n = 10                         # number of trials (change as needed)
p = np.mean(data)              # probability of success

print('Number of Trials:', n)
print('Probability of Success:', p)

# 3. Generate possible number of successes
x = np.arange(0, n + 1)

# 4. Compute PMF and CDF
pmf = binom.pmf(x, n, p)
cdf = binom.cdf(x, n, p)

# 5. Compute mean and standard deviation
mean = n * p
std_dev = np.sqrt(n * p * (1 - p))

print('Mean:', mean)
print('Standard Deviation:', std_dev)

# 6. Plot the Binomial Distribution curve
plt.figure(figsize=(8, 5))

plt.plot(x, pmf, color='blue', marker='o',
         label='Binomial Distribution Curve')

plt.bar(x, pmf, color='orange', alpha=0.4,
        label='Probability')

plt.axvline(mean, color='red', linestyle='--', label='Mean')
plt.axvline(mean + std_dev, color='green', linestyle=':', label='+1 Std Dev')
plt.axvline(mean - std_dev, color='green', linestyle=':', label='-1 Std Dev')

plt.title('Binomial Distribution Curve')
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# 7. Calculate probabilities
p_exactly_8 = binom.pmf(8, n, p)
p_at_least_5 = 1 - binom.cdf(4, n, p)
p_at_most_5 = binom.cdf(5, n, p)

print('P(X = 8):', p_exactly_8)
print('P(X >= 5):', p_at_least_5)
print('P(X <= 5):', p_at_most_5)
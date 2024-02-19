import math
import random


# Generate random pebble sizes
def create_sample(mean, variance, n=100):
    return [random.gauss(mean, math.sqrt(variance)) for _ in range(n)]


# Calculate the mean for each sample as well as the overall mean and variance for the entire set
def calculate_mean_variance(samples):
    sample_means = [sum(sample) / len(sample) for sample in samples]
    overall_mean = sum(sample_means) / len(sample_means)
    overall_variance = sum((x - overall_mean) ** 2 for x in sample_means) / (len(sample_means) - 1)
    return overall_mean, overall_variance


# Use the t-distribution to calculate the probability
def t_distribution_probability(nu, t):
    def gamma(x):
        return math.sqrt(2 * math.pi / x) * (x / math.e) ** x

    def t_distribution(x, nu):
        coef = gamma((nu + 1) / 2) / (math.sqrt(nu * math.pi) * gamma(nu / 2))
        return coef * (1 + x ** 2 / nu) ** (-(nu + 1) / 2)

    def simpsons_rule(f, a, b, n, nu):
        # Chat Gpt helped me write this function 
        h = (b - a) / n
        s = f(a, nu) + f(b, nu)
        for i in range(1, n, 2):
            s += 4 * f(a + i * h, nu)
        for i in range(2, n-1, 2):
            s += 2 * f(a + i * h, nu)
        return s * h / 3

    return simpsons_rule(t_distribution, -100, t, 10000, nu)

# The mesh parameters for the Supplier A (1"x1") and Supplier B (7/8"x7/8")
mean_a, variance_a = 1, 0.1  # 1"x1" mesh for Supplier A
mean_b, variance_b = 7/8, 0.1  # 7/8"x7/8" mesh for Supplier B

# Pass the supplier data through the create sample function
samples_a = [create_sample(mean_a, variance_a) for _ in range(11)]
samples_b = [create_sample(mean_b, variance_b) for _ in range(11)]

# Calculate the mean and variance for the two supplier samples
mean_a, var_a = calculate_mean_variance(samples_a)
mean_b, var_b = calculate_mean_variance(samples_b)

# Calculate the t-value for a 1-sided t-test using the variances and means from supplier A and B
s_pooled = math.sqrt(((10 * var_a) + (10 * var_b)) / 58)
t_value = (mean_a - mean_b) / (s_pooled * math.sqrt(2 / 11))

# Degrees of freedom for the t-test
nu = 2 * 10  # (n-1) + (n-1) for two samples each of size 11

# Calculate the probability from the t-value
probability = t_distribution_probability(nu, t_value)

print(f"Mean gravel size for Supplier A: {mean_a:.2f} inches")
print(f"Mean gravel size for Supplier B: {mean_b:.2f} inches")
print(f"T-value for the comparison: {t_value:.2f}")
print(f"Probability of a significant difference between suppliers: {probability:.4f}")

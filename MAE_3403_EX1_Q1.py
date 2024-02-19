import random


"""Goal: Create a code that creates 11 normally distributed samples of rock sizes that contain N=100 
rocks the program should then report the mean and variance for each sample as well as the mean and variance
  of the sampling mean"""


def create_sample(n, mu, sigma, k=12):
    """Create a sample of 'n' rocks using the random function and the central limit theorem"""
    # Create a loop that will create random rock sizes
    return [mu + sigma * (sum(random.random() for _ in range(k)) - k / 2) for _ in range(n)]
    # ChatGPT Helped me write the function above


def mean_calculation(sample):
    # Calculates the mean of the randomly generated rock size sample
    return sum(sample) / len(sample)


def variance_calculation(sample, mean):
    # Calculates the variance of the randomly generated rock size sample
    return sum((x - mean) ** 2 for x in sample) / (len(sample) - 1)


def rock_sieving(mu=0.3125, sigma=0.02, n=100, samples=11):
    """Create a function that simulates sieving through the crushed rock pile. The mean is defined by the
    midpoint between the 1" mesh and the 3/8" mesh. Assuming a range of rock sizes that are between
    1.5 inches and 0.125 inches, the variance would be 0.02 over a sample of 100 rocks"""
    sample_means = []
    # Creates an array to store the means of each sample
    sample_variances = []
    # Creates an array to store the variances of each sample

    for _ in range(samples):
        # Initiate loop for Sample iterations

        sample = create_sample(n, mu, sigma)
        # Calls create sample function to create one sample wit 'n' number of rock sizes

        sample_mean = mean_calculation(sample)
        # passes sample through the mean calculation function and returns calculated mean

        sample_variance = variance_calculation(sample, sample_mean)
        # passes sample through the variance calculation function and returns calculated variance

        sample_means.append(sample_mean)
        # Stores sample mean into sample means array to be called back later for total samples calculations
        sample_variances.append(sample_variance)
        # Stores sample variance into sample variances array to be called back later for total samples calculations

        print(f"Sample mean: {sample_means}, Sample variance: {sample_variances}")

    total_mean = mean_calculation(sample_means)
    # Calculates the total mean of all samples from stored values in sample means array

    total_variance = variance_calculation(sample_means, total_mean)
    # Calculates the total variance of all samples from stored values in sample variances array

    print(f"Total mean of Samples means: {total_mean}, Total Variance of Samples means: {total_variance}")


rock_sieving()

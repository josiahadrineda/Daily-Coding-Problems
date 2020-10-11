import random

#bias is in favor of 0, range: (0, 1)
def toss_biased():
    bias = 0.69

    rand = random.random()
    return 0 if rand < bias else 1

def determine_biases(iterations):
    biases = {0:0, 1:0}
    unbiases = {0:0, 1:0}
    for i in range(iterations):
            flip = toss_biased()
            biases[flip] += 1

            flip = not flip if i % 2 == 0 else flip
            unbiases[flip] += 1

    for k in biases:
        biases[k] = round(biases[k] / iterations, 2)

    for k in unbiases:
        unbiases[k] = round(unbiases[k] / iterations, 2)

    return biases, unbiases

def toss_unbiased():
    biases, unbiases = determine_biases(1000000)
    print("Bias 0: {}\nBias 1: {}\nUnbias 0: {}\nUnbias 1:{}\n".format(biases[0], biases[1], unbiases[0], unbiases[1]))

    rand = random.random()
    return 0 if rand < biases[0] else 1

print(toss_unbiased())
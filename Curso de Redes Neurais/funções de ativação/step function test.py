import numpy as np

def stepfunction(soma):
    if (soma >= 1):
        return 1
    return 0 

def sigmoidFunction(soma):
    return 1 / (1 + np.exp(-soma))

def tanhFunction(soma):
    return (np.exp(soma) - np.exp(-soma)) / (np.exp(soma) + np.exp(-soma))

def reluFunction(soma):
    if soma >= 0:
        return soma
    return 0

def linearFunction(soma) :
    return soma

def softmaxFunction(x):
    ex = np.exp(x)
    return ex / ex.sum()

teste = stepfunction(-1)
teste = sigmoidFunction(-0.358)
teste = tanhFunction(0.358)
teste = reluFunction(0.358)
teste = linearFunction(0.255)
valores = [7.0, 2.0, 1.3]
print (softmaxFunction(valores))

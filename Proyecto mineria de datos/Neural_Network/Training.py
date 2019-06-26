from Neural_Network.LogicTraining import initValues, netInput, calcError
tupla = (1, 0, 1)
trainingRate = 0.9
inpWeights, midWeights, bias = initValues()
# inpWeights = [[0.2, -0.3],[0.4, 0.1], [-0.5, 0.2]] # los ejemplos del libro
# midWeights = [-0.3, -0.2]
# bias = [-0.4, 0.2, 0.1]

def netCalculations():
    outputs = netInput(inpWeights, midWeights, bias, tupla)
    return outputs


def errorNodes(outputs): # envia a errors (una lista) los errores y añadimos el ultimo explicitamente
    finalError = outputs[-1] * ((1 - outputs[-1]) ** 2)
    errors = calcError(finalError, outputs, midWeights)
    errors.append(finalError)
    return errors


def updating(): # funcion que actualiza todos los valores
    outputs = netCalculations()
    errors = errorNodes(outputs)
    for unit in range(len(midWeights)):
        midWeights[unit] = midWeights[unit] + trainingRate * errors[-1] * outputs[unit]
    for unit in range(len(inpWeights)):
        for w in range(len(inpWeights[0])):
            inpWeights[unit][w] = inpWeights[unit][w] + trainingRate * errors[w] * tupla[unit]
        bias[unit] = bias[unit] + trainingRate * errors[unit]

def getValues():
    return inpWeights, midWeights, bias
import math
import random

class NeuralNetwork():
    def __init__(self):
        random.seed(1)
        self.weights = [random.uniform(-1,1),random.uniform(-1,1),random.uniform(-1,1)]

    def think(self,neuron_inputs):
        sum_of_weighted_inputs = self.sum_of_weighted_inputs(neuron_inputs)
        neuron_output = self.sigmoid(sum_of_weighted_inputs)
        return neuron_output

    def train(self,training_set_examples,number_of_iterations):
        for iteration in range(number_of_iterations):
            for training_set_example in training_set_examples:
                predicted_output = self.think(training_set_example["inputs"])
                error_in_output = training_set_example["output"] - predicted_output
                
                for index in range(len(self.weights)):
                    neuron_input = training_set_example["inputs"][index]
                    adjust_weight = neuron_input * error_in_output * self.sigmoid_gradient(predicted_output)
                    self.weights[index] += adjust_weight



    def sigmoid(self,sum_of_weighted_inputs):
        return 1/(1 + math.exp(-sum_of_weighted_inputs))

    def sigmoid_gradient(self,neuron_output):
        return neuron_output * (1 - neuron_output)

    def sum_of_weighted_inputs(self,neuron_inputs):
        sum_of_weighted_inputs = 0
        for index,neuron_input in enumerate(neuron_inputs):
            sum_of_weighted_inputs += self.weights[index] * neuron_input

        return sum_of_weighted_inputs


neural_network = NeuralNetwork()
print("Random Starting weights "+ str(neural_network.weights))

training_set_examples = [
                         {"inputs":[0,0,1],"output":0},
                         {"inputs":[1,1,1],"output":1},
                         {"inputs":[1,0,1],"output":1},
                         {"inputs":[0,1,1],"output":0},
                        ]

neural_network.train(training_set_examples,number_of_iterations=10000)
print("new weights after training "+ str(neural_network.weights))
new_situation = [1,0,0]
prediction = neural_network.think(new_situation)
print("predictions after training "+ str(prediction))
import numpy as np
import time

def sigmoid(x): #Defining the sigmoid function for computation
    return 1.0/(1.0 + np.exp(-x))


class NeuralNetworkXOR: #Class to be called for initializing the Neural Network

    def __init__(self, nInput, nHiddenLayer, nOutputLayer):
        self.alpha = 0.5 #Learning Rate of the network

        self.nInput = nInput #Number of Neurons in the input layer
        self.nHiddenLayer = nHiddenLayer #Number of Neurons in the Hidden Layer
        self.nOutputLayer = nOutputLayer #Number of Neurons in the Output Layer

        self.hiddenWeights = np.random.random((self.nHiddenLayer, self.nInput+1)) #Initializing weight matrices, to serve as connections         between Input and Hidden layer
        self.outputWeights = np.random.random((self.nOutputLayer, self.nHiddenLayer+1))#Initializing weight matrices to serve as                 connections between Hidden layer and output neuron

        self.hiddenLayerActivation = np.zeros((self.nHiddenLayer, 1), dtype=float) #Serves as a container, for matrix multiplication of         weights and input values
        self.outputLayerActivation = np.zeros((self.nOutputLayer, 1), dtype=float) #Servers as a container, for matrix multiplication of         output weights and resultant output from the hidden layer

        self.initialOutput = np.zeros((self.nInput+1, 1), dtype=float) #Container of input values to be initialized
        self.hiddenLayerOutput = np.zeros((self.nHiddenLayer+1, 1), dtype=float) #Container of hidden layer values after multiplication         and sigmoid activation
        self.outputLayerOutput = np.zeros((self.nOutputLayer, 1),  dtype=float) #Container of Final output following forward propagation         and final application of Sigmoid, for output.

        self.hiddenLayerDelta = np.zeros(self.nHiddenLayer, dtype=float) #Error propgated from hidden layer to weights between input             and hidden layer
        self.outputLayerDelta = np.zeros(self.nOutputLayer, dtype=float) #Error propagated from output from final layer to the weights           between hidden layer and output layer
"""
Initialization of forward propagation which allows for updation of weight values in order to learn a represenatation, which in this case means forward propagating a set of input values which is the truth table corresponding to Exclusive OR Gate
"""
    def forward(self, input):
        self.initialOutput[:-1, 0] = input #Initializing all but the topmost part of the hidden layer as Input
        self.initialOutput[-1:, 0] = 1.0 #Initializing bias neuron value


        self.hiddenLayerActivation = np.dot(self.hiddenWeights, self.initialOutput) #Matrix computation where weights are multiplied by         the weights between input and hidden layer
        self.hiddenLayerOutput[:-1, :] = sigmoid(self.hiddenLayerActivation) #Applying sigmoid to the the matrix computation

        self.hiddenLayerOutput[-1:, :] = 1.0 #Initializing the first value of the hidden neurons to 1

        self.outputLayerActivation = np.dot(self.outputWeights, self.hiddenLayerOutput) #Matrix multiplication of hidden layer                   computation and the weights b/w hidden layer and output neuron
        self.outputLayerOutput = sigmoid(self.outputLayerActivation) #Applying sigmoid activation to output neuron 

    def backward(self, teach):

        error = self.outputLayerOutput - np.array(teach, dtype=float) #Calculation of error in output of Forward Propagation and the             expected output
        self.outputLayerDelta = (1 - sigmoid(self.outputLayerActivation)) * sigmoid(self.outputLayerActivation) * error #Computation of         error between output and hidden layer, using formula z * g(ij)
        self.hiddenLayerDelta = (1 - sigmoid(self.outputLayerActivation)) * sigmoid(self.hiddenLayerActivation) *                               np.dot(self.outputWeights[:, :-1].transpose(), self.outputLayerDelta) #Computation of error done simultaneously between hidden           output and input weights

        self.hiddenWeights -= self.alpha * np.dot(self.hiddenLayerDelta, self.initialOutput.transpose()) #Updating weights between               hidden layer and input layer
        self.outputWeights -= self.alpha * np.dot(self.outputLayerDelta, self.hiddenLayerOutput.transpose())#Updating weights between           hidden layer and output layer

    def getOutput(self): #Defining output function
        return self.outputLayerOutput

if __name__ == '__main__': 

    xorSet = [[0, 0], [0, 1], [1, 1], [1, 0]] #Input for training
    xorTeach = [[0], [1], [0], [1]] #Corresponding output values to be taught

    nn = NeuralNetworkXOR(2, 2, 1) #Calling the class

    count = 0
    while True:
        rnd = np.random.randint(0, 4) #Generating random number between 0 and 4

        nn.forward(xorSet[rnd]) #Random training data picked up over the given cases

        nn.backward(xorTeach[rnd]) #Propagating backwards on expected outputs
        print count, xorSet[rnd], nn.getOutput()[0],
        #Parameters for output determination
        if nn.getOutput()[0] > 0.8: 
            print 'TRUE'
        elif nn.getOutput()[0] < 0.2:
            print 'FALSE'

						
t_start = time.clock()
    
		print
    count += 1







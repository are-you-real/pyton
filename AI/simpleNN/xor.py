import numpy as np

class NeuralNetwor(y):
    def __init__(self,y):
        # Seed the random number generator
        np.random.seed(1)

        # randomly initialize our weights with mean 0
        self.syn0 = 2*np.random.random((4,3)) - 1
        self.syn1 = 2*np.random.random(4,1)) - 1
        print('syn0:'+str(self.syn0))
        print('syn1:'+str(self.syn1))

    def nonlin(self,x,deriv=False):
    	if(deriv==True):
    	    return x*(1-x)

    	return 1/(1+np.exp(-x))

    def think(self,X):
        l0 = X
        l1 = self.nonlin(np.dot(l0,self.syn0))
        l2 = self.nonlin(np.dot(l1,self.syn1))
        return l2

    def train(self,X,y):



        for j in range(60000):

        	# Feed forward through layers 0, 1, and 2

            l0 = X
            l1 = self.nonlin(np.dot(l0,self.syn0))
            l2 = self.nonlin(np.dot(l1,self.syn1))

            # how much did we miss the target value?
            l2_error = y - l2

            if (j% 10000) == 0:
                print ("Error:" + str(np.mean(np.abs(l2_error))))

            # in what direction is the target value?
            # were we really sure? if so, don't change too much.
            l2_delta = l2_error*self.nonlin(l2,deriv=True)

            # how much did each l1 value contribute to the l2 error (according to the weights)?
            l1_error = l2_delta.dot(self.syn1.T)

            # in what direction is the target l1?
            # were we really sure? if so, don't change too much.
            l1_delta = l1_error * self.nonlin(l1,deriv=True)

            self.syn1 += l1.T.dot(l2_delta)
            self.syn0 += l0.T.dot(l1_delta)


if __name__ == "__main__":
    training_inputs = np.array([[0,0,1],
                                [0,1,0],
                                [0,1,1],
                                [1,0,0]])

    training_outputs = np.array([[1],
    			                 [1],
    			                 [0],
    			                 [1]])

    neural_network = NeuralNetwor()

    neural_network.train(training_inputs, training_outputs)

    '''
    A = str(input("Input 1: "))
    B = str(input("Input 2: "))
    C = str(input("Input 3: "))

    print("New situation: input data = ", A, B, C)
    print("Output data: ")
    print(neural_network.think(np.array([A, B, C])))
    '''

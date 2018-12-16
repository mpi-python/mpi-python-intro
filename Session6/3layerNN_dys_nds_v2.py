# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 16:56:46 2018

@author: U979223
"""
import numpy as np

def nonlin(x,deriv=False):
    if (deriv == True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
## load non-dys data
path = "Z:/Project/featureExtraction_opensmile"
#x1 = np.genfromtxt(path+'/nds/eGemaps/nds01.csv',delimiter=",")
#x1_train = x1[1:61,1:89]
#num_rows,num_cols = x1_train.shape
#y1_train = np.zeros((num_rows,1))
xnds1 = np.genfromtxt(path+'/nds/eGemaps/nds01.csv',delimiter=",")
xnds2 = np.genfromtxt(path+'/nds/eGemaps/nds02.csv',delimiter=",")
xnds3 = np.genfromtxt(path+'/nds/eGemaps/nds03.csv',delimiter=",")
xnds4 = np.genfromtxt(path+'/nds/eGemaps/nds04.csv',delimiter=",")
xnds5 = np.genfromtxt(path+'/nds/eGemaps/nds05.csv',delimiter=",")
xnds1_train = xnds1[1:51,1:89] # 50-train,20-test
xnds2_train = xnds2[1:101,1:89] # 100-train, 30-test
xnds3_train = xnds3[1:101,1:89] # 100-train, 40-test
xnds4_train = xnds4[1:101,1:89] # 100-train, 30-test
xnds5_train = xnds5[1:101,1:89] # 100-train, 30-test
xnds_train = np. concatenate((xnds1_train,xnds2_train,xnds3_train,xnds4_train,xnds5_train))
ynds_train = np.zeros((xnds_train.shape[0],1)) # non-dys = 0
## load dys data
#x2 = np.genfromtxt(path+'/eGemaps_arff/all_subj_sent_egemaps.csv',delimiter=",")
#x2_train = x2[1:31,2:90]
#row,cols = x2_train.shape
#y2_train = np.ones((row,1))
xdys = np.genfromtxt(path+'/eGemaps_arff/all_subj_sent_egemaps.csv',delimiter=",")
xdys_train = xdys[1:31,2:90]
ydys_train = np.ones((xdys_train.shape[0],1)) # dys = 1
## train X, Y
X = np.concatenate((xnds_train,xdys_train,xdys_train,xdys_train))
X = X[:,(9,11,12,23,26,44,45,48,50,54,56)]
#X = X[:,[12]]

Y = np.concatenate((ynds_train,ydys_train,ydys_train,ydys_train))
## train X normalization
maxi = X.max(axis = 0)
mini = X.min(axis = 0)
norX = (X - mini.T)/(maxi.T-mini.T)
## test
xnds_test = np.concatenate((xnds1[61:71,1:89],xnds2[110:121,1:89],xnds3[120:131,1:89],xnds4[101:110,1:89],xnds5[111:121,1:89]))
xdys_test = xdys[31:41,2:90]
x_test = np.concatenate((xdys_test,xnds_test))
x_test=x_test[:,(9,11,12,23,26,44,45,48,50,54,56)]
#x_test=x_test[:,[12]]

ynds_test = np.zeros((xnds_test.shape[0],1))
ydys_test = np.ones((xdys_test.shape[0],1))
y_test = np.concatenate((ydys_test,ynds_test))

norx = (x_test - mini.T)/(maxi.T-mini.T)
#X = np.array([ [0,0,1],
#               [0,1,1],
#               [1,0,1],
#               [1,1,1]])
    
#y = np.array([[0,1,1,0]]).T

np.random.seed(1)

# randomly initialize our weights with mean 0
syn0 = 2*np.random.random((11,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1
#syn2 = 2*np.random.random((20,1)) - 1
b0=2*np.random.random((1,4)) - 1
b1=2*np.random.random((1,1)) - 1

for j in range(600000): # In each iteration training the model three times
    # feed forward through layers 0,1,2
    xy=np.c_[norX,Y]
    np.random.shuffle(xy) # randomly list all instances
    for i in range(3):  # choose 40 instance to train the model      
        temp1x = xy[i*40:i*40+40,:-1] # train three times
        temp1y = xy[i*40:i*40+40,-1:]
        
        l0 = temp1x # input layer
        l1 = nonlin(np.dot(l0,syn0)+b0) # hidden layer output
        l2 = nonlin(np.dot(l1,syn1)+b1) # output layer
    #    l3 = nonlin(np.dot(l2,syn2))
        # error
    #    l3_error = Y - l3
        l2_error = temp1y - l2 # error in output layer, here = target - output
        
        if (j%10000) == 0:
            print("Error:" + str(np.mean(np.abs(l2_error))))
            
        # in what direction is the target value?
        # were we really sure? if so, don't change too much
    #    l3_delta = l3_error * nonlin(l3,deriv=True)
        
        # how much did each l1 value contribute to the l2 error
        # according to the weights?
    #    l2_error = l3_delta.dot(syn2.T)
        
        # in what direction is the target l1?
        # were we really sure? if so, don't change too much.
        # l2_error here is used as learning rate
        # to update weights, we need to compute derivation 
        # deriv(Error/w5) = deriv(Error/OUTo1)*deriv(OUTo1/NETo1)*deriv(NETo1/w5)
        #          = -1 * OUTo1*(1-OUTo1) * OUTh1
        #          = -1 * nonlin(l2,deriv) * l1
        # update of syn1 = syn1 + learning_rate * deriv(Error/w5)
        #                = syn1 + l1.T.dot(l2_delta) 
        #                = syn1 + l1.T.dot(l2_error * -1 * nonlin(l2))
        # delta = deriv(Error/OUTo1)*deriv(OUTo1/NETo1)
        #          = -1 * OUTo1*(1-OUTo1) 
        #          = -1 * nonlin(l2,deriv)
        # l2_delta = learning_rate * delta = l2_error * nonlin(l2)
        # where NETo1 is weights(input layer to hidden layer, here is syn0) * input(here is X)
        # w5 is hidden neuron 1 to outout 1
        # OUTo1 is the outpu of NETo1 passed activation function(here is sigmoid)
        # Error = SUM((target - output)^2 * (1/2))
        # but in this program, Error = target - output = Y - l2 = Y - OUTo1
        l2_delta = l2_error * nonlin(l2,deriv=True)       
        
        l1_error = l2_delta.dot(syn1.T)        
        # in what direction is the target l1?
        # were we really sure? if so, don't change too much.
        # 
        l1_delta = l1_error * nonlin(l1,deriv=True)
    #    syn2 += l2.T.dot(l3_delta)
    
        # update weights & bias
        syn1 += l1.T.dot(l2_delta)
        syn0 += l0.T.dot(l1_delta)
        b0+=np.ones((40,1)).T.dot(l1_delta)
        b1+=np.ones((40,1)).T.dot(l2_delta)


ll = norx
yl1t = nonlin(np.dot(ll,syn0)+b0)
yyt = nonlin(np.dot(yl1t,syn1)+b1)
#y_computed_test = nonlin(np.dot(l2,syn2))

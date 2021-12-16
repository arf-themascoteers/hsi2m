import torch
import torch.nn as nn
from machine import Machine
import time
import numpy as np
import data_reader
import os
import train
import plotter
from data_reader import DataReader
import plotter


def test():
    dr = DataReader()
    _, y_all = dr.get_all_data()
    plotter.plot_single(y_all, dr.cutoff)
    x_train, y_train, x_test, y_test = dr.get_data()

    model = Machine()
    #if not os.path.isfile("models/machine.h5"):
    train.train()
    model = torch.load("models/machine.h5")

    criterion = torch.nn.MSELoss(reduction='mean')
    y_test_pred = model(x_test)
    loss = criterion(y_test_pred, y_test)
    print(f"Loss: {loss}")
    plotter.plot(y_test.detach().numpy(), y_test_pred.detach().numpy())


if __name__ == "__main__":
    test()

import numpy as np
from lib import mode


class Node:
    def __init__(self, x: np.ndarray, y: np.ndarray):
        self.x = x
        self.y = y
        self.children = []
        self.column_index = None
        self.threshold = None

    def is_node(self):
        # TODO hyperparameter: when do I have to stop splitting?
        return len(set(self.y)) == 1

    def split(self):
        # TODO implement
        pass

    def predict(self, x_test_row: np.ndarray) -> int:
        # Recursive exit condition
        if self.is_node():
            return mode(self.y)

        # Choose "left" or "right" child
        if x_test_row[self.column_index] < self.threshold:
            return self.children[0].predict(x_test_row)
        return self.children[1].predict(x_test_row)


class DecisionTree:
    def __init__(self):
        self.root = None

    def fit(self, x_train: np.ndarray, y_train: np.ndarray):
        self.root = Node(x_train, y_train)

    def predict(self, x: np.ndarray):
        pass


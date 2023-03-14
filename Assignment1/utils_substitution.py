import pickle


def read_pickle(file_name):
    with open(file=file_name, mode='rb') as file:
        eng_dist = pickle.load(file)
    return eng_dist
import pickle

class FileHandler:

    @staticmethod
    def save_data(data, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(data, file)
        except Exception as e:
            print(f"Error saving data: {e}")


    @staticmethod
    def load_data(filename):
        try:
            with open(filename,'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return None
        except Exception as e:
            print(f"Error loading data: {e}")
            return None

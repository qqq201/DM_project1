import csv

class dataframe:
    def __init__(self):
        self.data = []
        self.attr_id = dict()


    def load_csv(self, file):
        with open(file, newline='') as f:
            reader = csv.reader(f)
            self.data = list(reader)

            for attr, i in zip(self.data[0], range(len(self.data[0]))):
                self.attr_id[attr] = i

            self.data = self.data[1:]


    def save_csv(self, file):
        with open(file, 'w') as f:
            write = csv.writer(f)
            write.writerow(self.attr_id.keys())
            write.writerows(self.data)


    def attr_missing_value(self):
        pass

    def nrows_missing_value(self):
        pass

    def substitute_mean(self):
        pass

    def substitue_median(self):
        pass

    def substitue_mode(self):
        pass

    def remove_attr(self, threshold):
        pass

    def remove_duplicate(self):
        pass

    def min_max_normalize(self):
        pass

    def z_score_normalize(self):
        pass

    def plus(self, attr1, attr2):
        pass

    def minus(self, attr1, attr2):
        pass

    def multiply(self, attr1, attr2):
        pass

    def divide(self, attr1, attr2):
        pass

    def calculate(self, expression):
        pass


def main():
    df = dataframe()
    df.load_csv("test.csv")
    df.save_csv("test2.csv")


if __name__ == '__main__':
    main()

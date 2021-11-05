import csv

def correct_datatype(c):
    if c == '':
        return None

    try:
        if str(int(c)) == c: return int(c)
    except ValueError:
        return c
    try:
        if str(float(c)) == c: return float(c)
    except ValueError:
        return c


def mean(arr):
    n = 0
    sum = 0

    # calculate mean
    for i in range(len(arr)):
        if arr[i] is not None:
            sum += arr[i]
            n += 1

    return sum / n


def median(arr):
    # find available values
    values = []

    for value in arr:
        if value is not None:
            values.append(value)

    # sorting values
    values.sort()

    # find median
    n = len(values)
    mid = (n-1)//2

    if n % 2:
        return values[mid]
    else:
        return (values[mid] + values[mid + 1]) / 2


class dataframe:
    def __init__(self):
        self.data = []
        self.attributes = []


    def load_csv(self, file):
        with open(file, newline='') as f:
            # read data as 2d list
            reader = csv.reader(f)
            self.data = list(reader)
            self.attributes = self.data[0]

        self.data = [[correct_datatype(entry) for entry in row] for row in self.data[1:]]


    def save_csv(self, file):
        with open(file, 'w') as f:
            write = csv.writer(f)
            # write the header
            write.writerow(self.attributes)

            # write data
            write.writerows(self.data)


    def get_column(self, attr):
        index = self.attributes.index(attr)
        return [row[index] for row in self.data]


    def list_missing(self, args):
        print("Missing value attributes: ", end="")
        for i in range(len(self.attributes)):
            column = [row[i] for row in self.data]

            if any(value is None for value in column):
                print(self.attributes[i], end=", ")


    def count_nrows_missing(self, args):
        count = 0

        for row in self.data:
            if any(value == None for value in row):
                count += 1

        print(f"Number of rows has missing value: {count}")


    def impute_mean(self, attributes):
        for attr in attributes:
            if attr in self.attributes:
                column = self.get_column(attr)
                datatype = type(column[0])

                if datatype == float or datatype == int:
                    # calculate mean
                    substitute = mean(column)

                    # impute mean
                    c = self.attributes.index(attr)
                    for r in range(len(column)):
                        if column[r] is None:
                            self.data[r][c] = substitute
                else:
                    print(f"{attr} is not numeric!")
            else:
                print(f"Does not exist {attr}")


    def impute_median(self, attributes):
        for attr in attributes:
            if attr in self.attributes:
                column = self.get_column(attr)
                datatype = type(column[0])

                if datatype == float or datatype == int:
                    # calculate median
                    substitute = median(column)

                    # impute median
                    c = self.attributes.index(attr)
                    for r in range(len(column)):
                        if column[r] is None:
                            self.data[r][c] = substitute
                else:
                    print(f"{attr} is not numeric!")
            else:
                print(f"Does not exist {attr}")



    def impute_mode(self, attributes):
        '''
        impute missing line of attributes with mode
        attributes is a list of attrbutes need to be imputed
        '''
        pass

    def impute(self, args):
        if args.method == 'mean':
            self.impute_mean(args.attributes)
        elif args.method == 'median':
            self.impute_median(args.attributes)
        elif args.method == 'mode':
            self.impute_mode(args.attributes)
        else:
            print("Unknown method: Only mean, median and mode are accepted");

        if args.output:
            self.save_csv(args.output)



    def remove_missing_rows(self, threshold):
        '''
        remove missing rows with a threshold
        '''
        pass

    def remove_missing_cols(self, threshold):
        n = len(self.data)
        m = len(self.attributes)

        missing_rates = [0 for _ in range(m)]

        # count number missing row
        for r in range(n):
            for c in range(m):
                if self.data[r][c] is None:
                    missing_rates[c] += 1

        remain_index = []

        for index in range(m):
            if missing_rates[index] * 100 / n <= threshold:
                remain_index.append(index)
            else:
                self.attributes.pop(index)

        self.data = [[self.data[r][i] for i in remain_index] for r in range(n)]


    def remove_missing(self, args):
        if args.type == "row":
            self.remove_missing_rows(args.threshold)
        elif args.type == "column":
            self.remove_missing_cols(args.threshold)
        else:
            print("Unknown type: Only row and column are accepted");

        self.save_csv(args.output)


    def remove_duplicate(self, args):
        '''
        remove duplicate rows
        '''
        # implement here

        # save new file
        self.save_csv(args.output)


    def min_max_normalize(self, attribute):
        '''
        normalize attribute by min max method
        '''
        pass


    def z_score_normalize(self, attribute):
        '''
        normalize attribute by z score method
        '''
        pass


    def normalize(self, args):
        if args.method == "min_max":
            self.min_max_normalize(args.attribute)
        elif args.method == "z_score":
            self.z_score_normalize(args.attribute)
        else:
            print("Unknown method: Only min_max and z_score are accepted");

        self.save_csv(args.output)


    def mutate(self, args):
        new_attr = args.new_attr
        expression = args.expression

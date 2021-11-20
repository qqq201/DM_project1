import csv
import math
from expression_handle import *

def correct_datatype(c):
    '''
        convert string to its true datatype
    '''
    if c == '':
        return None
    try:
        if str(float(c)) == c: return float(c)
    except TypeError: return c
    except ValueError: return c

    try:
        if str(int(c)) == c: return int(c)
    except TypeError: return c
    except ValueError: return c



def mean(arr):
    '''
        find mean from array
    '''
    n = 0
    sum = 0

    # calculate mean
    for i in range(len(arr)):
        if arr[i] is not None:
            sum += arr[i]
            n += 1

    print(sum / n)
    return sum / n


def median(arr):
    '''
        find median array
    '''
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


def mode(arr):
    '''
        find mode from array
    '''

    # calculate frequency of each value in array
    Dict = {}

    for value in arr:
        if value in Dict:
            Dict[value] = Dict[value] + 1
        else:
            Dict[value] = 1

    # find value with maximum frequency
    m = 0
    for key in Dict:
        if Dict[key] > m :
            m = Dict[key]

    return m


def min(arr):
    '''
        find min of array
    '''
    if arr != None:
        m = arr[0]
        for i in arr:
            if i < m:
                m = i

    return m


def max(arr):
    '''
        find max of array
    '''
    if arr != None:
        m = arr[0]
        for i in arr:
            if i > m:
                m = i

    return m


def standard_deviation(arr, mean, n):
    '''
        calculate standard_deviation from array
    '''
    if mean is None:
        mean = mean(arr)

    s = 0
    for i in range(n):
        s += (arr[i] - mean)**2
    return math.sqrt(s / n)


def attribute_type(arr):
    '''
        find datatype of array
    '''
    for value in arr:
        if value is not None:
            return type(value)
    return None


class Dataframe:
    def __init__(self):
        self.data = []  # 2D array
        self.attributes = [] # name


    def load_csv(self, file):
        with open(file, newline='') as f:
            # read data as 2d list
            reader = csv.reader(f)
            self.data = list(reader)
            self.attributes = self.data[0]

        n = len(self.data)
        m = len(self.data[0])
        self.data = [[correct_datatype(self.data[r][c]) for c in range(m)] for r in range(1, n)]



    def save_csv(self, file):
        with open(file, 'w', newline='') as f:
            write = csv.writer(f)
            # write the header
            write.writerow(self.attributes)

            # write data
            write.writerows(self.data)


    def get_column(self, attr):
        '''
            get a column based on attribute name
        '''
        index = 0
        try:
            index = self.attributes.index(attr)
        except ValueError:
            print(f"Does not exist {attr}")
            return None

        return [row[index] for row in self.data]


    def list_missing(self, args):
        '''
            list attributes have missing value
        '''
        print("Missing value attributes: ", end="")
        for i in range(len(self.attributes)):
            column = [row[i] for row in self.data]

            if any(value is None for value in column):
                print(self.attributes[i], end=", ")


    def count_nrows_missing(self, args):
        '''
            count number of rows has missing value
        '''
        count = 0

        for row in self.data:
            if any(value == None for value in row):
                count += 1

        print(f"Number of rows has missing value: {count}")


    def impute_mean(self, attributes):
        '''
            impute missing value with mean
        '''
        for attr in attributes:
            column = self.get_column(attr)
            if column is not None:
                datatype = attribute_type(column)
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
        '''
            impute missing value with mean
        '''
        for attr in attributes:
            column = self.get_column(attr)
            if column is not None:
                datatype = attribute_type(column)

                if datatype == float or datatype == int:
                    # calculate mode
                    substitute = median(column)

                    # impute mode
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
            impute missing value with mode
        '''
        for attr in attributes:
            column = self.get_column(attr)
            if column is not None:
                datatype = attribute_type(column)

                if datatype == str:
                    # calculate mode
                    substitute = mode(column)

                    # impute mode
                    c = self.attributes.index(attr)
                    for r in range(len(column)):
                        if column[r] is None:
                            self.data[r][c] = substitute
                else:
                    print(f"{attr} is not nominal!")
            else:
                print(f"Does not exist {attr}")


    def impute(self, args):
        '''
            handle impute command
        '''
        if args.method == 'mean':
            self.impute_mean(args.attributes)
        elif args.method == 'median':
            self.impute_median(args.attributes)
        elif args.method == 'mode':
            self.impute_mode(args.attributes)
        else:
            print("Unknown method: Only mean, median and mode are accepted");

        # save file
        if args.output:
            self.save_csv(args.output)



    def remove_missing_rows(self, threshold):
        '''
            remove missing rows with a threshold
        '''
        n = len(self.data)
        m = len(self.attributes)

        missing_rates = [0 for _ in range(n)]

        # count number missing columns
        for r in range(n):
            for c in range(m):
                if self.data[r][c] is None:
                    missing_rates[r] += 1

        remain_index = []

        for index in range(n):
            if missing_rates[index] * 100 / n <= threshold:
                remain_index.append(index)

        self.data = [[self.data[r][c] for c in range(m)] for r in range(n) if r in remain_index]


    def remove_missing_cols(self, threshold):
        '''
            remove missing columns with a threshold
        '''
        n = len(self.data)
        m = len(self.attributes)

        missing_rates = [0 for _ in range(m)]

        # count number missing rows
        for r in range(n):
            for c in range(m):
                if self.data[r][c] is None:
                    missing_rates[c] += 1

        remain_index = []

        for index in range(m):
            if missing_rates[index] * 100 / n <= threshold:
                remain_index.append(index)

        self.attributes = [self.attributes[i] for i in remain_index]
        self.data = [[self.data[r][i] for i in remain_index] for r in range(n)]


    def remove_missing(self, args):
        '''
            handle remove missing command
        '''
        if args.type == "row":
            self.remove_missing_rows(args.threshold)
        elif args.type == "column":
            self.remove_missing_cols(args.threshold)
        else:
            print("Unknown type: Only row and column are accepted");

        # save file
        if args.output:
            self.save_csv(args.output)


    def remove_duplicate(self, args):
        '''
            remove duplicated rows
        '''
        # implement here
        n = len(self.data)
        m = len(self.attributes)

        delete_id = []
        for i in range(len(self.data)):
            for j in range(i+1,len(self.data),1):
                if (self.data[i] == self.data[j]):
                    delete_id.append(j)

        self.data = [[self.data[r][c] for c in range(m)] for r in range(n) if r not in delete_id]

        # save file
        if args.output:
            self.save_csv(args.output)


    def min_max_normalize(self, attribute):
        '''
            normalize attribute by min max method
        '''
        column = self.get_column(attribute)
        if column is not None:
            datatype = attribute_type(column)

            if datatype == float or datatype == int:
                column_min = min(column)
                column_max = max(column)
                data_norm = [ (c - column_min) / (column_max - column_min) for c in column]

                id_column = self.attributes.index(attribute)

                for i in range(len(self.data)):
                    self.data[i][id_column] = data_norm[i]

            else:
                print(f"{attribute} is not numeric!")
        else:
            print(f"Does not exist {attribute}")


    def z_score_normalize(self, attribute):
        '''
            normalize attribute by z score method
        '''
        column = self.get_column(attribute)
        if column is not None:
            datatype = attribute_type(column)

            if datatype == float or datatype == int:
                column_mean = mean(column)
                column_std = standard_deviation(column,column_mean, len(column))

                id_column = self.attributes.index(attribute)
                for i in range(len(self.data)):
                    self.data[i][id_column] = (column[i] - column_mean) / column_std

            else:
                print(f"{attribute} is not numeric!")
        else:
            print(f"Does not exist {attribute}")


    def normalize(self, args):
        '''
            handle normalize command
        '''
        if args.method == "min_max":
            self.min_max_normalize(args.attribute)
        elif args.method == "z_score":
            self.z_score_normalize(args.attribute)
        else:
            print("Unknown method: Only min_max and z_score are accepted");

        if args.output:
            self.save_csv(args.output)


    def mutate(self, args):
        '''
            create new attribute by expression
        '''

        # get expression
        expression = ' '.join(args.expression)

        # calculate expression using Polish Notation Algorithm
        # convert to postfix order
        postfix = PostorderConvert(expression)
        s = [];
        l = len(postfix);

        for entry in postfix:
            if is_alphabet(entry[0]):
                column = self.get_column(entry)
                if column is not None:
                    datatype = attribute_type(column)

                    if datatype == float or datatype == int:
                        s.append(column)
                    else:
                        print(f"{entry} is not numberic. Can not execute operation on non-numeric attribute.")
                        return
                else:
                    return
            else:
                a = s[-1]
                s.pop()
                b = s[-1]
                s.pop()
                s.append(operate(b, a, entry))


        # add new attribute
        self.attributes.append(args.new_attr)

        for i in range(len(s[0])):
            self.data[i].append(s[0][i])

        if args.output:
            self.save_csv(args.output)

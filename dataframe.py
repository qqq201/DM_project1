import csv

class dataframe:
    def __init__(self):
        self.data = []

        # dictionary mapping attribute with its index
        self.attr_id = dict()


    def load_csv(self, file):
        with open(file, newline='') as f:
            # read data as 2d list
            reader = csv.reader(f)
            self.data = list(reader)

            # mapping attributes with indices
            for attr, i in zip(self.data[0], range(len(self.data[0]))):
                self.attr_id[attr] = i

            # remove header
            self.data = self.data[1:]


    def save_csv(self, file):
        with open(file, 'w') as f:
            write = csv.writer(f)
            # write the header
            write.writerow(self.attr_id.keys())
            # write data
            write.writerows(self.data)


    def list_missing(self, args):
        pass


    def count_nrows_missing(self, args):
        pass


    def impute_mean(self, attrbutes):
        pass

    def impute_median(self, attrbutes):
        pass

    def impute_mode(self, attrbutes):
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

        self.save_csv(args.output)



    def remove_missing_rows(self, threshold):
        pass

    def remove_missing_attr(self, threshold):
        pass

    def remove_missing(self, args):
        if args.type == "row":
            self.remove_missing_rows(args.threshold)
        elif args.type == "column":
            self.remove_missing_attr(args.threshold)
        else:
            print("Unknown type: Only row and column are accepted");


    def remove_duplicate(self, args):
        # implement here
        self.save_csv(args.output)


    def min_max_normalize(self, attribute):
        pass


    def z_score_normalize(self, attribute):
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

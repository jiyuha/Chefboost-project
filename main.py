import pandas as pd
import CB as cb
# ----------------------------------------------

parallelism_cases = [True]

if __name__ == '__main__':

    for enableParallelism in parallelism_cases:
        print("-------------------------")
        print("Validation set case")
        df = pd.read_csv("dataset/please_small.csv")
        print(df)
        train_data, test_data = cb.train_test_split(df)
        config = {'algorithm': 'C4.5', 'enableParallelism': enableParallelism}

        model = cb.fit(train_data, config, validation_df=test_data)

    print("-------------------------")
    print("unit tests completed successfully...")

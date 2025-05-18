from get_data import load
from calculate import calculate_all_metric
import pandas as pd
import sys


def main(argv):
    try:
        data_frame = load(argv[1])
    except:
        exit("Error while loading data")
    subject_data = data_frame.select_dtypes(include=float)
    
    
    metrics_dict = {
        "Count": [],
        "Mean": [],
        "Std": [],
        "Min": [],
        "25%": [],
        "50%": [],
        "75%": [],
        "Max": [],
    }

    subjects = list(subject_data.columns)

    for subject in subjects:
        result = calculate_all_metric(subject_data[subject])
        for metric in metrics_dict.keys():
            metrics_dict[metric].append(result[metric])

    df_metrics = pd.DataFrame(metrics_dict, index=subjects).T

    df_metrics = df_metrics.round(6)

    pd.set_option('display.max_rows', None)
    print(df_metrics)

if __name__ == "__main__":
    main(sys.argv)
import pandas as pd
import math

def calculate_all_metric(column):
    mean = calculate_mean(column)
    std = calculate_std(column, mean)
    min = calculate_min(column)
    max = calculate_max(column)
    perc_25 = calculate_percentile(column, 25)
    perc_50 = calculate_percentile(column, 50)
    perc_75 = calculate_percentile(column, 75)
    
    return {
        "Count": column.count(),  # Safe count of non-NaNs
        "Mean": mean,
        "Std": std,
        "Min": min,
        "25%": perc_25,
        "50%": perc_50,
        "75%": perc_75,
        "Max": max,
    }


def calculate_mean(column) -> float:
    total = 0
    count = 0
    for value in column:
        if not pd.isna(value):
            total += value
            count += 1
    return total / count if count > 0 else float('nan')

def calculate_std(column, mean) -> float:
    total = 0
    count = 0
    for value in column:
        if not pd.isna(value):
            total = (value - mean)**2 + total
            count += 1
    return math.sqrt(total / (count - 1))

def calculate_min(column) -> float:
    min = column[0]
    for value in column:
        if not pd.isna(value):
            if value < min:
                min = value
    return min

def calculate_max(column) -> float:
    max = column[0]
    for value in column:
        if not pd.isna(value):
            if value > max:
                max = value
    return max

def sort_data(column):
    sorted_column = column.sort_values().dropna().tolist()
    return sorted_column

def calculate_percentile(column, percentile):
    sorted_column = sort_data(column)
    length = len(sorted_column)
    rank = percentile * ((length - 1) / 100)
    lower_index = int(rank)
    upper_index = int(rank) + 1
    weight = rank - lower_index

    if upper_index >= length:
        return sorted_column[lower_index]
    
    return sorted_column[lower_index] * (1 - weight) + sorted_column[upper_index] * weight
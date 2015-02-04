import pandas as pd


padding = " "
limited_columns = ["make","price","city mpg","highway mpg","horsepower",
                   "weight","riskiness","losses"]


def get_make_labels(data):
    return [padding] + [x.title() for x in pd.Series(data["make"]).unique()]


def get_make_id_map(data):
    return {x:i for (i,x) in enumerate(get_make_labels(data)) if x != padding}


def get_make_ids(data):
    return sorted(get_make_id_map(data).values())


def get_raw_data():
    data_file = "../data/autos-clean.csv"
    return pd.read_csv(data_file)


def get_make_data(make, pddata):
    return pddata[(pddata["make"] == make)]


def get_make_counts(pddata, lower_bound=0):
    counts = []
    filtered_makes = []
    for make in get_all_auto_makes():
        data = get_make_data(make, pddata)
        count = len(data.index)
        if count >= lower_bound:
            filtered_makes.append(make)
            counts.append(count)
    return (filtered_makes, list(zip(filtered_makes, counts)))


def get_limited_data(cols=None, lower_bound=None):
    if not cols:
        cols=limited_columns
    data = get_raw_data()[cols]
    if lower_bound:
        (makes, _) = get_make_counts(data, lower_bound)
        data = data[data["make"].isin(makes)]
    return data


def get_all_auto_makes():
     return pd.Series(get_raw_data()["make"]).unique()



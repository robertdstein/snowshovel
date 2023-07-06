"""
Module containing functions to read and parse alerts
"""
from pathlib import Path

import pandas as pd
from avro.datafile import DataFileReader
from avro.io import DatumReader
from tqdm import tqdm


def read_single_alert(path: Path) -> DataFileReader:
    """
    Function to read avro alerts

    :param path: Path to the files
    :return: Avro dict
    """
    with open(path, 'rb') as f:
        freader = DataFileReader(f, DatumReader())
        return next(freader)['candidate']


def parse_alerts(data_dir: Path, n_to_read: int | None = None) -> pd.DataFrame:
    """
    Function to load the first 'n' alerts from a data directory

    :param data_dir: data directory to read
    :param n_to_read: Number of alerts to read (default is all alerts)
    :return: Dataframe containing the alerts
    """
    paths = sorted([x for x in data_dir.glob("*.avro")])

    if n_to_read is None:
        n_to_read = len(paths)

    all_alerts = []

    for path in tqdm(paths[:n_to_read], total=n_to_read):
        alert = read_single_alert(path)
        all_alerts.append(alert)

    return pd.DataFrame(all_alerts)

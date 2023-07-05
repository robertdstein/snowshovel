from pathlib import Path
from fastavro import reader


def read_alert(path: Path):
    """
    Function to read avro alerts

    :param path: Path to the files
    :return:
    """

    with open(path, 'rb') as fo:
        return [record for record in reader(fo)]

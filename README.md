# snowshovel

## Install instructions

Firstly, start downloading some test data from e.g: https://ztf.uw.edu/alerts/public/ztf_public_20230609.tar.gz

### Clone from Github

```bash
git clone git@github.com:robertdstein/snowshovel.git
```

### Create a clean virtual environment, using conda

```bash
conda create python=3.11 -n snowshovel
```

### Activate the virtual environment

```bash
conda activate snowshovel
```

### Install the requirements

```bash
cd snowshovel
pip install -e .
```

This will install all the necessary packages.

### Set up the jupyter kernel

```bash
python -m ipykernel install --user --name=snowshovel
```
This ensures that the python environment is available.

## Set up the correct path

You will need to do this each time you start a new terminal session.

### Unix (Linux/MacOS)

```bash
export SNOWSHOVEL_DATA_DIR=/path/to/data
```

### Windows

```bash
set SNOWSHOVEL_DATA_DIR=/path/to/data
```

## Using the code

### Start a jupyter notebook

Go to the directory with the code and type:

```bash
cd notebooks
jupyter notebook
```

This should open up a jupyter notebook in your browser. 

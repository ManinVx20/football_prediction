# Football Prediction

Football prediction is a Python project that crawls data and predicts match winners in FIFA World Cup 2022.

## Packages

- [Python](https://www.python.org/)
- [Pip](https://pip.pypa.io/en/stable/)
- [Virtualenv](https://pypi.org/project/virtualenv/)
- [Scrapy](https://scrapy.org/)

## Preparation

These guides are for Ubuntu-based systems.

To install Scrapy, you need to install these dependencies:

```bash
sudo apt-get install python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
```

Use the package manager pip to install virtualenv that creates virtual environment for installing other packages:

```bash
pip install virtualenv
```
Go to the root of the project and create virtual environment:

```bash
virtualenv venv
```

Run this command to active the virtual environment. You should do this everytime you work on the project:

```bash
source venv/bin/activate
```

Inside a virtual environment, you can install Scrapy with pip after that:

```bash
pip install scrapy
```

## Usage

Go to football_prediction/crawler while inside a virtual environment and use these commands to re-crete datas.

For football matches of the FIFA World Cups from 1930 to 2018:


```bash
scrapy crawl match -O ../data/fifa_world_cup_historical_data.csv
```

For football matches of the FIFA World Cups 2022:


```bash
scrapy crawl match -O ../data/fifa_world_cup_fixtures_data.csv -a tag=new
```

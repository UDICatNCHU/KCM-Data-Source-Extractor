<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [KCM input](#kcm-input)
  - [Getting Started](#getting-started)
    - [Prerequisities](#prerequisities)
    - [Installing](#installing)
  - [Running & Testing](#running--testing)
  - [Run](#run)
- [How to train KCM with PTT](#how-to-train-kcm-with-ptt)
    - [Break down into end to end tests](#break-down-into-end-to-end-tests)
    - [And coding style tests](#and-coding-style-tests)
    - [Results](#results)
  - [Built With](#built-with)
  - [Contributors](#contributors)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# KCM input  


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisities

1. OS：Ubuntu / OSX would be nice
2. environment：need python3 `sudo apt-get update; sudo apt-get install; python3 python3-dev`

### Installing

1. `git clone https://github.com/UDICatNCHU/KCM-Data-Source-Extractor.git`
2. 使用虛擬環境：
  1. `virtualenv venv`
  2. 啟動方法
    1. for Linux：`. venv/bin/activate`
    2. for Windows：`venv\Scripts\activate`
3. `pip install -r requirements.txt`

## Running & Testing

## Run

# How to train KCM with PTT
```
from KCM.__main__ import KCM
k = KCM('cht', 'ptt')
k.removeDB()
k.main()

print(k.get('臺灣', 10))
print(k.get('pizza', 10))
```
1. Execute : `python manage.py runserver`. If it work fine on [here](http://127.0.0.1) , then it's done. Congratulations~~

### Break down into end to end tests

目前還沒寫測試...

### And coding style tests

目前沒有coding style tests...

### Results


## Built With

* python3.5
* Django==1.10.0

## Contributors

* **張泰瑋** [david](https://github.com/david30907d)

## License

## Acknowledgments

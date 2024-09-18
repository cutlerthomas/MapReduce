#!/bin/bash
../../hadoop-3.3.6/bin/hadoop jar ../../hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar -mapper mapper.py -reducer reducer.py -input input/car_prices.txt -output car_prices
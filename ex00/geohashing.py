#!/usr/bin/python3
# coding: utf-8

import sys
import antigravity


def run():
    if len(sys.argv) != 4:
        raise Exception("Wrong number of arguments! Example: python3 geohashing.py latitude longitude yy-mm-dd-dow")

    try:
        latitude = float(sys.argv[1])
    except Exception:
        raise Exception("Latitude in not float!")
    if latitude < -89 or latitude > 89:
        raise Exception("Latitude range from -89 to 89")

    try:
        longitude = float(sys.argv[2])
    except Exception:
        raise Exception("Longitude is not float!")
    if longitude < -179 or longitude > 179:
        raise Exception("Longitude range from -179 to 179")

    splinted_dow = sys.argv[3].split('-')
    if len(splinted_dow) != 4:
        raise Exception("Wrong last argument it must by like yy-mm-dd-dow.\
         Dow - daily opening price of the Dow Jones.")

    try:
        int(splinted_dow[0])
    except Exception:
        raise Exception("Year is not int")

    month = 0
    try:
        month = int(splinted_dow[1])
    except Exception:
        raise Exception("Month is not int")
    if month < 0 or month > 12:
        raise Exception("Wrong month value")

    day = 0
    try:
        day = int(splinted_dow[2])
    except Exception:
        raise Exception("Day is not int")
    if day < 0 or day > 31:
        raise Exception("Wrong day value")

    try:
        float(splinted_dow[3])
    except Exception:
        raise Exception("Daily opening price of the Dow Jones is not float")

    try:
        datedow = bytes(sys.argv[3], 'utf-8')
    except Exception:
        raise Exception("datedow byte convert error")
    antigravity.geohash(latitude, longitude, datedow)


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        print(ex)

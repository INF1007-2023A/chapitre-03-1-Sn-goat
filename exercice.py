#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    new_number_sqrt_root = math.sqrt(a)
    return new_number_sqrt_root


def square(a: float) -> float:
    new_number_sqrt = a ** 2
    return new_number_sqrt


def average(a: float, b: float, c: float) -> float:
    new_number_avg = (a + b + c) / 3
    return new_number_avg


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    angle_radian = math.degrees(angle_degs)
    angle_radian_mins = math.degrees((360 * angle_mins)/ 1440 )
    angle_radian_secs = math.degrees((360 * angle_secs)/ 86400)

    return angle_radian, angle_radian_mins, angle_radian_secs


def to_degrees(angle_rads: float) -> tuple:
    angle_degrees = math.radians(angle_rads)
    return angle_degrees


def to_celsius(temperature: float) -> float:
    temp_celsius = (temperature - 32) / 1.8
    return temp_celsius


def to_farenheit(temperature: float) -> float:
    temp_farenheit = (temperature * 1.8) + 32
    return temp_farenheit




def main() -> None:
    print("La racine carré de 144 est", square_root(144))

    print("Le carré de 12 est", square(12))

    print("Moyenne des nombres 2, 4, 6 c'est", average(2, 4, 6))

    print("Conversion de 100 degres, 2 minutes et 45 secondes en radians", to_radians(180, 2, 45))
    
    print("Conversion de 1 radian en degres",  to_degrees(1))
    
    print("Conversion de 100 Celsius en Farenheit", to_farenheit(100.0))
    print("Conversion de 451 Farenheit en Celsius", to_celsius(451.0))


print(main())

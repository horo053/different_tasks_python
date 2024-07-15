#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}


# TODO здесь заполнение словаря
m_l = (((sites.get('Moscow')[0] - sites.get('London')[0]) ** 2) + ((sites.get('Moscow')[1] - sites.get('London')[1]) ** 2)) ** 0.5
l_p = (((sites.get('London')[0] - sites.get('Paris')[0]) ** 2) + ((sites.get('London')[1] - sites.get('Paris')[1]) ** 2)) ** 0.5
p_m = (((sites.get('Moscow')[0] - sites.get('Paris')[0]) ** 2) + ((sites.get('Moscow')[1] - sites.get('Paris')[1]) ** 2)) ** 0.5


distances["Moscow-London"] = m_l
distances["London-Moscow"] = m_l
distances["London-Paris"] = l_p
distances["Paris-London"] = l_p
distances["Moscow-Paris"] = m_l
distances["Paris-Moscow"] = m_l

pprint(distances)
#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#from codecs import open - на случай открытия файлов в Python 2 содержащих кириллицу


changes_to_do = {}


#'overall_statistic\groups.txt'

def look_up(file_name):
    with open(file_name, 'r') as f:
        for line in f.readlines():
            to_dict = line.strip('\n').split('\t')
            changes_to_do[to_dict[0]] = to_dict[1]

def save_down(file_name, *args_to_increase):
    with open(file_name, 'w') as f:
        for typez, count in changes_to_do.items():
            if typez in args_to_increase:
                f.write(typez + '\t' + str( int(count) + 1 ) + '\n')
                continue
            f.write(typez + '\t' + count + '\n')



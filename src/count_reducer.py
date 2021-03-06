#!/usr/bin/env python  
   
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:15:37 2015

@author: Wenliang Zhao

reducer function for word count
"""

from operator import itemgetter  
import sys  
  
edge_dict = {}  
   
# input comes from STDIN  
for line in sys.stdin:  
    line = line.strip()  
   
    temp_list = line.split('\\t', 1)
    if (len(temp_list) > 1):  
        try:  
            edge_string, count = temp_list[0].strip(), int(temp_list[1].strip())
        except ValueError:  
            pass 
        else:
            edge_dict[edge_string] = edge_dict.get(edge_string, 0) + count
  
sorted_edge_dict = sorted(edge_dict.items(), key=itemgetter(0))  
  
for s, c in sorted_edge_dict:  
    temp_list = s.split(",",2)
    print '%s\\t%s\\t%s\\t%s\\t'% (temp_list[0].strip(), temp_list[1].strip(), temp_list[2].strip(), c)

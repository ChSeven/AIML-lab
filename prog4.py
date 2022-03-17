import csv
from math import log

def decision_tree(data, labels):
    results = [row[-1] for row in data]
    if results.count(results[0]) == len(results):
        return results[0]
         
    max_gain_attribute = select_attribute(data)
    tree = { max_gain_attribute : {} }
    del(labels[max_gain_attribute])
    nodes = [row[max_gain_attribute]  for row in data]
    unique_nodes = set(nodes)
    for node in unique_nodes:
        sublabels = labels[:]
        tree[max_gain_attribute][node] = decision_tree(split_data(data, max_gain_attribute, node), sublabels)
    print(tree)
    return tree


def split_data(data, attribute, value):
    new_data = []
    for row in data:
      if row[attribute] == value:
            #print(row)
            new_row = row[:attribute]
            new_row.extend(row[attribute+1:])
            new_data.append(new_row)
            #row=row+1
    return new_data


def select_attribute(data):
    base_entropy = entropy(data)
    attributes = len(data[0])-1 
    print(attributes)
    best_attribute = -1
    max_info_gain = -1

    for attribute in range(attributes):
        values = [rec[attribute] for rec in data]
        unique_values = set(values)
        attr_entropy = 0
        
        for value in unique_values:
            new_data = split_data(data, attribute, value)
            prob = len(new_data) / len(data)
            new_entropy = prob * entropy(new_data)
            attr_entropy += new_entropy
        info_gain = base_entropy - attr_entropy
        if info_gain > max_info_gain:
            max_info_gain = info_gain
            best_attribute = attribute
    return best_attribute


def entropy(data):
    total_rows = len(data)
    dict_outcomes = {}

    for row in data:
        outcome = row[-1]
        if outcome not in dict_outcomes.keys():        
            dict_outcomes[outcome] = 0
        dict_outcomes[outcome] += 1
    entropy = 0
    
    for key in dict_outcomes:
        prob = dict_outcomes[key] / total_rows
        entropy -= prob * log(prob, 2)
    return entropy


def getData(file):
    csv_file = csv.reader(open(file))
    data = []
    for row in csv_file:
        data.append(row)
        print(row)        
    return data

def main():
    file = "prog3.csv"
    data = getData(file)
    labels = data[0]
    tree = decision_tree(data[1:], labels)
    print(".............Decision Treee...........")    
    #print(labels)
    print(tree)
main()

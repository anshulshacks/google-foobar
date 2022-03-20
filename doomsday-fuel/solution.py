import numpy as np
from fractions import Fraction

def solution(m):
    # Solved using Absorbing Markov Chains.
    # There is a wonderful article on Wikipedia.
    input_matrix = np.array(m)
    if (len(m) <= 2):
        return [1, 1]

    num_of_transient_states = 0
    num_of_absorbing_states = 0
    transient_states = []
    absorbing_states = []
    for i in range(len(m)):
        zeros = 0
        sum_of_row = 0
        for j in range(len(m[i])):
            if m[i][j] == 0:
                zeros += 1
            sum_of_row += m[i][j]
            if (sum_of_row == 0 and m[i][j] == 0 and j == len(m[i]) - 1):
                sum_of_row = 1
            
        for k in range(len(m[i])):
            m[i][k] = m[i][k] / float(sum_of_row)
        if zeros == len(m[i]):
            num_of_absorbing_states += 1
            absorbing_states.append(i)
        else:
            num_of_transient_states += 1
            transient_states.append(i)
    
    transient_to_transient = []

    for rowIndex in transient_states:
        row = []
        for columnIndex in transient_states:
            row.append(m[rowIndex][columnIndex])
        transient_to_transient.append(row)


    transient_to_absorbing = []
    for i in transient_states:
        row = []
        for index in absorbing_states:
            row.append(m[i][index])
        transient_to_absorbing.append(row)
    
    
    identity_transient = np.eye(num_of_transient_states)
    
    transient_to_transient_matrix = np.array(transient_to_transient)
    transient_to_absorbing_matrix = np.array(transient_to_absorbing)
    
    fundamental_matrix = np.linalg.inv(np.subtract(identity_transient, transient_to_transient_matrix))

    
    probability_matrix = np.dot(fundamental_matrix, transient_to_absorbing_matrix)
    
    
    
    fraction_list = []
    for val in probability_matrix[0]:
        fraction_list.append(Fraction(val).limit_denominator())
    
    lcm = find_lcm(fraction_list)
    
    ans_list = []
    for val in fraction_list:
        ans_list.append(int(val.numerator * (lcm / val.denominator)))
    ans_list.append(lcm)
    return ans_list

# Finds LCM of fractions for final step of problem.
def find_lcm(list_of_fractions):
    denominators = []
    for val in list_of_fractions:
        denominators.append(val.denominator)

    max = 0
    total_product = 1
    for denominator in denominators:
        if denominator > max:
            max = denominator
        total_product *= denominator
    counter = max

    lcm = total_product
    while counter < total_product:
        for i in range(len(denominators)):
            if (counter % denominators[i] != 0):
                break
            if (i == len(denominators) - 1):

                lcm = counter
        if lcm != total_product:
            break
        counter += max
    return lcm

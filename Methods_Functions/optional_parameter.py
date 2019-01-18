

#Similar to functions , Methods are also  defined by keyword 'def'

# a -> parameter 1 (variable)

# a takes the default value 0


def calculate_sum(a=0):
    '''
    :param a: 1
    :return: a+1
    '''
    return a+1

# Call sum function


print  calculate_sum(1) #we pass a =1
print  calculate_sum()  #we don't pass any value so default value of a is 0

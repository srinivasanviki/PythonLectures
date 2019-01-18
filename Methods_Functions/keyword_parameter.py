

#Similar to functions , Methods are also  defined by keyword 'def'

# **kwargs -> parameter 1 (variable)



def get_args(**kwargs):
    '''
    :param kwargs: a=1
    :return: {'a':1}
    '''
    return  kwargs

# Call sum function


print  get_args(a=1) #we pass a =1



#Similar to functions , Methods are also  defined by keyword 'def'

# a -> parameter 1 (variable)
# b -> parameter 2 (variable)

class sum():
    def calculate_sum(self,a,b):
        '''
        :param a: 1
        :param b: 2
        :return: a+b => 3
        '''
        return (a+b)

# Call sum function

sum=sum()
print sum.calculate_sum(1,2)





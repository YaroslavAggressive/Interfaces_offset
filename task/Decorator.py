


# def method_wrapper(file):
#     def printer(func):
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             file.(res)
#             file.write("\n")
#             return res
#         return wrapper
#     return printer


def print_iter(file_name):
    file = open(file_name, "w")    
    def RealGrapgIterator(our_class):
        class NewDirReader:
    
            def __init__(self, *args, **kwargs):
                self._obj = our_class(*args, **kwargs)
    
            # @printer(file_name)
            def __next__(self):
                next_elem = self._obj.__next__()
                file.write("Name: " + str(next_elem[0]) + "Num of sequences: " + str(next_elem[1]))
                return next_elem
                # return self._obj.__next__()
    
            def __iter__(self):
                return self
    
    
        return NewDirReader
    return RealGrapgIterator
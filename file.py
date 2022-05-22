from operator import itemgetter

def greeter(func):
    def inner(*args):
        output=func(*args)
        return 'Aloha ' + output.title()
    return inner


def sums_of_str_elements_are_equal(func):
    def inner(*args):
        output=func(*args).split()
        sums=[]
        for i in output:
            if i.startswith('-'):
                i=i[1:]
                sum=0
                for j in i:
                    sum+=int(j)
                sums.append(-sum)
            else:
                sum=0
                for j in i:
                    sum+=int(j)
                sums.append(sum)
        if sums[0]==sums[1]:
            return str(sums[0])+' == '+str(sums[1])
        else:
            return str(sums[0]) + ' != ' + str(sums[1])
    return inner


def format_output(*required_keys):
    def outer(func):
        def get_val(dictionary, key):
            key = key.split('__')
            if len(key) > 1:
                return ' '.join(itemgetter(*tuple(key))(dictionary))
            else:
                if dictionary.get(key[0])=='':
                    return 'Empty value'
                return dictionary.get(key[0])
        def inner(*args,**kwargs):
            output=func(*args,**kwargs)
            keys=[]
            for i in required_keys:
                keys.append(i.split('__'))
            keys=sum(keys,[])
            for i in keys:
                if i not in output.keys():
                    raise ValueError
            return dict([(i, get_val(output,i)) for i in required_keys])
        return inner
    return outer


def add_method_to_instance(klass):
    def outer(func):
        def inner(*args, **kwargs):
            return func()
        setattr(klass, func.__name__, inner)
        return inner
    return outer



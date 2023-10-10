class DjangoSingletonWrapper(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DjangoSingletonWrapper, cls).__new__(cls)
        return cls.instance
    
class DjangoWrapperChild(DjangoSingletonWrapper):
    pass

djangoWrapper = DjangoSingletonWrapper()
djangoWrapperChild = DjangoWrapperChild()

print(djangoWrapperChild is djangoWrapper)

djangoWrapper.singl_variable = "Singleton Variable"

print (djangoWrapperChild.singl_variable)

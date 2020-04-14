import functools


class SingletonClassic:
    _instance = None

    @staticmethod
    def get_instance():
        if SingletonClassic._instance is None:
            SingletonClassic._instance = SingletonClassic()
        return SingletonClassic._instance

    def __init__(self):
        """ 
        Simulate a "private constructor" 
        """
        if SingletonClassic._instance != None:
            raise TypeError(
                "Singletons must be accessed through `get_instance()`nl")
        else:
            SingletonClassic._instance = self


class SingletonDecoratorClass:
    def __init__(self, cls):
        self._instance = None
        self._cls = cls

    def get_instance(self):
        if self._instance is None:
            self._instance = self._cls()
        return self._instance

    def __call__(self):
        raise TypeError(
            'Singletons must be accessed through `get_instance()`')


# From PEP318
def SingletonDecoratorFunc(cls):
    instances = {}

    @functools.wraps(cls)
    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return get_instance

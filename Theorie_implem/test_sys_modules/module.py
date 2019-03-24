import abc

class Module(abc.ABC):
    
    @abc.abstractmethod
    def get_description(self):
        pass
        
    @abc.abstractmethod
    def start(self, params):
        pass
    
    @abc.abstractmethod
    def stop(self):
        pass
        
    @abc.abstractmethod
    def distrib_output(self):
        pass
        
    @abc.abstractmethod
    def is_active(self):
        pass

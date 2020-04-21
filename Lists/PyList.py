class PyList:
        
        def __init__(self): 
                
                self.worker = []
            
        def add(self, item):
          
              self.item = item
              
              self.worker = self.worker + [self.item]
              
              return self.worker
              
        def insert(self, item, pos):
          
              self.item = item
              self.pos = pos
              
              


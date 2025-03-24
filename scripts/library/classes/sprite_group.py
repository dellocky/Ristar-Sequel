class sprite_group(list):
    def __init__(self, *args):
        super().__init__(*args)
        #self.name = name
    
    def run(self, func, *args, **kwargs):
        for sprite in self:
            getattr(sprite, func)(*args, **kwargs)
    """
    def get_time(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        output = func(*args, **kwargs)
        end_time = default_timer()-start_time
        print(f"Function Time = {end_time}")
        return output
    return wrapper
    """

    


        

        
            



        
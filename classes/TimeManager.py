class TimeManager:
    """
    Singleton class to manage time in the gps.
    """
    _instance = None
    time = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TimeManager, cls).__new__(cls)
        return cls._instance
    
    @classmethod
    def advanceTime(cls, seconds):
        cls.time += seconds
        # print(f"Time advanced by {seconds} seconds. Current time: {cls.time}")
    
    @classmethod
    def getTime(cls):
        return cls.time
    
    @classmethod
    def resetTime(cls):
        cls.time = 0
        # print("Time reset to 0")
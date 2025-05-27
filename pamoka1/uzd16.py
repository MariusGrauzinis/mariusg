class TimeUtils:
    @staticmethod
    def time_to_seconds(time_string):

        hours, minutes, seconds = map(int, time_string.split(":"))
        
        total_seconds = hours * 3600 + minutes * 60 + seconds
        
        return total_seconds



time_string = "01:11:33"
seconds = TimeUtils.time_to_seconds(time_string)
print(f"Total seconds in '{time_string}' is {seconds} seconds.")
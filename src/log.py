class log :
    def __init__(self):
        import time
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())    
        ## create log file if it doesn't exist
        try:
            with open("log.log", "r") as f:
                pass
        except FileNotFoundError:
            with open("log.log", "w") as f:
                pass


    def log_log(self,user,message):
        with open("log.log", "a") as f:
            log_entry = f"[{self.time}] : {user} : {message}\n"
            f.write(log_entry)

        print(f"Logged: {log_entry.strip()}")

    def print_log(self,user_in=None):
        with open("log.log", "r") as f:
            logs = f.readlines()
            logs_list = []
            for log in logs:
                time , user, message = log.split(" : ")
                if user_in is None or user_in == user.strip():
                    logs_list.append(log)


        ###print logs with newest first
        logs_output = ""
        for log in reversed(logs_list):
            logs_output += f"<p>{log.strip()}</p>\n"

        return logs_output

"""
log = log() 
user = 'test'
message = 'This is a test log message.'

log.log_log(user,message)

log.print_log('cfo')
"""

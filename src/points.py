
class points:
    def __init__(self):

        ### create points and maxfile if it doesn't exist
        try:
            with open("points.log", "r") as f:
                pass
        except FileNotFoundError:
            with open("points.log", "w") as f:
                pass

        try:
            with open("maxlevel.txt", "r") as f:
                pass
        except FileNotFoundError:
            with open("maxlevel.txt", "w") as f:
                pass

    
    def get_maxlevel(self,user):
   
        with open('./maxlevel.txt','r') as f:
            lines = f.readlines()
        
        for line in lines:
            print('maxlevel line:', line)
            usr, level = line.split(' : ')
            if usr == user:
                maxlevel = int(level)
                return maxlevel

        else:
            return -1



    def add_points(self, user, points, level=None):
        #from src.log import log
        maxlevel = self.get_maxlevel(user)
        print('maxlevel:', maxlevel)
        if level is not None and level > maxlevel:
            with open("points.log", "a") as f:
                points_entry = f"{user} : {points}\n"
                f.write(points_entry)


    def get_points(self, user_in=None):
        with open("points.log", "r") as f:
            points_lines = f.readlines()
            total_points = 0
            for line in points_lines:
                user, points = line.split(" : ")
                if user_in is None or user_in == user.strip():
                    total_points += int(points.strip())
        return total_points
    
    ## calculta rank among all users    
    def get_rank(self, user):       
        with open("points.log", "r") as f:
            points_lines = f.readlines()
            user_points = {}
            for line in points_lines:
                user_entry, points = line.split(" : ")
                user_entry = user_entry.strip()
                points = int(points.strip())
                if user_entry in user_points:
                    user_points[user_entry] += points
                else:
                    user_points[user_entry] = points

        # Sort users by points in descending order
        sorted_users = sorted(user_points.items(), key=lambda x: x[1], reverse=True)

        # Find the rank of the specified user
        rank = 1
        for u, p in sorted_users:
            if u == user:
                return rank
            rank += 1
        return None  # User not found
    
    def get_scoreboard(self):
        with open("points.log", "r") as f:
            points_lines = f.readlines()
            user_points = {}
            for line in points_lines:
                user_entry, points = line.split(" : ")
                user_entry = user_entry.strip()
                points = int(points.strip())
                if user_entry in user_points:
                    user_points[user_entry] += points
                else:
                    user_points[user_entry] = points

        # Sort users by points in descending order
        sorted_users = sorted(user_points.items(), key=lambda x: x[1], reverse=True)
        return sorted_users
    
    def get_number_of_players(self):
        with open("points.log", "r") as f:
            points_lines = f.readlines()
            user_set = set()
            for line in points_lines:
                user_entry, points = line.split(" : ")
                user_entry = user_entry.strip()
                user_set.add(user_entry)
        return len(user_set)
    
    ##Update maxlevel for user and delete old entry
    def update_maxlevel(self, user, level): 
        print('updating maxlevel for user:', user, 'to level:', level)
        with open('./maxlevel.txt','r') as f:
            lines = f.readlines()
        
        with open('./maxlevel.txt','w') as f:
            user_found = False  
            for line in lines:
                usr, lvl = line.split(' : ')
                if usr == user:
                    if int(lvl) < level:
                        f.write(f"{user} : {level}\n")
                    else:
                        f.write(line)
                    user_found = True
                else:
                    f.write(line)
            if not user_found:
                f.write(f"{user} : {level}\n")
       
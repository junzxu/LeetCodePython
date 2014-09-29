class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        if not path:
            return ""
        length = len(path)
        cur_folder = "" #depthest folder visited
        cur_path = []   #contains a list of folders
        for index in range(0,length+1):
            if index==length or path[index] == "/":
                if cur_folder == ".": # when encouter a ".", just ignore it
                    cur_folder = ""
                    continue
                elif cur_folder == "..": # when encouter a "..", pop the previous folder
                    cur_folder = ""
                    if len(cur_path)>0:
                        cur_path.pop()
                    continue
                else:
                    if len(cur_folder) >0:  # if it's a valid folder, add it to path
                        cur_path.append(cur_folder)
                    cur_folder = ""
            else: #increment current folder name
                cur_folder += path[index]
        
        
        return "/" + "/".join(cur_path)
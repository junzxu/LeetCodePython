class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        #"/a/./b/../../c/", => "/c"
        if not path:
            return ""
        folders = path.split('/')
        stack = []
        for folder in folders:
            if folder == '.' or folder == '':
                continue
            elif folder == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(folder)
                
        newPath = "/".join(stack)
        return '/' + newPath
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        arr=[]
        if target[0]!=1:
            for i in range(target[0]-1):
                arr.append("Push")
                arr.append("Pop")
            arr.append("Push")
            for i in range(len(target)-1) :
                diff=target[i+1]-target[i]
                if diff==1:
                    arr.append("Push")
                if diff>1:
                    arr.append("Push")
                    for j in range(diff-1):
                        arr.append("Pop")
                        arr.append("Push")
        else:
            arr.append("Push")
                
            
            for i in range(len(target)-1) :
                diff=target[i+1]-target[i]
                if diff==1:
                    arr.append("Push")
                if diff>1:
                    arr.append("Push")
                    for j in range(diff-1):
                        arr.append("Pop")
                        arr.append("Push")

        return arr
                    
            
            
            
        
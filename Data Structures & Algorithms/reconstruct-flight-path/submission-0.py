class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #sort tickets
        tickets.sort()
        #create adjacency list
        #map every src node to an empty list
        #src : [] for src,dst in tickets
        adj = {src: [] for src,dst in tickets }
        #build adjacency list
        #go through every src destination in tickets
        for src,dst in tickets:
            #for this src in adj append destination
            #src as key
            adj[src].append(dst)
        #create result array with starting value of "JFK"
        res = ["JFK"]
        #dfs passing some source node
        #seeing if we can find a valid path
        def dfs(src):
            #base case 1 if we find our result
            #if the len of result == tickets + 1
            #return true that we found a valid path
            if (len(res) == len(tickets)+1):
                return True
            #if we can't find a solution 
            #if src we're at is not in adj list (no outgoing edges)
            #return False
            if src not in adj:
                return False
            #go through all the neighbors
            #enumerate so we can go through the index as WELL as the item
            #create temporary copy of the list v
            temp = list(adj[src])
            #for i, v in temp:
            for i, v in enumerate(temp):
                #pop from ACTUAl adjacency list the ith index adj[src].pop(i)
                adj[src].pop(i)
                #add to result the v
                res.append(v)
                #call dfs on v if it returns true return True
                if dfs(v):
                    return True
                #if not return True backtrack decision
                #insert what was popped 
                # adj[src].insert(i,v)
                adj[src].insert(i,v)
                #pop from the end of the result
                res.pop()
            #return false if forloop doesn't return True
            return False
        #call dfs with jfk
        dfs("JFK")
        #return res
        return res






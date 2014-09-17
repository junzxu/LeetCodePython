class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if not ratings:
            return 0
        n = len(ratings)
        candies = [1]*n  #initially all child has 1 candy
        sorted_rating = range(0,n);
        sorted_rating.sort(key=lambda x:ratings[x]) #sort index of child by their ratings 
        for i,index in enumerate(sorted_rating):
            left = 0
            right = 0
            if index-1 >=0 and ratings[index] > ratings[index-1]: #compare candy with neighbors
                left = candies[index-1]
            if index+1 < n and ratings[index] > ratings[index+1]:
                right = candies[index+1]
            if left != 0 or right != 0:
                candies[index] = max(left,right)+1 #each kid get 1 more candy than his highest rank neigbor
        return sum(candies)
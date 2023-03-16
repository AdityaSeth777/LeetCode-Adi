Problem -> <https://leetcode.com/problems/check-if-it-is-a-straight-line/description/?envType=study-plan&id=programming-skills-i>


We first handle the special case when there are only two points in the array, since any two points form a straight line. For arrays with three or more points, we can check if they lie on a straight line by calculating the slope between each pair of consecutive points. If the slopes are equal, then the points lie on a straight line.

We start by initializing the first two points as x1, y1 and x2, y2. We then loop through the remaining points and check if each point (x, y) lies on the same line as the first two points using the formula for the slope of a line between two points: (y2 - y1) / (x2 - x1). If the slopes between any pair of consecutive points are not equal, then the points do not lie on a straight line, and we return False. If we have checked all pairs of consecutive points and none of them have a different slope, then the points lie on a straight line, and we return True.

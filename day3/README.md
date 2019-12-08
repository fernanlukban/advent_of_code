# Day 3 Solution

My idea is that we look at this problem using the perspective of line segments. Each direction we go creates either a horizontal or vertical line segment. We now just need to find one horizontal line segment from the first wire and one vertical line segment from the second wire or vice versa to get where they intersect.

To do so, I'm going to be saving them based on whether they're horizontal or vertical and where they exist on the graph.

Once I start iterating on the second wire, I just have to check if the line segment I'm currently has a corresponding intersecting line segment from the first wire.

If I denote the line segment using place, start, end, then the pairing line segment will have a place such that it is inside the start and end of the line segment from the second wire.

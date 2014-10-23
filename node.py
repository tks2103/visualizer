#def parabola_intersection(segment, point):
#  perpendicular = segment.perpendicular_line_to_midpoint()
#  horizontal_intersection = perpendicular.intersection_with_horizontal(point.y)
#  parabola_segment = Segment(horizontal_intersection, segment.midpoint())
#  return parabola_segment.midpoint()

#def direction(segment, point):
#  intersection_point = parabola_intersection(segment, point)
#  if(point.x < intersection_point.x):
#    return 'left'
#  else:
#    return 'right'
'''
node1 = Node(None, None, Point(1, 1))

tree = Tree(node1)

node3 = Node(None,  None,  Point(1, 2))
node5 = Node(None,  None,  Point(2, 1))
node6 = Node(None,  None,  Point(4, 3))
node4 = Node(node5, node6, Segment(Point(2, 1), Point(4, 3)))
node2 = Node(node3, node4, Segment(Point(1, 2), Point(2, 1)))

tree = Tree(node2)
print(tree.search(Point(0, -10)))
#assert(tree.serialize() == " ((1, 1)(1, 0)) (1, 1) ((1, 0)(1, 1)) (1, 0) (1, 1) ")
'''

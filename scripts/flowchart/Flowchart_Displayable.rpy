init -100 python early:
    import math

    class DetroitConnectionDisplayable(renpy.Displayable):
        def __init__(self, start_node, end_node, all_nodes, color, width, connection_index, connection_type, is_visited=False, **kwargs):
            super(DetroitConnectionDisplayable, self).__init__(**kwargs)
            self.color = color
            self.width = width
            self.connection_index = connection_index
            self.all_nodes = all_nodes
            self.is_visited = is_visited
            
            # Store nodes for additional context
            self.start_node = start_node
            self.end_node = end_node
            
            self.start_right = start_node.x + (220 if start_node.major_event else 180)
            self.start_center_y = start_node.y + (60 if start_node.major_event else 40) // 2
            self.end_left = end_node.x
            self.end_center_y = end_node.y + (60 if end_node.major_event else 40) // 2

            if connection_type is None:
                self.connection_type = self.determine_connection_type()
            else:
                self.connection_type = connection_type
                
            self.segments = self.calculate_flow_based_path()
            self.arrow_points = self.calculate_arrow()


        def determine_connection_type(self):
            """Automatically determine connection type based on node relationship"""
            if self.start_node.major_event and not self.end_node.major_event:
                return "major_to_minor"
            elif not self.start_node.major_event and self.end_node.major_event:
                return "minor_to_major"
            elif not self.start_node.major_event and not self.end_node.major_event:
                # Vertical alignment check
                if abs(self.start_node.x - self.end_node.x) < 50:
                    return "minor_vertical"
                else:
                    return "minor_horizontal"
            else:
                return "major_to_major"

        def calculate_flow_based_path(self):
            """Clean 90-degree connections with 40px offsets"""
            start_x = self.start_right
            start_y = self.start_center_y
            end_x = self.end_left
            end_y = self.end_center_y
            
            # Calculate horizontal direction
            h_offset = 40 if end_x > start_x else -40
            v_offset = 40 if end_y > start_y else -40
            
            return [
                (start_x, start_y),
                (start_x + h_offset, start_y),  # Horizontal offset from start
                (start_x + h_offset, end_y - v_offset),  # Vertical alignment
                (end_x, end_y - v_offset),  # Horizontal approach to end
                (end_x, end_y)  # Final vertical connection
            ]
        def direct_straight_path(self):
            """Single segment connection"""
            return [
                (self.start_right, self.start_center_y),
                (self.end_left, self.end_center_y)
            ]

        def direct_angled_path(self):
            """One right-angle bend only when needed"""
            x_mid = (self.start_right + self.end_left) // 2
            y_mid = (self.start_center_y + self.end_center_y) // 2
            
            if abs(self.start_center_y - self.end_center_y) < 20:
                return self.direct_straight_path()
                
            return [
                (self.start_right, self.start_center_y),
                (x_mid, self.start_center_y),
                (x_mid, self.end_center_y),
                (self.end_left, self.end_center_y)
            ]
        def optimized_vertical_path(self):
            """Straight vertical connection between minor nodes"""
            mid_x = (self.start_right + self.end_left) // 2
            return [
                (self.start_right, self.start_center_y),
                (mid_x, self.start_center_y),
                (mid_x, self.end_center_y),
                (self.end_left, self.end_center_y)
            ]

        def direct_horizontal_path(self):
            """Direct horizontal connection between aligned nodes"""
            return [
                (self.start_right, self.start_center_y),
                (self.end_left, self.end_center_y)
            ]

        def smart_safe_path(self):
            """Improved collision avoidance with simpler logic"""
            path = []
            current_x, current_y = self.start_right, self.start_center_y
            target_x, target_y = self.end_left, self.end_center_y
            
            # First move horizontally
            path.append((current_x, current_y))
            mid_x = current_x + (target_x - current_x) * 0.4
            path.append((mid_x, current_y))
            
            # Then move vertically if needed
            if abs(current_y - target_y) > 20:
                path.append((mid_x, target_y))
            
            path.append((target_x, target_y))
            
            return path

        def simplify_path(self, path):
            """Remove unnecessary intermediate points"""
            simplified = [path[0]]
            for point in path[1:]:
                last = simplified[-1]
                # Only keep points that change direction
                if (abs(point[0] - last[0]) > 10 or (abs(point[1] - last[1]) > 10)):
                    simplified.append(point)
            return simplified

        # Update collision detection
        def rectangle_collision(self, x1, y1, x2, y2):
            """Check if line segment collides with any major nodes or outcomes"""
            for node in self.all_nodes:
                if node in [self.start_node, self.end_node]:
                    continue

                # Dynamically calculate node dimensions
                node_width = 220 if node.major_event else 180
                node_height = 60 if node.major_event else 40

                # Expand collision area by 10%
                nx = node.x - node_width * 0.1
                ny = node.y - node_height * 0.1
                nw = node_width * 1.2
                nh = node_height * 1.2

                if self.line_intersects_rect(x1, y1, x2, y2, nx, ny, nw, nh):
                    return True
            return False
        def line_intersects_rect(self, x1, y1, x2, y2, rx, ry, rw, rh):
            """Check if line segment intersects rectangle using Liang-Barsky algorithm"""
            # Define rectangle boundaries
            left = rx
            right = rx + rw
            bottom = ry
            top = ry + rh

            # Initialize parametric values
            t0 = 0.0
            t1 = 1.0
            dx = x2 - x1
            dy = y2 - y1

            # Test against rectangle boundaries
            for edge in range(4):
                if edge == 0:  # Left
                    p = -dx
                    q = x1 - left
                elif edge == 1:  # Right
                    p = dx
                    q = right - x1
                elif edge == 2:  # Bottom
                    p = -dy
                    q = y1 - bottom
                else:  # Top
                    p = dy
                    q = top - y1

                if p == 0:
                    # Line is parallel to this boundary
                    if q < 0:
                        # Entire segment is outside
                        return False
                    continue

                t = q / p
                
                if p < 0:
                    # Segment enters the boundary
                    if t > t1:
                        return False
                    if t > t0:
                        t0 = t
                else:
                    # Segment exits the boundary
                    if t < t0:
                        return False
                    if t < t1:
                        t1 = t

            # If we survived all tests, there's an intersection
            return t0 < t1 and t1 > 0

        def right_then_down_path(self):
            """Simplified path calculation"""
            # Direct horizontal then vertical path
            return [
                (self.start_right, self.start_center_y),
                (self.start_right + (self.end_left - self.start_right) * 0.8, self.start_center_y),
                (self.start_right + (self.end_left - self.start_right) * 0.8, self.end_center_y),
                (self.end_left, self.end_center_y)
            ]

        def vertical_path(self):
            """Between minor nodes (vertical only)"""
            # Adjust horizontal extension based on node relationship
            extension = 40 + (10 * self.connection_index)
            
            return [
                (self.start_right, self.start_center_y),
                (self.start_right + extension, self.start_center_y),
                (self.start_right + extension, self.end_center_y),
                (self.end_left, self.end_center_y)
            ]

        def horizontal_path(self):
            """Between minor nodes (horizontal)"""
            return [
                (self.start_right, self.start_center_y),
                (self.start_right + (self.end_left - self.start_right) // 2, self.start_center_y),
                (self.start_right + (self.end_left - self.start_right) // 2, self.end_center_y),
                (self.end_left, self.end_center_y)
            ]

        def outcome_path(self):
            """Direct path to outcomes"""
            return [
                (self.start_right, self.start_center_y),
                (self.end_left, self.end_center_y)
            ]

        def down_then_right_path(self):
            """From last minor to next major (down then right)"""
            # Adjust vertical drop based on context
            vertical_drop = 50 + (10 * self.connection_index)
            
            return [
                (self.start_right, self.start_center_y),
                (self.start_right + 40, self.start_center_y),
                (self.start_right + 40, self.start_center_y + vertical_drop),
                (self.end_left - 80, self.start_center_y + vertical_drop),
                (self.end_left - 80, self.end_center_y),
                (self.end_left, self.end_center_y)
            ]
            
        def major_connection_path(self):
            """Connection between major nodes"""
            # Direct connection with slight curve for major nodes
            mid_y = (self.start_center_y + self.end_center_y) // 2
            
            return [
                (self.start_right, self.start_center_y),
                (self.start_right + (self.end_left - self.start_right) * 0.3, self.start_center_y),
                (self.start_right + (self.end_left - self.start_right) * 0.7, self.end_center_y),
                (self.end_left, self.end_center_y)
            ]

        def calculate_safe_path(self):
            """Calculate path that avoids other nodes - fallback method"""
            path = []
            path.append((self.start_right, self.start_center_y))
            
            # Initial horizontal then vertical path
            mid_x = (self.start_right + self.end_left) // 2
            
            # First segment: horizontal from start
            current_x = self.start_right
            current_y = self.start_center_y
            
            # Horizontal movement first
            target_x = mid_x + (30 * self.connection_index)
            target_y = current_y
            
            # Check horizontal collision
            if self.rectangle_collision(current_x, current_y, target_x, target_y):
                # Move vertically first to avoid collision
                vertical_offset = 40 * (1 if self.connection_index % 2 else -1)
                path.append((current_x, current_y + vertical_offset))
                current_y += vertical_offset
                target_y = current_y
            
            path.append((target_x, target_y))
            
            # Vertical movement to target Y
            if self.rectangle_collision(target_x, current_y, target_x, self.end_center_y):
                # Move horizontally around obstacle
                horizontal_offset = 60 * (1 if self.connection_index % 2 else -1)
                path.append((target_x + horizontal_offset, current_y))
                path.append((target_x + horizontal_offset, self.end_center_y))
                target_x += horizontal_offset
            else:
                path.append((target_x, self.end_center_y))
            
            # Final horizontal to end
            path.append((self.end_left, self.end_center_y))
            
            return path

        def node_collision(self, x, y):
            """Check if point collides with any node"""
            for node in self.all_nodes:
                if node == self.start_node or node == self.end_node:
                    continue  # Skip start and end nodes
                    
                node_w = 220 if node.major_event else 180
                node_h = 60 if node.major_event else 40
                if (node.x < x < node.x + node_w and
                    node.y < y < node.y + node_h):
                    return True
            return False

        def rectangle_collision(self, x1, y1, x2, y2):
            """Check if line segment collides with any major nodes or outcomes"""
            for node in self.all_nodes:
                if node in [self.start_node, self.end_node]:
                    continue

                # Dynamically calculate node dimensions
                node_width = 220 if node.major_event else 180
                node_height = 60 if node.major_event else 40

                # Expand collision area by 10%
                nx = node.x - node_width * 0.1
                ny = node.y - node_height * 0.1
                nw = node_width * 1.2
                nh = node_height * 1.2

                if self.line_intersects_rect(x1, y1, x2, y2, nx, ny, nw, nh):
                    return True
            return False

        def calculate_arrow(self):
            """Calculate arrowhead points"""
            # Get the last segment for arrow direction
            if len(self.segments) >= 2:
                last_segment = self.segments[-2:]
                dx = last_segment[1][0] - last_segment[0][0]
                dy = last_segment[1][1] - last_segment[0][1]
                angle = math.atan2(dy, dx)
                
                arrow_size = 8 if not self.is_visited else 10  # Slightly smaller for non-visited
                base_x = self.end_left - 10 * math.cos(angle)
                base_y = self.end_center_y - 10 * math.sin(angle)
                
                return [
                    (base_x, base_y),
                    (base_x - arrow_size * math.cos(angle - math.pi/6), base_y - arrow_size * math.sin(angle - math.pi/6)),
                    (base_x - arrow_size * math.cos(angle + math.pi/6),base_y - arrow_size * math.sin(angle + math.pi/6))
                ]
            return []
        def major_direct_path(self):
            """Direct connection between major nodes."""
            mid_y = (self.start_center_y + self.end_center_y) // 2

            return [
                (self.start_right, self.start_center_y),
                (self.start_right + (self.end_left - self.start_right) * 0.3, self.start_center_y),
                (self.start_right + (self.end_left - self.start_right) * 0.7, self.end_center_y),
                (self.end_left, self.end_center_y)
            ]
        def render(self, width, height, st, at):
            print(f"Rendering connection from {self.start_node.id} to {self.end_node.id}")
            render = renpy.Render(width, height)
            canvas = render.canvas()
            
            # Draw all path segments
            for i in range(len(self.segments)-1):
                start = self.segments[i]
                end = self.segments[i+1]
                canvas.line(self.color, start, end, self.width)
            
            # Draw arrowhead
            if len(self.arrow_points) >= 3:
                canvas.polygon(self.color, self.arrow_points)
            
            return render
            
    def draw_detroit_connection(st, at, start_node, end_node, all_nodes, color=None, width=None, connection_index=0, connection_type=None, is_visited=False):
        """Draw a connection between nodes with Detroit-style routing."""
        # Set default width based on visited state
        if width is None:
            width = 3 if is_visited else 1.5

        # Set default colors based on node types and visited state
        if is_visited:
            color = "#3e7cdb"  # Blue for visited connections
        else:
            if hasattr(end_node, 'node_type') and end_node.node_type == 'outcome':
                color = "#606060"  # Darker gray for outcome nodes
            else:
                color = "#909090"  # Light gray for regular connections

        # Return a single DetroitConnectionDisplayable object
        return DetroitConnectionDisplayable(
            start_node, end_node, all_nodes, color, width, connection_index, connection_type, is_visited
        ), None
# ------------------------------------------------------------------------ Flowchart Default Variables
init -999 python:
    from collections import OrderedDict
    class Flowchart:
# ------------------------------------------------------------------------ Flowchart Class
        def __init__(self, name):
            self.name = name
            self.nodes = {}
            self.visited_paths = set()  
            self.visited_nodes = set()
            self.current_node = None  
            self.zoom_level = 1.0     
            self._version = 1

        def add_node(self, node):
            if not hasattr(node, "visited"):
                node.visited = False
            if not hasattr(node, "connections"):
                node.connections = []
            self.nodes[node.id] = node

        def __getstate__(self):
            return vars(self)
        
        def __setstate__(self, state):
            vars(self).update(state)
            # Handle version upgrades
            if not hasattr(self, '_version'):
                self._version = 1
        # In Flowchart class
        def mark_path_visited(self, start_id, end_id):
            """Record both directions for bidirectional paths"""
            self.visited_paths.add((start_id, end_id))
            # Add reverse connection if exists
            self.visited_paths.add((end_id, start_id))

        def is_path_visited(self, start_id, end_id):
            """Check both directions for any visited status"""
            return ((start_id, end_id) in self.visited_paths) or ((end_id, start_id) in self.visited_paths)

        def mark_visited(self, node_id):
            """Mark a node as visited"""
            if node_id in self.nodes:
                self.visited_nodes.add(node_id)
                self.nodes[node_id].visited = True
                self.completion = self.calculate_completion()

        def set_current(self, node_id):
            """Set the current node"""
            if node_id in self.nodes:
                self.current_node = node_id
                
        def render(self, st, at):
            """Render the entire flowchart."""
            displayables = []
            
            # Render all connections
            connection_index = 0
            for node_id, node in self.nodes.items():
                for conn in node.connections:
                    target_id = conn.get("target")
                    connection_type = conn.get("type", "normal")
                    
                    if target_id in self.nodes:
                        target_node = self.nodes[target_id]
                        
                        # Check if this path has been visited
                        is_visited = self.is_path_visited(node_id, target_id)
                        
                        # Render the connection
                        displayables.append(
                            draw_detroit_connection(
                                st, at, node, target_node, 
                                list(self.nodes.values()),
                                connection_index=connection_index,
                                connection_type=connection_type,
                                is_visited=is_visited
                            )
                        )
                        connection_index += 1

                # Render the node itself
                displayables.append(draw_flowchart_node(st, at, node))
            
            return displayables
        
        def get_all_paths_dfs(self):
            """
            Returns a list of all reachable node IDs from the current node,
            including branches, using depth-first traversal.
            """
            visited = set()
            path = []

            def dfs(node_id):
                if node_id in visited or node_id not in self.nodes:
                    return
                visited.add(node_id)
                path.append(node_id)
                for conn in self.nodes[node_id].connections:
                    dfs(conn["target"])

            start_node = self.current_node or "start"
            if start_node not in self.nodes:
                start_node = next(iter(self.nodes))  # fallback

            dfs(start_node)
            return path

        def get_flattened_path(self):
            """
            Returns a flattened list of all node IDs in the primary progression path,
            including nested branches (recursively).
            """
            def recurse_path(node_id, visited):
                if node_id in visited:
                    return []
                visited.add(node_id)

                node = self.nodes.get(node_id)
                if not node:
                    return []

                path = [node_id]

                # Recurse into branches (nested sub-nodes)
                if hasattr(node, "branches"):
                    for sub_id in node.branches:
                        path.extend(recurse_path(sub_id, visited))

                # Follow first linear connection only
                if hasattr(node, "connections"):
                    for conn in node.connections:
                        if isinstance(conn, dict):
                            conn_id = conn.get("id")
                        elif isinstance(conn, (tuple, list)):
                            conn_id = conn[0]
                        else:
                            continue

                        if conn_id and conn_id not in visited:
                            path.extend(recurse_path(conn_id, visited))
                            break  # Follow just first connection

                return path

            start_node = self.current_node or next(iter(self.nodes), None)
            return recurse_path(start_node, set()) if start_node else []

        def get_nested_paths(self, start_node_id="start"):
            """
            Return nested structure of node traversal.
            Example:
            {
                "start": {
                    "talk": {
                        "save_fish": {},
                        "leave_fish": {}
                    }
                }
            }
            """
            visited = set()

            def recurse(node_id):
                if node_id in visited:
                    return {}
                visited.add(node_id)
                node = self.nodes.get(node_id)
                if not node:
                    return {}
                return {conn["target"]: recurse(conn["target"]) for conn in node.connections}

            return {start_node_id: recurse(start_node_id)}

        def zoom_in(self):
            """Increase the zoom level"""
            self.zoom_level = min(self.zoom_level + 0.1, 2.0)  # Limit zoom to 2.0x

        def zoom_out(self):
            """Decrease the zoom level"""
            self.zoom_level = max(self.zoom_level - 0.1, 0.5)  # Limit zoom to 0.5x

        def save_flowchart_state(self):
            return {
                "relationships": persistent.relationships_stats,
                "unlocked_nodes": [n.id for n in self.visited_nodes]
            }
        
        def load_flowchart_state(self, data):
            persistent.relationships_stats = data["relationships"]
            for node_id in data["unlocked_nodes"]:
                self.mark_visited(node_id)

        def calculate_completion(self):
            """
            Returns completion % based only on reachable nodes from the current path,
            not all nodes globally.
            """
            reachable_nodes = self.get_all_paths_dfs()
            total = len(reachable_nodes)
            visited = len([node_id for node_id in reachable_nodes if node_id in self.visited_nodes])

            if total == 0:
                return 0.0

            return (visited / total) * 100.0


            return (visited / total) * 100.0
    def debug_check_flowchart(fc):
        """Detailed connection analysis"""
        print("\n=== CONNECTION ANALYSIS ===")
        
        # Count all connections in the flowchart
        all_connections = []
        connection_sources = set()
        
        for node_id, node in fc.nodes.items():
            connections = getattr(node, 'connections', [])
            for conn in connections:
                all_connections.append((node_id, conn.get("target")))
                connection_sources.add(node_id)
        
        print(f"Total connections in system: {len(all_connections)}")
        print(f"Nodes with outgoing connections: {len(connection_sources)}")
        
        # Print connection sources
        print("\nNodes that SHOULD have connections:")
        for node_id in sorted(connection_sources):
            node = fc.nodes.get(node_id)
            if node:
                pos = f"{getattr(node, 'x', '?')}, {getattr(node, 'y', '?')}"
                print(f"- {node_id} at {pos}")
        
        # Print nodes without connections
        print("\nNodes WITHOUT connections:")
        for node_id, node in fc.nodes.items():
            if not getattr(node, 'connections', []):
                pos = f"{getattr(node, 'x', '?')}, {getattr(node, 'y', '?')}"
                print(f"- {node_id} at {pos}")
        
        # Verify connection targets
        print("\nConnection targets:")
        missing_targets = 0
        for source, target in all_connections:
            if target not in fc.nodes:
                missing_targets += 1
                print(f"! {source} -> {target} (MISSING TARGET)")
        
        print(f"\nMissing targets: {missing_targets}")
        print("=== ANALYSIS COMPLETE ===")

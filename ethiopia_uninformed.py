state_space_graph = {
  "Arad": [("Timisoara", 118), ("Sibiu", 140), ("Zerind", 75)],
  "Bucharest": [("Urziceni", 85), ("Pitesti", 101), ("Giurgiu", 90)],
  "Craiova": [("Dobreta", 120), ("Pitesti", 138), ("Rimnicu Vilcea", 146)],
  "Dobreta": [("Mehadia", 75)],
  "Eforie": [("Hirsova", 86)],
  "Fagaras": [("Sibiu", 99)],
  "Giurgiu": [("Ruse", 77)],
  "Hirsova": [("Urziceni", 98)],
  "Iasi": [("Vaslui", 92)],
  "Lugoj": [("Timisoara", 111)],
  "Mehadia": [("Drobeta Turnu Severin", 75)],
  "Oradea": [("Zerind", 71)],
  "Pitesti": [("Rimnicu Vilcea", 97)],
  "Rimnicu Vilcea": [("Sibiu", 80)],
  "Ruse": [("Giurgiu", 58)],
  "Sibiu": [("Oradea", 151)],
  "Timisoara": [("Lugoj", 111)],
  "Urziceni": [("Vaslui", 142)],
  "Vaslui": [("Iasi", 92)],
  "Zerind": [("Arad", 75)],
}
state_space_graph_et = {
    'Asmera': ['Axum', 'Adigrat'],
    'Axum': ['Shire', 'Adwa', 'Asmera'],
    'Adigrat': ['Asmera', 'Adwa','Mekelle'],
    'Shire': ['Axum','Debarke','Humera'],
    'Adwa': ['Axum','Adigrat','Mekelle'],
    'Mekelle': ['Adwa','Adigrat','Sekota','Alamata'],
    'Debarke':['Shire','Gondar'],
    'Humera':['Shire','Gondar','Kartum'],
    'Sekota':['Mekelle', 'Alamata','Lalibela'],
    'Alamata':['Mekelle','Sekota','Woldia','Samara'],
    'Gondar': ['Debarke','Humera','Azezo','Metema'],
    'Kartum': ['Humera','Metema'],
    'Lalibela':['Sekota','Woldia','Debre_Tabor'],
    'Woldia': ['Alamata','Lalibela','Dessie','Samara'],
    'Samara':['Alamata','Fanti_Rasu','Woldia','Gabi_Rasu'],
    'Azezo':['Gondar','Metema','Bahir_Dar'],
    'Metema':['Gondar','Azezo','Kartum'],
    'Debre_Tabor':['Bahir_Dar', 'Lalibela'],
    'Dessie': ['Woldia','Kemise'],
    'Fanti_Rasu': ['Samara', 'Kilbet_Rasu'],
    'Gabi_Rasu': ['Samara','Awash'],
    'Bahir_Dar': ['Azezo','Debre_Tabor','Injibara','Finote_Selam','Metekel'],
    'Kemise': ['Dessie','Debre_Sina'],
    'Kilbet_Rasu': ['Fanti_Rasu'],
    'Awash': ['Chiro','Gabi_Rasu','Matahara'],
    'Debre_Sina': ['Kemise','Debre_Markos','Debre_Birhan'],
    'Chiro':['Awash', 'Dire_Dawa'],
    'Matahara':['Awash','Adama'],
    'Debre_Markos':['Debre_Sina','Finote_Selam'],
    'Injibara': ['Finote_Selam','Bahir_Dar'],
    'Finote_Selam': ['Debre_Markos','Injibara','Bahir_Dar'],
    'Metekel':['Bahir_Dar','Assosa'],
    'Debre_Birhan':['Debre_Sina','Addis_Abeba'],
    'Dire_Dawa': ['Chiro','Harar'],
    'Adama': ['Matahara','Addis_Abeba','Batu','Assella'],
    'Assosa':['Metekel','Dembi_Dollo'],
    'Addis_Abeba':['Debre_Birhan','Adama','Ambo'],
    'Harar':['Dire_Dawa','Babile'],
    'Batu': ['Buta_Jirra','Adama','Shashemene'],
    'Assella':['Adama','Assasa'],
    'Dembi_Dollo': ['Assosa','Gimbi','Gambella'],
    'Ambo':['Addis_Abeba','Nekemete','Wolkite'],
    'Babile':['Harar','Jigjiga'],
    'Buta_Jirra':['Batu','Worabe'],
    'Shashemene': ['Batu','Hossana','Dodolla','Hawassa'],
    'Assasa':['Assella','Dodolla'],
    'Gimbi':['Dembi_Dollo','Nekemete'],
    'Gambella': ['Dembi_Dollo','Gore'],
    'Nekemete': ['Gimbi','Ambo','Bedelle'],
    'Wolkite':['Ambo','Worabe','Jimma'],
    'Jigjiga':['Babile','Dega_Habur'],
    'Worabe': ['Buta_Jirra','Wolkite','Hossana'],
    'Hossana':['Shashemene','Worabe', 'Wolaita_Sodo'],
    'Dodolla':['Assasa','Bale','Shashemene'],
    'Hawassa':['Shashemene','Dilla'],
    'Gore':['Gambella','Tepi','Bedelle'],
    'Bedelle': ['Nekemete','Jimma','Gore'],
    'Jimma':['Wolkite','Bedelle','Bonga'],
    'Dega_Habur':['Jigjiga','Goba','Kebri_Dehar'],
    'Wolaita_Sodo': ['Hossana','Dawro','Arba_Minch'],
    'Bale':['Dodolla','Goba','Sof_Oumer','Liben'],
    'Dilla': ['Hawassa','Bule_Hora'],
    'Tepi':['Gore','Mezan_Teferi','Bonga'],
    'Bonga':['Jimma','Tepi','Mezan_Teferi','Dawro'],
    'Goba':['Bale','Sof_Oumer','Dega_Habur'],
    'Kebri_Dehar':['Dega_Habur','Sof_Oumer','Werder','Gode'],
    'Dawro':['Bonga','Wolaita_Sodo','Basketo'],
    'Arba_Minch':['Wolaita_Sodo','Basketo','Konso'],
    'Sof_Oumer':['Kebri_Dehar','Goba','Bale'],
    'Liben':['Bale'],
    'Bule_Hora':['Dilla','Yabello'],
    'Mezan_Teferi':['Tepi','Bonga','Basketo'],
    'Werder': ['Kebri_Dehar'],
    'Basketo':['Dawro','Arba_Minch','Bench_Maji','Mezan_Teferi'],
    'Konso': ['Arba_Minch','Yabello'],
    'Yabello':['Bule_Hora','Konso','Moyale'],
    'Bench_Maji':['Basketo','Juba'],
    'Moyale':['Yabello','Narobi'],
    'Juba':['Bench_Maji'],
    'Narobi':['Moyale'],
    'Gode':['Kebri_Dehar','Dollo','Mokadisho'],
    'Dollo':['Gode'],
    'Mokadisho':['Gode']
}
import heapq
class Searcher:

    def __init__(self, state_space_graph, initial_state, goal_state):
        self.graph = state_space_graph
        self.initial_state = initial_state
        self.goal_state = goal_state

    def search(self, strategy):
        """
        Performs a search using the specified strategy.
        :param strategy: "bfs" or "dfs"
        :return: The path from the initial state to the goal state,
                or None if the goal state is not found.
        """
        if strategy == "bfs":
            return self.breadth_first_search()
        elif strategy == "dfs":
            return self.depth_first_search()
        else:
            raise ValueError("Invalid search strategy:", strategy)

    def breadth_first_search(self):
        """
        Performs a Breadth-First Search (BFS) on the state space graph.
        :return: The path from the initial state to the goal state,
                or None if the goal state is not found.
        """
        visited = set()
        queue = [(self.initial_state, [])]

        while queue:
            state, path = queue.pop(0)
            visited.add(state)

            if state == self.goal_state:
                return path + [state]

            for neighbor in self.graph[state]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [state]))

        return None

    def depth_first_search(self):
        """
        Performs a Depth-First Search (DFS) on the state space graph.
        :return: The path from the initial state to the goal state,
                or None if the goal state is not found.
        """
        visited = set()
        stack = [(self.initial_state, [])]

        while stack:
            state, path = stack.pop()
            visited.add(state)

            if state == self.goal_state:
                return path + [state]

            for neighbor in self.graph[state]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [state]))

        return None

    def uniform_cost_search(self):
        """
        Performs a Uniform Cost Search (UCS) on the state space graph.
        :return: The path from the initial state to the goal state,
                or None if the goal state is not found.
        """
        visited = set()
        queue = [(0, self.initial_state, [])]  # (cost, state, path)

        while queue:
            cost, state, path = heapq.heappop(queue)
            visited.add(state)

            if state == self.goal_state:
                return path + [state]
            print(self.graph[state])
            for neighbor, neighbor_cost in self.graph[state]:
                if neighbor not in visited:
                    total_cost = cost + neighbor_cost
                    heapq.heappush(queue, (total_cost, neighbor, path + [state]))

        return None
# initial_state = 'Dessie'
# goal_state = 'Dollo'

# # Create a Searcher object
# searcher = Searcher(state_space_graph_et, initial_state, goal_state)

# # Perform BFS and DFS searches
# bfs_path = searcher.search("bfs")
# dfs_path = searcher.search("dfs")

# # Print the results
# if bfs_path:
#   print("BFS Path:", bfs_path)
# else:
#   print("BFS failed to find a path.")

# if dfs_path:
#   print("DFS Path:", dfs_path)
# else:
#   print("DFS failed to find a path.")
searcher = Searcher(state_space_graph, "Bucharest", "Sibiu")
path = searcher.uniform_cost_search()
print("Path:", path)
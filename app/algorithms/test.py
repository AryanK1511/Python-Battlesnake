from graphviz import Digraph

def create_minimax_tree():
    # Initialize a Digraph for the tree
    dot = Digraph(comment='Minimax Tree')

    # Adding nodes and edges from the provided output
    dot.node('A', 'Root\n(Down, 212.0)')
    dot.node('B', 'Max\nUp\n214.0')
    dot.node('C', 'Max\nDown\n213.0')
    dot.node('D', 'Max\nLeft\n214.0')
    dot.node('E', 'Max\nRight\n213.0')

    dot.node('F', 'Min\nUp\n214.0')
    dot.node('G', 'Min\nDown\n213.0')
    dot.node('H', 'Min\nLeft\n214.0')
    dot.node('I', 'Min\nRight\n213.0')

    dot.node('J', 'Max\nUp\n148.3')
    dot.node('K', 'Max\nDown\n148.3')
    dot.node('L', 'Max\nLeft\n147.3')
    dot.node('M', 'Max\nRight\n146.3')

    dot.node('N', 'Min\nUp\n147.3')
    dot.node('O', 'Min\nDown\n146.3')
    dot.node('P', 'Min\nLeft\n147.3')
    dot.node('Q', 'Min\nRight\n145.3')

    # Edges for the tree
    dot.edges(['AB', 'AC', 'AD', 'AE'])
    dot.edges(['BF', 'CG', 'DH', 'EI'])
    dot.edges(['FJ', 'GK', 'HL', 'IM'])
    dot.edges(['JN', 'KO', 'LP', 'MQ'])

    return dot

# Create the Minimax tree
minimax_tree = create_minimax_tree()

# Render the tree to a file
minimax_tree.render('/mnt/data/minimax_tree', format='png', cleanup=True)

'/mnt/data/minimax_tree.png'

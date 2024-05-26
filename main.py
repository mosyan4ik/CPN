from snakes.nets import *
snakes.plugins.load("gv", "snakes.nets", "nets")
from nets import *

net = PetriNet('Resource Allocation')

U = Range('U', 'p', 'q')
I = Range('I', 0, 1000)
E = Range('E', 'e')

net.add_place(Place('A', [('q', 0), ('q', 0), ('q', 0)]))
net.add_place(Place('B', [('p', 0), ('p', 0)]))
net.add_place(Place('C', []))
net.add_place(Place('D', []))
net.add_place(Place('E', []))
net.add_place(Place('R', ['e']))
net.add_place(Place('S', ['e', 'e', 'e']))
net.add_place(Place('T', ['e', 'e']))

net.add_transition(Transition('T1', Expression('x == "q"')))
net.add_transition(Transition('T2'))
net.add_transition(Transition('T3'))
net.add_transition(Transition('T4'))
net.add_transition(Transition('T5'))

net.add_input('A', 'T1', MultiArc([Variable('x'), Variable('i')]))
net.add_output('B', 'T1', MultiArc([Expression('("q", i)')]))

net.add_input('B', 'T2', MultiArc([Variable('x'), Variable('i')]))
net.add_input('S', 'T2', MultiArc([Variable('e'), Variable('E')]))
net.add_output('C', 'T2', MultiArc([Variable('x'), Variable('i')]))

net.add_input('C', 'T3', MultiArc([Variable('x'), Variable('i')]))
net.add_output('D', 'T3', MultiArc([Variable('x'), Variable('i')]))

net.add_input('D', 'T4', MultiArc([Variable('x'), Variable('i')]))
net.add_output('E', 'T4', MultiArc([Variable('x'), Expression('i+1')]))

net.add_input('E', 'T5', MultiArc([Variable('x'), Variable('i')]))
net.add_output('A', 'T5', MultiArc([Expression('("q", i+1)')]))
net.add_output('B', 'T5', MultiArc([Expression('("p", i+1)')]))

net.draw('resource_allocation.png')

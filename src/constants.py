from enum  import Enum

from .equations import OB_equations2      as eqF
from .equations import boundary_equations as BC

# Define bounding values
X_MIN         = 0.977#0.95
X_MAX         = 1.123#1.15
Y_MIN         = 0.977
Y_MAX         = 1.123
Z_VAL         = 0.01

# Neighbor/channel names
CENTER        = "cen"
UP            = "up"
DOWN          = "down"
LEFT          = "left"
RIGHT         = "right"
INLET         = "inlet"
OUTLET        = "outlet"
INNER         = "inner"

# Neighbor info
NEIGHBOR_NUM  = 5
NEIGHBOR_LOC  = [CENTER, UP, DOWN, LEFT, RIGHT]
CHANNEL_TYPE  = [INLET, OUTLET]
NEIGHBOR      = dict((v,k) for k,v in enumerate(NEIGHBOR_LOC))
C_TYPE        = [
                    [INNER, UP,   LEFT ],
                    [INNER, UP,   RIGHT],
                    [INNER, DOWN, LEFT ],
                    [INNER, DOWN, RIGHT]
                ]

# System parameters
H             = eqF.H
DX            = eqF.DX
DY            = eqF.DY
LAMBDA        = eqF.LAMBDA
COORD         = eqF.COORD

# Equation information
EQ_NUM        = eqF.get_equation_number()
EQ_NAMES      = eqF.get_equation_names()
VAR_NAMES     = eqF.get_component_names()
ATTRIBUTES    = eqF.get_vars()

# Inner corner information
INNR_CRNR_LOC = BC.get_inner_corners()

# Simulation parameters
NULL_NEIGHBOR = -1
LOAD_INTERVAL = 500
COORD_TOL     = 0.001
DELIM         = "_"

# Argument combinations valid for all subviews test functions.

common_arg_combos = [
    ({"material": ["PbTe", "SnSe"]}, None),
    ({"characterization": ["positron"]}, "positron emission tomography"),
    ({"material": ["graphene"], "descriptor": ["doped"]}, None),
    ({}, "Ceder"),
]

"""
Helper function that remvoes every None
origin or returns ["*"] to allow all origins
if all the elements are None.
"""


def get_origin_list(allowed_origins):
    if allowed_origins == []:
        return ["*"]
    if None not in allowed_origins:
        return allowed_origins
    if all(elem is None for elem in allowed_origins):
        return ["*"]
    return [elem for elem in allowed_origins if elem is not None]

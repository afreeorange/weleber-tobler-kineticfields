# coding: utf-8

from __future__ import division
from math import (atan,
                  cos,
                  fabs,
                  pi,
                  radians,
                  tan
                  )


def compute(isopter_points=None):
    result = {
        'steradians': None,
        'percent_of_sphere': None,
    }

    if not isopter_points:
        return result
    else:
        result['steradians'] = 0.0

    RD = [_[0] if _[0] < 90 else 90 for _ in isopter_points]
    TD = [_[1] for _ in isopter_points]

    R = map(radians, RD)
    T = map(radians, TD)

    for i, e in enumerate(T):
        try:
            if R[i+1] == 0:
                continue
        except IndexError:
            pass

        try:
            D = fabs(T[i+1] - T[i])
            cos_X = cos((0.5) * (R[i+1] - R[i]))
            cos_Y = cos((0.5) * (R[i+1] + R[i]))
            E = 2 * atan((cos_X/cos_Y) * (1/tan(0.5 * D))) + D - pi
        except Exception:
            pass

        try:
            if T[i+1] < T[i]:
                E = E * (-1)
        except IndexError:
            pass

        result['steradians'] += E

    result['percent_of_sphere'] = result['steradians']/(4 * pi) * 100

    return result

# coding: utf-8

from __future__ import division
from math import (atan,
                  cos,
                  fabs,
                  pi,
                  radians,
                  tan
                  )


class KineticField(object):
    def __init__(self, isopter_points=None):
        super(KineticField, self).__init__()
        self._isopter_points = isopter_points
        self._steradians = None
        self._percent_of_sphere = None

        if self._isopter_points:
            self.__compute()

    @property
    def isopter_points(self):
        return self._isopter_points
    
    @isopter_points.setter
    def isopter_points(self, value):
        self._isopter_points = value
        self.__compute()

    @property
    def steradians(self):
        return self._steradians

    @property
    def percent_of_sphere(self):
        return self._percent_of_sphere

    def __compute(self):
        self._steradians = 0.0

        RD = [_[0] if _[0] < 90 else 90 for _ in self._isopter_points]
        TD = [_[1] for _ in self._isopter_points]

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

            self._steradians += E

        self._percent_of_sphere = self._steradians/(4 * pi) * 100

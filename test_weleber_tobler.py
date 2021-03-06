# coding: utf-8

import unittest
from weleber_tobler import kineticfield


# These values were obtained from the paper in /misc
test_data = (
        {
            'dataset': [(54.7, 1.0), (51, 14.9), (50.2, 29.7),
                        (40.2, 45.7), (39.4, 59.6), (35.6, 73.6),
                        (32.7, 100.4), (31.9, 118.7), (33.6, 135.1),
                        (33.4, 149.5), (34.6, 164.8), (36.5, 179.6),
                        (35.7, 195.3), (37.3, 210.7), (36.2, 225.3),
                        (35.6, 241.0), (34.3, 258.1), (41.4, 270.7),
                        (45.3, 285.0), (50.6, 299.9), (51.0, 314.8),
                        (54.8, 329.9), (54.4, 344.6), (0.0, 0.0),
                        (0.0, 0.0), (0.0, 0.0)],
            'expected_steradians': 1.565
        },
        {
            'dataset': [(77.6, 14.9), (74.9, 30.5), (69.1, 45.5),
                        (55.6, 60.4), (48.0, 75.0), (45.5, 90.3),
                        (42.1, 104.6), (41.5, 119.4), (42.9, 134.7),
                        (46.4, 149.5), (52.2, 165.0), (53.5, 179.7),
                        (53.2, 195.3), (54.3, 210.2), (58.6, 225.1),
                        (58.8, 235.0), (61.2, 240.3), (61.8, 255.3),
                        (65.7, 270.3), (73.8, 285.2), (80.5, 299.7),
                        (81.5, 314.8), (81.3, 330.1), (80.7, 345.0),
                        (80.3, 353.9), (0.0, 0.0)],
            'expected_steradians': 3.377
        },
        {
            'dataset': [(18.2, 4.2), (17.4, 9.1), (16.1, 11.3),
                        (14.9, 12.3), (13.2, 9.0), (12.2, 0.4),
                        (12.7, 348.3), (14.1, 342.5), (16.0, 341.5),
                        (17.6, 343.8), (18.4, 348.2), (18.6, 354.1),
                        (0.0, 0.0), (0.0, 0.0), (0.0, 0.0),
                        (0.0, 0.0), (0.0, 0.0), (0.0, 0.0),
                        (0.0, 0.0), (0.0, 0.0), (0.0, 0.0),
                        (0.0, 0.0), (0.0, 0.0), (0.0, 0.0),
                        (0.0, 0.0), (0.0, 0.0)],
            'expected_steradians': 0.012
        },
        {
            'dataset': [(90.0, 4.2), (90.0, 15.4), (90.0, 30.2),
                        (79.1, 45.2), (67.2, 60.4), (54.8, 75.5),
                        (47.4, 90.4), (45.4, 104.6), (44.0, 120.0),
                        (47.3, 135.3), (51.8, 149.6), (57.8, 165.2),
                        (58.7, 180.0), (60.0, 195.3), (61.6, 210.2),
                        (62.1, 225.2), (59.3, 233.3), (62.9, 240.3),
                        (69.2, 255.0), (68.4, 270.0), (77.2, 285.2),
                        (80.8, 288.4), (90.0, 299.7), (90.0, 315.4),
                        (90.0, 328.9), (90.0, 344.6)],
            'expected_steradians': 4.058
        }
    )


class WeleberToblerTest(unittest.TestCase):
    def __assertion(self, n):
        self.assertEqual(
            round(
                kineticfield.compute(
                    isopter_points=test_data[n]['dataset']).get('steradians'),
                3),
            test_data[n]['expected_steradians']
            )

    def test_case_one(self):
        return self.__assertion(0)

    def test_case_two(self):
        return self.__assertion(1)

    def test_case_three(self):
        return self.__assertion(2)

    def test_case_four(self):
        return self.__assertion(3)


if __name__ == '__main__':
    unittest.main()

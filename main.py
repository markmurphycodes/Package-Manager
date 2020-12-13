# Mark Murphy, 001223523

import os
import sys

import graph
import parcel
from myHash import Hash
from parcel import Parcel


# Hard-coded graph
def createGraph():
    g = graph.Graph()

    l0 = graph.Vertex("0")
    l1 = graph.Vertex("1")
    l2 = graph.Vertex("2")
    l3 = graph.Vertex("3")
    l4 = graph.Vertex("4")
    l5 = graph.Vertex("5")
    l6 = graph.Vertex("6")
    l7 = graph.Vertex("7")
    l8 = graph.Vertex("8")
    l9 = graph.Vertex("9")
    l10 = graph.Vertex("10")
    l11 = graph.Vertex("11")
    l12 = graph.Vertex("12")
    l13 = graph.Vertex("13")
    l14 = graph.Vertex("14")
    l15 = graph.Vertex("15")
    l16 = graph.Vertex("16")
    l17 = graph.Vertex("17")
    l18 = graph.Vertex("18")
    l19 = graph.Vertex("19")
    l20 = graph.Vertex("20")
    l21 = graph.Vertex("21")
    l22 = graph.Vertex("22")
    l23 = graph.Vertex("23")
    l24 = graph.Vertex("24")
    l25 = graph.Vertex("25")
    l26 = graph.Vertex("26")

    g.addVertex(l0)
    g.addVertex(l1)
    g.addVertex(l2)
    g.addVertex(l3)
    g.addVertex(l4)
    g.addVertex(l5)
    g.addVertex(l6)
    g.addVertex(l7)
    g.addVertex(l8)
    g.addVertex(l9)
    g.addVertex(l10)
    g.addVertex(l11)
    g.addVertex(l12)
    g.addVertex(l13)
    g.addVertex(l14)
    g.addVertex(l15)
    g.addVertex(l16)
    g.addVertex(l17)
    g.addVertex(l18)
    g.addVertex(l19)
    g.addVertex(l20)
    g.addVertex(l21)
    g.addVertex(l22)
    g.addVertex(l23)
    g.addVertex(l24)
    g.addVertex(l25)
    g.addVertex(l26)

    g.addEdge(l0, l1, 7.2)
    g.addEdge(l0, l2, 3.8)
    g.addEdge(l0, l3, 11.0)
    g.addEdge(l0, l4, 2.2)
    g.addEdge(l0, l5, 3.5)
    g.addEdge(l0, l6, 10.9)
    g.addEdge(l0, l7, 8.6)
    g.addEdge(l0, l8, 7.6)
    g.addEdge(l0, l9, 2.8)
    g.addEdge(l0, l10, 6.4)
    g.addEdge(l0, l11, 3.2)
    g.addEdge(l0, l12, 7.6)
    g.addEdge(l0, l13, 5.2)
    g.addEdge(l0, l14, 4.4)
    g.addEdge(l0, l15, 3.7)
    g.addEdge(l0, l16, 7.6)
    g.addEdge(l0, l17, 2.0)
    g.addEdge(l0, l18, 3.6)
    g.addEdge(l0, l19, 6.5)
    g.addEdge(l0, l20, 1.9)
    g.addEdge(l0, l21, 3.4)
    g.addEdge(l0, l22, 2.4)
    g.addEdge(l0, l23, 6.4)
    g.addEdge(l0, l24, 2.4)
    g.addEdge(l0, l25, 5.0)
    g.addEdge(l0, l26, 3.6)

    g.addEdge(l1, l2, 7.1)
    g.addEdge(l1, l3, 6.4)
    g.addEdge(l1, l4, 6.0)
    g.addEdge(l1, l5, 4.8)
    g.addEdge(l1, l6, 1.6)
    g.addEdge(l1, l7, 2.8)
    g.addEdge(l1, l8, 4.8)
    g.addEdge(l1, l9, 6.3)
    g.addEdge(l1, l10, 7.3)
    g.addEdge(l1, l11, 5.3)
    g.addEdge(l1, l12, 4.8)
    g.addEdge(l1, l13, 3.0)
    g.addEdge(l1, l14, 4.6)
    g.addEdge(l1, l15, 4.5)
    g.addEdge(l1, l16, 7.4)
    g.addEdge(l1, l17, 6.0)
    g.addEdge(l1, l18, 5.0)
    g.addEdge(l1, l19, 4.8)
    g.addEdge(l1, l20, 9.5)
    g.addEdge(l1, l21, 10.9)
    g.addEdge(l1, l22, 8.3)
    g.addEdge(l1, l23, 6.9)
    g.addEdge(l1, l24, 10.0)
    g.addEdge(l1, l25, 4.4)
    g.addEdge(l1, l26, 13.0)

    g.addEdge(l2, l3, 9.2)
    g.addEdge(l2, l4, 4.4)
    g.addEdge(l2, l5, 2.8)
    g.addEdge(l2, l6, 8.6)
    g.addEdge(l2, l7, 6.3)
    g.addEdge(l2, l8, 5.3)
    g.addEdge(l2, l9, 1.6)
    g.addEdge(l2, l10, 10.4)
    g.addEdge(l2, l11, 3.0)
    g.addEdge(l2, l12, 5.3)
    g.addEdge(l2, l13, 6.5)
    g.addEdge(l2, l14, 5.6)
    g.addEdge(l2, l15, 5.8)
    g.addEdge(l2, l16, 5.7)
    g.addEdge(l2, l17, 4.1)
    g.addEdge(l2, l18, 3.6)
    g.addEdge(l2, l19, 4.3)
    g.addEdge(l2, l20, 3.3)
    g.addEdge(l2, l21, 5.0)
    g.addEdge(l2, l22, 6.1)
    g.addEdge(l2, l23, 9.7)
    g.addEdge(l2, l24, 6.1)
    g.addEdge(l2, l25, 2.8)
    g.addEdge(l2, l26, 7.4)

    g.addEdge(l3, l4, 5.6)
    g.addEdge(l3, l5, 6.9)
    g.addEdge(l3, l6, 8.6)
    g.addEdge(l3, l7, 4.0)
    g.addEdge(l3, l8, 11.1)
    g.addEdge(l3, l9, 7.3)
    g.addEdge(l3, l10, 1.0)
    g.addEdge(l3, l11, 6.4)
    g.addEdge(l3, l12, 11.1)
    g.addEdge(l3, l13, 3.9)
    g.addEdge(l3, l14, 4.3)
    g.addEdge(l3, l15, 4.4)
    g.addEdge(l3, l16, 7.2)
    g.addEdge(l3, l17, 5.3)
    g.addEdge(l3, l18, 6.0)
    g.addEdge(l3, l19, 10.6)
    g.addEdge(l3, l20, 5.9)
    g.addEdge(l3, l21, 7.4)
    g.addEdge(l3, l22, 4.7)
    g.addEdge(l3, l23, .6)
    g.addEdge(l3, l24, 6.4)
    g.addEdge(l3, l25, 10.1)
    g.addEdge(l3, l26, 10.1)

    g.addEdge(l4, l5, 1.9)
    g.addEdge(l4, l6, 7.9)
    g.addEdge(l4, l7, 5.1)
    g.addEdge(l4, l8, 7.5)
    g.addEdge(l4, l9, 2.6)
    g.addEdge(l4, l10, 6.5)
    g.addEdge(l4, l11, 1.5)
    g.addEdge(l4, l12, 7.5)
    g.addEdge(l4, l13, 3.2)
    g.addEdge(l4, l14, 2.4)
    g.addEdge(l4, l15, 2.7)
    g.addEdge(l4, l16, 1.4)
    g.addEdge(l4, l17, .5)
    g.addEdge(l4, l18, 1.7)
    g.addEdge(l4, l19, 6.5)
    g.addEdge(l4, l20, 3.2)
    g.addEdge(l4, l21, 5.2)
    g.addEdge(l4, l22, 2.5)
    g.addEdge(l4, l23, 6.0)
    g.addEdge(l4, l24, 4.2)
    g.addEdge(l4, l25, 5.4)
    g.addEdge(l4, l26, 5.5)

    g.addEdge(l5, l6, 6.3)
    g.addEdge(l5, l7, 4.3)
    g.addEdge(l5, l8, 4.5)
    g.addEdge(l5, l9, 1.5)
    g.addEdge(l5, l10, 8.7)
    g.addEdge(l5, l11, .8)
    g.addEdge(l5, l12, 4.5)
    g.addEdge(l5, l13, 3.9)
    g.addEdge(l5, l14, 3.0)
    g.addEdge(l5, l15, 3.8)
    g.addEdge(l5, l16, 5.7)
    g.addEdge(l5, l17, 1.9)
    g.addEdge(l5, l18, 1.1)
    g.addEdge(l5, l19, 3.5)
    g.addEdge(l5, l20, 4.9)
    g.addEdge(l5, l21, 6.9)
    g.addEdge(l5, l22, 4.2)
    g.addEdge(l5, l23, 9.0)
    g.addEdge(l5, l24, 5.9)
    g.addEdge(l5, l25, 3.5)
    g.addEdge(l5, l26, 7.2)

    g.addEdge(l6, l7, 4.0)
    g.addEdge(l6, l8, 4.2)
    g.addEdge(l6, l9, 8.0)
    g.addEdge(l6, l10, 8.6)
    g.addEdge(l6, l11, 6.9)
    g.addEdge(l6, l12, 4.2)
    g.addEdge(l6, l13, 4.2)
    g.addEdge(l6, l14, 8.0)
    g.addEdge(l6, l15, 5.8)
    g.addEdge(l6, l16, 7.2)
    g.addEdge(l6, l17, 7.7)
    g.addEdge(l6, l18, 6.6)
    g.addEdge(l6, l19, 3.2)
    g.addEdge(l6, l20, 11.2)
    g.addEdge(l6, l21, 12.7)
    g.addEdge(l6, l22, 10.0)
    g.addEdge(l6, l23, 8.2)
    g.addEdge(l6, l24, 11.7)
    g.addEdge(l6, l25, 5.1)
    g.addEdge(l6, l26, 14.2)

    g.addEdge(l7, l8, 7.7)
    g.addEdge(l7, l9, 9.3)
    g.addEdge(l7, l10, 4.6)
    g.addEdge(l7, l11, 4.8)
    g.addEdge(l7, l12, 7.7)
    g.addEdge(l7, l13, 1.6)
    g.addEdge(l7, l14, 3.3)
    g.addEdge(l7, l15, 3.4)
    g.addEdge(l7, l16, 3.1)
    g.addEdge(l7, l17, 5.1)
    g.addEdge(l7, l18, 4.6)
    g.addEdge(l7, l19, 6.7)
    g.addEdge(l7, l20, 8.1)
    g.addEdge(l7, l21, 10.4)
    g.addEdge(l7, l22, 7.8)
    g.addEdge(l7, l23, 4.2)
    g.addEdge(l7, l24, 9.5)
    g.addEdge(l7, l25, 6.2)
    g.addEdge(l7, l26, 10.7)

    g.addEdge(l8, l9, 4.8)
    g.addEdge(l8, l10, 11.9)
    g.addEdge(l8, l11, 4.7)
    g.addEdge(l8, l12, .6)
    g.addEdge(l8, l13, 7.6)
    g.addEdge(l8, l14, 7.8)
    g.addEdge(l8, l15, 6.6)
    g.addEdge(l8, l16, 7.2)
    g.addEdge(l8, l17, 5.9)
    g.addEdge(l8, l18, 5.4)
    g.addEdge(l8, l19, 1.0)
    g.addEdge(l8, l20, 8.5)
    g.addEdge(l8, l21, 10.3)
    g.addEdge(l8, l22, 7.8)
    g.addEdge(l8, l23, 11.5)
    g.addEdge(l8, l24, 9.5)
    g.addEdge(l8, l25, 2.8)
    g.addEdge(l8, l26, 14.1)

    g.addEdge(l9, l10, 9.4)
    g.addEdge(l9, l11, 1.1)
    g.addEdge(l9, l12, 5.1)
    g.addEdge(l9, l13, 4.6)
    g.addEdge(l9, l14, 3.7)
    g.addEdge(l9, l15, 4.0)
    g.addEdge(l9, l16, 6.7)
    g.addEdge(l9, l17, 2.3)
    g.addEdge(l9, l18, 1.8)
    g.addEdge(l9, l19, 4.1)
    g.addEdge(l9, l20, 3.8)
    g.addEdge(l9, l21, 5.8)
    g.addEdge(l9, l22, 4.3)
    g.addEdge(l9, l23, 7.8)
    g.addEdge(l9, l24, 4.8)
    g.addEdge(l9, l25, 3.2)
    g.addEdge(l9, l26, 6.0)

    g.addEdge(l10, l11, 7.3)
    g.addEdge(l10, l12, 12.0)
    g.addEdge(l10, l13, 4.9)
    g.addEdge(l10, l14, 5.2)
    g.addEdge(l10, l15, 5.4)
    g.addEdge(l10, l16, 8.1)
    g.addEdge(l10, l17, 6.2)
    g.addEdge(l10, l18, 6.9)
    g.addEdge(l10, l19, 11.5)
    g.addEdge(l10, l20, 6.9)
    g.addEdge(l10, l21, 8.3)
    g.addEdge(l10, l22, 4.1)
    g.addEdge(l10, l23, .4)
    g.addEdge(l10, l24, 4.9)
    g.addEdge(l10, l25, 11.0)
    g.addEdge(l10, l26, 6.8)

    g.addEdge(l11, l12, 4.7)
    g.addEdge(l11, l13, 3.5)
    g.addEdge(l11, l14, 2.6)
    g.addEdge(l11, l15, 2.9)
    g.addEdge(l11, l16, 6.3)
    g.addEdge(l11, l17, 1.2)
    g.addEdge(l11, l18, 1.0)
    g.addEdge(l11, l19, 3.7)
    g.addEdge(l11, l20, 4.1)
    g.addEdge(l11, l21, 6.2)
    g.addEdge(l11, l22, 3.4)
    g.addEdge(l11, l23, 6.9)
    g.addEdge(l11, l24, 5.2)
    g.addEdge(l11, l25, 3.7)
    g.addEdge(l11, l26, 6.4)

    g.addEdge(l12, l13, 7.3)
    g.addEdge(l12, l14, 7.8)
    g.addEdge(l12, l15, 6.6)
    g.addEdge(l12, l16, 7.2)
    g.addEdge(l12, l17, 5.9)
    g.addEdge(l12, l18, 5.4)
    g.addEdge(l12, l19, 1.0)
    g.addEdge(l12, l20, 8.5)
    g.addEdge(l12, l21, 10.3)
    g.addEdge(l12, l22, 7.8)
    g.addEdge(l12, l23, 11.5)
    g.addEdge(l12, l24, 9.5)
    g.addEdge(l12, l25, 2.8)
    g.addEdge(l12, l26, 14.1)

    g.addEdge(l13, l14, 1.3)
    g.addEdge(l13, l15, 1.5)
    g.addEdge(l13, l16, 4.0)
    g.addEdge(l13, l17, 3.2)
    g.addEdge(l13, l18, 3.0)
    g.addEdge(l13, l19, 6.9)
    g.addEdge(l13, l20, 6.2)
    g.addEdge(l13, l21, 8.2)
    g.addEdge(l13, l22, 5.5)
    g.addEdge(l13, l23, 4.4)
    g.addEdge(l13, l24, 7.2)
    g.addEdge(l13, l25, 6.4)
    g.addEdge(l13, l26, 10.5)

    g.addEdge(l14, l15, .6)
    g.addEdge(l14, l16, 6.4)
    g.addEdge(l14, l17, 2.4)
    g.addEdge(l14, l18, 2.2)
    g.addEdge(l14, l19, 6.8)
    g.addEdge(l14, l20, 5.3)
    g.addEdge(l14, l21, 7.4)
    g.addEdge(l14, l22, 4.6)
    g.addEdge(l14, l23, 4.8)
    g.addEdge(l14, l24, 6.3)
    g.addEdge(l14, l25, 6.5)
    g.addEdge(l14, l26, 8.8)

    g.addEdge(l15, l16, 5.6)
    g.addEdge(l15, l17, 1.6)
    g.addEdge(l15, l18, 1.7)
    g.addEdge(l15, l19, 6.4)
    g.addEdge(l15, l20, 4.9)
    g.addEdge(l15, l21, 6.9)
    g.addEdge(l15, l22, 4.2)
    g.addEdge(l15, l23, 5.6)
    g.addEdge(l15, l24, 5.9)
    g.addEdge(l15, l25, 5.7)
    g.addEdge(l15, l26, 8.4)

    g.addEdge(l16, l17, 7.1)
    g.addEdge(l16, l18, 6.1)
    g.addEdge(l16, l19, 7.2)
    g.addEdge(l16, l20, 10.6)
    g.addEdge(l16, l21, 12.0)
    g.addEdge(l16, l22, 9.4)
    g.addEdge(l16, l23, 7.5)
    g.addEdge(l16, l24, 11.1)
    g.addEdge(l16, l25, 6.2)
    g.addEdge(l16, l26, 13.6)

    g.addEdge(l17, l18, 1.6)
    g.addEdge(l17, l19, 4.9)
    g.addEdge(l17, l20, 3.0)
    g.addEdge(l17, l21, 5.0)
    g.addEdge(l17, l22, 2.3)
    g.addEdge(l17, l23, 5.5)
    g.addEdge(l17, l24, 4.0)
    g.addEdge(l17, l25, 5.1)
    g.addEdge(l17, l26, 5.2)

    g.addEdge(l18, l19, 4.4)
    g.addEdge(l18, l20, 4.6)
    g.addEdge(l18, l21, 6.6)
    g.addEdge(l18, l22, 3.9)
    g.addEdge(l18, l23, 6.5)
    g.addEdge(l18, l24, 5.6)
    g.addEdge(l18, l25, 4.3)
    g.addEdge(l18, l26, 6.9)

    g.addEdge(l19, l20, 7.5)
    g.addEdge(l19, l21, 9.3)
    g.addEdge(l19, l22, 6.8)
    g.addEdge(l19, l23, 11.4)
    g.addEdge(l19, l24, 8.5)
    g.addEdge(l19, l25, 1.8)
    g.addEdge(l19, l26, 13.1)

    g.addEdge(l20, l21, 2.0)
    g.addEdge(l20, l22, 2.9)
    g.addEdge(l20, l23, 6.4)
    g.addEdge(l20, l24, 2.8)
    g.addEdge(l20, l25, 6.0)
    g.addEdge(l20, l26, 4.1)

    g.addEdge(l21, l22, 4.4)
    g.addEdge(l21, l23, 7.9)
    g.addEdge(l21, l24, 3.4)
    g.addEdge(l21, l25, 7.9)
    g.addEdge(l21, l26, 4.7)

    g.addEdge(l22, l23, 4.5)
    g.addEdge(l22, l24, 1.7)
    g.addEdge(l22, l25, 6.8)
    g.addEdge(l22, l26, 3.1)

    g.addEdge(l23, l24, 5.4)
    g.addEdge(l23, l25, 10.6)
    g.addEdge(l23, l26, 7.8)

    g.addEdge(l24, l25, 7.0)
    g.addEdge(l24, l26, 1.3)

    g.addEdge(l25, l26, 8.3)

    return g


# Hard-coded hash table
def getHash():
    packageHash = Hash(40)

    packageHash.insert(Parcel(1, 5, (10, 30), "SLC", "84115", 21, "undelivered"))
    packageHash.insert(Parcel(2, 9, (17, 0), "SLC", "84106", 44, "undelivered"))
    packageHash.insert(Parcel(3, 8, (17, 0), "SLC", "84103", 2, "undelivered"))
    packageHash.insert(Parcel(4, 18, (17, 0), "SLC", "84115", 4, "undelivered"))
    packageHash.insert(Parcel(5, 19, (17, 0), "SLC", "84111", 5, "undelivered"))
    packageHash.insert(Parcel(6, 13, (10, 30), "W Valley", "84119", 88, "undelivered"))
    packageHash.insert(Parcel(7, 2, (17, 0), "SLC", "84106", 8, "undelivered"))
    packageHash.insert(Parcel(8, 12, (17, 0), "SLC", "84103", 9, "undelivered"))
    packageHash.insert(Parcel(9, 19, (17, 0), "SLC", "84103", 2, "undelivered"))  # Wrong address
    packageHash.insert(Parcel(10, 25, (17, 0), "SLC", "84105", 1, "undelivered"))
    packageHash.insert(Parcel(11, 10, (17, 0), "SLC", "84118", 1, "undelivered"))
    packageHash.insert(Parcel(12, 16, (17, 0), "W Valley", "84119", 1, "undelivered"))
    packageHash.insert(Parcel(13, 6, (10, 30), "SLC", "84104", 2, "undelivered"))
    packageHash.insert(Parcel(14, 20, (10, 30), "MillCreek", "84117", 88, "undelivered"))
    packageHash.insert(Parcel(15, 21, (9, 0), "Holladay", "84117", 4, "undelivered"))
    packageHash.insert(Parcel(16, 21, (10, 30), "Holladay", "84117", 88, "undelivered"))
    packageHash.insert(Parcel(17, 14, (17, 0), "SLC", "84119", 2, "undelivered"))
    packageHash.insert(Parcel(18, 3, (17, 0), "SLC", "84123", 6, "undelivered"))
    packageHash.insert(Parcel(19, 4, (17, 0), "SLC", "84115", 37, "undelivered"))
    packageHash.insert(Parcel(20, 17, (10, 30), "SLC", "84115", 37, "undelivered"))
    packageHash.insert(Parcel(21, 17, (17, 0), "SLC", "84115", 3, "undelivered"))
    packageHash.insert(Parcel(22, 26, (17, 0), "Murray", "84121", 2, "undelivered"))
    packageHash.insert(Parcel(23, 23, (17, 0), "SLC", "84118", 5, "undelivered"))
    packageHash.insert(Parcel(24, 22, (17, 0), "Murray", "84107", 7, "undelivered"))
    packageHash.insert(Parcel(25, 24, (10, 30), "SLC", "84117", 7, "undelivered"))
    packageHash.insert(Parcel(26, 24, (17, 0), "SLC", "84117", 25, "undelivered"))
    packageHash.insert(Parcel(27, 1, (17, 0), "SLC", "84104", 5, "undelivered"))
    packageHash.insert(Parcel(28, 11, (17, 0), "SLC", "84115", 7, "undelivered"))
    packageHash.insert(Parcel(29, 2, (10, 30), "SLC", "84106", 2, "undelivered"))
    packageHash.insert(Parcel(30, 12, (10, 30), "SLC", "84103", 1, "undelivered"))
    packageHash.insert(Parcel(31, 15, (10, 30), "SLC", "84119", 1, "undelivered"))
    packageHash.insert(Parcel(32, 15, (17, 0), "SLC", "84119", 1, "undelivered"))
    packageHash.insert(Parcel(33, 9, (17, 0), "SLC", "84106", 1, "undelivered"))
    packageHash.insert(Parcel(34, 21, (10, 30), "Holladay", "84117", 2, "undelivered"))
    packageHash.insert(Parcel(35, 1, (17, 0), "SLC", "84104", 88, "undelivered"))
    packageHash.insert(Parcel(36, 7, (17, 0), "W Valley", "84119", 88, "undelivered"))
    packageHash.insert(Parcel(37, 19, (10, 30), "SLC", "84111", 2, "undelivered"))
    packageHash.insert(Parcel(38, 19, (17, 0), "SLC", "84111", 9, "undelivered"))
    packageHash.insert(Parcel(39, 6, (17, 0), "SLC", "84104", 9, "undelivered"))
    packageHash.insert(Parcel(40, 18, (10, 30), "SLC", "84115", 45, "undelivered"))

    return packageHash


def main(argv):
    # Initialize the packages and graph to be used throughout the program
    packageHash = getHash()
    g = createGraph()

    print("___________________________________________________")
    print("Welcome to the WGUPS parcel calculator!")
    print("___________________________________________________")
    print()
    print("To view the status of all packages, include the hour and minutes as two separate cmd line arguments.")
    print()
    print("eg. main.py 8 30")
    print("This will display the status of all packages at 8:30")
    print()
    print("To view the status of a single package, include the package id number as a third argument.")
    print()
    print("eg. main.py 11 45 8")
    print("This will display the status of package 8 at 11:45")
    print("___________________________________________________")
    print()
    print()

    # The program will take 3 command line args: Hours, minutes and packages
    # Hours and minutes will determine the time at which package statuses will be printed to the terminal
    # Packages will be a list of packages to print. The default will be all packages
    if len(argv) >= 2:
        displayTime = parcel.timeClock(int(argv[0]), int(argv[1]))
        displayPackage = [x.idNumber for x in packageHash.hashTable]

    if len(argv) == 3:
        displayPackage = [int(argv[2])]

    elif len(argv) > 3 or (len(argv) < 2 and len(argv) != 0):
        print("cmd line args are: Hours, Minutes, Package.")
        print("To view all packages, exclude Package from cmd line args.")
        return -1

    elif len(argv) == 0:
        displayPackage = None
        displayTime = None

    if len(argv) != 0:
        print("Status to be shown at : ", displayTime)
        print("Package to be displayed: ", displayPackage)
        print()
        print()

    # All trucks are loaded with the packages that they are required to have given the assignment parameters
    truck1 = parcel.Truck([15, 13, 14, 16, 19, 20], packageHash, "T1")
    truck2 = parcel.Truck([3, 18, 36, 38], packageHash, "T2")
    truck3 = parcel.Truck([6, 25, 28, 32], packageHash, "T3")

    # These are the packages without delivery deadlines
    lowPriority = [2, 4, 5, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27, 33, 35, 39]

    # These are the packages that aren't pre-loaded or  low priority
    remainingPackages = [i for i in range(1, 41) if
                         i not in truck1.packages and i not in truck2.packages and i not in truck3.packages and i not in lowPriority]

    # Trucks 1 and 2 are loaded with packages according to time requirements and distance
    parcel.greedyTruck(g, [truck1, truck2, truck1], remainingPackages, lowPriority, packageHash)

    # Get a shortest path for the remaining low priority packages
    lowPriorityNodes = parcel.getNodes(lowPriority, packageHash)
    lowPriorityNodes = graph.tsp(g, lowPriorityNodes)[1]

    # Low priority packages are loaded onto trucks 2 and 3
    parcel.linkLowPriority(g, [truck3, truck2], lowPriority, lowPriorityNodes, packageHash)

    parcel.getBestPath(g, [truck1, truck2, truck3], packageHash)

    # Makes sure that no packages have inadvertently been marked as delivered
    for package in packageHash.hashTable:
        package.status = "undelivered"
        package.deliveryTime = parcel.timeClock(0, 0)

    printed = [x.idNumber for x in packageHash.hashTable if x.idNumber not in truck3.packages]

    # If truck 3 has any packages, truck 1 will need to return to the depot before truck 3 can deliver packages.
    if len(truck3.packages) > 0:
        truck1.nodes.append(0)

    #
    # The next block of code is where packages are delivered to their destinations
    time = parcel.timeClock(8, 0)
    t1Distance = parcel.deliverPackages(g, truck1, packageHash, time, printed, displayTime, displayPackage)

    parcel.getBestPath(g, [truck2, truck3], packageHash)
    t2Distance = parcel.deliverPackages(g, truck2, packageHash, time, printed, displayTime, displayPackage)

    printed = [x.idNumber for x in packageHash.hashTable if x.idNumber in truck3.packages]
    for package in packageHash.hashTable:
        if package.deliveryTruck == "T3":
            package.status = "undelivered"
            package.deliveryTime = parcel.timeClock(0, 0)

    time.setTime(9, 5)
    t3Distance = parcel.deliverPackages(g, truck3, packageHash, time, printed, displayTime, displayPackage)

    distance = t1Distance + t2Distance + t3Distance

    if displayTime and displayTime > time:
        print("All packages have been delivered by ", time)
        print()
        print("_______________________________")
        print("               TIME: ", time)
        print("_______________________________")
        parcel.printPackages(packageHash, printed=[i.idNumber for i in packageHash.hashTable])

    print()
    print("Truck 1 distance: ", t1Distance)
    print("Truck 1 path: ", truck1.nodes)
    print("Truck 1 packages: ", truck1.packages)
    print()

    print("Truck 2 distance: ", t2Distance)
    print("Truck 2 path: ", truck2.nodes)
    print("Truck 2 packages: ", truck2.packages)
    print()

    print("Truck 3 distance: ", t3Distance)
    print("Truck 3 path: ", truck3.nodes)
    print("Truck 3 packages: ", truck3.packages)
    print()

    print("Final Distance: ", distance)
    print("Time completed: ", time)
    print("_______________________________")
    print()

    return distance


if __name__ == "__main__":

    def cls():
        os.system('cls')


    while True:
        cls()
        final = main(sys.argv[1:])
        if final < 110:
            break

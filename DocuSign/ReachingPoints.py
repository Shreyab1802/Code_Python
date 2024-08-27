from coordinateProblem import gcd


class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if sx == tx and sy == ty: return True
            if tx > ty:
                tx -= ty
            else:
                ty -= tx
        return False


####### Better Solution #########


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:

        if (g := gcd(sx, sy)) != gcd(tx, ty): return False
        (sx, sy), (tx, ty) = (sx // g, sy // g), (tx // g, ty // g)

        while tx > sx and ty > sy: (tx, ty) = (tx % ty, ty % tx)

        return ((tx, ty % sx) == (sx, sy % sx) and ty >= sy) or (
                (tx % sy, ty) == (sx % sy, sy) and tx >= sx)
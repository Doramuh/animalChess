# unittest for Python 
import unittest
import model

class Testing(unittest.TestCase):

    # to test the movement of the pieces
    def test_pieceMove(self): 
        rat = model.pieces("rat", 1, 1, "a1")
        rat.move("a2")
        self.assertEqual(rat.position, "a2")

    # to test piece capture
    def test_pieceCaptrue(self):
        cat=model.piece("cat",2,2,"a2")
        rat=model.piece("rat",1,1,"a1")
        self.assertEqual(cat.capture("a1"),"a1")

    # test if rat can go into river
    def test_piecerat(self):
        rat=model.piece("rat",1,1,"b3")
        rat.move("b4")
        self.assertEqual(rat.position,"b4")

    # test if rat can capture elephant
    def test_ratelephant(self):
        elephant=model.piece("elephant",8,2,"a2")
        rat=model.piece("rat",1,1,"a1")
        self.assertEqual(rat.captrue("a2"),"a1")

    # test if rat can not capture rat from land to water
    def test6(self):
        rat1 = model.pieces("rat",1,1,"b4")
        rat2 = model.pieces("rat",2,2,"b3")
        rat1.capture("b3")
        self.assertEqual(rat1.position,"b4")

    # test if rat can capture in water
    def test7(self):
        rat1 = model.pieces("rat",1,1,"b4")
        rat2 = model.pieces("rat",2,2,"b5")
        rat1.capture("b5")
        self.assertEqual(rat1.position,"b5")
    
    # test if lion or tiger can jump over water
    def test8(self):
        lion = model.pieces("lion",1,1"b3")
        lion.move("b7")
        self.assertEqual(lion.position,"b7")
    
    # test if lion will be blocked by rat in water
    def test9(self):
        lion = model.pieces("lion",1,1,"b3")
        rat = model.pieces("rat",2,2,"b4")
        lion.move("b7")
        self.assertEqual(lion.position,"b3")

    # to test if lion and tiger can jump and capture at the same time
    def test_lionTigerJumpingCapture(self):
        lion = model.pieces("lion", 7, 1, "b3")
        rat = model.pieces("rat", 1, 2, "b7")
        lion.capture("b7")
        self.assertEqual(lion.position, "b7")

    # to test the trap capture regardless of capture rank
    def test_trapCapture(self):
        rat = model.pieces("rat", 1, 1 "c2")
        cat = model.pieces("cat", 2, 2, "c1")
        rat.capture("c1")
        self.assertEqual(rat.position, "c1")
    
    # to test the game if it is over
    def test_gameEnd(self):
        logic = model.logic()
        rat = model.pieces("rat", 1, 1 "c9")
        rat.move("d9")
        self.assertTrue(logic.end)

if __name__ == '__main__': 
    unittest.main()

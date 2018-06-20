import unittest

from BAliBASEProcesser import AlignAnalizer
import os


class TestMethods(unittest.TestCase):
    # Check that gives an exception for a wrong name
    def test_read_and_process_max_balibase_throw_error_wrong_file(self):
        self.align = AlignAnalizer('BB1101', False)
        with self.assertRaises(Exception):
            self.align.read_and_process_max_balibase()

    def test_read_and_process_min_balibase_throw_error_wrong_file(self):
        self.align = AlignAnalizer('BB1101', False)
        with self.assertRaises(Exception):
            self.align.read_and_process_min_balibase()

    # If there are both none, none is giving an exception
    def test_lower_case_ID_max_ok(self):
        self.align = AlignAnalizer('bb11001', False)
        self.align1 = AlignAnalizer('BB11001', False)
        res = self.align.read_and_process_max_balibase()
        res1 = self.align.read_and_process_max_balibase()
        self.assertEqual(res, res1)

    def test_lower_case_ID_max_ok_1(self):
        self.align = AlignAnalizer('BB11001', False)
        self.align1 = AlignAnalizer('bB11001', False)
        res = self.align.read_and_process_max_balibase()
        res1 = self.align.read_and_process_max_balibase()
        self.assertEqual(res, res1)

    def test_lower_case_ID_max_ok_2(self):
        self.align = AlignAnalizer('Bb11001', False)
        self.align1 = AlignAnalizer('bB11001', False)
        res = self.align.read_and_process_max_balibase()
        res1 = self.align1.read_and_process_max_balibase()
        self.assertEqual(res, res1)

    def test_lower_case_ID_min_ok(self):
        self.align = AlignAnalizer('bb11001', False)
        self.align1 = AlignAnalizer('BB11001', False)
        res = self.align.read_and_process_min_balibase()
        res1 = self.align1.read_and_process_min_balibase()
        self.assertEqual(res, res1)

    def test_lower_case_ID_min_ok_1(self):
        self.align = AlignAnalizer('BB11001', False)
        self.align1 = AlignAnalizer('bB11001', False)
        res = self.align.read_and_process_min_balibase()
        res1 = self.align1.read_and_process_min_balibase()
        self.assertEqual(res, res1)

    def test_lower_case_ID_min_ok_2(self):
        self.align = AlignAnalizer('Bb11001', False)
        self.align1 = AlignAnalizer('bB11001', False)
        res = self.align.read_and_process_min_balibase()
        res1 = self.align.read_and_process_min_balibase()
        self.assertEqual(res, res1)

    #Finally we are going to check that the files are created correctly
    def test_file_FUN_or_VAR_doesnt_exist_root(self):
        self.align = AlignAnalizer('Bb11002', False)
        with self.assertRaises(Exception):
            self.align.read_and_process_max_balibase()
    def test_files_best_seq_created(self):
        self.align = AlignAnalizer('Bb11001', False)
        self.align.read_and_process_max_balibase()
        r1 = os.path.isfile('/results/Best_sp_seq.txt')
        r2 = os.path.isfile('/results/Best_strike_seq.txt')
        r3 = os.path.isfile('/results/Best_tc_seq.txt')
        self.assertEqual(r1, r2)
        self.assertEqual(r3, r2)

    def test_files_best_value_created(self):
        self.align = AlignAnalizer('Bb11001', False)
        self.align.read_and_process_max_balibase()
        r1 = os.path.isfile('/results/Best_sp_value.txt')
        r2 = os.path.isfile('/results/Best_strike_value.txt')
        r3 = os.path.isfile('/results/Best_tc_value.txt')
        self.assertEqual(r1, r2)
        self.assertEqual(r3, r2)

    def test_files_worse_seq_created(self):
        self.align = AlignAnalizer('Bb11001', False)
        self.align.read_and_process_max_balibase()
        r1 = os.path.isfile('/results/Worse_sp_seq.txt')
        r2 = os.path.isfile('/results/Worse_strike_seq.txt')
        r3 = os.path.isfile('/results/Worse_tc_seq.txt')
        self.assertEqual(r1, r2)
        self.assertEqual(r3, r2)

    def test_files_worse_seq_created(self):
        self.align = AlignAnalizer('Bb11001', False)
        self.align.read_and_process_max_balibase()
        r1 = os.path.isfile('/results/Worse_sp_value.txt')
        r2 = os.path.isfile('/results/Worse_strike_value.txt')
        r3 = os.path.isfile('/results/Worse_tc_value.txt')
        self.assertEqual(r1, r2)
        self.assertEqual(r3, r2)

    def tearDown(self):
        print("Test passed correctly")

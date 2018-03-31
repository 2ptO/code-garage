import unittest
import time
import os
import q42

class TestQ42(unittest.TestCase):
    def setUp(self):
        # Create three files to test
        self.test_files = ["file1.py", "file2.py", "file3.py"]
        # Create duplicate files for the first two files
        self.dup_files = ["dup_" + file for file in self.test_files[:2]]
        self.working_dir = os.getcwd() + "/temp_for_q42/"
        os.makedirs(self.working_dir)

    def tearDown(self):
        for test_file in self.test_files + self.dup_files:
            os.remove(os.path.join(self.working_dir, test_file))
        os.removedirs(self.working_dir)
    
    def test_dup_files(self):
        for test_file in self.test_files:
            with open(os.path.join(self.working_dir, test_file), "w+") as f:
                f.write("print({} says Hello, world)".format(test_file))
                # Artifical sleep to differentiate creation time
                time.sleep(1)
                f.close()

        
        for test_file in self.dup_files:
            with open(os.path.join(self.working_dir, test_file), "w+") as f:
                f.write("print({} says Hello, world)".format(test_file))
                time.sleep(1)
                f.close()

        # Verify duplicates
        exp_duped_files = set()
        exp_duped_files.add((os.path.join(self.working_dir,"dup_file1.py"),
                                os.path.join(self.working_dir,"file1.py")))
        exp_duped_files.add((os.path.join(self.working_dir,"dup_file2.py"),
                                os.path.join(self.working_dir,"file2.py")))
        act_dup_files = q42.find_duped_files(self.working_dir)
        for dup_file in act_dup_files:
            self.assertIn(dup_file, exp_duped_files)

            


    
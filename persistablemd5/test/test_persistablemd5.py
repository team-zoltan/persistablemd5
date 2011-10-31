# -*- coding: utf-8 -*-
"""
test_persistablemd5.py

test the PersistableMD5 object
"""
import hashlib
import unittest

from persistablemd5.persistablemd5 import PersistableMD5


class TestPersistableMD5(unittest.TestCase):
    """
    Test perisistable md5 object
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_simple_create(self):
        """
        test simply creating a PersistableMD5
        """
        md5 = PersistableMD5()

    def test_loads_state_from_getstate_output(self):
        """
        test that __setstate__ handles the output of __getstate__
        """
        test_string = "a short test string"
        md5 = PersistableMD5(test_string)
        state = md5.__getstate__()
        new_md5 = PersistableMD5()
        new_md5.__setstate__(state)
        self.assertEqual(new_md5.digest(), md5.digest())

    def test_digest_matches_standard_library_md5(self):
        """
        test that a simple update producs the same digest as the python
        standard library md5 module
        """
        test_string = "a short test string"
        standard_md5 = hashlib.md5()
        md5 = PersistableMD5()

        standard_md5.update(test_string)
        md5.update(test_string)

        self.assertEqual(md5.digest(), standard_md5.digest())

    def test_takes_an_initial_argument(self):
        """
        handles an initial argument just as the standard md5 would
        """
        test_string = "a short test string"
        standard_md5 = hashlib.md5(test_string)
        md5 = PersistableMD5(test_string)

        self.assertEqual(md5.digest(), standard_md5.digest())


    def test_restored_object_can_be_updated_further(self):
        """
        make sure that an object can have data added to it after it has been restored
        """
        md5 = PersistableMD5()
        md5.update('some data')
        state = md5.__getstate__()
        new_md5 = PersistableMD5()
        new_md5.__setstate__(state)
        new_md5.update(' more data')
        check_md5 = hashlib.md5('some data more data')
        self.assertEqual(new_md5.digest(), check_md5.digest())


if __name__ == '__main__':
    unittest.main()

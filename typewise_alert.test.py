import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    self.assertTrue((typewise_alert.infer_breach(60, 30, 50) == 'TOO_HIGH')
    self.assertTrue((typewise_alert.infer_breach(20, 20, 20) == 'NORMAL')



if __name__ == '__main__':
  unittest.main()

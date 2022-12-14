import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(60, 30, 50) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.infer_breach(20, 20, 20) == 'NORMAL')
    
  #def test_classify_temperature_breach(self):
    #self.assertTrue(typewise_alert.Passive.classify_temperature_breach('PASSIVE-COOLING',20) == 'NORMAL')
    #self.assertTrue(typewise_alert.Passive.classify_temperature_breach('PASSIVE-COOLING',40) == 'TOO-HIGH')
    #self.assertTrue(typewise_alert.Active.classify_temperature_breach('ACTIVE-COOLING',50) == 'TOO-HIGH')
    #self.assertTrue(typewise_alert.Active.classify_temperature_breach('ACTIVE-COOLING',45) == 'NORMAL')
    #self.assertTrue(typewise_alert.Med.classify_temperature_breach('ACTIVE-COOLING',40) == 'NORMAL')
    

  #def test_send_to_email(self):
    #self.assertTrue(typewise_alert.send_to_email('TOO_LOW') == 'Hi, the temperature is too low')
    #self.assertTrue(typewise_alert.send_to_email('TOO_HIGH') == 'Hi, the temperature is too high')
    
if __name__ == '__main__':
  unittest.main()

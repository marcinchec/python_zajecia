# def funkcja():
#     logging.info("Start")
import dziewiate_zajecia
class Testy(object):
    def test_answer_type(self):
        assert isinstance(dziewiate_zajecia.num2text(1),basestring)
    def test_zero(self):
        assert dziewiate_zajecia.num2text(0)=='zero'
    def test_jeden(self):
        assert dziewiate_zajecia.num2text(1)=='jeden'
    def test_dwa(self):
        assert dziewiate_zajecia.num2text(2)=='dwa'
from base import Base

class TestClassDemo(Base):
    value = 0

    def test_one(self):
        self.value = 1
        self.check_value(self.value, 1)

    def test_two(self):
        self.check_value(self.value, 1)

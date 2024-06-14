class TestClassDemo:
    value = 0

    def test_qa_date(self, env, date_column):
        assert env == "qa"
        assert date_column == "load_date"

    # fixtures can be provided in any order
    def test_date_qa(self, date_column, env):
        assert env == "qa"
        assert date_column == "load_date"

    def test_uat(self, env):
        assert env == "uat"

    def test_qa(self, env):
        assert env == "qa"

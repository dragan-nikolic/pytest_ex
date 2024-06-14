import pytest

# td.sf.config.user
# td.sf.data.idh-t_ddo-period_flash_comp_sales

class TestClassDemo:
    def test_env(self, td):
        print(td)
        assert td['sf_user'] == 'dragan'
        


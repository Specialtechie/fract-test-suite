import pytest

@pytest.mark.usefixtures("init_driver")
class TestLogin:

    def test_open_site(self):
        self.driver.get("https://example.com")
        assert "Example Domain" in self.driver.title
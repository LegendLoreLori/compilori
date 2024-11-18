import pytest
from src import driver


class TestPreprocess:
    def test_preprocess_does_not_explode(self, source_dir):
        assert driver.preprocess(source_dir) == "int main(void) {\nreturn 2;\n}"


class TestLex:
    @pytest.mark.parametrize(
        "source_content",
        [
            "main () {\n int; }",
            "foo bar;\nfoobar ;",
            "int 1;",
            "void",
            "return a; }",
        ],
    )
    def test_lex_valid_input(self, source_content):
        assert isinstance(driver.lex(source_content), list)

    @pytest.mark.xfail(raises=ValueError, strict=True)
    @pytest.mark.parametrize(
        "source_content",
        ["1a;", "main(){};\n", "", "-", "==", "@", ",", "'", '"', "?", "/", "|", "&&"],
    )
    def test_lex_raise_on_invalid_input(self, source_content):
        assert isinstance(driver.lex(source_content), list)

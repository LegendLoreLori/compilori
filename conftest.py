import pytest

CONTENT = "int main(void) {\nreturn 2;\n}\n"


@pytest.fixture(scope="session")
def source_dir(tmp_path_factory):
    """store temporary .c source files to operate on"""
    path = tmp_path_factory.mktemp("tmp_data") / "source.c"
    path.write_text(CONTENT, encoding="utf-8")
    return path

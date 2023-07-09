from setuptools import setup, find_packages

import pathlib
__version__ = "1.0.0"

setup(
    name="qml_element",
    version=__version__,
    author="林柏君",
    author_email="1355767057@qq.com",
    description="仿element ui样式风格的qml组件库",
    packages=find_packages(),
    package_data={
        "componentLib": [i.as_posix() for i in filter(
            lambda f:f.is_file(), pathlib.Path("qml_element/componentLib").rglob("*"))]
    },
    include_package_data=True
)

from setuptools import find_packages, setup

setup(
    name="dream-engine",
    version="0.2.0",
    description="Persistencia de patrones durante el sueño artificial",
    author="Laboratorio Halden de Conciencia Sintética",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.7",
)

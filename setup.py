"""
Setup script for Humsafar Financial AI Assistant
"""

from setuptools import setup, find_packages

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="humsafar-financial-ai-assistant",
    version="1.0.0",
    author="Akshay Kumar Bedre",
    author_email="your.email@example.com",
    description="A comprehensive suite of financial calculators for AI-powered financial decision making",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akshaykumarbedre/humsafar-financial-ai-assistant",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        # No external dependencies required - uses only Python standard library
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.9",
            "mypy>=0.910",
        ],
    },
    entry_points={
        "console_scripts": [
            "humsafar-calc=humsafar_financial_ai.finance_calculators:main",
        ],
    },
    keywords="finance calculator loan emi investment mutual-fund ppf nps ai mcp",
    project_urls={
        "Bug Reports": "https://github.com/akshaykumarbedre/humsafar-financial-ai-assistant/issues",
        "Source": "https://github.com/akshaykumarbedre/humsafar-financial-ai-assistant",
    },
)
#!/usr/bin/env python
import pytest

"""Tests for `python_sample` package."""

# from python_sample import python_sample


@pytest.fixture
def response():
  """Sample pytest fixture.

  See more at: http://doc.pytest.org/en/latest/fixture.html
  """
  # import requests
  # return requests.get('https://github.com/audreyfeldroy/cookiecutter-pypackage')


def test_content(response):
  """Sample pytest test function with the pytest fixture as an argument."""
  # from bs4 import BeautifulSoup
  # assert 'GitHub' in BeautifulSoup(response.content).title.string
  assert 1 == 1

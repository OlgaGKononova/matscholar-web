import unittest

import matscholar_web.search.view as msweb_view
from matscholar_web.constants import valid_search_filters
from matscholar_web.tests.util import (
    MatScholarWebBaseTest,
    elastic_host_defined,
)

"""
Tests for the main search view.
"""

# Functions to exclude from this test
EXCLUDE = ["guided_search_box_elastic_html"]


class TestSearchViews(MatScholarWebBaseTest):
    def test_search_view(self):
        self.run_test_for_all_functions_in_module(msweb_view, EXCLUDE)

    @unittest.skipIf(not elastic_host_defined, "Elastic credentials invalid.")
    def test_guided_search_box_elastic_html(self):
        f = msweb_view.guided_search_box_elastic_html
        arg_combos = [(v,) for v in valid_search_filters]
        self.run_test_for_individual_arg_combos(f, arg_combos)

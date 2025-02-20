from __future__ import absolute_import

from unittest import TestCase

from plotly.session import (update_session_plot_options, SHARING_OPTIONS,
                            _session)
from plotly.exceptions import PlotlyError


class TestSession(TestCase):

    def test_update_session_plot_options_invalid_sharing_argument(self):

        # Return PlotlyError when sharing arguement is not
        # 'public', 'private' or 'secret'

        kwargs = {'sharing': 'priva'}
        self.assertRaises(PlotlyError, update_session_plot_options, **kwargs)

    def test_update_session_plot_options_valid_sharing_argument(self):

        # _session['plot_options'] should contain sharing key after
        # update_session_plot_options is called by correct arguments
        # 'public, 'private' or 'secret'

        for key in SHARING_OPTIONS:
            kwargs = {'sharing': key}
            update_session_plot_options(**kwargs)
            self.assertEqual(_session['plot_options'], kwargs)

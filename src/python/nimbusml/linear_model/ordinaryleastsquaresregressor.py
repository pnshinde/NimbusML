# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
OrdinaryLeastSquaresRegressor
"""

__all__ = ["OrdinaryLeastSquaresRegressor"]


from sklearn.base import RegressorMixin

from ..base_predictor import BasePredictor
from ..internal.core.linear_model.ordinaryleastsquaresregressor import \
    OrdinaryLeastSquaresRegressor as core
from ..internal.utils.utils import trace


class OrdinaryLeastSquaresRegressor(
        core, BasePredictor, RegressorMixin):
    """

    Train an OLS regression model

    .. remarks::
        `Ordinary least squares (OLS)
        <https://en.wikipedia.org/wiki/Ordinary_least_squares>`_ is a
        parameterized
        regression method. It assumes that the conditional mean of the
        dependent variable follows a linear function of
        the dependent variables. By minimizing the squares of the difference
        between observed values and the
        predictions, the parameters of the regressor can be estimated.


        **Reference**

            `Ordinary least squares (OLS)
            <https://en.wikipedia.org/wiki/Ordinary_least_squares>`_


    :param feature: see `Columns </nimbusml/concepts/columns>`_.

    :param label: see `Columns </nimbusml/concepts/columns>`_.

    :param weight: see `Columns </nimbusml/concepts/columns>`_.

    :param normalize: Specifies the type of automatic normalization used:

        * ``"Auto"``: if normalization is needed, it is performed
          automatically. This is the default choice.
        * ``"No"``: no normalization is performed.
        * ``"Yes"``: normalization is performed.
        * ``"Warn"``: if normalization is needed, a warning
          message is displayed, but normalization is not performed.

        Normalization rescales disparate data ranges to a standard scale.
        Feature
        scaling insures the distances between data points are proportional
        and
        enables various optimization methods such as gradient descent to
        converge
        much faster. If normalization is performed, a ``MaxMin`` normalizer
        is
        used. It normalizes values in an interval [a, b] where ``-1 <= a <=
        0``
        and ``0 <= b <= 1`` and ``b - a = 1``. This normalizer preserves
        sparsity by mapping zero to zero.

    :param caching: Whether trainer should cache input training data.

    :param l2_regularization: L2 regularization weight.

    :param calculate_statistics: Whether to calculate per parameter
        significance statistics.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:func:`FastLinearRegressor
        <nimbusml.linear_model.FastLinearRegressor>`,
        :py:func:`LightGbmRegressor <nimbusml.ensemble.LightGbmRegressor>`,
        :py:func:`FastForestRegressor <nimbusml.ensemble.FastForestRegressor>`,
        :py:func:`FastTreesRegressor <nimbusml.ensemble.FastTreesRegressor>`,
        :py:func:`GamRegressor <nimbusml.ensemble.GamRegressor>`.

    .. index:: models, regression, linear

    Example:
       .. literalinclude:: /../nimbusml/examples/OrdinaryLeastSquaresRegressor.py
              :language: python
    """

    @trace
    def __init__(
            self,
            normalize='Auto',
            caching='Auto',
            l2_regularization=1e-06,
            calculate_statistics=True,
            feature=None,
            label=None,
            weight=None,
            **params):

        if 'feature_column_name' in params:
            raise NameError(
                "'feature_column_name' must be renamed to 'feature'")
        if feature:
            params['feature_column_name'] = feature
        if 'label_column_name' in params:
            raise NameError(
                "'label_column_name' must be renamed to 'label'")
        if label:
            params['label_column_name'] = label
        if 'example_weight_column_name' in params:
            raise NameError(
                "'example_weight_column_name' must be renamed to 'weight'")
        if weight:
            params['example_weight_column_name'] = weight
        BasePredictor.__init__(self, type='regressor', **params)
        core.__init__(
            self,
            normalize=normalize,
            caching=caching,
            l2_regularization=l2_regularization,
            calculate_statistics=calculate_statistics,
            **params)
        self.feature = feature
        self.label = label
        self.weight = weight

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)
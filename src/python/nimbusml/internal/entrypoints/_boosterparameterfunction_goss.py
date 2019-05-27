# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
goss
"""

import numbers

from ..utils.entrypoints import Component
from ..utils.utils import try_set


def goss(
        top_rate=0.2,
        other_rate=0.1,
        minimum_split_gain=0.0,
        maximum_tree_depth=0,
        minimum_child_weight=0.1,
        subsample_frequency=0,
        subsample_fraction=1.0,
        feature_fraction=1.0,
        l2_regularization=0.01,
        l1_regularization=0.0,
        **params):
    """
    **Description**
        Gradient-based One-Side Sampling.

    :param top_rate: Retain ratio for large gradient instances.
        (settings).
    :param other_rate: Retain ratio for small gradient instances.
        (settings).
    :param minimum_split_gain: Minimum loss reduction required to
        make a further partition on a leaf node of the tree. the
        larger, the more conservative the algorithm will be.
        (settings).
    :param maximum_tree_depth: Maximum depth of a tree. 0 means no
        limit. However, tree still grows by best-first. (settings).
    :param minimum_child_weight: Minimum sum of instance
        weight(hessian) needed in a child. If the tree partition step
        results in a leaf node with the sum of instance weight less
        than min_child_weight, then the building process will give up
        further partitioning. In linear regression mode, this simply
        corresponds to minimum number of instances needed to be in
        each node. The larger, the more conservative the algorithm
        will be. (settings).
    :param subsample_frequency: Subsample frequency for bagging. 0
        means no subsample. Specifies the frequency at which the
        bagging occurs, where if this is set to N, the subsampling
        will happen at every N iterations.This must be set with
        Subsample as this specifies the amount to subsample.
        (settings).
    :param subsample_fraction: Subsample ratio of the training
        instance. Setting it to 0.5 means that LightGBM randomly
        collected half of the data instances to grow trees and this
        will prevent overfitting. Range: (0,1]. (settings).
    :param feature_fraction: Subsample ratio of columns when
        constructing each tree. Range: (0,1]. (settings).
    :param l2_regularization: L2 regularization term on weights,
        increasing this value will make model more conservative.
        (settings).
    :param l1_regularization: L1 regularization term on weights,
        increase this value will make model more conservative.
        (settings).
    """

    entrypoint_name = 'goss'
    settings = {}

    if top_rate is not None:
        settings['TopRate'] = try_set(
            obj=top_rate,
            none_acceptable=True,
            is_of_type=numbers.Real,
            valid_range={
                'Inf': 0.0,
                'Max': 1.0})
    if other_rate is not None:
        settings['OtherRate'] = try_set(
            obj=other_rate,
            none_acceptable=True,
            is_of_type=numbers.Real,
            valid_range={
                'Inf': 0.0,
                'Max': 1.0})
    if minimum_split_gain is not None:
        settings['MinimumSplitGain'] = try_set(
            obj=minimum_split_gain,
            none_acceptable=True,
            is_of_type=numbers.Real, valid_range={'Min': 0.0})
    if maximum_tree_depth is not None:
        settings['MaximumTreeDepth'] = try_set(
            obj=maximum_tree_depth,
            none_acceptable=True,
            is_of_type=numbers.Real,
            valid_range={
                'Max': 2147483647,
                'Min': 0})
    if minimum_child_weight is not None:
        settings['MinimumChildWeight'] = try_set(
            obj=minimum_child_weight,
            none_acceptable=True,
            is_of_type=numbers.Real, valid_range={'Min': 0.0})
    if subsample_frequency is not None:
        settings['SubsampleFrequency'] = try_set(
            obj=subsample_frequency,
            none_acceptable=True,
            is_of_type=numbers.Real,
            valid_range={
                'Max': 2147483647,
                'Min': 0})
    if subsample_fraction is not None:
        settings['SubsampleFraction'] = try_set(
            obj=subsample_fraction,
            none_acceptable=True,
            is_of_type=numbers.Real,
            valid_range={
                'Inf': 0.0,
                'Max': 1.0})
    if feature_fraction is not None:
        settings['FeatureFraction'] = try_set(
            obj=feature_fraction,
            none_acceptable=True,
            is_of_type=numbers.Real,
            valid_range={
                'Inf': 0.0,
                'Max': 1.0})
    if l2_regularization is not None:
        settings['L2Regularization'] = try_set(
            obj=l2_regularization,
            none_acceptable=True,
            is_of_type=numbers.Real, valid_range={'Min': 0.0})
    if l1_regularization is not None:
        settings['L1Regularization'] = try_set(
            obj=l1_regularization,
            none_acceptable=True,
            is_of_type=numbers.Real, valid_range={'Min': 0.0})

    component = Component(
        name=entrypoint_name,
        settings=settings,
        kind='BoosterParameterFunction')
    return component

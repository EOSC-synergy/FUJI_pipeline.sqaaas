# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from fuji_server.models.base_model_ import Model
from fuji_server.models.fair_result_common_score import FAIRResultCommonScore  # noqa: F401,E501
from fuji_server.models.fair_result_evaluation_criterium import FAIRResultEvaluationCriterium  # noqa: F401,E501
from fuji_server import util


class FAIRResultCommon(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, metric_identifier: str=None, metric_name: str=None, metric_tests: Dict[str, FAIRResultEvaluationCriterium]=None, test_status: str='fail', score: FAIRResultCommonScore=None):  # noqa: E501
        """FAIRResultCommon - a model defined in Swagger

        :param id: The id of this FAIRResultCommon.  # noqa: E501
        :type id: int
        :param metric_identifier: The metric_identifier of this FAIRResultCommon.  # noqa: E501
        :type metric_identifier: str
        :param metric_name: The metric_name of this FAIRResultCommon.  # noqa: E501
        :type metric_name: str
        :param metric_tests: The metric_tests of this FAIRResultCommon.  # noqa: E501
        :type metric_tests: Dict[str, FAIRResultEvaluationCriterium]
        :param test_status: The test_status of this FAIRResultCommon.  # noqa: E501
        :type test_status: str
        :param score: The score of this FAIRResultCommon.  # noqa: E501
        :type score: FAIRResultCommonScore
        """
        self.swagger_types = {
            'id': int,
            'metric_identifier': str,
            'metric_name': str,
            'metric_tests': Dict[str, FAIRResultEvaluationCriterium],
            'test_status': str,
            'score': FAIRResultCommonScore
        }

        self.attribute_map = {
            'id': 'id',
            'metric_identifier': 'metric_identifier',
            'metric_name': 'metric_name',
            'metric_tests': 'metric_tests',
            'test_status': 'test_status',
            'score': 'score'
        }
        self._id = id
        self._metric_identifier = metric_identifier
        self._metric_name = metric_name
        self._metric_tests = metric_tests
        self._test_status = test_status
        self._score = score

    @classmethod
    def from_dict(cls, dikt) -> 'FAIRResultCommon':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FAIRResultCommon of this FAIRResultCommon.  # noqa: E501
        :rtype: FAIRResultCommon
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this FAIRResultCommon.


        :return: The id of this FAIRResultCommon.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this FAIRResultCommon.


        :param id: The id of this FAIRResultCommon.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def metric_identifier(self) -> str:
        """Gets the metric_identifier of this FAIRResultCommon.


        :return: The metric_identifier of this FAIRResultCommon.
        :rtype: str
        """
        return self._metric_identifier

    @metric_identifier.setter
    def metric_identifier(self, metric_identifier: str):
        """Sets the metric_identifier of this FAIRResultCommon.


        :param metric_identifier: The metric_identifier of this FAIRResultCommon.
        :type metric_identifier: str
        """
        if metric_identifier is None:
            raise ValueError("Invalid value for `metric_identifier`, must not be `None`")  # noqa: E501

        self._metric_identifier = metric_identifier

    @property
    def metric_name(self) -> str:
        """Gets the metric_name of this FAIRResultCommon.


        :return: The metric_name of this FAIRResultCommon.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name: str):
        """Sets the metric_name of this FAIRResultCommon.


        :param metric_name: The metric_name of this FAIRResultCommon.
        :type metric_name: str
        """
        if metric_name is None:
            raise ValueError("Invalid value for `metric_name`, must not be `None`")  # noqa: E501

        self._metric_name = metric_name

    @property
    def metric_tests(self) -> Dict[str, FAIRResultEvaluationCriterium]:
        """Gets the metric_tests of this FAIRResultCommon.


        :return: The metric_tests of this FAIRResultCommon.
        :rtype: Dict[str, FAIRResultEvaluationCriterium]
        """
        return self._metric_tests

    @metric_tests.setter
    def metric_tests(self, metric_tests: Dict[str, FAIRResultEvaluationCriterium]):
        """Sets the metric_tests of this FAIRResultCommon.


        :param metric_tests: The metric_tests of this FAIRResultCommon.
        :type metric_tests: Dict[str, FAIRResultEvaluationCriterium]
        """

        self._metric_tests = metric_tests

    @property
    def test_status(self) -> str:
        """Gets the test_status of this FAIRResultCommon.


        :return: The test_status of this FAIRResultCommon.
        :rtype: str
        """
        return self._test_status

    @test_status.setter
    def test_status(self, test_status: str):
        """Sets the test_status of this FAIRResultCommon.


        :param test_status: The test_status of this FAIRResultCommon.
        :type test_status: str
        """
        allowed_values = ["pass", "fail", "indeterminate"]  # noqa: E501
        if test_status not in allowed_values:
            raise ValueError(
                "Invalid value for `test_status` ({0}), must be one of {1}"
                .format(test_status, allowed_values)
            )

        self._test_status = test_status

    @property
    def score(self) -> FAIRResultCommonScore:
        """Gets the score of this FAIRResultCommon.


        :return: The score of this FAIRResultCommon.
        :rtype: FAIRResultCommonScore
        """
        return self._score

    @score.setter
    def score(self, score: FAIRResultCommonScore):
        """Sets the score of this FAIRResultCommon.


        :param score: The score of this FAIRResultCommon.
        :type score: FAIRResultCommonScore
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")  # noqa: E501

        self._score = score

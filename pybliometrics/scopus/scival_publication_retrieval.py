from collections import namedtuple
from typing import List, NamedTuple, Optional, Union

from pybliometrics.scopus.superclasses import Retrieval
from pybliometrics.scopus.utils import check_parameter_value


class ScivalPublicationRetrieval(Retrieval):
    def __init__(
        self, identifier: str, refresh: Union[bool, int] = False, **kwds: str
    ) -> None:
        """Interaction with the SciVal Publications API.
        :param identifier: The identifier of a document.
        :param refresh: Whether to refresh the cached file if it exists or not.
                        If int is passed, cached file will be refreshed if the
                        number of days since last modification exceeds that value.
        :param kwds: Keywords passed on as query parameters.  Must contain
                     fields and values mentioned in the API specification at
                     https://dev.elsevier.com/documentation/PlumXMetricsAPI.wadl.

        Raises
        ------
        ValueError
            If the parameter `refresh` is not one of the allowed values.

        Notes
        -----
        The directory for cached results is `{path}/FULL/{identifier}`,
        where `path` is specified in your configuration file.
        """

        self._identifier = identifier

        # Load json
        self._refresh = refresh
        self._view = "FULL"
        Retrieval.__init__(
            self, identifier=identifier, api="ScivalPublicationsRetrieval", **kwds
        )

    def __str__(self):
        """Print a summary string."""
        return str(self._json)

from ..doctools import document
from .geom_path import geom_path


@document
class geom_line(geom_path):
    """
    Connected points

    {usage}

    Parameters
    ----------
    {common_parameters}
    fun_y : function, optional (default: None)
        Any function that takes a array-like and returns a value.
        (Generally used in coordination with stat = 'summary')
    
    See Also
    --------
    plotnine.geoms.geom_path - For documentation of
        other parameters.
    """

    def setup_data(self, data):
        return data.sort_values(['PANEL', 'group', 'x'])

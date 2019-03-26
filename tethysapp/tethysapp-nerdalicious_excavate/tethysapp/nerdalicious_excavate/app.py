from tethys_sdk.base import TethysAppBase, url_map_maker


class NerdaliciousExcavate(TethysAppBase):
    """
    Tethys app class for Nerdalicious Excavate.
    """

    name = 'Nerdalicious Excavate'
    index = 'nerdalicious_excavate:home'
    icon = 'nerdalicious_excavate/images/icon.gif'
    package = 'nerdalicious_excavate'
    root_url = 'nerdalicious-excavate'
    color = '#5b3b26'
    description = 'Used to find seepage and slope stability'
    tags = 'excavate, seepage, slopestability'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='nerdalicious-excavate',
                controller='nerdalicious_excavate.controllers.home'
            ),
        )

        return url_maps

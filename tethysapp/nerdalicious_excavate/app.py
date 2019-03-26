from tethys_sdk.base import TethysAppBase, url_map_maker


class NerdaliciousExcavate(TethysAppBase):
    """
    Tethys app class for Nerdalicious Excavate.
    """

    name = 'Nerdalicious Excavate'
    index = 'nerdalicious_excavate:home'
    icon = 'nerdalicious_excavate/images/diagram.png'
    package = 'nerdalicious_excavate'
    root_url = 'nerdalicious_excavate'
    color = '#5b3b26'
    description = 'Used to find seepage and slope stability'
    tags = 'excavate,seep,stability'
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
            UrlMap(
                name='mockup',
                url='nerdalicious-excavate/mockup',
                controller='nerdalicious_excavate.controllers.mockup'
            ),
            UrlMap(
                name='proposal',
                url='nerdalicious-excavate/proposal',
                controller='nerdalicious_excavate.controllers.proposal'
            ),
            UrlMap(
                name='geoproc',
                url='nerdalicious-excavate/geoproc',
                controller='nerdalicious_excavate.controllers.geoproc'
            ),
        )

        return url_maps

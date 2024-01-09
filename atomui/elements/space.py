from nicegui.elements.mixins.disableable_element import DisableableElement


class Space(DisableableElement):
    def __init__(self) -> None:
        super().__init__(tag='q-space')

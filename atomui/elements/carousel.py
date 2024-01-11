from nicegui import ui
from nicegui.elements.mixins.disableable_element import DisableableElement
from typing import Optional, Callable, Any, Union

from .base import BindableUi
from ..utils.signals import ReadonlyRef, is_ref, effect
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value


class CarouselSlide(DisableableElement):
    # TODO: 还未实现
    def __init__(
        self,
        position: Optional[str] = None,
        offset_x: Optional[int] = None,
        offset_y: Optional[int] = None,
    ) -> None:
        """Carousel Control [user-defined]

        :param position: top-right/ top-left/ bottom-right/ bottom-left/ top/ bottom/ left/ right
        """
        super().__init__(tag='q-carousel-control')
        self._props['position'] = position
        self._classes.append('nicegui-carousel-control')


class CarouselSlideBindableUi(BindableUi[ui.carousel_slide]):
    def __init__(
        self,
        *,
        name: Optional[TMaybeRef[str]] = None,
        img_src: Optional[TMaybeRef[str]] = None,
        disable: Optional[TMaybeRef[bool]] = False
    ):
        kws = {"name": name}
        value_kws = convert_kws_ref2value(kws)
        element = ui.carousel_slide(**value_kws)
        super().__init__(element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        kws_extra = {"img_src": img_src, "disable": disable}
        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        return super().bind_prop(prop, ref_ui)


class CarouselBindableUi(BindableUi[ui.carousel]):
    def __init__(
        self,
        *,
        value: Optional[TMaybeRef[Union[str, ui.carousel_slide, CarouselSlideBindableUi]]] = None,
        on_value_change: Optional[Callable[..., Any]] = None,
        animated: Optional[TMaybeRef[bool]] = False,
        arrows: Optional[TMaybeRef[bool]] = False,
        navigation: Optional[TMaybeRef[bool]] = False,
        fullscreen: Optional[TMaybeRef[bool]] = False,
        no_route_fullscreen_exit: Optional[TMaybeRef[bool]] = False,
        keep_alive: Optional[TMaybeRef[bool]] = False,
        keep_alive_include: Optional[TMaybeRef[str]] = None,
        keep_alive_exclude: Optional[TMaybeRef[str]] = None,
        keep_alive_max: Optional[TMaybeRef[int]] = None,
        infinite: Optional[TMaybeRef[bool]] = False,
        swipeable: Optional[TMaybeRef[bool]] = False,
        vertical: Optional[TMaybeRef[bool]] = False,
        autoplay: Optional[TMaybeRef[Union[bool, int]]] = False,
        padding: Optional[TMaybeRef[bool]] = False,
        prev_icon: Optional[TMaybeRef[str]] = None,
        next_icon: Optional[TMaybeRef[str]] = None,
        navigation_position: Optional[TMaybeRef[str]] = "bottom/right",
        navigation_icon: Optional[TMaybeRef[str]] = None,
        navigation_active_icon: Optional[TMaybeRef[str]] = None,
        thumbnails: Optional[TMaybeRef[bool]] = False,
        dark: Optional[TMaybeRef[bool]] = False,
        height: Optional[TMaybeRef[str]] = None,
        control_color: Optional[TMaybeRef[str]] = None,
        control_type: Optional[TMaybeRef[str]] = None,
        transition_prev: Optional[TMaybeRef[str]] = "fade",
        transition_next: Optional[TMaybeRef[str]] = "fade",
        transition_duration: Optional[TMaybeRef[int]] = 300,
    ):
        """Literal value of param

        :param keep_alive_include: (e.g.) a,b / "/a|b/" / ['a', 'b']
        :param keep_alive_exclude: (e.g.) a,b / "/a|b/" / ['a', 'b']
        :param autoplay: (e.g.) 2500 / True / False
        :param prev_icon: (e.g.) map & ion-add & img:https://xxx/logo.svg / img:path/to/image.png
        :param navigation_icon: (e.g.) map & ion-add & img:https://xxx/logo.svg / img:path/to/image.png
        :param navigation_active_icon: (e.g.) map & ion-add & img:https://xxx/logo.svg / img:path/to/image.png
        :param navigation_position: top / right / bottom / left
        :param height: (e.g.) 16px / 2rem
        :param control_color: (e.g.) primary / teal-10
        :param control_type: regular / flat / outline / push / unelevated
        :param transition_prev: (e.g.) fade / slide-down
        :param transition_next: (e.g.) fade / slide-down
        """
        kws = {
            "value": value,
            "animated": animated,
            "on_value_change": on_value_change,
            "arrows": arrows,
            "navigation": navigation
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.carousel(**value_kws)
        super().__init__(element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        kws_extra = {
            "fullscreen": fullscreen,
            "no-route-fullscreen-exit": no_route_fullscreen_exit,
            "transition-prev": transition_prev,
            "transition-next": transition_next,
            "keep-alive": keep_alive,
            "keep-alive-include": keep_alive_include,
            "keep-alive-exclude": keep_alive_exclude,
            "keep-alive-max": keep_alive_max,
            "infinite": infinite,
            "swipeable": swipeable,
            "vertical": vertical,
            "autoplay": autoplay,
            "control-type": control_type,
            "padding": padding,
            "height": height,
            "position": prev_icon,
            "next-icon": next_icon,
            "navigation-icon": navigation_icon,
            "navigation-active-icon": navigation_active_icon,
            "navigation-position": navigation_position,
            "thumbnails": thumbnails,
            "dark": dark,
            "control_color": control_color,
            "transition_duration": transition_duration,
        }
        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        if prop == "value":
            return self.bind_value(ref_ui)

        return super().bind_prop(prop, ref_ui)

    def bind_value(self, ref_ui: ReadonlyRef[bool]):
        @effect
        def _():
            self.element.on_value_change(ref_ui.value)

        return self

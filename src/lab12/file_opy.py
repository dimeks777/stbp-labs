# coding: UTF-8
import sys
l1lll11_opy_ = sys.version_info [0] == 2
l11l1ll_opy_ = 2048
l11l11l_opy_ = 7
def l111ll_opy_ (l11l_opy_):
    global l1ll11_opy_
    l11lll1_opy_ = ord (l11l_opy_ [-1])
    l1lll1ll_opy_ = l11l_opy_ [:-1]
    l11111_opy_ = l11lll1_opy_ % len (l1lll1ll_opy_)
    l1l1111_opy_ = l1lll1ll_opy_ [:l11111_opy_] + l1lll1ll_opy_ [l11111_opy_:]
    if l1lll11_opy_:
        l1ll11l_opy_ = l1ll1_opy_ () .join ([l1l1l1_opy_ (ord (char) - l11l1ll_opy_ - (l11_opy_ + l11lll1_opy_) % l11l11l_opy_) for l11_opy_, char in enumerate (l1l1111_opy_)])
    else:
        l1ll11l_opy_ = str () .join ([chr (ord (char) - l11l1ll_opy_ - (l11_opy_ + l11lll1_opy_) % l11l11l_opy_) for l11_opy_, char in enumerate (l1l1111_opy_)])
    return eval (l1ll11l_opy_)
import l1lll1l_opy_ as l111l1_opy_
import hashlib
import unicodedata
from l1ll1ll_opy_.l1ll111_opy_ import l1lll1l1_opy_
from l1ll1ll_opy_.l1ll1l1l_opy_ import l11l1_opy_
from l1ll1ll_opy_.l1l1l_opy_ import HMAC
from l1llllll_opy_ import l1llll1_opy_
def l1l1llll_opy_(l1l111l_opy_):
    if l1l111l_opy_ == l111ll_opy_ (u"ࠧࡦࡰࠪ࠴"):
        l1llll1l_opy_ = l111l1_opy_.l1llll11_opy_(
            l111ll_opy_ (u"ࠨࡧࡱࡣࡼࡵࡲࡥࡵ࠱ࡸࡽࡺࠧ࠵"),
            names=[l111ll_opy_ (u"ࠩࡺࡳࡷࡪࡳࠨ࠶")]
        ).l11lll_opy_().l1ll1l11_opy_(l111ll_opy_ (u"ࠪࡻࡴࡸࡤࡴࠩ࠷"))
        l1l_opy_ = l1llll1l_opy_.l1lll111_opy_()[l111ll_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪ࠸")]
    elif l1l111l_opy_ == l111ll_opy_ (u"ࠬࡻࡡࠨ࠹"):
        l1llll1l_opy_ = l111l1_opy_.l1llll11_opy_(
            l111ll_opy_ (u"࠭ࡵࡢࡡࡺࡳࡷࡪࡳ࠯ࡶࡻࡸࠬ࠺"),
            names=[l111ll_opy_ (u"ࠧࡸࡱࡵࡨࡸ࠭࠻")]
        ).l11lll_opy_().l1ll1l11_opy_(l111ll_opy_ (u"ࠨࡹࡲࡶࡩࡹࠧ࠼"))
        l1l_opy_ = l1llll1l_opy_.l1lll111_opy_()[l111ll_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ࠽")]
    return l1l_opy_
class l1l1l1l1_opy_(object):
  def __init__(self, seed):
    self.index = 0
    self.seed = seed
    self.buffer = ll_opy_ (u"ࠥࠦ࠾")
  def __call__(self, n):
    while len(self.buffer) < n:
        self.buffer += HMAC.new(self.seed +
                                l1llll1_opy_(l111ll_opy_ (u"ࠦࡁࡏࠢ࠿"), self.index)).digest()
        self.index += 1
    result, self.buffer = self.buffer[:n], self.buffer[n:]
    return result
def l1ll1l1_opy_(text, l1111_opy_):
    l1l1lll_opy_ = l11l1_opy_.l111ll1_opy_(1024, l1111l1_opy_=l1l1l1l1_opy_(l1l1lll1_opy_(l1111_opy_)))
    l11l1l_opy_ = l1l1lll_opy_.l11l1l_opy_().l11l1l1_opy_(l111ll_opy_ (u"ࠬࡖࡅࡎࠩࡀ"))
    print(l111l1l_opy_ (u"࠭ࡐࡖࡄࡏࡍࡈࠦࡋࡆ࡛ࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠺ࠡࡽࡳࡹࡧࡲࡩࡤࡡ࡮ࡩࡾࢃࠧࡁ"))
    l1111ll_opy_ = l1lll1l1_opy_.new(l11l1_opy_.l1l1ll_opy_(l11l1l_opy_))
    l111l11_opy_ = l1111ll_opy_.l1ll1l1_opy_(text)
    return l111l11_opy_
def l1l11ll_opy_(l111l11_opy_, l1111_opy_):
    l1l1lll_opy_ = l11l1_opy_.l111ll1_opy_(1024, l1111l1_opy_=l1l1l1l1_opy_(l1l1lll1_opy_(l1111_opy_)))
    l111111_opy_ = l1l1lll_opy_.l11l1l1_opy_(l111ll_opy_ (u"ࠧࡑࡇࡐࠫࡂ"))
    print(l111l1l_opy_ (u"ࠨࡒࡕࡍ࡛ࡇࡔࡆࠢࡎࡉ࡞ࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠼ࠣࡿࡵࡸࡩࡷࡣࡷࡩࡤࡱࡥࡺࡿࠪࡃ"))
    l1111ll_opy_ = l1lll1l1_opy_.new(l11l1_opy_.l1l1ll_opy_(l111111_opy_))
    l1l11l_opy_ = l1111ll_opy_.l1l11ll_opy_(l111l11_opy_)
    return l1l11l_opy_
class l1l1l1ll_opy_(Exception):
    l111ll_opy_ (u"ࠤࠥࠦࡗࡧࡩࡴࡧࡧࠤ࡮࡬ࠠࡢࠢࡪ࡭ࡻ࡫࡮ࠡࡄࡌࡔ࠸࠿ࠠ࡮ࡰࡨࡱࡴࡴࡩࡤࠢࡳ࡬ࡷࡧࡳࡦࠢࡦࡥࡳࡴ࡯ࡵࠢࡥࡩࠥࡪࡥࡤࡱࡧࡩࡩࠦࡩ࡯ࡶࡲࠤࡦࠦࡳࡦࡳࡸࡩࡳࡩࡥࠡࡱࡩࠤࡧࡿࡴࡦࡵ࠱ࠦࠧࠨࡄ")
def l1ll111l_opy_(l111_opy_: int) -> int:
    try:
        return {12: 128, 15: 160, 18: 192, 21: 224, 24: 256}[l111_opy_]
    except KeyError:
        raise l1l1l1ll_opy_(
            l111ll_opy_ (u"ࠥࡍࡳࡼࡡ࡭࡫ࡧࠤࡳࡻ࡭ࡣࡧࡵࠤࡴ࡬ࠠࡸࡱࡵࡨࡸࠦࡰࡳࡱࡹ࡭ࡩ࡫ࡤ࠭ࠢࠥࡅ")
            l111ll_opy_ (u"ࠦࡇࡏࡐ࠴࠻ࠣࡱࡳ࡫࡭ࡰࡰ࡬ࡧࠥࡶࡨࡳࡣࡶࡩࡸࠦࡡࡳࡧࠣࡳࡳࡲࡹࠡࡵࡳࡩࡨ࡯ࡦࡪࡧࡧࠤ࡫ࡵࡲࠡ࠳࠵࠰ࠥ࠷࠵࠭ࠢ࠴࠼࠱ࠦ࠲࠲࠮ࠣࡳࡷࠦ࠲࠵ࠢࡺࡳࡷࡪࡳ࠯ࠤࡆ")
        )
def l1l1ll11_opy_(phrase: str) -> bytes:
    if not all(c in l1l111_opy_ for c in phrase):
        raise l1l1l1ll_opy_(
            l111l1l_opy_ (u"ࠧࡏ࡮ࡷࡣ࡯࡭ࡩࠦ࡭࡯ࡧࡰࡳࡳ࡯ࡣࠡࡲ࡫ࡶࡦࡹࡥࠡࡽࡵࡩࡵࡸࠨࡱࡪࡵࡥࡸ࡫ࠩࡾࠢࡳࡶࡴࡼࡩࡥࡧࡧ࠰ࠥࡶࡨࡳࡣࡶࡩࠥࡩ࡯࡯ࡶࡤ࡭ࡳࡹࠠࡢࡰࠣ࡭ࡳࡼࡡ࡭࡫ࡧࠤࡨ࡮ࡡࡳࡣࡦࡸࡪࡸ࠮ࠣࡇ")
        )
    words = phrase.split()
    l1ll11ll_opy_ = l1ll111l_opy_(len(words))
    l1lllll1_opy_ = l1ll11ll_opy_ // 32
    bits = 0
    for l1l1l1l_opy_ in words:
        bits <<= 11
        try:
            bits |= l1lll_opy_[l1l1l1l_opy_]
        except KeyError:
            raise l1l1l1ll_opy_(
                l111l1l_opy_ (u"ࠨࡉ࡯ࡸࡤࡰ࡮ࡪࠠ࡮ࡰࡨࡱࡴࡴࡩࡤࠢࡳ࡬ࡷࡧࡳࡦࠢࡾࡶࡪࡶࡲࠩࡲ࡫ࡶࡦࡹࡥࠪࡿࠣࡴࡷࡵࡶࡪࡦࡨࡨ࠱ࠦࡷࡰࡴࡧࠤࠬࢁࡷࡰࡴࡧࢁࠬࠦࡩࡴࠢࡱࡳࡹࠦࡩ࡯ࠢࡷ࡬ࡪࠦࡂࡊࡒ࠶࠽ࠥࡽ࡯ࡳࡦ࡯࡭ࡸࡺ࠮ࠣࡈ")
            )
    l11l11_opy_ = bits & (2 ** l1lllll1_opy_ - 1)
    bits >>= l1lllll1_opy_
    data = bits.to_bytes(l1ll11ll_opy_ // 8, byteorder=l111ll_opy_ (u"ࠢࡣ࡫ࡪࠦࡉ"))
    l1lll1_opy_ = hashlib.sha256(data).digest()[0] >> (
        8 - l1lllll1_opy_
    )
    return data
def l1l1ll1l_opy_(txt: str) -> str:
    l111ll_opy_ (u"ࠣࠤࠥࡅࡸࠦࡷࡦࠢࡲࡲࡱࡿࠠࡤࡱࡱࡷ࡮ࡪࡥࡳࠢࡨࡲ࡬ࡲࡩࡴࡪࠣࡻࡴࡸࡤ࡭࡫ࡶࡸࡸࠦࡡ࡯ࡦࠣࡷࡹࡸࠠࡪࡰࡳࡹࡹࠨࠢࠣࡊ")
    assert type(txt) is str
    return unicodedata.l1ll_opy_(l111ll_opy_ (u"ࠤࡑࡊࡐࡊࠢࡋ"), txt)
def l1l1lll1_opy_(l1111_opy_: str, l11ll11_opy_: str = l111ll_opy_ (u"ࠥࠦࡌ")) -> bytes:
    l1l1ll11_opy_(l1111_opy_)
    l1111_opy_ = l1l1ll1l_opy_(l1111_opy_)
    l11ll11_opy_ = l111ll_opy_ (u"ࠦࡲࡴࡥ࡮ࡱࡱ࡭ࡨࠨࡍ") + l1l1ll1l_opy_(l11ll11_opy_)
    l111l_opy_ = l1111_opy_.encode(l111ll_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦࡎ"))
    l1ll1lll_opy_ = l11ll11_opy_.encode(l111ll_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧࡏ"))
    l1l1ll1_opy_ = hashlib.pbkdf2_hmac(
        l111ll_opy_ (u"ࠢࡴࡪࡤ࠹࠶࠸ࠢࡐ"), l111l_opy_, l1ll1lll_opy_, l1ll1l_opy_
    )
    print(l111l1l_opy_ (u"ࠨࡉࡈࡒࡊࡘࡁࡕࡇࡇࠤࡘࡋࡅࡅࠢࠣࠤࠥࠦࠠࠡ࠼ࠣࡿࡸࡺࡲࡦࡶࡦ࡬ࡪࡪ࠮ࡩࡧࡻࠬ࠮ࢃࠧࡑ"))
    return l1l1ll1_opy_
l11111l_opy_ = l111ll_opy_ (u"ࠩࡨࡲࠬࡒ")
l1l111_opy_ = {
    l111ll_opy_ (u"ࠪࡹࡦ࠭ࡓ"): l111ll_opy_ (u"ࠦࠥ࠭రలఴశಕహ఻౔షహ఻ౚ౜ి఺఼ాీూౄెుృ౅ే౉ో్ైొ౎౑౓ࠧࡔ"),
    l111ll_opy_ (u"ࠬ࡫࡮ࠨࡕ"): l111ll_opy_ (u"ࠨࠠࡢࡤࡦࡨࡪ࡬ࡧࡩ࡫࡭࡯ࡱࡳ࡮ࡰࡲࡴࡶࡸࡺࡵࡷࡹࡻࡽࡿࠨࡖ")
}[l11111l_opy_]
l1lll_opy_ = l1l1llll_opy_(l1l111l_opy_=l11111l_opy_)
l1ll1l_opy_ = 2048
if __name__ == l111ll_opy_ (u"ࠧࡠࡡࡰࡥ࡮ࡴ࡟ࡠࠩࡗ"):
    text = l111ll_opy_ (u"ࠨࡊࡨࡰࡱࡵࠠࡸࡱࡵࡰࡩ࠭ࡘ")
    l1111_opy_ = l111ll_opy_ (u"ࠩࡤࡧ࡭࡯ࡥࡷࡧࠣࡥࡨࡵࡵࡴࡶ࡬ࡧࠥࡧࡤࡷࡣࡱࡧࡪࠦࡡࡨࡴࡨࡩࠥࡧࡩࡳࡲࡲࡶࡹࠦࡢࡪࡴࡧࠤࡧࡸࡡࡷࡧࠣࡦࡷ࡯ࡤࡨࡧࠣࡦࡷࡵࡣࡤࡱ࡯࡭ࠥࡩ࡯ࡳࡴࡨࡧࡹࠦࡤࡰࡰࡤࡸࡪࠦࡥ࡭ࡧࡰࡩࡳࡺ࡙ࠧ")
    l1ll1111_opy_ = l111ll_opy_ (u"ࠥࡉࡓࡉࡒ࡚ࡒࡗࡍࡔࡔ࡚ࠢ")
    print(l111ll_opy_ (u"ࠦࡂࠨ࡛")*(82 + len(l1ll1111_opy_)))
    print(l111ll_opy_ (u"ࠧࡃࠢ࡜")*40, l1ll1111_opy_, l111ll_opy_ (u"ࠨ࠽ࠣ࡝")*40)
    print(l111ll_opy_ (u"ࠢ࠾ࠤ࡞")*(82 + len(l1ll1111_opy_)))
    print(l111l1l_opy_ (u"ࠨࡑࡵ࡭࡬࡯࡮ࡢ࡮ࠣࡸࡪࡾࡴࠡࠢࠣࠤࠥࠦࠠࠡ࠼ࠣࡿࡹ࡫ࡸࡵࡿࠪ࡟"))
    print(l111l1l_opy_ (u"ࠩࡐࡲࡪࡳ࡯࡯࡫ࡦࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠽ࠤࢀࡳ࡮ࡦ࡯ࡲࡲ࡮ࡩࡽࠨࡠ"))
    l111l11_opy_ = l1ll1l1_opy_(text.encode(), l1111_opy_)
    print(l111l1l_opy_ (u"ࠪࡉࡳࡩࡲࡺࡲࡷࡩࡩࠦࡴࡦࡺࡷࠤࠥࠦࠠࠡࠢࠣ࠾ࠥࢁࡥ࡯ࡥࡵࡽࡵࡺࡥࡥࡡࡷࡩࡽࡺ࠮ࡩࡧࡻࠬ࠮ࢃࠧࡡ"))
    print()
    l1ll11l1_opy_ = l111ll_opy_ (u"ࠦࡉࡋࡃࡓ࡛ࡓࡘࡎࡕࡎࠣࡢ")
    print(l111ll_opy_ (u"ࠧࡃࠢࡣ")*(82 + len(l1ll11l1_opy_)))
    print(l111ll_opy_ (u"ࠨ࠽ࠣࡤ")*40, l1ll11l1_opy_, l111ll_opy_ (u"ࠢ࠾ࠤࡥ")*40)
    print(l111ll_opy_ (u"ࠣ࠿ࠥࡦ")*(82 + len(l1ll11l1_opy_)))
    l1l11l_opy_ = l1l11ll_opy_(l111l11_opy_, l1111_opy_)
    print(l111l1l_opy_ (u"ࠩࡇࡩࡨࡸࡹࡱࡶࡨࡨࠥࡺࡥࡹࡶࠣࠤࠥࠦࠠࠡࠢ࠽ࠤࢀࡪࡥࡤࡴࡼࡴࡹ࡫ࡤࡠࡶࡨࡼࡹ࠴ࡤࡦࡥࡲࡨࡪ࠮ࠩࡾࠩࡧ"))
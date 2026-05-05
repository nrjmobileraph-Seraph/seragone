import builtins

_ORIG_OPEN = builtins.open
_TARGET = "/home/ubuntu/labo_27d/banc_27d_enrichi_v4.csv"
_LOCAL = "/home/ubuntu/seragone/auditactionsv1/CONTROLE_MULTIMONDES_V1ZD_SANDBOX_PRECHECK_BORN_20260505_194846/sandbox_born_inputs/inputs/banc_27d_enrichi_v4.csv"

def open(file, *args, **kwargs):
    try:
        if str(file) == _TARGET:
            file = _LOCAL
    except Exception:
        pass
    return _ORIG_OPEN(file, *args, **kwargs)

try:
    import pandas.io.common as _pic
    _orig_get_handle = _pic.get_handle
    def _get_handle(path_or_buf, *args, **kwargs):
        try:
            if str(path_or_buf) == _TARGET:
                path_or_buf = _LOCAL
        except Exception:
            pass
        return _orig_get_handle(path_or_buf, *args, **kwargs)
    _pic.get_handle = _get_handle
except Exception:
    pass

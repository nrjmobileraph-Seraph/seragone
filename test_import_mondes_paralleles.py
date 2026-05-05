import mondes_paralleles_engine as canon
import mondesparallelesengine as alias

assert hasattr(canon, "MondesParalleles")
assert hasattr(canon, "compute_sub_signals")
assert hasattr(alias, "MondesParalleles")
assert hasattr(alias, "compute_sub_signals")

print("OK_MondesParalleles_imports")

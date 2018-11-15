# -*- coding: utf-8 -*-
import re
def safe_int(s, default=None):
    try:
        return int(s)
    except (ValueError, TypeError):
        return default


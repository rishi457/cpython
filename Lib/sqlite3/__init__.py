"""
pysqlite2: DB-API 2.0 compliant interface to SQLite 3

Copyright (C) 2005 Gerhard Häring <gh@ghaering.de>

This file is part of pysqlite.

This software is provided 'as-is', without any express or implied warranty.
In no event will the authors be held liable for any damages arising from the
use of this software.

Permission is granted to anyone to use this software for any purpose, including
commercial applications, and to alter it and redistribute it freely, subject
to the following restrictions:

1. The origin of this software must not be misrepresented; you must not
   claim that you wrote the original software. If you use this software
   in a product, an acknowledgment in the product documentation would be
   appreciated but is not required.
2. Altered source versions must be plainly marked as such, and must not be
   misrepresented as being the original software.
3. This notice may not be removed or altered from any source distribution.
"""

import sqlite3.dbapi2 as dbapi2

__all__ = dbapi2.__all__
__version__ = dbapi2.sqlite_version
__sqlite_version__ = dbapi2.sqlite_version_info

_deprecated_names = dbapi2._deprecated_names

def __getattr__(name):
    if name in _deprecated_names:
        from warnings import warn

        warn(f"{name} is deprecated and will be removed in Python 3.14",
             DeprecationWarning, stacklevel=2)
        return globals()[f"_deprecated_{name}"]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

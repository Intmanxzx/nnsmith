try:
    from nnsmith._version import __version__, __version_tuple__
except ImportError:
    from importlib.metadata import PackageNotFoundError, version

    try:
        __version__ = version("nnsmith")
    except PackageNotFoundError:
        __version__ = "local-dev"

try:
    from nnsmith._version import __version__, __version_tuple__
except ImportError:
    from importlib.metadata import PackageNotFoundError, version

    try:
        # The PyPI distribution is "nnsmith-autofusex"; the import name stays "nnsmith".
        __version__ = version("nnsmith-autofusex")
    except PackageNotFoundError:
        __version__ = "local-dev"

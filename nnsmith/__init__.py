try:
    from nnsmith._version import __version__, __version_tuple__
except ImportError:
    from importlib.metadata import PackageNotFoundError, version

    try:
        # The PyPI distribution is "autofusex-nnsmith"; the import name stays "nnsmith".
        __version__ = version("autofusex-nnsmith")
    except PackageNotFoundError:
        __version__ = "local-dev"

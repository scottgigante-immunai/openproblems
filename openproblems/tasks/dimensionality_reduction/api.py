from ...data.sample import load_sample_data
from ...tools.decorators import dataset

import numpy as np


def check_dataset(adata):
    """Check that dataset output fits expected API."""
    return True


def check_method(adata, is_baseline=False):
    """Check that method output fits expected API."""
    assert "X_emb" in adata.obsm
    if not is_baseline:
        assert adata.obsm["X_emb"].shape[1] == 2
    assert np.all(np.isfinite(adata.obsm["X_emb"]))
    return True


@dataset()
def sample_dataset():
    """Create a simple dataset to use for testing methods in this task."""
    return load_sample_data()


def sample_method(adata):
    """Create sample method output for testing metrics in this task."""
    import scanpy as sc

    sc.tl.pca(adata)
    adata.obsm["X_emb"] = adata.obsm["X_pca"][:, :2]
    return adata

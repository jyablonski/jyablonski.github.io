import os
import tempfile

from server import app, freezer


def test_freezer_configuration():
    """Test that the freezer is configured correctly."""
    assert app.config["FREEZER_DESTINATION"] == "docs"


def test_freeze_builds_without_error():
    """Test that the freeze process completes without errors."""
    # Use a temporary directory to avoid overwriting the real docs folder
    with tempfile.TemporaryDirectory() as tmpdir:
        original_dest = app.config["FREEZER_DESTINATION"]
        app.config["FREEZER_DESTINATION"] = tmpdir

        try:
            # This should not raise any exceptions
            freezer.freeze()

            # Verify that files were created
            assert os.path.exists(tmpdir)
            files = os.listdir(tmpdir)
            assert len(files) > 0, "Freeze should generate output files"

            # Check that index.html was created
            assert os.path.exists(os.path.join(tmpdir, "index.html")), (
                "index.html should be generated"
            )

        finally:
            # Restore original configuration
            app.config["FREEZER_DESTINATION"] = original_dest

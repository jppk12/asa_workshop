
def test_module_import():
    try:
        import mymodule.sky_sim
    except Exception as e:
        raise AssertionError("Failed to import mymodule")
    return

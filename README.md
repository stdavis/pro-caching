# Generating Traditional Raster Caches with ArcGIS Pro

## Goal

Generate a traditional raster cache in the exploded format (one file per tile) using ArcGIS Pro (not ArcGIS Server).

## Issues

### Anti-aliasing ✅

I'm unable to generate a cache that uses anti-aliasing for feature geometry or text labels. This was originally logged as an enhancement request as a result of one of my support cases (ENH-000136615). The enhancement is marked as implemented at Pro v2.8, however, it doesn't appear to be working to me at v2.9.

Update (Nov 2022): A bug has been created for this in at v3.0.2: [BUG-000153899](https://my.esri.com/#/support/bugs/BUG-000153899).

Update (Mar 2025): This bug seems to have been fixed in v3.4. 👍

### Exploded format ✅

I'm also unable to create a cache in the exploded format. This is recorded as [BUG-000136613](https://my.esri.com/#/support/bugs/BUG-000136613) which is marked as a duplicate of [BUG-000158716](https://my.esri.com/#/support/bugs/BUG-000158716).

Update (Mar 2025): Esri support has confirmed that this bug is fixed in the upcoming v3.5 release. 👍

### Unable to restart cache generation

I'm unable to use the `RECREATE_EMPTY_TILES` parameter to update tiles for an existing cache in a stand-alone python script. I don't want to do our entire state-wide cache that takes days in a single job so I break it up. When I attempt to run the ManageTileCache tool with the `RECREATE_EMPTY_TILES` parameter, it fails with the following error:

```text
arcgisscripting.ExecuteError: Failed to execute. Parameters are not valid.
ERROR 000258: Output C:\projects\pro-caching\Cache\Terrain\Terrain already exists
Failed to execute (ManageTileCache).
```

This work just fine if you run the tool within Pro via the Python window, a notebook or in the geoprocessing tool dialog. It only fails when run in a stand-alone script.

## Steps to reproduce issues

1. `propy pro-test.py`
1. Notice error message that is returned.
1. Open `Maps.aprx`
1. Run the following code in a notepad or Python window:

```python
arcpy.management.ManageTileCache(
    in_cache_location=r"C:\projects\pro-caching\Cache",
    manage_mode="RECREATE_EMPTY_TILES",
    in_cache_name="Terrain",
    in_datasource="Terrain",
    tiling_scheme="ARCGISONLINE_SCHEME",
    import_tiling_scheme=None,
    scales=[18489297.737236],
    area_of_interest=r"C:\projects\pro-caching\data.geodatabase\main.test_extent",
    max_cell_size=None,
    min_cached_scale=591657527.591555,
    max_cached_scale=70.5310735,
    ready_to_serve_format="NON_READY_TO_SERVE_FORMAT"
)
```

Notice that it works when run within Pro, but not in the `pro-test.py` script.

## History

### 6/30/2023

Verified that both bugs still exist at `v3.1.2`. 😞

### 6/18/2024

Verified that both bugs still exist at `v3.3.0`. 😞
Tried both DirectX 11 and 12 with and without hardware acceleration. No change.

### 3/20/2025

Verified that antialiasing is fixed and exploded format will be fixed. Found the restart bug.

# Generating Traditional Raster Caches with ArcGIS Pro

## Goal

Generate a traditional raster cache in the exploded format (one file per tile) using ArcGIS Pro (not ArcGIS Server).

## Issues

### Exploded format ✅

I'm also unable to create a cache in the exploded format. This is recorded as [BUG-000136613](https://my.esri.com/#/support/bugs/BUG-000136613) which is marked as a duplicate of [BUG-000158716](https://my.esri.com/#/support/bugs/BUG-000158716).

Update (Mar 2025): Esri support has confirmed that this bug is fixed in the upcoming v3.5 release. 👍

### Unable to write JPEGs ❌

I have been unable to get the `ManageTileCache` tool to write JPEGs. I have tried using the ``import_tiling_scheme` parameter to import a tiling scheme that has JPEG as the format, but it still writes PNGs. I have also tried pointing the tool at an existing cache with a tiling scheme file that has the JPEG format, but it still writes PNGs.

## Steps to reproduce issues above

1. `propy pro-test.py`
1. Open `Maps.aprx`
1. Notice that the `Format` is set to `Cache/PNG` in the properties of the `Cache/Existing/Terrain` cache.
1. Notice that their is a bundle file in `Cache/Exploded/_alllayers/L04` and not individual image files.
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

## Possible Improvements

It would be nice if there was a way to generate caches directly to the exploded format. I was not able to make this happen. There does not seem to be a related parameter in the `ManageTileCache` tool and it seems to ignore the `CacheStorageInfo` setting in the `config.xml` file.

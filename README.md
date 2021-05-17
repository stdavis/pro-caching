# Generating Traditional Raster Caches with ArcGIS Pro

## Goal

Generate a traditional raster cache in the exploded format (one file per tile) using ArcGIS Pro (not ArcGIS Server).

## Issues

### Anti-aliasing

I'm unable to generate a cache that uses anti-aliasing for feature geometry or text labels.

### Exploded format

I'm also unable to create a cache in the exploded format.

## Steps to reproduce issues

1. ArcGIS Pro -> Options -> Display
![screenshot](options.png)
1. `pypro pro-test.py`
1. Open `Maps.aprx`
1. Compare source map "Terrain" to "Preview" and notice that the anti-alias settings were not honored when the cache was built.
![screenshot](compare.png)
1. Open `.\Cache\Exploded\_alllayers\L12` and notice that the cache is still in the compact format despite "EXPLODED" to "storage_format_type"
![screenshot](bundle.png)

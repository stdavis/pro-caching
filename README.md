# Generating Traditional Raster Caches with ArcGIS Pro

## Goal

Generate a traditional raster cache in the exploded format (one file per tile) using ArcGIS Pro (not ArcGIS Server).

## Issues

### Anti-aliasing

I'm unable to generate a cache that uses anti-aliasing for feature geometry or text labels. This was originally logged as an enhancement request as a result of one of my support cases (ENH-000136615). The enhancement is marked as implemented at Pro v2.8, however, it doesn't appear to be working to me. Perhaps I'm missing something?

### Exploded format

I'm also unable to create a cache in the exploded format. This is recorded as BUG-000136613. It shows that this is in the product plan. 👍

## Steps to reproduce issues

1. ArcGIS Pro -> Options -> Display
![screenshot](options.png)
1. `pypro pro-test.py`
1. Open `Maps.aprx`
1. Compare source map "Terrain" to "Preview" and notice that the anti-alias settings were not honored when the cache was built.
![screenshot](compare.png)
1. Open `.\Cache\Exploded\_alllayers\L12` and notice that the cache is still in the compact format despite "EXPLODED" to "storage_format_type"
![screenshot](bundle.png)

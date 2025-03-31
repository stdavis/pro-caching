import arcpy
from pathlib import Path
from shutil import rmtree

current_directory = Path(__file__).parent.absolute()
pro_project_path = current_directory / "Maps.aprx"
cache_directory = current_directory / "Cache"

if cache_directory.exists():
    print(f"clearing out: {str(cache_directory)}")
    rmtree(cache_directory)
    cache_directory.mkdir()

local_project = arcpy.mp.ArcGISProject(pro_project_path)
pro_map = local_project.listMaps("Terrain")[0]
test_extent = current_directory / "data.geodatabase" / "main.test_extent"

arcpy.env.parallelProcessingFactor = '100%'
arcpy.env.overwriteOutput = True

print("building cache")
arcpy.management.ManageTileCache(
    str(cache_directory),
    manage_mode="RECREATE_ALL_TILES",
    in_cache_name="Terrain",
    in_datasource=pro_map,
    tiling_scheme="ARCGISONLINE_SCHEME",
    area_of_interest=str(test_extent),
    min_cached_scale=591657527.591555,
    max_cached_scale=9027.977411,
    scales=[36978595.474472],
)

print("exploding cache")
#: This tool does not output in the exploded format despite passing "EXPLODED" to "storage_format_type"
#: Should be fixed in Pro v3.5 (Ref: BUG-000158716)
arcpy.management.ExportTileCache(
    str(cache_directory / "Terrain" / "Terrain"),
    str(cache_directory),
    "Exploded",
    export_cache_type="TILE_CACHE",
    storage_format_type="EXPLODED",
)

print("building jpegs")
arcpy.management.ManageTileCache(
    str(cache_directory),
    manage_mode="RECREATE_EMPTY_TILES",
    in_cache_name="Existing",
    in_datasource=pro_map,
    tiling_scheme="ARCGISONLINE_SCHEME",
    area_of_interest=str(test_extent),
    min_cached_scale=591657527.591555,
    max_cached_scale=9027.977411,
    scales=[18489297.737236],
)

import arcpy
from pathlib import Path
from shutil import rmtree

current_directory = Path(__file__).parent.absolute()
pro_project_path = current_directory / 'Maps.aprx'
cache_directory = current_directory / 'Cache'

if cache_directory.exists():
    print(f'clearing out: {str(cache_directory)}')
    rmtree(cache_directory)
    cache_directory.mkdir()

local_project = arcpy.mp.ArcGISProject(pro_project_path)
pro_map = local_project.listMaps('Terrain')[0]

arcpy.env.parallelProcessingFactor = 4

print('building cache')
test_extent = current_directory / 'data.geodatabase' / 'main.test_extent'
#: ISSUE 1 - This tool isn't honoring the anti-aliasing setting the Pro -> Options -> Display
#: It doesn't look like this enhancement was actually implemented: ENH-000136615
arcpy.management.ManageTileCache(str(cache_directory.parent), manage_mode='RECREATE_ALL_TILES',
    in_cache_name='Cache', in_datasource=pro_map, tiling_scheme='ARCGISONLINE_SCHEME',
    area_of_interest=str(test_extent), min_cached_scale=591657527.591555, max_cached_scale=9027.977411)

print('exploding cache')
#: ISSUE 2 - This tool does not output in the exploded format despite passing "EXPLODED" to "storage_format_type"
arcpy.management.ExportTileCache(str(cache_directory / 'Terrain'), str(cache_directory), 'Exploded',
    export_cache_type='TILE_CACHE', storage_format_type='EXPLODED')

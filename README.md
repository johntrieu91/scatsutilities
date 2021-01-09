# scatsutilities 

![](https://github.com/johntrieu91/scatsutilities/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/johntrieu91/scatsutilities/branch/main/graph/badge.svg)](https://codecov.io/gh/johntrieu91/scatsutilities) ![Release](https://github.com/johntrieu91/scatsutilities/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/scatsutilities/badge/?version=latest)](https://scatsutilities.readthedocs.io/en/latest/?badge=latest)

Python package providing utilities to process SCATS traffic system data

## Installation

```bash
$ pip install scatsutilities
```

## Features

- Processing and conversion of LX files (showing offsets and linkages between SCATS sites) to GIS compatible files (geopackages, gpkg)

## Dependencies

- Geopandas 0.8+
- Pandas 1.0+
- Shapely 1.7+

See poetry.lock for a list of dependencies.

## Usage

### Make directories
```python
>>> from scatsutilities import scatsutilities
>>> from pathlib import Path
>>> input_folder_path = 'path/to/dir'
>>> scatsutilities.make_output_dir(input_folder_path)
```

### Process LX files to create GIS files

```python
>>> from scatsutilities import scatsutilities
>>> from pathlib import Path
>>> lx_file_path = 'path/to/lx/file.lx'
>>> scats_sites_path = 'path/to/scats/locations.csv'
>>> output_folder = 'path/to/dir'
>>> df, error_ints, error_subsys = scatsutilities.lx_to_gis(lx_file_path=lx_file_path,
                                                            scats_sites_path=scats_sites_path,
                                                            col_scats_x='Longitude',
                                                            col_scats_y='Latitude',
                                                            scats_input_crs_id=4326,
                                                            scats_projected_crs_id=8058,
                                                            output_folderPath_LX_processed=output_folder,
                                                            output_gis_folderPath=output_folder,
                                                            break_at_nonNumeric=True,
                                                            search_term_intID='INT=',
                                                            search_term_subsystem='S#=',
                                                            search_term_pp='PP',
                                                            search_term_subsystemData='SS=',
                                                            search_limit=20,
                                                            skip_initial_lines=10)
```

## Documentation

The official documentation is hosted on Read the Docs: https://scatsutilities.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/johntrieu91/scatsutilities/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).

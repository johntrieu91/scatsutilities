from pathlib import Path
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString

def pp_breakdown(plan_item, break_at_nonNumeric):
    """
    Helper function to extract Phase Plan (PP) data from the SCATS LX files
    PP data defines the "internal reference point" for each intersection that offsets are
    calculated from. 
    The data is normally reported 2x PP per line
    This function will break the two components up and return a list with the offset data

    Parameters
    ----------
    plan item : str
        Line from the LX file (as str) in the format:
        `PP1=0,0F!PP2=0,0F!`
        Or similar
    break_at_nonNumeric : bool
        Tag for whether to raise Exception and break function call if 
        `connected_site` output is non-numeric.
        If True, this will raise an Exception.
        If False, this will override the `connected_site` ID to '-2' 
        (to distinguish it from other sites with no link which are '-1')
        
    Returns
    -------
    output : list
        [offset1, offset2, offset_start, offset_phase, connected_site]
        [lower offset number, upper offset number, tag if offset is start-of-phase, 
        phase of offset, site linked to (if relevant)]
        connected_site is `-1` unless it has an SL tag, and slaved to another site
    """
    connected_site = '-1' # needed to manage UnboundLocalError
    
    try:
        plan_item_split = plan_item.split(',')

        if len(plan_item_split) == 1:
            if 'SL' in plan_item_split[0]:
                plan_item_split_SL = plan_item_split[0].split('SL')
                offset1 = plan_item_split_SL[0]
                offset2 = plan_item_split_SL[0]

                temp = plan_item_split_SL[1]
                if '^' in temp:
                    offset_start = 1
                else:
                    offset_start = 0

                if offset_start:
                    temp = temp.split('^')
                    connected_site = temp[0]
                    offset_phase = temp[1]
                else:
                    connected_site = temp[:-1]
                    offset_phase = temp[-1]

                output = [offset1, offset2, offset_start,
                          offset_phase, connected_site]
                # print(output)

            else:
                output = ['-1', '-1', '-1', 'ERR', '-1']
        else:
            offset1 = plan_item_split[0]
            temp = plan_item_split[1]

            if '^' in temp:
                offset_start = 1
            else:
                offset_start = 0

            if offset_start:
                temp = temp.split('^')
                offset2 = temp[0]
                offset_phase = temp[1]
            else:
                offset2 = temp[:-1]
                offset_phase = temp[-1]

            # not slaved to another site
            connected_site = -1

            output = [offset1, offset2, offset_start,
                      offset_phase, connected_site]
            # print(output)
    except:
        print('ERROR')
        print(plan_item, plan_item_split)
        connected_site = '-1'
        output = ['-1', '-1', '-1', 'ERR', '-1']
    
    # check if the site ID linked is valid
    try:
        int(connected_site)
    except ValueError as e:
        print(f'[ERROR] Non-numeric linked site {connected_site} \n',
              'Check and fix LX file -> all Site IDs should be integers')
        if break_at_nonNumeric:
            raise ValueError
        else:
            output = output[0:4]
            output.append('-2')

    return output

def lp_breakdown(plan_item, break_at_nonNumeric):
    """
    Helper function to extract Link Plan (LP) data from the SCATS LX files
    LP data defines offsets between intersections (and between the internal reference point
    defined in the PP data)
    The data is normally reported 1x LP per line (note: different to PP data)
    This function will return a list with the offset data
    
    Parameters
    ----------
    plan item : str
        Line from the LX file (as str) in the format:
        `LP1=6,10A3118!`
        Or similar
    break_at_nonNumeric : bool
        Tag for whether to raise Exception and break function call if 
        `connected_site` output is non-numeric.
        If True, this will raise an Exception.
        If False, this will override the `connected_site` ID to '-2' 
        (to distinguish it from other sites with no link which are '-1')
    
    Returns
    -------
    output : list
        [offset1, offset2, offset_start, offset_phase, connected_site]
        [lower offset number, upper offset number, tag if offset is start-of-phase, 
        phase of offset, site linked to (if relevant)]
    """
    connected_site = '-1' # needed to manage UnboundLocalError
    
    try:
        plan_item_split = plan_item.split(',')

        if len(plan_item_split) == 1:
            if 'SL' in plan_item_split[0]:
                plan_item_split_SL = plan_item_split[0].split('SL')
                offset1 = plan_item_split_SL[0]
                offset2 = plan_item_split_SL[0]

                temp = plan_item_split_SL[1]
                if '^' in temp:
                    offset_start = 1
                else:
                    offset_start = 0

                if offset_start:
                    temp = temp.split('^')
                    connected_site = temp[0]
                    offset_phase = temp[1]
                else:
                    connected_site = temp[:-1]
                    offset_phase = temp[-1]

                output = [offset1, offset2, offset_start, offset_phase, connected_site]
                # print(output)
            else:
                # no linkages
                output = ['0', '0', '0', '0', '0']
        else:
            offset1 = plan_item_split[0]
            temp = plan_item_split[1]

            if '^' in temp:
                offset_start = 1
            else:
                offset_start = 0

            if offset_start:
                temp = temp.split('^')
                offset2 = temp[0]
                offset_phase = temp[1][0]
                connected_site = temp[1][1:]
            else:
                # e.g. 30B1073
                phase_char = 0
                for index, char in enumerate(temp):
                    if not char.isnumeric():
                        phase_char = index
                
                offset2 = temp[:phase_char]
                offset_phase = temp[phase_char]
                connected_site = temp[phase_char+1 :]

            output = [offset1, offset2, offset_start, offset_phase, connected_site]
            # print(output)
    except:
        print(f'[ERROR] Processing subsystem data: {plan_item}, split to {plan_item_split}')
        connected_site = '-1'
        output = ['-1', '-1', '-1', 'ERR', '-1']
    
    # check if the site ID linked is valid
    try:
        int(connected_site)
    except ValueError as e:
        print(f'[ERROR] Non-numeric linked site {connected_site} \n',
              'Check and fix LX file -> all Site IDs should be integers')
        if break_at_nonNumeric:
            raise ValueError
        else:
            output = output[0:4]
            output.append('-2')
        
    return output

def make_output_dir(input_folder_path):
    """
    Makes output folder path if it does not exist
    
    Parameters
    ----------
    folder_path : str or PosixPath
        Folder path
    
    Returns
    -------
    None
    """
    Path(input_folder_path).mkdir(parents=True, exist_ok=True)


def lx_to_gis(lx_file_path, 
              scats_sites_path, 
              col_scats_x='Longitude', 
              col_scats_y='Latitude', 
              scats_input_crs_id=4326, 
              scats_projected_crs_id=8058, 
              output_folderPath_LX_processed=None, 
              output_gis_folderPath=None,
              break_at_nonNumeric=True,
              search_term_intID='INT=',
              search_term_subsystem='S#=',
              search_term_pp='PP',
              search_term_subsystemData='SS=',
              search_limit=20,
              skip_initial_lines=10):
    """
    Reads SCATS LX file and exports Phase Plan and Link Plan data as table and geopackages.
    
    Used to process SCATS LX files, extract the Phase Plan (PP) and Link Plan (LP) data. This data is
    processed and converted into a dataframe table, and also exported as a multi-layer geopackage. 
    
    Parameters
    ----------
    lx_file_path : str or PosixPath
        File path to the SCATS LX file
        
    scats_sites_path : str or PosixPath
        File path to the csv file identifying the SCATS Site ID number, and the associated
        latitude and longitude coordinates of each site. 
        Example for New South Wales, Australia is available from:
        https://opendata.transport.nsw.gov.au/dataset/traffic-lights-location
        (as at 8 January 2021)
    
    col_scats_x : str, optional
        Name of column in `scats_sites_path` with the x-coordinate data for each 
        SCATS site (by Site ID)
        Default value is 'Longitude'
        
    col_scats_y : str, optional
        Name of column in `scats_sites_path` with the y-coordinate data for each 
        SCATS site (by Site ID)
        Default value is 'Latitude'
    
    scats_input_crs_id : int, optional
        Coordinate system of the x,y coordinates from `scats_sites_path`, as EPSG id number
        Default value is 4326, which refers to EPSG:4326 and the WGS 84 projection system
        (i.e. conventional lat/long coordinates)
        
    scats_projected_crs_id : int, optional
        Coordinate system to transfer the `scats_sites_path` coordinate data into, as EPSG id number
        It is STRONGLY RECOMMENDED to use a project coordinate system (e.g. GDA2020 MGA Zone xx, or GDA2020 Lambert)
        Default value is 8058, which refers to EPSG:8058 and the GDA2020 NSW Lambert projection system
        This is a projected coordinate system
        
    output_folderPath_LX_processed : str or PosixPath, optional
        Folder path to export the processed LX data to
        Default value is None, which will not export a file
    
    output_gis_folderPath : str or PosixPath, optional
        Folder path to export the process LX data as GIS geopackages (.gpkg)
        Default value is None, which will not export a file

    break_at_nonNumeric : bool, optional
        Tag to decide if the code should break at each invalid Site ID or Subsystem ID to allow user
        to review and investigate LX file.
        If set to False, the code will record a '-2' code in the `connected_site` output data 
        Default value is True, which will cause the code to break everytime it encounters an 
        invalid Site ID or Subsystem ID.
    
    search_term_intID : str, optional
        For debugging only
        Search term to identify lines with the Site ID number (as string)
        Default value is 'INT=', which is the search term
        
    search_term_subsystem : str, optional
        For debugging only
        Search term to identify lines with the Subsystem ID number applicable to the Site ID
        Default value is 'S#=', which is the search term
        
    search_term_pp : str, optional
        For debugging only
        Search term to identify lines with the Phase Plan (PP) (as string)
        Default value is 'PP', which is the search term
        
    search_term_subsystemData : str, optional
        For debugging only
        Search term to identify lines with the Subsystem ID number 
        (as string) containing the Link Plan (LP) data
        Default value is 'SS=', which is the search term
        
    search_limit : int, optional
        For debugging only
        Maximum number of lines to search in LX file for PP and LP data 
        (after finding the Site ID or Subsystem ID)
        Default value is 20, which will search through a maximum of 20 lines
        
    skip_initial_lines : int, optional
        For debugging only
        Used in `search_term_subsystemData` search to skip over the metadata in initial rows
        Default value is 10, which will skip the initial 10 lines of the LX file
    
    Outputs
    -------
    df : pandas.DataFrame
        Dataframe of processed LX data, with:
        - INT_ID, SUBSYSTEM_ID, PP1, PP2, PP3, PP4
        - SUBSYSTEM_ID, LP1, LP2, LP3, LP4
    
    error_ints : ::list:: of str
        List of Site IDs with invalid data
        Format of ['Site ID', 'Error message']
        
    error_subsys : ::list:: of str
        List of Subsystem IDs with invalid data
        Format of ['Site ID', 'Error message']
        
    Exports
    -------
    df : CSV file

    
    """
    ### PART 1 - READ IN DATA
    # Read LX file
    # NOTE: this has been changed to a context manager, 
    # with file read only where required later in the code

    
    # Read SCATS site location data
    df_scatsLoc = pd.read_csv(Path(scats_sites_path))
    # convert to gpd.GeoDataFrame
    gdf_scatsLoc = gpd.GeoDataFrame(df_scatsLoc, 
                                    geometry=gpd.points_from_xy(df_scatsLoc[col_scats_x], df_scatsLoc[col_scats_y]))
    # set CRS
    gdf_scatsLoc = gdf_scatsLoc.set_crs(epsg=scats_input_crs_id)
    # re-project to NSW Lambert (project coordinate system)
    if scats_projected_crs_id:
        gdf_scatsLoc = gdf_scatsLoc.to_crs(epsg=scats_projected_crs_id)
    
    ### PART 2 - EXTRACT LX FILE DATA
    # initialise lists
    lx_int_data = [] # stores the final PP data
    lx_subsys_data = [] # stores the final LP data
    error_ints = [] # stores any intersection PP with errors
    error_subsys = [] # stores any subsystem LP with errors
    
    
    ### PART 2A - INTERSECTION PHASE PLAN DATA
    # iterate through LX file to extract PP data
    with open(Path(lx_file_path), 'r') as f:
        lines = f.readlines()
        
        for count, line in enumerate(lines):
            site_data = [] # temp storage of data
            # search for lines with intersection ID number
            if search_term_intID in line:
                line_items = line.strip().split('!')
                # take index=1 with `INT=`
                site_id = line_items[1]
                # split on `=` and take index=1 with the TCS ID
                site_id = site_id.split('=')
                site_id = site_id[1].strip()

                try:
                    int(site_id)
                    site_data.append(site_id)
                except ValueError as e:
                    if break_at_nonNumeric:
                        print(f'[ERROR] Non-numeric Site ID identified: {site_id}, ValueError: {e}')
                        # add to error list with message
                        error_ints.append([site_id, 'Non-numeric Site ID'])
                        raise ValueError
                    else:
                        print(f'[WARNING] Non-numeric Site ID identified: {site_id}, ValueError: {e}')
                        # add to error list with message
                        error_ints.append([site_id, 'Non-numeric Site ID'])
                        # return to start of loop because site ID is invalid
                        continue

                # search for lines with subsystem ID number, within a few rows of the intersection ID number
                line_n_search = count
                stop_loop = 0
                while not stop_loop:
                    if search_term_subsystem in lines[line_n_search]:
                        subsystem_line_items = lines[line_n_search].strip().split('!')
                        # take index=0 with `S#=`
                        subsystem_id = subsystem_line_items[0]
                        # split on `=` and take index=1 with the Subsystem ID
                        subsystem_id = subsystem_id.split('=')
                        subsystem_id = subsystem_id[1].strip()
                        
                        try:
                            int(subsystem_id)
                            site_data.append(subsystem_id)
                            # found what we were looking for -> set breaking condition for loop
                            stop_loop = 1
                        except ValueError as e:
                            if break_at_nonNumeric:
                                print(f'[ERROR] Non-numeric Subsystem ID: {subsystem_id}, ValueError: {e}')
                                # add to error list with message
                                error_ints.append([site_id, f'Non-numeric Subsystem ID {subsystem_id} for Site ID'])
                                raise ValueError
                            else:
                                print(f'[WARNING] Non-numeric Subsystem ID: {subsystem_id}, ValueError: {e}')
                                # add to error list with message
                                error_ints.append([site_id, f'Non-numeric Subsystem ID {subsystem_id} for Site ID'])
                                # allow search to continue, in case valid subsystem available

                    # prevent infinite loop
                    # didn't find what we were looking for -> set breaking condition for loop
                    if line_n_search > (count + search_limit):
                        stop_loop = 1
                        # add to error list with message
                        error_ints.append([site_id, 'Subsystem not found'])

                    # increment line number
                    line_n_search += 1

                # search for lines with Phase Plan (PP) data, within a few rows of the intersection ID number
                # this defines the local offset point for the intersection
                # PP1 -> PP4
                # reminder: range(1,5,2) means [1, 3]
                # reminder: SCATS LX PP data comes over 2 lines, such as:
                # PP1=0,0F!PP2=0,0F!
                # PP3=0,0F!PP4=0,0F!
                # therefore, can extract two PP at a time
                for pp_id in range(1,5,2):
                    line_n_search = count
                    stop_loop = 0
                    search_term_pp = f'PP{pp_id}='
                    print(f'[INFO] Processing Site {site_id}, PP{pp_id}')

                    while not stop_loop:
                        if search_term_pp in lines[line_n_search]:
                            pp_line_items = lines[line_n_search].strip().split('!')

                            # get first PP (PP1 or PP3)
                            pp_item = pp_line_items[0]
                            # split on `=` and take index=1 with the PP data
                            pp_item = pp_item.split('=')
                            pp_item = pp_item[1].strip()
                            # append PP1 data
                            site_data.append(pp_item)
                            # extract PP1 metadata
                            pp_data = pp_breakdown(pp_item, break_at_nonNumeric)
                            for pp_data_item in pp_data:
                                site_data.append(pp_data_item)

                            # get second PP (PP2 or PP4)
                            pp_item = pp_line_items[1]
                            # split on `=` and take index=1 with the PP data
                            pp_item = pp_item.split('=')
                            pp_item = pp_item[1].strip()
                            # append PP2 data
                            site_data.append(pp_item)
                            # extract PP2 metadata
                            pp_data = pp_breakdown(pp_item, break_at_nonNumeric)
                            for pp_data_item in pp_data:
                                site_data.append(pp_data_item)

                            # found what we were looking for -> set breaking condition for loop
                            stop_loop = 1

                        # prevent infinite loop
                        # didn't find what we were looking for -> set breaking condition for loop
                        if line_n_search > (count + search_limit):
                            stop_loop = 1
                            # add to error list with message
                            error_ints.append([site_id, 'Subsystem not found'])

                        # increment line number
                        line_n_search += 1

            # if we have all the data we need, append to the main list
            ### UPDATE to be desired number of parameters when all done
            if len(site_data) > 0:
                lx_int_data.append(site_data)

        print(f'[INFO] Number of PP plan items identified: {len(lx_int_data)}')
    
        ### PART 2B - SUBSYSTEM LINK PLAN DATA
        # iterate through LX file to extract LP data
        for count, line in enumerate(lines):
            subsys_data = [] # temp storage of data
            # search for lines with subsystem ID number (second section search)
            if (search_term_subsystemData in line) and (count > skip_initial_lines):
                line_items = line.strip().split('!')
                # take index=0 with `SS=`
                subsys_id = line_items[0].strip()
                # split on `=` and take index=1 with the Subsystem ID
                subsys_id = subsys_id.split('=')
                subsys_id = subsys_id[1].strip()

                subsys_data.append(subsys_id)


                # search for lines with Link Plan (LP) data, within a few rows of the subsystem ID number
                # this defines the offset point from other linked intersections
                # LP1 -> LP4
                # reminder: range(1,5) means [1, 2, 3, 4]
                # reminder: SCATS LX LP data comes over 4 lines -> need to extract one at a time
                for lp_id in range(1,5):
                    line_n_search = count
                    stop_loop = 0
                    search_term_lp = f'LP{lp_id}='
                    print(f'[INFO] Processing Subsystem {subsys_id}, LP{lp_id}')
                    
                    while not stop_loop:
                        if search_term_lp in lines[line_n_search]:
                            lp_line_items = lines[line_n_search].strip().split('!')

                            # get the LP data
                            lp_item = lp_line_items[0]
                            # split on `=` and take index=1 with the Subsystem ID
                            lp_item = lp_item.split('=')
                            lp_item = lp_item[1].strip()
                            # append LP data
                            subsys_data.append(lp_item)
                            # extract LP metadata
                            lp_data = lp_breakdown(lp_item, break_at_nonNumeric)
                            for lp_data_item in lp_data:
                                subsys_data.append(lp_data_item)

                            # found what we were looking for -> set breaking condition for loop
                            stop_loop = 1

                        # prevent infinite loop
                        # didn't find what we were looking for -> set breaking condition for loop
                        if line_n_search > (count + search_limit):
                            stop_loop = 1
                            # add to error list with message
                            error_subsys.append([subsys_id, 'Subsystem not found'])

                        # increment line number
                        line_n_search += 1

                # if we have all the data we need, append to the main list        
                ### UPDATE to be desired number of parameters when all done
                if len(subsys_data) > 0:
                    lx_subsys_data.append(subsys_data)

        print(f'[INFO] Number of LP plan items identified: {len(lx_subsys_data)}')
    
    print(f'[INFO] Parsed through LX file - relevant data extracted')
    
    ### PART 3 - CONVERT LX DATA TO DATAFRAMES
    # set column names
    columns_intData = ['site_id', 'subsystem_id',
                       'PP1_data', 'PP1_offset1', 'PP1_offset2', 'PP1_phaseStart', 'PP1_phase', 'PP1_slaved',
                       'PP2_data', 'PP2_offset1', 'PP2_offset2', 'PP2_phaseStart', 'PP2_phase', 'PP2_slaved',
                       'PP3_data', 'PP3_offset1', 'PP3_offset2', 'PP3_phaseStart', 'PP3_phase', 'PP3_slaved',
                       'PP4_data', 'PP4_offset1', 'PP4_offset2', 'PP4_phaseStart', 'PP4_phase', 'PP4_slaved']

    columns_subsysData = ['subsystem_id',
                          'LP1_data', 'LP1_offset1', 'LP1_offset2', 'LP1_phaseStart', 'LP1_phase', 'LP1_slaved',
                          'LP2_data', 'LP2_offset1', 'LP2_offset2', 'LP2_phaseStart', 'LP2_phase', 'LP2_slaved',
                          'LP3_data', 'LP3_offset1', 'LP3_offset2', 'LP3_phaseStart', 'LP3_phase', 'LP3_slaved',
                          'LP4_data', 'LP4_offset1', 'LP4_offset2', 'LP4_phaseStart', 'LP4_phase', 'LP4_slaved']
    
    # create dataframes
    df_intData = pd.DataFrame(lx_int_data, columns=columns_intData)
    df_subsys = pd.DataFrame(lx_subsys_data, columns=columns_subsysData)
    # merge dataframes
    df = df_intData.merge(df_subsys, on='subsystem_id', how='left')
    # fill any locations with no data with -1
    df = df.fillna(-1) # tag for no data
    
    # convert site_id to integer
    df['site_id'] = df['site_id'].astype('int')
    df['PP1_slaved'] = df['PP1_slaved'].astype('int')
    df['PP2_slaved'] = df['PP2_slaved'].astype('int')
    df['PP3_slaved'] = df['PP3_slaved'].astype('int')
    df['PP4_slaved'] = df['PP4_slaved'].astype('int')
    df['LP1_slaved'] = df['LP1_slaved'].astype('int')
    df['LP2_slaved'] = df['LP2_slaved'].astype('int')
    df['LP3_slaved'] = df['LP3_slaved'].astype('int')
    df['LP4_slaved'] = df['LP4_slaved'].astype('int')
    
    # sort values
    df = df.sort_values(by=['site_id'])
    
    if output_folderPath_LX_processed:
        # check if directories exist; create if not
        make_output_dir(output_folderPath_LX_processed)
        # export file
        lx_fileName = Path(lx_file_path)
        lx_fileName = lx_fileName.stem
        df.to_csv(Path(output_folderPath_LX_processed,f'LX_processed_{lx_fileName}.csv'), index=False)
    
    ### PART 4 - CONVERT TO GIS / GEODATAFRAME
    # reduce the gdf to only the columns required for merging
    gdf_scatsLoc_merge = gdf_scatsLoc[['Equipment_ID', 'geometry']]
    # merge point data
    df = df.merge(gdf_scatsLoc_merge, left_on='site_id', right_on='Equipment_ID', how='left')
    df = df.drop(columns=['Equipment_ID'])
    # convert back into gpd.GeoDataFrame
    gdf_lx = gpd.GeoDataFrame(df, geometry='geometry')
    
    # extract sites with no geometry data for review
    gdf_lx_noData = gdf_lx.loc[gdf_lx.geometry == None]
    if output_gis_folderPath:
        # check if directories exist; create if not
        make_output_dir(output_gis_folderPath)
        # export file
        gdf_lx_noData.to_csv(Path(output_gis_folderPath)/'gdf_lx_noGeometry.csv', index=False)
    # delete the sites without geometry data
    gdf_lx = gdf_lx.loc[gdf_lx.geometry != None]
    
    ### PART 5 - EXPORT TO GPKG
    # extract data by plans (1..4)
    for plan_id in range(1, 5):
        print(f'[INFO] Exporting geopackage for Plan ID: {plan_id}')

        # reduce the SCATS locations gdf to only the columns required for merging
        gdf_scatsLoc_merge = gdf_scatsLoc[['Equipment_ID', 'geometry']]

        # PART 5A - CREATE PPx DATA EXPORT
        # Show the internal reference point of each intersection
        # setup columns names to extract
        column_names = ['site_id', 'subsystem_id',
                        f'PP{plan_id}_data', f'PP{plan_id}_offset1', f'PP{plan_id}_offset2',
                        f'PP{plan_id}_phaseStart', f'PP{plan_id}_phase', f'PP{plan_id}_slaved',
                        f'LP{plan_id}_data', f'LP{plan_id}_offset1', f'LP{plan_id}_offset2',
                        f'LP{plan_id}_phaseStart', f'LP{plan_id}_phase', f'LP{plan_id}_slaved',
                        'geometry']

        # filter gdf
        gdf = gdf_lx[column_names]

        # rename the PPx_Data and LPx_Data columns -> this will make creating generic GIS styles easier
        gdf = gdf.rename(columns={f'PP{plan_id}_data': 'PP_data',
                                  f'LP{plan_id}_data': 'LP_data'})

        # export to file by plan_id
        if output_gis_folderPath:
            # check if directories exist; create if not
            make_output_dir(output_gis_folderPath)
            # export file
            export_filename = f'LX_plan{plan_id}_{lx_fileName[:-3]}.gpkg'
            layer_name = f'PP{plan_id}_data'
            gdf.to_file(Path(output_gis_folderPath)/export_filename,
                        driver='GPKG',
                        layer=layer_name)

        # PART 5B - CREATE LPx DATA EXPORTS
        # Show the adjacent sites the intersection is linked to
        # Note: LPx = standard linkage between sites, SL = SLaved & hard-linkage

        # rename the geometry column to minimise conflict with later LP data joins
        gdf = gdf.rename(columns={'geometry': 'geometry_PP'})

        # merge point data
        gdf = gdf.merge(gdf_scatsLoc_merge,
                        left_on=f'LP{plan_id}_slaved',
                        right_on='Equipment_ID',
                        how='left')
        gdf = gdf.drop(columns=['Equipment_ID'])

        # rename the geometry column to minimise conflict with geometry for LineString
        gdf = gdf.rename(columns={'geometry': 'geometry_LP'})

        # delete any rows where LP_geometry is None -> we don't need these (and will cause error anyway)
        gdf = gdf.loc[gdf.geometry_LP != None]

        # check if df is empty
        # skip export if empty - there's nothing anyway
        if gdf.shape[0] > 0:
            # create LineString for LP linkages
            gdf['geometry'] = None
            for row in gdf.itertuples():
                gdf.loc[row.Index, 'geometry'] = LineString([row.geometry_PP, row.geometry_LP])

            # export to file by plan_id
            # create export-specific variable & drop PP and LP geometry columns
            # (multiple geometry columns cause errors)
            gdf_export = gdf.drop(columns=['geometry_PP', 'geometry_LP'])
            # export file
            if output_gis_folderPath:
                # check if directories exist; create if not
                make_output_dir(output_gis_folderPath)
                # export file
                export_filename = f'LX_plan{plan_id}_{lx_fileName[:-3]}.gpkg'
                layer_name = f'LP{plan_id}_data'
                gdf_export.to_file(Path(output_gis_folderPath)/export_filename,
                                   driver='GPKG', layer=layer_name)
        else:
            print('[INFO] No LP sites')

        # PART 5C - CREATE SL DATA EXPORTS
        # Show the adjacent sites the intersection is linked to
        # Note: LPx = standard linkage between sites, SL = SLaved & hard-linkage

        # delete the 'geometry' column -> this will be re-created later for the SL sites
        try:
            gdf = gdf.drop(columns=['geometry'])
        except KeyError:
            print('[WARNING] `geometry` column not in df. This may be an expected outcome if there was no LP export')

        # merge point data
        gdf = gdf.merge(gdf_scatsLoc_merge,
                        left_on=f'PP{plan_id}_slaved',
                        right_on='Equipment_ID',
                        how='left')
        gdf = gdf.drop(columns=['Equipment_ID'])

        # rename the geometry column to minimise conflict with geometry for LineString
        gdf = gdf.rename(columns={'geometry': 'geometry_SL'})

        # delete any rows where LP_geometry is None -> we don't need these (and will cause error anyway)
        gdf = gdf.loc[gdf.geometry_SL != None]

        # check if df is empty
        # skip export if empty - there's nothing anyway
        if gdf.shape[0] > 0:
            # create LineString for SL linkages
            gdf['geometry'] = None
            for row in gdf.itertuples():
                gdf.loc[row.Index, 'geometry'] = LineString([row.geometry_PP, row.geometry_SL])

            # export to file by plan_id
            # create export-specific variable & drop PP and LP geometry columns
            # (multiple geometry columns cause errors)
            gdf_export = gdf.drop(columns=['geometry_PP', 'geometry_LP', 'geometry_SL'])
            # export file
            if output_gis_folderPath:
                # check if directories exist; create if not
                make_output_dir(output_gis_folderPath)
                # export file
                export_filename = f'LX_plan{plan_id}_{lx_fileName[:-3]}.gpkg'
                layer_name = f'SL{plan_id}_data'
                gdf_export.to_file(Path(output_gis_folderPath)/export_filename,
                                   driver='GPKG', layer=layer_name)
                print(f'[INFO] DONE Exporting geopackage for Plan ID: {plan_id}')
        else:
            print('[INFO] No SL sites')
    
    return df, error_ints, error_subsys


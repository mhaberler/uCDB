import os
import cdblib

def xyz_to_cdb(xyz_directory, cdb_filename):
    """
    Converts a directory of XYZ map tiles into a CDB file.
    
    :param xyz_directory: Path to the root directory containing XYZ map tiles.
    :param cdb_filename: Name of the output CDB file.
    """
    with open(cdb_filename, 'wb') as f:
        with cdblib.Writer(f) as writer:
            for root, dirs, files in os.walk(xyz_directory):
                for file in files:
                    # Calculate the tile path relative to the xyz_directory
                    relative_path = os.path.relpath(os.path.join(root, file), xyz_directory)
                    
                    # Read the tile data
                    with open(os.path.join(root, file), 'rb') as f:
                        tile_data = f.read()
                    
                    # Store in CDB with relative path as key
                    #print(relative_path, len(tile_data))
                    writer.put(relative_path.encode('utf-8'), tile_data)

    print(f"Successfully created CDB file: {cdb_filename}")

# Example usage
xyz_directory = '/Volumes/MAPDATA/mapdata/embedded/austria-14'
cdb_filename = 'map_tiles.cdb'
xyz_to_cdb(xyz_directory, cdb_filename)

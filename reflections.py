from sqlalchemy import MetaData, create_engine, Table, select

# setting up our initial objects
metadata = MetaData()
engine = create_engine('sqlite:///Chinook_Sqlite.sqlite')

# Reflecting the artist table
artist = Table('Artist', metadata, autoload=True, autoload_with=engine)
print(artist.columns.keys())

print('the artis id and names are, ')
# querying the data from artist table
s = select([artist]).limit(5)
rp = engine.execute(s).fetchall()

for row in rp:
    print(row)

# reflecting the Album table

album = Table('Album', metadata, autoload=True, autoload_with=engine)

# seeing the foreign keys in the album table
print(album.foreign_keys)

# joining the Artist table with Album
print(str(artist.join(album)))

# To reflect the entire tables of the database to the metadata
metadata.reflect(bind=engine)

# see all the tables in the database
print(metadata.tables.keys())

# reflecting the playlist table
playlist = metadata.tables['Playlist']

# querying the playlist table
s = select([playlist]).limit(5)
rp = engine.execute(s).fetchall()

for i in rp:
    print(i)

# To see the album table metadata
album = metadata.tables['Album']
print(album.metadata.tables)
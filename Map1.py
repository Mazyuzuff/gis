import mapnik
m = mapnik.Map(1280,720)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#ffff00')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('Blue'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('YUSUF',s)
ds = mapnik.Shapefile(file="ne_110m_admin_0_countries.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('YUSUF')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'world.tif', 'tif')
print "rendered image to 'world.tif' "
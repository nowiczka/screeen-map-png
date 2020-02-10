def preparar_mapas():

  # -*- coding: latin-1 -*-
  import pandas as pd
  import geopandas as gpd
  import folium 
  from selenium import webdriver
  import time
  from openpyxl import Workbook, load_workbook
  import os.path
  from pyproj import Proj, transform


  def convert_xy(x,y):
      inProj= Proj(init='epsg:25830')
      outProj= Proj(init='epsg:4326')
      lng,lat = transform(inProj,outProj,x,y)
      return lng,lat

  # INPUT
  path_source = "path/to/excel.xlsx"
  data = pd.read_excel(path_source, encoding='utf-8')
  path="path/to/chromedriver.exe"
  driver=webdriver.Chrome(path)
  delay=20

  for index, row in data.iterrows():
      codigo_par = str(row.CODIGO_PAR) # nombre del mapa
      # check if file exsists

      if os.path.isfile("C:\\1048_ATM\\source\\imagenes\\D4\\"+codigo_par+'.png'):
          pass
      else:

          y = row.YCOORD
          x = row.XCOORD

          y,x = convert_xy(x,y)

          m = folium.Map(
              location=[x, y],
              zoom_start=16 )
          folium.Marker([x, y], popup=row.CODIGO_PAR).add_to(m)

          #m.save(codigo_par+".html")
          tmpurl= codigo_par+".html"
          driver.get(tmpurl)
          #Give the map tiles some time to load
          time.sleep(delay)
          driver.save_screenshot(codigo_par+'.png')
  driver.quit()
  return
  

if __name__ == "__main__":
    print('Ejecutando como programa principal')
    preparar_mapas()



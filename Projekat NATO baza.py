#Uvozenje neophodnih biblioteka

from shapely.geometry import Point
import geopandas as gpd
from fiona.crs import from_epsg
import matplotlib.pyplot as plt

#Definisanje tacaka sa pripadajucim (transformisanim) kordinatama
t1= Point(7453584.060986399, 4961801.704394146) #Toplana Novi Beograd
t2= Point(7454604.2808871325, 4965099.83687202) #Hotel Jugoslavija
t3= Point(7458341.06842165, 4957519.214248948) #Policijska akademija
t4= Point(7451765.071851798, 4964427.67105084) #Trafostanica Bezanijska kosa
t5= Point(7454452.833709708, 4964680.81541619) #Ambasada Kine
t6= Point(7456000.51254964, 4963641.822834653) #Poslovni centar Usce
t7= Point(7458524.465349869, 4963053.595464628) #Zgrada RTS
t8= Point(7446477.902032011, 4955581.57486435) #Most na Savi Ostruznica
t9= Point(7461973.653631955, 4950349.359019956) #Avalski toranj
t10= Point(7444238.035534927, 4926499.638687417) #TE Kolubara Veliki Crljeni
t11= Point(7457486.539469711, 4959399.181880689) #KBC Dragisa Misovic
t12= Point(7433967.212861937, 4947840.100402942) #TE Nikola Tesla

#Proveravanje tipa objekta
print(t1)
print (type(t1))

#Kreiranje liste tacaka
lista = [(t1, "Toplana Novi Beograd"), (t2, "Hotel Jugoslavija"),(t3, "Policijska akademija"), (t4, "Trafostanica Bezanijska kosa"),(t5, "Ambasada Kine"),(t6, "Poslovni centar Usce"),(t7, "Zgrada RTS"), (t8, "Most na Savi Ostruznica"),(t9, "Avalski toranj"),
(t10, "TE Kolubara Veliki Crljeni"),(t11, "KBC Dragisa Misovic"), (t12,"TE Nikola Tesla")]

#Kreiranje GeoDataFrame-a
prostor = gpd.GeoDataFrame()
prostor['geometry'] = None

#Iteracija redova, kreiranje kolone koja predstavlja geometriju (koordinate tačaka) i kolone koja predstavlja Ime lokaliteta, sa ispisanim nazivima entiteta iz liste
for id, (lokacija, naziv) in enumerate(lista):
    prostor.loc[id, 'geometry'] = lokacija
    prostor.loc[id, 'Naziv objekta'] = naziv

#Učitavanje koordinatnog sistema i prikazivanje tačaka na grafikonu
prostor.crs = from_epsg(6316)
prostor.plot(facecolor='red')
plt.title('NATO bombardovanje - civilni objekti')
plt.show()

#Davanje naziva novom shp fajlu i snimanje istog
out_file = r'C:\Users\PC\Desktop\GIS Programiranje\NATO baza\Objekti.shp'  
prostor.to_file(out_file)

#Učitavanje datoteke Grad Beograd.shp
fp = r'C:\Users\PC\Desktop\GIS Programiranje\NATO baza\Grad Beograd.shp'
prostor_poly= gpd.read_file(fp)
print(prostor)
print(prostor_poly.crs)
print(prostor_poly['geometry'].head())

#Promena imena kolone "Opstina" u "Naziv opstine"
prostor_poly = prostor_poly.rename(columns={'Opstina':'Naziv opstine'})
prostor_poly.columns
print(prostor_poly)

#Dodat novi atribut površina za svaki red
prostor_poly['Povrsina'] = prostor_poly['geometry'].area / 1000000
print(prostor_poly['Povrsina'].head())
print("Povrsine su jednake (km2):", prostor_poly)

prostor_poly.crs = from_epsg(6316)
print(prostor_poly.crs)

#Prikazivanje karte Grada Beograda
prostor_poly.plot(column='Naziv opstine', color='none', edgecolor='black', legend=False)
plt.title('Grad Beograd')
plt.tight_layout()
plt.show()

# Kreiranje novog shp file-a sa granicom opština Grada Beograda i proračunatim površinama
out_file2 = r'C:\Users\PC\Desktop\GIS Programiranje\NATO baza\Grad Beograd opstine.shp'
prostor_poly.to_file(out_file2)

print(prostor.crs)
print(prostor_poly.crs)

# Spajanje geoentiteta (objekata) sa kartom Grada Beograda i prikazivanje rezultata na karti
prostor.to_crs(prostor_poly.crs, inplace= True)
preklapanje = prostor.geometry._append(prostor_poly.geometry)
print(preklapanje.crs)
print(preklapanje)

fig, ax = plt.subplots()

prostor_poly.plot(ax=ax, color='none', edgecolor='black')

prostor.plot(ax=ax, color='red')

plt.title('Prostorna raspodela lokacija civlinih objekata gadjanih od strane NATO 1999. god u Gradu Beogradu')
plt.show()

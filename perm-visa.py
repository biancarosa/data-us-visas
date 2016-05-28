import rows
from io import BytesIO

print '------\nReading file\n-----'
filename = 'data/PERM_Disclosure_Data_FY16_Q2_shorter.csv' # shorter csv
f = open(filename,'r')
filedata = f.read()
f.close()

filedata = filedata.replace('2007_NAICS_US_CODE', 'COLUMN_2007_NAICS_US_CODE')
filedata = filedata.replace('2007_NAICS_US_TITLE', 'COLUMN_2007_NAICS_US_TITLE')
visas_data = rows.import_from_csv(BytesIO(filedata))

print 'Hey, rows automatically identified the types:'
for field_name, field_type in visas_data.fields.items():
    print '{} is {}'.format(field_name, field_type)

print '------\nStart analysis\n-----'
certified = filter(lambda row: row.case_status == 'Certified',  visas_data)
denied = filter(lambda row: row.case_status == 'Denied', visas_data)
print 'Certified vs Denied: {} vs {}'.format(len(certified), len(denied))

developer_code = "15-1133"
developers = filter(lambda row: row.pw_soc_code == developer_code,  visas_data)
non_developers = filter(lambda row: row.pw_soc_code != developer_code,  visas_data)
print 'Devs vs Non-Devs: {} vs {}'.format(len(developers), len(non_developers))

developers_certified = filter(lambda row: row.case_status == 'Certified'
                                and row.pw_soc_code == developer_code,  visas_data)
developers_denied = filter(lambda row: row.case_status == 'Denied'
                                and row.pw_soc_code != developer_code,  visas_data)
print 'Devs Certified vs Devs Denied: {} vs {}'.format(len(developers_certified), len(developers_denied))

brazil = filter(lambda row: row.country_of_citizenship == 'BRAZIL', visas_data)
other_countries = filter(lambda row: row.country_of_citizenship != 'BRAZIL', visas_data)
print 'Brazil vs Other countries: {} vs {}'.format(len(brazil), len(other_countries))

brazil_certified = filter(lambda row: row.case_status == 'Certified'
                                and  row.country_of_citizenship == 'BRAZIL',  visas_data)
brazil_denied = filter(lambda row: row.case_status == 'Denied'
                                    and row.country_of_citizenship != 'BRAZIL',  visas_data)
print 'Brazil Certified vs Brazil Denied: {} vs {}'.format(len(brazil_certified), len(brazil_denied))

import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

certified_by_country = {}
for row in visas_data:
    if (row.case_status == 'Certified'):
        if not certified_by_country.get(row.country_of_citizenship):
            certified_by_country[row.country_of_citizenship] = 0
        certified_by_country[row.country_of_citizenship] += 1

country = certified_by_country.keys()
y_pos = certified_by_country.values()
arange = np.arange(len(country))
plt.barh(arange, y_pos, align='center', alpha=0.4)
plt.yticks(arange, country)
plt.xlabel('Certifications approved')
plt.title('Foreign Labor Certification approved grouped by country')

plt.savefig('plot.png')

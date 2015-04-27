import urllib2
a = {'01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26'}
for i in a:
    url="http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R" + str(i) + ".txt"
    vhi_url = urllib2.urlopen(url)
    name = "data/vhi_id_" + str(i)+ ".csv"
    out = open(str(name), 'wb')
    out.write(vhi_url.read())
    out.close()
    print "VHI " + str(i) +" is downloaded."
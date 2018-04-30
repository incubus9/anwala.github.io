import clusters
blognames,words,data=clusters.readfile('blogdataascii.txt') 
clust=clusters.hcluster(data) 
clusters.drawdendrogram(clust,blognames,jpeg='blogcluster.jpg')

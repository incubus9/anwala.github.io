import clusters

blognames,words,data=clusters.readfile('blogdataascii.txt')
clust=clusters.hcluster(data)
clusters.printclust(clust,labels=blognames)


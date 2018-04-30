import clusters

blognames,words,data=clusters.readfile('blogsdata.txt') 
coords=clusters.scaledown(data)
clusters.draw2d(coords,blognames,jpeg='blogs2d.jpg')

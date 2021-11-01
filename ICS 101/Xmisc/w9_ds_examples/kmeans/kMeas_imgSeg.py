import numpy
import matplotlib.pylab as pylab
import matplotlib.image as Image




class KMeans:
   def __init__(self,k,dim,length):
       self.k=k
       self.dim=dim
       self.len=length
       self.centres=numpy.zeros((k, dim))

   def randomInit(self, data):
       ## initialize the centers using a random data entry
       for i in range(self.k):
           self.centres[i]=data[numpy.random.randint(self.len)].copy()
           print(self.centres[i])

   def iterate(self, data):
       ## Compute distances between centres and data points. 
       ## Start with the first centre and then append the rest to the array
       distances = numpy.ones((1,self.len))*numpy.sum((data-self.centres[0,:])**2,axis=1)
       for j in range(self.k-1):
           distances = numpy.append(distances,numpy.ones((1,self.len))*numpy.sum((data-self.centres[j+1,:])**2,axis=1),axis=0)
       ## 'distances' is a 2D array: row for centres, column for data items
       ## Identify the closest cluster for each data item
       cluster = distances.argmin(axis=0)
       cluster = numpy.transpose(cluster*numpy.ones((1,self.len)))
       ## Update the cluster centres as the mean of data items that are closest to them
       for j in range(self.k):
           thisCluster = numpy.where(cluster==j,1,0)
           if numpy.sum(thisCluster)>0:
               self.centres[j,:] = numpy.sum(data*thisCluster,axis=0)/numpy.sum(thisCluster)
       ## membership is calculated on-the-fly; no need to update explicitly
       return self.centres

   def match(self, item):
       dist=numpy.sum((item-self.centres)**2,axis=1)
       winner=dist.argmin(axis=0)
       return winner


class ImageSegmentation:
   def __init__(self,imagename,numberofcentres):
      self.name=imagename
      self.image=Image.imread(self.name) 
      self.k=numberofcentres   
      h, w, _ =self.image.shape
      npix=h*w
      #ima=numpy.array(self.image)
      pixdata=self.image.reshape(npix,3)
      ## conduct clustering with k=numberofcentres
      km=KMeans(k=self.k,dim=3,length=len(pixdata))
      km.randomInit(pixdata)
      for i in range(10):  #it seems that 10 iterations are sufficient  
         centers=km.iterate(pixdata)
#        for c in centers:  # hiden them, just for the purpose of a clear screen 
#          print c,
#          print 'it.=',i
      for j in range(len(pixdata)-1):
         bmu=km.match(pixdata[j])
         # now replacing colour
         pixdata[j]=km.centres[bmu]
      # the shape-adjusting
      self.clusteredima=numpy.array(pixdata).reshape(self.image.shape)
     
# main program, to show the result of segmentation with different k value

for k in range(2,4):   # to try different k value

   Result=ImageSegmentation(r'D:\\My Drive\\NYU Main\\NYU Y1S1\\ICS Section 002\\Lec Slides\\Week 9\\kmeans\\bird.png',k) #to another picture, only need to change the file name
   print('The segmentation of image:%s with %s centres is completed ' % (Result.name,k))
   pylab.figure('K=%s'%k) # give the title for each figure
   pylab.imshow(Result.clusteredima)

pylab.show()# demonstrate all the figures





   


   

   

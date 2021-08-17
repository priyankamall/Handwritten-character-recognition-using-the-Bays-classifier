f <- list.files(".", full.names=TRUE)
i<-c()
d6<-c()
k=1
while(k<=100)
{
p<-load.image(f[k])
p<-resize(p,round(width(p)/4),round(height(p)/4))
p<-as.matrix.data.frame(p)
p0<-sum(p)
p1<-sum(dist(as.matrix(p)))
i<-append(d6,p0)
d6<-append(d6,p1)
k=k+1
}

c<-as.data.frame(cbind(c,d4))
e<-as.data.frame(cbind(e,d5))
i<-as.data.frame(cbind(i,d6))
colnames(c)<-c("Fill%","Ecnrm")
colnames(e)<-c("Fill%","Ecnrm")
colnames(i)<-c("Fill%","Ecnrm")
test<-as.data.frame(rbind(c,e,i))
times<-200
trainc<-as.data.frame(cbind(m,as.vector(c(rep("C",times))),d1))
traine<-as.data.frame(cbind(n,as.vector(c(rep("E",times))),d2))
traini<-as.data.frame(cbind(o,as.vector(c(rep("I",times))),d3))
colnames(trainc)<-c("Fill%","crctr","Ecnrm")
colnames(traine)<-c("Fill%","crctr","Ecnrm")
colnames(traini)<-c("Fill%","crctr","Ecnrm")
train<-as.data.frame(rbind(trainc,traine,traini))
train$`Fill%`<-as.numeric(as.character(train$`Fill%`))
train$`Ecnrm`<-as.numeric(as.character(train$`Ecnrm`))
model<-naive_bayes(crctr ~ .,data=train,laplace=1)
plot(model)
pred<-predict(model,test,type='prob')
count=0
i=1
while(i<=300)
{
  if(i<=100)
  {
    if(which.max(pred[i,])==1)
      count=count+1
  }
  if(i>100&&i<=200)
  {
   
      if(which.max(pred[i,])==2)
        count=count+1
   
  }
  if(i>200)
  {
    if(which.max(pred[i,])==3)
      count=count+1
  }
  i=i+1
}
accuracy<-(300-count)/300
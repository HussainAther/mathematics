%{
K-means (kmeans) clustering.
}%
for i=1:length(d)
    plot([ d(i,1) cents(gidx(i),1) ], ...
[ d(i,2) cents(gidx(i),2) ],lineCol(gidx(i)))
end

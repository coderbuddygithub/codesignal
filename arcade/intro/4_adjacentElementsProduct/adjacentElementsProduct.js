function adjacentElementsProduct(inputArray) {
    large=0;
    
    for(i=0;i<inputArray.length;i++){
        result=inputArray[i]*inputArray[i+1];
        if(i==0){
            large=result
        }
        if(result>large){
            large=result
        }
    }
    return large

}